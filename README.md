# Dravit AI

Agent skill for creating, changing and inspecting Dravit projects through existing MCP tools: project identity, shared work versions, modelling stages, saved Levels, units, retries, visual checks and human-use reasoning.

**Public preview: candidate version `0.2.2`, not yet a tagged or behaviorally evaluated release.**

## Install with one command

Requires a supported local agent such as Codex or Claude Code, Node.js 22.20+ and an authenticated Dravit MCP connection.

```sh
npx skills add AlexItDev91/dravit-ai --skill dravit-project-authoring
```

Choose the agent when prompted. Installation is project-scoped by default; add `-g` for use across projects. A direct global Codex installation is:

```sh
npx skills add AlexItDev91/dravit-ai --skill dravit-project-authoring -a codex -g
```

Connect your Dravit account separately using your agent's remote MCP/OAuth setup and `https://dravit.pro/mcp`. Installing the instructions does not authorize project access.

## Check and install updates

```sh
npx skills check
npx skills update dravit-project-authoring
```

Use `npx skills update` to update all installed skills. Choose the same project/global scope; `-g` targets global installations. Changes are retrieved from this repository when you update; a GitHub push does not itself replace installed local files.

See the [skills CLI documentation](https://github.com/vercel-labs/skills/blob/main/docs/commands.md). Cloud ChatGPT/Claude use the package/upload channels below; a terminal install does not install into a cloud account.

## Canonical source

The single editable methodology is [skills/dravit-project-authoring/SKILL.md](skills/dravit-project-authoring/SKILL.md) and its 22 reference documents/collections. OpenAI metadata, Claude ZIP and MCP-guide artifacts derive from those same files. Runtime use needs only the connected Dravit MCP and instructions, never BIM source, a database, shell access or developer skills.

## Protocol handbook

The skill contains exact parameter schemas for all 211 supported inner authoring operations, 550 operation examples with prerequisites, and 19 full native-call examples. Structural/roof/opening/circulation and Interior/Site/Pipe/Generic handbooks explain dependencies and editing behavior. Availability includes all 283 finite operation names with explicit unsupported reasons. These counts describe the reviewed source snapshot, not an engineering certification.

Cloud clients retrieve the same content through `dravit_guide`: start with `overview` and `protocol`, then load the relevant named section. On command/example collections pass `operation` to retrieve one operation and optionally `example_id` to select a recipe. This avoids loading the full catalog into every task. Keep the guide's version/content pins for the stage.

## Source and contracts

- [Publication configuration](packaging/publication.json) identifies the actual public repository and publisher. Public license selection and the registered ChatGPT MCP ID remain pending.
- [Compatibility](packaging/compatibility.json) names the observed protocol/core tools and exact guide sections. The current server has no independently established catalog release number; catalog version/fingerprint remain pending until the actual evaluation records them. A protocol number is not a catalog version.
- [Evaluation status](packaging/evaluation.json) is pending. [Acceptance cases](evaluation/acceptance.json) retain all 32 E1 case identities and behavior expectations. Existing no-skill baseline is not an evaluation of this skill. No new test suite is duplicated here.
- [Client matrix](packaging/delivery.json) separates published, installed and active versions, web/desktop/voice, new/open chat and updates. Every acceptance entry is pending. Grok remains deferred.

Source review on 2026-10-22 used Dravit's actual MCP server/tool descriptions, command/read/preview/lifecycle schemas and E8 knowledge contracts. Available catalog commands do not establish a program validator. The skill remains capability-driven as additional existing checks are adapted.

## Packaging after the deferred verification stage

The Python 3.12+ stdlib-only builder uses explicit file allowlists. It does not install a package, connect an account, read tokens, contact MCP or publish anything. Run it from this directory when build/validation is in scope:

```sh
python3 scripts/package.py validate
python3 scripts/package.py build --output dist
```

The current invocation is a draft even though its candidate version is `0.2.2`. It emits a portable Agent Plugins ZIP with `plugin.json` and remote `mcp.json`, a Claude skill-folder ZIP, guide JSON, receipt and `SHA256SUMS`. If a real `chatgpt_registered_app_id` is configured, it also emits a ChatGPT wrapper using `.app.json`; that wrapper uses the existing registered connection instead of duplicating a raw remote MCP dependency. All manifest versions come from `metadata.version`.

Archive entries are sorted, stored without compression and use a fixed timestamp/permissions, so identical source/configuration produces identical ZIP bytes. The output directory must be new. Only the skill, its references/UI metadata, chosen license and generated client wiring enter installable archives. Package scripts, application files, user projects, evaluation traces and runtime credentials do not enter those archives. Review archive contents for credentials as part of the deferred package gate; an allowlist is not a claim that evaluation has happened.

The source validator checks the narrow authored frontmatter contract, names/version, file set, local Markdown links and configured metadata. It is not a full YAML parser, an upstream client JSON Schema validator or a behavioral test. The next stage must also run skill-creator's `quick_validate.py`, actual upstream manifest schemas, archive inspection and the controlled E1/E4 behavioral runs.

## Independent release and maintenance

The canonical public repository is [AlexItDev91/dravit-ai](https://github.com/AlexItDev91/dravit-ai). It is checked out inside BIM as the Git submodule `integrations/dravit-skill`: one editable source, tracked by a specific commit in BIM. The MCP server vendors a checksum-pinned generated guide.

From the BIM root, initialize this nested checkout with:

```sh
git submodule update --init integrations/dravit-skill
```

Commit skill changes in this repository's `main`, push them here, then update the submodule commit recorded in BIM. Application code, credentials, user projects and private evaluation traces do not belong in this repository.

Before a tagged release, the owner must select the SPDX license, replace [the draft rights notice](LICENSE.md), and record the actual package/behavioral evaluation. Source publication alone does not satisfy the release gate.

Use `main` for source development. PATCH fixes instructions within their existing contract; MINOR adds supported workflows and pre-1.0 incompatibilities; MAJOR records incompatible post-1.0 contracts. The Dravit application's `VERSION` is independent. Never republish a version/tag with changed contents.

Before release, bind [evaluation](packaging/evaluation.json) to the exact guide `content_sha256` and observed command `catalog_fingerprint`. Record all named checks as `passed`, repeated controlled behavioral runs (at least five), and each acceptance case's passing expectation result with a sanitized `evidence_path` under `evaluation/receipts/` and its `evidence_sha256`. A shared sanitized receipt can cover multiple cases; preserve raw calls, images, revisions and control outputs in the approved evaluation evidence location. Do not publish tokens or real user-project data. A verdict such as expected unknown can pass its behavioral expectation without declaring the building checked.

Finalize `CHANGELOG.md` as `## X.Y.Z`, commit the verified source in main, then create the immutable tag `dravit-skill-vX.Y.Z`. On that tag:

```sh
python3 scripts/package.py build --release --output dist
```

Release mode refuses a dirty source, a repository rooted outside this package, missing public metadata/license, mismatched tag, unchecked catalog or incomplete/stale evaluation. The workflow additionally verifies that its configured repository is the current public GitHub repository and refuses an existing release before publication. A Git release alone does not close E5/E6 or update an installed client.

## Guide delivery

The generated `dravit-skill-vX.Y.Z-guide.json` has `schema_version`, skill/version, `release_status`, source identity, compatibility, `content_sha256` and five `{path, sha256, content}` documents. Paths are relative to the skill root. Sections are `overview`, `workflow`, `verification`, `spatial-reasoning` and `human-use` exactly as in compatibility metadata.

For `content_sha256`, sort document paths lexicographically, concatenate `path:sha256(UTF-8 content)` plus a newline for each, then SHA-256 the UTF-8 concatenation. `source.tree_sha256` uses the same algorithm over all explicitly allowlisted package-source files, including referenced sanitized evaluation receipts. The guide content digest therefore stays stable when only packaging metadata changes. The build receipt separately records every output file's checksum and source commit/tree.

The server should pin the artifact checksum and verify every document/content digest before delivering a section. A `dravit_guide` discovered in a client can deliver those same sections without filesystem skills. Do not fetch instructions from Git on each task. A server's draft guide must stay marked draft. Before public release, use the checked immutable release artifact. Reading a guide is not native package installation or automatic package update.

## Installation and update channels to verify

These are authoring paths from official documentation reviewed on 2026-10-21, not successful Dravit deliveries. Exact account/workspace availability and consumer surfaces require E5/E6 evidence.

| Client/channel | Installation path for the later authorized stage | Update boundary |
|---|---|---|
| ChatGPT registered plugin | Register the actual Dravit HTTPS MCP connection, configure its real technical ID, build the wrapper and follow the supported test/submission/directory path | Record actual submitted/approved/published states and native updater behavior. Replacing hosted MCP does not update bundled skill files |
| Claude personal skill | Upload the generated skill-folder ZIP through Customize → Skills → Create skill → Upload; enable it and separately connect Dravit via OAuth | Personal upload update behavior must be measured. Preserve the previous artifact and OAuth grant; do not promise shared-skill update behavior for uploads |
| Claude shared/org skill | Use only available authorized sharing or organizational publication after personal validation | Official documentation distinguishes shared recipient updates at next use from organization updates that follow their review path; measure the selected channel |
| MCP-guide fallback | In the actual session discover/read the same pinned methodology and execute the control task | Instruction refresh is not native package update. New/open chat, voice and actual consumption remain separate checks |

For ChatGPT, do not invent a public package ID/URL or use `npx` to install into a cloud account. A local Codex marketplace or CLI install does not prove consumer ChatGPT acceptance. Claude Code does not prove Claude web/desktop. No shell is needed for end-user modeling; Claude may require its account's code-execution capability for loading custom skills according to its current product settings.

For local agents, use the install/update commands above. Their project/global scope is separate from cloud ChatGPT/Claude installation channels.

For each E5/E6 receipt retain the fields listed in the client matrix. Test clean installation, direct and indirect invocation, one shared MCP version for two participants, preserved main, new and open chat, the next real package version, stale cache, failed update and grant preservation. Confirm actual instruction consumption plus model/view behavior; the model reciting a version number is insufficient. Test voice independently. E3 aggregates those receipts; E4 compares with the same no-skill scenarios and retains brief violations and unknown checks separately.

Official packaging sources: [OpenAI plugin packaging](https://developers.openai.com/plugins/build/plugins), [OpenAI submission](https://developers.openai.com/plugins/deploy/submission), [Agent Plugins manifest schema](https://agent-plugins.org/schemas/1.0.0/plugin.schema.json), [Agent Plugins MCP schema](https://agent-plugins.org/schemas/1.0.0/mcp.schema.json), [Agent Skills format](https://agentskills.io/specification), [Claude custom skills and updates](https://support.claude.com/en/articles/12512180-use-skills-in-claude). Client schemas and channels can change; recheck them before actual delivery.
