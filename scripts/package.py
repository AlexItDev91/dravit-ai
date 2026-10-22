#!/usr/bin/env python3
"""Validate/package the standalone Dravit skill without application dependencies."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from hashlib import sha256
import json
from pathlib import Path, PurePosixPath
import re
import subprocess
from urllib.parse import unquote, urlsplit
from zipfile import ZIP_STORED, ZipFile, ZipInfo


ROOT = Path(__file__).resolve().parents[1]
SKILL_NAME = "dravit-project-authoring"
SKILL_PREFIX = f"skills/{SKILL_NAME}/"
SECTION_PATHS = {
    "overview": "SKILL.md",
    "workflow": "references/authoring-workflow.md",
    "verification": "references/verification.md",
    "spatial-reasoning": "references/spatial-reasoning.md",
    "human-use": "references/human-use.md",
    "protocol": "references/protocol.md",
    "native-tools": "references/native-tools.md",
    "availability": "references/availability.md",
    "commands-structure": "references/commands-structure.md",
    "commands-openings": "references/commands-openings.md",
    "commands-roof": "references/commands-roof.md",
    "commands-circulation": "references/commands-circulation.md",
    "commands-interior": "references/commands-interior.md",
    "commands-site": "references/commands-site.md",
    "commands-pipes": "references/commands-pipes.md",
    "commands-generic": "references/commands-generic.md",
    "commands-workflows": "references/commands-workflows.md",
    "structure-recipes": "references/structure-recipes.md",
    "catalog-recipes": "references/catalog-recipes.md",
    "examples-structure": "references/examples-structure.json",
    "examples-catalog": "references/examples-catalog.json",
    "examples-workflows": "references/examples-workflows.json",
    "examples-protocol": "references/examples-protocol.json",
}
SKILL_PATHS = (*SECTION_PATHS.values(), "agents/openai.yaml")
SOURCE_PATHS = (
    ".gitignore", ".github/workflows/release.yml", "README.md", "CHANGELOG.md",
    "LICENSE.md", "scripts/package.py", "packaging/compatibility.json",
    "packaging/publication.json", "packaging/evaluation.json",
    "packaging/delivery.json", "evaluation/acceptance.json",
    *(SKILL_PREFIX + path for path in SKILL_PATHS),
)
HEX_SHA256 = re.compile(r"[a-f0-9]{64}\Z")
MAXIMUM_GUIDE_BYTES = 1048576
SEMVER = re.compile(r"(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)\Z")
PUBLICATION_FIELDS = {
    "schema_version", "state", "repository", "publisher", "license",
    "source_branch", "release_tag_prefix", "mcp_url", "chatgpt_registered_app_id",
}
EVALUATION_CHECKS = {
    "skill_format_and_links", "manifest_schemas_and_archive_contents",
    "behavioral_with_and_without_skill", "affected_and_critical_regressions",
}


class PackageError(ValueError):
    """An invalid source or unmet release prerequisite."""


@dataclass(frozen=True)
class Source:
    files: dict[str, bytes]
    version: str
    publication: dict
    compatibility: dict
    evaluation: dict
    acceptance: dict


def require(condition: bool, message: str) -> None:
    if not condition:
        raise PackageError(message)


def digest(content: bytes) -> str:
    return sha256(content).hexdigest()


def file_set_hash(files: dict[str, bytes]) -> str:
    """SHA256 of sorted UTF-8 path:sha256(bytes) newline records."""
    records = "".join(f"{path}:{digest(files[path])}\n" for path in sorted(files))
    return digest(records.encode("utf-8"))


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")


def unique_object(pairs: list[tuple[str, object]]) -> dict:
    value = {}
    for key, item in pairs:
        require(key not in value, f"Duplicate JSON key: {key}")
        value[key] = item
    return value


def read_source(path: str) -> bytes:
    relative = PurePosixPath(path)
    require(not relative.is_absolute() and ".." not in relative.parts, "Source path must stay inside the package")
    target = ROOT.joinpath(*relative.parts)
    require(all(not parent.is_symlink() for parent in (target, *target.parents) if parent != ROOT.parent), f"Symlink source is forbidden: {path}")
    require(target.is_file() and target.resolve().is_relative_to(ROOT), f"Missing package source: {path}")
    content = target.read_bytes()
    require(b"\x00" not in content, f"Unexpected binary source: {path}")
    content.decode("utf-8")
    return content


def parse_json(files: dict[str, bytes], path: str) -> dict:
    value = json.loads(files[path], object_pairs_hook=unique_object)
    require(isinstance(value, dict), f"Expected a JSON object: {path}")
    return value


def https_url(value: object) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlsplit(value)
    return bool(parsed.scheme == "https" and parsed.hostname and not parsed.username
                and not parsed.password and not parsed.query and not parsed.fragment)


def validate_links(files: dict[str, bytes]) -> None:
    for path, content in files.items():
        if not path.endswith(".md"):
            continue
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", content.decode("utf-8")):
            target = target.strip("<>").split("#", 1)[0]
            if not target:
                continue
            if urlsplit(target).scheme:
                require(https_url(target), f"Unexpected link scheme or credentialed URL: {path}")
                continue
            resolved = (ROOT / path).parent.joinpath(unquote(target)).resolve()
            require(resolved.is_relative_to(ROOT) and resolved.is_file(), f"Broken package link in {path}: {target}")
            relative = resolved.relative_to(ROOT).as_posix()
            require(relative in files, f"Link target is outside the source allowlist: {path}")
            if path.startswith(SKILL_PREFIX):
                require(relative.startswith(SKILL_PREFIX), f"Runtime skill link requires a non-bundled source: {path}")


def load_source() -> Source:
    files = {path: read_source(path) for path in SOURCE_PATHS}
    entry = files[SKILL_PREFIX + "SKILL.md"].decode("utf-8")
    header = re.fullmatch(r"---\n(.*?)\n---\n(.+)", entry, re.S)
    require(header is not None, "SKILL.md must have YAML frontmatter and a body")
    metadata = header.group(1)
    require(re.search(rf"^name: {SKILL_NAME}$", metadata, re.M) is not None, "Skill name/folder mismatch")
    description = re.search(r"^description: (.+)$", metadata, re.M)
    require(description is not None and len(description.group(1)) <= 1024, "Invalid skill description")
    version_match = re.search(r'^metadata:\n  version: "([^"]+)"$', metadata, re.M)
    require(version_match is not None, "metadata.version must be a quoted SemVer")
    version = version_match.group(1)
    require(SEMVER.fullmatch(version) is not None, "Version must be MAJOR.MINOR.PATCH")
    actual_skill_paths = {path.relative_to(ROOT / SKILL_PREFIX).as_posix()
                          for path in (ROOT / SKILL_PREFIX).rglob("*") if path.is_file()}
    require(actual_skill_paths == set(SKILL_PATHS), "Unexpected or missing skill file; update the explicit allowlist intentionally")
    publication = parse_json(files, "packaging/publication.json")
    require(set(publication) == PUBLICATION_FIELDS and publication["schema_version"] == 1, "Invalid publication metadata fields")
    require(publication["source_branch"] == "main" and publication["release_tag_prefix"] == "dravit-skill-v", "Unexpected source branch or tag policy")
    require(https_url(publication["mcp_url"]), "MCP endpoint must be HTTPS without credentials/query/fragment")
    require(publication["repository"] is None or https_url(publication["repository"]), "Invalid public repository URL")
    app_id = publication["chatgpt_registered_app_id"]
    require(app_id is None or (isinstance(app_id, str) and re.fullmatch(r"plugin_asdk_app[A-Za-z0-9_-]+", app_id)), "Use a real registered ChatGPT MCP technical ID")
    compatibility = parse_json(files, "packaging/compatibility.json")
    require(compatibility["protocol_version"] == 1 and compatibility["guide_sections"] == SECTION_PATHS, "Unsupported protocol or guide-section mapping")
    evaluation = parse_json(files, "packaging/evaluation.json")
    acceptance = parse_json(files, "evaluation/acceptance.json")
    case_ids = [row["id"] for row in acceptance["cases"]]
    require(len(case_ids) == len(set(case_ids)) == acceptance["baseline_case_count"], "Evaluation case identities must be unique and complete")
    for result in evaluation["results"]:
        path = result.get("evidence_path", "")
        require(path.startswith("evaluation/receipts/") and path.endswith((".json", ".md")), "Evidence must be a sanitized local receipt")
        files[path] = read_source(path)
        require(result.get("evidence_sha256") == digest(files[path]), "Evaluation receipt checksum mismatch")
    validate_links(files)
    return Source(files, version, publication, compatibility, evaluation, acceptance)


def git(*arguments: str) -> str:
    result = subprocess.run(["git", "-C", str(ROOT), *arguments], capture_output=True, text=True, check=False)
    require(result.returncode == 0, "Git source identity is unavailable or inconsistent")
    return result.stdout.strip()


def source_identity(source: Source, release: bool) -> dict:
    try:
        commit = git("rev-parse", "HEAD")
        dirty = bool(git("status", "--porcelain", "--untracked-files=all", "--", str(ROOT)))
    except PackageError:
        require(not release, "A release requires its dedicated Git repository")
        commit, dirty = None, True
    return {
        "repository": source.publication["repository"], "commit_sha": None if dirty else commit,
        "tree_sha256": file_set_hash(source.files),
        "tag": f"dravit-skill-v{source.version}" if release else None,
    }


def guide_artifact(source: Source, identity: dict, release: bool) -> dict:
    documents = {path: source.files[SKILL_PREFIX + path] for path in SECTION_PATHS.values()}
    artifact = {
        "schema_version": 1, "skill_name": SKILL_NAME, "version": source.version,
        "release_status": "release" if release else "draft", "source": identity,
        "compatibility": source.compatibility, "content_sha256": file_set_hash(documents),
        "documents": [{"path": path, "sha256": digest(content), "content": content.decode("utf-8")}
                      for path, content in sorted(documents.items())],
    }
    require(len(json_bytes(artifact)) <= MAXIMUM_GUIDE_BYTES, "Guide exceeds the server's 1 MiB instruction artifact budget; reduce duplication instead of raising the limit")
    return artifact


def require_release(source: Source, identity: dict, guide: dict) -> None:
    require(Path(git("rev-parse", "--show-toplevel")).resolve() == ROOT, "Extract the skill to its own repository before release; never release the BIM repository")
    require(not git("status", "--porcelain", "--untracked-files=all"), "Release source must be committed and clean")
    publication = source.publication
    require(publication["state"] == "public_repository" and https_url(publication["repository"]), "A verified separate public repository is required")
    require(isinstance(publication["publisher"], str) and bool(publication["publisher"].strip()), "Publisher is not configured")
    require(isinstance(publication["license"], str) and bool(publication["license"].strip()), "The owner must select a public release license")
    require(b"No public distribution license has been selected" not in source.files["LICENSE.md"], "Replace the draft rights notice with the selected license")
    require(git("describe", "--tags", "--exact-match", "HEAD") == identity["tag"], "The checked-out immutable tag must match metadata.version")
    main_ref = "refs/heads/main" if git("branch", "--show-current") == "main" else "refs/remotes/origin/main"
    git("merge-base", "--is-ancestor", identity["commit_sha"], main_ref)
    catalog = source.compatibility
    require(catalog["catalog_verification_status"] == "verified" and isinstance(catalog["catalog_fingerprint"], str)
            and HEX_SHA256.fullmatch(catalog["catalog_fingerprint"]), "Record the actually evaluated command catalog fingerprint")
    evaluation = source.evaluation
    require(evaluation["status"] == "passed" and evaluation["content_sha256"] == guide["content_sha256"], "Behavioral evaluation must bind to these exact instruction contents")
    require(evaluation["catalog_fingerprint"] == catalog["catalog_fingerprint"], "Evaluation/catalog fingerprint mismatch")
    require(set(evaluation["checks"]) == EVALUATION_CHECKS and all(value == "passed" for value in evaluation["checks"].values()), "Complete package, behavioral and critical regression gates first")
    require(type(evaluation["repetitions"]) is int and evaluation["repetitions"] >= 5, "Record repeated controlled behavioral runs, at least five")
    results = evaluation["results"]
    expected = {row["id"] for row in source.acceptance["cases"]}
    require(len(results) == len(expected) and {row["id"] for row in results} == expected
            and all(row["status"] == "passed" for row in results), "All acceptance cases require passing expectation receipts")
    require(f"## {source.version}\n" in source.files["CHANGELOG.md"].decode("utf-8"), "Finalize a matching changelog entry before release")


def plugin_files(source: Source, registered: bool) -> dict[str, bytes]:
    manifest = {
        "$schema": "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
        "name": "dravit-project-authoring", "version": source.version,
        "description": "Author and inspect Dravit projects with existing MCP capabilities.",
        "keywords": ["dravit", "bim", "project-authoring"],
    }
    for key in ("repository", "license"):
        if source.publication[key] is not None:
            manifest[key] = source.publication[key]
    if source.publication["publisher"] is not None:
        manifest["author"] = {"name": source.publication["publisher"]}
    files = {path: source.files[path] for path in source.files if path.startswith(SKILL_PREFIX)}
    files["LICENSE.md"] = source.files["LICENSE.md"]
    if registered:
        app_id = source.publication["chatgpt_registered_app_id"]
        require(app_id is not None, "ChatGPT wrapper requires a real registered MCP ID")
        manifest["extensions"] = {"com.openai": {"apps": "./.app.json"}}
        files[".app.json"] = json_bytes({"apps": {"dravit": {"id": app_id}}})
    else:
        files["mcp.json"] = json_bytes({
            "$schema": "https://agent-plugins.org/schemas/1.0.0/mcp.schema.json",
            "mcpServers": {"dravit": {"type": "streamable-http", "url": source.publication["mcp_url"]}},
        })
    files["plugin.json"] = json_bytes(manifest)
    return files


def write_zip(path: Path, files: dict[str, bytes]) -> None:
    with ZipFile(path, "x", compression=ZIP_STORED) as archive:
        for name, content in sorted(files.items()):
            item = ZipInfo(name, (1980, 1, 1, 0, 0, 0))
            item.create_system = 3
            item.external_attr = 0o100644 << 16
            archive.writestr(item, content)


def build(source: Source, guide: dict, output: Path) -> list[dict]:
    require(not output.exists(), "Output already exists; select a new directory to preserve earlier artifacts")
    output.mkdir(parents=True)
    prefix = f"dravit-skill-v{source.version}"
    write_zip(output / f"{prefix}-portable.zip", plugin_files(source, registered=False))
    claude = {f"{SKILL_NAME}/{path}": source.files[SKILL_PREFIX + path] for path in SECTION_PATHS.values()}
    claude[f"{SKILL_NAME}/LICENSE.md"] = source.files["LICENSE.md"]
    write_zip(output / f"{prefix}-claude.zip", claude)
    if source.publication["chatgpt_registered_app_id"] is not None:
        write_zip(output / f"{prefix}-chatgpt.zip", plugin_files(source, registered=True))
    (output / f"{prefix}-guide.json").write_bytes(json_bytes(guide))
    artifacts = [{"file": path.name, "sha256": digest(path.read_bytes()), "bytes": path.stat().st_size}
                 for path in sorted(output.iterdir())]
    receipt = {
        "schema_version": 1, "skill_name": SKILL_NAME, "version": source.version,
        "release_status": guide["release_status"], "source": guide["source"],
        "content_sha256": guide["content_sha256"], "compatibility": source.compatibility,
        "evaluation": source.evaluation, "delivery": parse_json(source.files, "packaging/delivery.json"),
        "artifacts": artifacts,
        "chatgpt_wrapper": "built" if source.publication["chatgpt_registered_app_id"] else "pending_registered_mcp_id",
        "publication": "not_performed", "client_acceptance": "not_performed",
    }
    receipt_path = output / f"{prefix}-receipt.json"
    receipt_path.write_bytes(json_bytes(receipt))
    artifacts = [*artifacts, {"file": receipt_path.name, "sha256": digest(receipt_path.read_bytes()), "bytes": receipt_path.stat().st_size}]
    (output / "SHA256SUMS").write_text("".join(f"{row['sha256']}  {row['file']}\n" for row in artifacts), encoding="utf-8")
    return artifacts


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("validate", "build"))
    parser.add_argument("--release", action="store_true", help="Require clean standalone tagged source and completed evaluation")
    parser.add_argument("--output", type=Path, default=ROOT / "dist", help="New output directory; never overwritten")
    args = parser.parse_args()
    try:
        source = load_source()
        identity = source_identity(source, args.release)
        guide = guide_artifact(source, identity, args.release)
        if args.release:
            require_release(source, identity, guide)
        result = {"version": source.version, "release_status": guide["release_status"], "content_sha256": guide["content_sha256"]}
        if args.action == "build":
            result["artifacts"] = build(source, guide, args.output.resolve())
        print(json.dumps(result, indent=2))
    except (PackageError, OSError, ValueError, KeyError, TypeError) as error:
        parser.exit(1, f"Package error: {error}\n")


if __name__ == "__main__":
    main()
