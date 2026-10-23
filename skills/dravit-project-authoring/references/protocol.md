# Dravit MCP protocol and complete request recipes

## Contents and notation

Use this reference to send requests without application source access. Read [native tools](native-tools.md) for registered tool names, [availability](availability.md) for the complete supported/unsupported vocabulary, and the relevant `commands-*` reference for every writable field. Read [construction recipes](structure-recipes.md) and [catalog recipes](catalog-recipes.md) for dependencies, presets and object behavior.

All examples use `{"name":"tool_name","arguments":{...}}`, the `params` of a standard MCP `tools/call`. In a connected client invoke that tool directly with its `arguments`; do not send this wrapper as another argument. Client-specific prefixes may surround the tool name. They do not change inner operation names such as `wall.create`.

Example IDs, UUIDs, hashes, names, prices and dimensions are illustrative. Substitute saved identities and the entire current revision returned by this account. A syntactically valid example does not establish that its target exists or its geometric prerequisites hold. Do not send example fixture IDs to a real account. The machine-readable [protocol examples](examples-protocol.json) give complete call arguments; [structural](examples-structure.json), [catalog](examples-catalog.json) and [workflow](examples-workflows.json) examples give inner batch entries with individual prerequisites. These are independent recipes, not one sequence to execute wholesale.

## 1. Bootstrap, choose or create a project

Load the guide before modeling, even when there is no local package:

```json
{"name":"dravit_guide","arguments":{"section":"overview"}}
```

Keep returned `version`, `content_sha256`, `release_status` and `available_sections`. Read only the needed sections using their exact section names and both `expected_version` and `expected_content_sha256`. Every reference in the installed package has a corresponding guide section listed in the overview. For `commands-*` or `examples-structure`, `examples-catalog`, `examples-workflows`, request only the operation you need:

```json
{"name":"dravit_guide","arguments":{"section":"commands-roof","operation":"roof.update"}}
```

```json
{"name":"dravit_guide","arguments":{"section":"examples-structure","operation":"roof.update"}}
```

Add `example_id` from one of those three example collections for a single recipe. `examples-protocol` contains full native calls and is read unfiltered; `operation`/`example_id` are not supported on that section. Carry the real version/content pins in both requests; omitted values above only keep the bootstrap examples legible. A filtered response hashes the returned excerpt as `document.sha256`, preserves the full document hash in `document.source_sha256` and keeps the same whole-guide `content_sha256`. An unfiltered section returns the full canonical document; prefer filtered retrieval for command/example collections. No shell, source checkout or developer skill is needed.

Find existing projects:

```json
{"name":"projects_list","arguments":{"page":1}}
```

Follow `next_page` until the intended project is identified. Match name and saved ID. `can_edit` reflects account access, not a promise that every product workflow exists through MCP. Then start or join its shared work version:

```json
{"name":"mcp_session_start","arguments":{"project_id":"project.example"}}
```

For an explicitly requested new project use this separate account tool instead:

```json
{"name":"project_create","arguments":{"name":"Courtyard study","request_id":"courtyard-create-1","idempotency_key":"courtyard-create-1"}}
```

Creation returns `project_id`, `mcp_version_id`, `revision` and `editor_url`, and already starts the shared work version. It is unavailable in a batch. Reuse the same key and name after a lost response. Never create a second project merely because a response is late. Retried creation can return its original revision; reread if it has since changed.

Only the user accepts the MCP version into main or deletes/closes it in Dravit. There is one shared current work document per project, not a copy per chat. Every mutation saves that document. There is no MCP backup/history/undo or automatic main merge.

## 2. Read model facts and discover exact schemas

Project reads use this envelope, not the mutation or preview envelope:

```json
{"name":"project_get","arguments":{"protocol_version":1,"request_id":"inspect-1","operation":"project.get","project_id":"project.example","arguments":{"include_document":true}}}
```

Preserve returned `revision`. Initial full document reads expose `document.editor.levels`, project-local type/preset definitions and physical objects. Later use bounded reads instead of rereading the whole document after every edit:

An empty project has no authoring Levels. If `document.editor.levels` is empty, its first `level.create` must use exactly `label:"Level 0"` and `elevation:{"value":0,"unit":"m"}`. Create that datum before any other Level or Level-dependent object. Reuse an existing saved Level when the project already has one. A preferred display name such as Ground can be set afterwards with `level.update`; the first-create rule does not permanently lock the name or elevation.

```json
{"name":"objects_list","arguments":{"protocol_version":1,"request_id":"list-1","operation":"objects.list","project_id":"project.example","arguments":{"level_id":"level.0","limit":25}}}
```

```json
{"name":"object_get","arguments":{"protocol_version":1,"request_id":"object-1","operation":"object.get","project_id":"project.example","arguments":{"object_id":"object.wall.example"}}}
```

Use opaque returned cursors with the same query/filter context. Read an exact saved object's family/kind, payload, parent and derived context. Do not infer IDs from labels or rename them. Axis, Level, Room, host Wall, roof mass/face/edge, Fence span and Pipe provider are different identities.

For unfamiliar or changed operations:

```json
{"name":"tool_describe","arguments":{"protocol_version":1,"request_id":"schema-1","operation":"tool.describe","project_id":"project.example","arguments":{"operation":"wall.create"}}}
```

The result gives `availability`, `candidate_supported`, `arguments_schema` and, for unsupported workflows, a reason. Reserved operation names do not imply a handler. `catalog.list` is unsupported; exact built-in enum/preset IDs come from schemas, saved project custom types from `project_get`. An installed guide is a reviewed snapshot; current server schemas decide whether a request can execute. On a mismatch read the new schema, finish or stop the current stage, then load a consistent guide version. Never guess a new parameter.

## 3. Units, placement and field semantics

Lengths normally use `{"value":0.9,"unit":"m"}`, points use `{"x":2,"y":3,"unit":"m"}`, angles use `{"value":90,"unit":"deg"}`. Pipe routes use the advertised absolute XYZ point shape. Read each schema: bare ratios, scalar values and point forms are not interchangeable. UI display `length_unit` does not rescale model coordinates. Convert the user's known units before submission; ask if the actual scale is unknown.

Physical model lengths and coordinates use a **1 mm (`0.001 m`) step**, including projects displayed in inches or feet. Convert known units to metres, then round to the nearest millimetre; decimal halves round away from zero: `0.0005 m → 0.001 m`, `-0.0005 m → -0.001 m`. For example, `1 in = 0.0254 m` becomes `0.025 m` in the model, and `1 ft = 0.3048 m` becomes `0.305 m`. Send canonical lengths on the first request. Angles, ratios and normalized directions are not lengths; derive areas and volumes from accepted dimensions without rounding m² or m³ as metres.

Canonicalize independent lengths before deriving a datum: Level `0.0006 m` and offset `0.0006 m` become `0.001 m` each, so their base elevation is `0.002 m`. Legacy readbacks can still contain finer values: reads never rewrite them. A successful command that saves the work document canonicalizes its physical lengths and dependent datums, including unchanged legacy objects; canonical zero is `0`. After a successful change use the canonical saved readback and returned revision for the next stage. If rounding collapses a required edge or positive dimension, handle the existing invalid/unsupported result; do not reconstruct it at finer precision. After a lost response, retry the **identical original payload and idempotency key**; do not recalculate or round an already submitted payload.


Create a Level before a dependent object. Use saved `level_id` and `base_offset` rather than writing derived `base_elevation`. A Room is logical zoning, not an enclosing Wall. Interior `room_id` asserts center-derived membership; moving/releveling may change that membership. Door/Window inherit their host's Level. Roof children and Fence Access inherit parent relationships. Derived assets, dimensions, projection payloads and validation statuses are not arbitrary writable data.

Schemas are closed (`additionalProperties:false`). On update omission generally preserves existing values; explicit `null` resets only fields whose schema and owner permit it. An empty patch can be a no-op for some families and invalid for another. Union schemas require exactly one branch. Do not mix fields from different action branches or include inactive Kitchen/preset fields. Preserve coupled parameters in a single valid final candidate.

## 4. Mutation envelope and atomic batches

Every authoring call carries all ten fields shown below. `expected_*` values come verbatim from the latest successful revision. The outer `operation` is `project.batch`; inner entries retain their own dotted operation names.

```json
{"name":"project_batch","arguments":{"protocol_version":1,"request_id":"enclosure-1","idempotency_key":"enclosure-1","operation":"project.batch","project_id":"project.example","mcp_version_id":"11111111-1111-4111-8111-111111111111","expected_snapshot_version":1,"expected_restore_generation":1,"expected_document_hash":"0000000000000000000000000000000000000000000000000000000000000000","arguments":{"commands":[{"operation":"level.create","local_id":"ground","arguments":{"label":"Level 0","elevation":{"value":0,"unit":"m"}}},{"operation":"wall.create","local_id":"south","arguments":{"height":{"value":2.8,"unit":"m"},"baseline":{"start":{"x":0,"y":0,"unit":"m"},"end":{"x":8,"y":0,"unit":"m"}},"level_id":{"local_id":"ground"},"base_offset":{"value":0,"unit":"m"},"wall_type":{"kind":"material","id":"material.concrete.c25_fixture"}}}]}}}
```

This minimal example assumes no existing Levels and creates the required Level 0 datum and one Wall on it. For a real project first inspect existing Levels and reuse the correct one when it exists. Complete an enclosure with the remaining baselines and intended wall type; the example's concrete type is an explicit catalog choice, not a universal wall default. Coordinate baselines define axes, not necessarily finished interior room dimensions. Account for thickness/alignment and verify actual faces before claiming an 8×6 m usable room.

The reviewed default batch limit is 32 entries; current discovery/configuration is authoritative. Use bounded coherent stages. A batch applies entries in order and saves once. Any failure rolls back the whole stage. Nested batches and noncandidate operations are unsupported. `local_id` is allowed on supported creates and `object.duplicate`; use `{"local_id":"ground"}` only in advertised reference positions and only after that alias was created. Aliases are not arbitrary string interpolation, cannot reference future entries and do not survive outside that batch. `local_object_ids` in the final receipt maps surviving aliases to stable saved IDs.

### Batch reference compatibility

The per-operation **Batch reference overrides** in every `commands-*` section are extracted from the actual batch schema. Normal/native argument schemas show saved string IDs; the listed batch paths additionally permit `{"local_id":"alias"}`. The alias label must match `^[a-z][a-z0-9_]{0,63}$`, be unique within that batch and refer to an earlier alias-bearing entry. Only entries whose generated `local_id_pattern` is non-null may declare an alias.

| Listed reference path | Compatible earlier creation |
|---|---|
| `level_id`, `top_level_id` | `level.create` |
| `room_id` | `room.create`; containment/final Level must still agree |
| Interior or Site family `object_id` | That exact family's `.create`; an alias of `object.duplicate` is not interchangeable in these family commands |
| Generic Shape `object_id` | `generic_shape.create` |
| Generic Group target, including `object.ungroup` | `generic_group.create` |
| Generic Group `object_ids[]` | `generic_shape.create`, in intended unique order |
| `host_fence_id` | `fence.create`; `host_span_id` still uses saved/construction vertex identities, never an alias |
| `provider_object_id` | `water_heater.create`, with the applicable profile and actual derived route context |
| `network_id` | `pipe.route.create`; node/fitting IDs still require saved graph reads |
| `host_wall_id` | A compatible earlier Wall or Foundation creation |
| `wall_type.id`, `foundation_type.id` | `catalog.type.create` for the matching custom type, with reference `kind:"custom"` |
| `catalog.type.update.object_id` | Matching custom type creation; requested family and actual result must agree |
| `object.duplicate/delete/material.assign.object_id` | Earlier supported object `.create` or `object.duplicate`, excluding Axis/Level/catalog-type creations; the operation's actual target applicability still applies |
| Other structural `object_id` paths advertised by its batch override | Earlier creation of the actual matching target family |

This table does not add a path to an operation whose generated override omits it. `roof_id` inside top/attic intent, roof child/mass/face IDs, `opening_preset_id`, `owner_id`, connector profile IDs, material/assembly IDs, Pipe node/fitting IDs and Fence span IDs do not accept an alias unless explicitly present in that operation's generated override. Save the prerequisite stage and read these identities before consuming them. A schema-allowed reference shape does not waive owner family/host validation.

Families with dedicated native tools may use them instead. For `wall_update` keep the same ten-field mutation envelope but set outer `operation` to `wall.update` and inner `arguments` to its exact schema. Interior/Site/Generic/Pipe commands use `project_batch`; do not invent a `bed_create` native tool.

## 5. Poll, retry, conflict and readback

A mutation may return `accepted` or `running` with `operation_id`. Poll:

```json
{"name":"operation_get","arguments":{"operation_id":"operation.example"}}
```

Only `succeeded` proves a committed result. Read `revision`, `changed_object_ids`, surviving alias map and errors from the final result, then carry that full revision into the next stage. A saved no-op may keep the same revision. Do not synthesize snapshot increments or change restore generation/hash yourself. An operation can also fail; inspect its specific error and field/entry context.

| Outcome | Next action |
|---|---|
| Lost response, unknown commit state | Poll the known operation; otherwise retry identical payload with the original idempotency key. Do not change the key to force a second action. |
| `version_conflict` | Read current saved state, identify intervening work, replan, then submit a new intended stage against that exact revision. |
| Validation/unknown field/invalid unit/unsupported action | Correct the actual field or explain the limit; do not strip meaningful assertions or bypass the owner. |
| `rate_limited` or temporary queue pressure | Respect returned retry guidance and bound retries; do not duplicate stages. |
| `access_revoked`, `forbidden`, entitlement failure or inaccessible target | Stop dependent work and report the access issue. Never use another identity or main document as a fallback. |
| Closed MCP version | Do not silently restart from main while retrying old work. A new explicit task can start/join a fresh session. |

Read back the changed object plus affected hosts/neighbors. A Wall/Level/Roof edit can update dependent objects outside the immediate target. Check actual receipt IDs and saved topology. A successful queued Save does not prove browser delivery, geometry usability or regulatory compliance.

## 6. Views, windows and validation

`project_view` uses a distinct native envelope with `revision`, `view` and explicit saved `level_id`; it does not take mutation `operation`/`expected_*` fields:

```json
{"name":"project_view","arguments":{"revision":{"project_id":"project.example","mcp_version_id":"11111111-1111-4111-8111-111111111111","snapshot_version":1,"restore_generation":1,"document_hash":"0000000000000000000000000000000000000000000000000000000000000000"},"view":"top","level_id":"level.0","object_ids":["object.wall.example"]}}
```

`project_view` returns synchronously with `status: "succeeded"`, `operation_id: null` and `result: {viewport_url, render_location: "client", ticket_expires_at, workflow}`. It returns no server PNG and creates no image job to poll. Open the returned URL in an agent-controlled browser with screenshots. Its fragment ticket is single-use and expires after 60 seconds; it establishes a two-hour read-only cookie session bound to this project and MCP version without another Dravit login. Never copy an OAuth bearer into a URL or share this capability URL.

Wait for `html[data-mcp-viewport-state="ready"]`; read and parse `#mcp-viewport-status`'s `data-receipt`, checking the complete loaded revision, `view`, `level_id`, `visible_object_ids`, `omitted_object_ids` and `reference_sources`. Inspect the actual screenshot. After every later completed Save reload that same tab and repeat readiness/receipt/screenshot checks against the Save revision. There is no WebSocket/Reverb, polling or automatic refresh in this viewer. A stale image does not verify a new Save. For another view or Level, issue a new `project_view` and navigate that tab to its new URL. A missing selected object/Level or closed MCP version is an error, never an implicit switch to main or another target. Expired access requires a new authorized view request.

Use `3d` with the same Level and, when needed, schema camera options; use actual `front/back/left/right` only for supported families. Top uses the working Level; 3D shows it and lower Levels. A Room's independent 3D, Site/Interior Side and independent nested Roof focus are unsupported. Filters/crop are observational. Copied Top underlays are separate reference sources, not authored geometry. If this client has no browser/screenshots, report visual verification as unavailable and continue independent supported work. MCP access alone does not supply this browser capability; there is no server PNG fallback. See [verification](verification.md).

To interpret "this window/selection", first list `editor_sessions` using the normal read envelope, `operation:"editor.sessions"` and `arguments:{"revision":...}`. Then repeat with an explicit returned `window_id`. Do not infer the most recent tab from `focused`. Context is advisory client telemetry; it cannot remotely select, bind or operate a browser. Resolve saved facts independently.

```json
{"name":"project_validate","arguments":{"revision":{"project_id":"project.example","mcp_version_id":"11111111-1111-4111-8111-111111111111","snapshot_version":1,"restore_generation":1,"document_hash":"0000000000000000000000000000000000000000000000000000000000000000"},"limit":25}}
```

Follow its report-specific cursor at the identical revision. Read the complete coverage matrix, applicability/population, issues and object results. Supported current checks include exact Door/Window host and own-parameter validation; other records may be saved statuses, semantic binding checks or admission-only guards. Zero issues over an empty population is not a whole-project pass. Generic collision, human routes, structural adequacy, daylight and ventilation are not certified by this validator. Repair a confirmed defect with normal object commands, read a new revision and request a new report. See [verification](verification.md) and [human use](human-use.md).

## 7. Shared document workflows

Use [workflow examples](examples-workflows.json) and [workflow schemas](commands-workflows.md).

- `object.duplicate` duplicates one supported catalog root or Generic Group with the existing +0.3 m/-0.3 m placement and an explicit target Level. It is not a generic structural copy command. Read the new ID and transform the duplicated family if supported. A Roof Window duplicates through `roof.update` action `roof_window_duplicate`.
- `object.delete` delegates to existing family deletion and cascades. For Level/Axis use their explicit family operation. A grouped child must be ungrouped first. Inspect dependents before deleting; do not delete the wrong object to force an edit.
- `object.material.assign` applies an exact advertised material or compatible assembly only where the current GUI owner supports it. Slab assembly presets can change thickness. Wall/Foundation use type catalogs; Room finishes use `room.update.finishes`; Roof/Stair have family material settings. Choosing an assembly and assigning an arbitrary price are different operations.
- `catalog.type.create` supports Wall, Foundation and Opening definitions. Create a custom Wall type for a partition with the exact role, recipe, thickness and complete finished price. `catalog.type.update` supports Wall/Foundation only. Use returned catalog IDs, not example IDs. Opening custom preset creation starts from one exact built-in filled Door/Window preset; custom preset update/delete are unavailable. Catalog prices in examples are demonstration inputs, not market evidence. Never invent a user-approved specification or actual estimate rate from them.
- Wall recipe unit depends on the explicit recipe: masonry/concrete listed in schema use m³; other Wall recipes use m². Every Foundation custom type price is per m³ of complete wall+footing+blinding. Component geometry and active section must agree with its existing kind. Do not submit a price per metre as `complete_unit_price_per_m3`. Updating a Wall recipe also requires a new complete price in its resulting unit.
- `project.settings.update` changes display `length_unit` only. `project.save` confirms the already saved current document and accepts no raw document. Main-only rename/share/delete/import/export/drawings/estimates/history/underlay writes remain unsupported through this protocol. Explain these limits before promising end-to-end delivery in those formats.

## 8. Turn a brief, image or voice request into stages

Resolve scale, project, intended use and required outcomes. For a new house order the real dependencies: Levels and optional Axes, physical enclosure and partitions, Room zoning, Floor/roof/stair structure and their dependencies, hosted openings, Interior/Site equipment, then detail/material settings. Select the relevant recipe rather than assuming all families share the same CRUD/transform shape. A roof preset is not a dormer or an attic Room; a Room polygon is not a physical partition; decorative furniture is not an engineering system.

Use the user's actual activities to choose fronts, approaches, openings and service access. A sketch establishes intent, not hidden dimensions or verified engineering performance. Preserve stated needs and explicitly track unresolved choices. After each coherent stage, check saved facts and applicable images. End with supported results, unresolved defects and unknown capabilities. The user need not supply application code, internal payloads or a prewritten MCP plan.
