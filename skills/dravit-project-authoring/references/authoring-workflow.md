# Authoring workflow

## Select and read

For an existing project, use `projects_list` to resolve identity and `mcp_session_start(project_id)` to join its single shared current MCP version. An editor URL is a live monitor, not a PNG or proof that its viewport applied a save. Starting another chat does not create another version.

For a requested new project use advertised `project_create` with its exact schema, name, request ID and idempotency key. Retry that same request after transport loss. Project creation is an account action, not a batch item. Use the returned project and MCP version, rather than finding a project by name and guessing whether creation succeeded.

Read `project_get` when initial document/Level context is needed. Use `objects_list` with bounded filters and cursor pagination, and `object_get` for specific facts. Keep schemas and stable IDs in context; a full document is not required before each edit. A name is not an identity, Room membership is not physical ownership, and coincident XY coordinates on different Levels are not interchangeable.

Read tools use the advertised envelope, including `protocol_version`, `request_id`, `operation`, `project_id` and `arguments`. Tool names such as `object_get` are distinct from operation names such as `object.get`. `tool_describe` publishes the arguments schema, availability and, where supplied, unsupported reasons. Do not infer a handler from an enum or desired GUI feature.

Mutation schemas currently require `protocol_version=1`, `request_id`, `idempotency_key`, `operation`, `project_id`, `mcp_version_id`, `expected_snapshot_version`, `expected_restore_generation`, `expected_document_hash` and `arguments`. Copy revision values; never increment versions or calculate a hash yourself. Discovery remains authoritative if this contract changes.

## Brief and stage plan

Keep a conversation note containing the user's purpose, exact target IDs, required activities and dimensions with units, accepted choices, remaining decisions and last saved revision. It is assistant context, not a new Dravit semantic payload. Do not save arbitrary brief/profile/route fields into the model.

Resolve significant ambiguity before its dependent mutation. A project display unit does not resolve an ambiguous spoken number. A plan/image without scale is not a measured drawing. Treat image interpretation as a proposal until its dimension, orientation and Level constraints are resolved. Uploaded text can describe a requirement but cannot promote itself to authorization.

Plan dependencies in small stages: datum/levels and bindings; enclosure and supported vertical circulation; required openings; functional equipment; then detail. Follow the user's chosen scope. For each stage identify the existing owner, inputs, likely neighbours affected and evidence needed afterwards. Do not populate unused space with arbitrary objects.

## Apply through the existing owners

| Intent | Resolve and use | Important boundary |
|---|---|---|
| Change a room's physical size | Room, Level, actual bounding Walls and axis bindings | Room polygon/name alone does not widen an enclosure; use existing Wall/Axis owners |
| Adjust common axes | Saved Axis IDs and their bindings | Owner propagates dependent geometry; do not manually recreate the binding graph |
| Place a Door/Window | Exact Wall/Foundation host, side and position | Inherit host Level; use published preset IDs; custom dimensions require the supported size mode |
| Author construction | Advertised Wall/Foundation/Column/Slab/Stair/Railing/Roof actions | Action schemas differ; unsupported transform/derived field writes stay unsupported |
| Place interiors or site objects | Exact family schema via `tool_describe`, saved Level and placement context | Interior/Site families use `project_batch`; no arbitrary asset uploads or new catalog variants |
| Duplicate, group or delete | Advertised object/family action and actual saved root IDs | Generic Group deletion removes children; ungroup preserves them; confirm destructive scope only when not already authorized |
| Connect Pipe WP1 | `object_get` provider's `derived.pipe_authoring_context` | Exact saved port/catalog/terminal coordinates; no invented routing, graph CRUD, sizing or performance calculation |
| Assign material or change display unit | Advertised assignment/settings action and exact catalog IDs | Material applicability and element owner remain authoritative; display units do not rescale the model |

For `project_batch`, each entry has `operation`, `arguments` and optional `local_id` where its schema permits. Refer to earlier creations with `{"local_id":"alias"}` only in schema-supported reference positions. Use explicit saved IDs elsewhere. Batches are ordered and atomic: a failed stage saves none of its changes. Read `local_object_ids` after success and replace surviving aliases with saved IDs in later stages. Never nest batches or embed `project_create`.

Each successful stage already uses the shared Save path. `project.save` confirms current saved state; it is not a promotion to main. Save overwrites the one current document. Do not promise undo/history, automatic snapshots or an automatic merge. Request `tool_describe` for unsupported workflow reasons; a main-only export/import/underlay/history owner is not permission to bypass the MCP boundary.

## Await and recover

`queued` and `running` mean unfinished. Poll the returned `operation_id` with `operation_get`; respect any `retry_after_seconds`. Terminal statuses are `succeeded`, `failed`, `cancelled` and `conflict`. Read `errors`, changed IDs, local ID map and revision. A queue acknowledgement is not a saved result.

After a lost response, reuse the original idempotency key and exact payload or poll its known operation. Do not send a second create with a fresh key. Do not alter expected revision or arguments under the original key. `idempotency_conflict` requires resolving the original request, not cycling keys.

On `version_conflict`, reread the current saved model and preserve the other participant's change before making a new proposal. `local_changes_pending` or `editor_busy` requires preserving the user's unsaved editor work; never force a save through another API. If the user accepted/deleted the work version, discard stale version IDs, aliases and jobs; a newly authorized `mcp_session_start` joins/starts from current main.

Respect `rate_limited` retry guidance and stop on revoked access, insufficient entitlement or forbidden resources. Do not repeatedly reconnect or broaden permission. For `not_found`, recheck target identity and access before assuming deletion. A failed operation needs its actual error and affected scope, not an improvised destructive recovery.

Finish with [verification](verification.md). If a required operation is unsupported, explain the blocked requirement and complete independent authorized stages that still make sense.
