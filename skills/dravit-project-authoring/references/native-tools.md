# Native MCP tools

These are registered `tools/call` names. Client prefixes are presentation only. Inner operation strings retain dots. An object operation absent here uses `project_batch`, not a guessed tool name. See [protocol](protocol.md). For authoring tools the `arguments` schema is linked through its operation reference rather than duplicated below.

## axis_create

Operation: `axis.create`.

Create a construction axis in the shared MCP document at an explicit metre coordinate. orientation is vertical, horizontal or custom; custom supports angle in degrees. Optional label. Returns the stable axis object ID through operation_get. Creation captures construction anchors on the new axis using the GUI owner. Axis grid GUI misclick locks do not block creation. Main is unchanged.

```json
{"type":"object","additionalProperties":false,"required":["protocol_version","request_id","idempotency_key","operation","project_id","mcp_version_id","expected_snapshot_version","expected_restore_generation","expected_document_hash","arguments"],"properties":{"protocol_version":{"type":"integer","enum":[1]},"request_id":{"type":"string","minLength":1,"maxLength":128},"idempotency_key":{"type":"string","minLength":1,"maxLength":128},"operation":{"type":"string","enum":["axis.create"]},"project_id":{"type":"string","minLength":1,"maxLength":255},"mcp_version_id":{"type":"string","pattern":"^[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}$"},"expected_snapshot_version":{"type":"integer","minimum":1},"expected_restore_generation":{"type":"integer","minimum":1},"expected_document_hash":{"type":"string","pattern":"^[a-f0-9]{64}$"},"arguments":{"description":"Use the exact axis.create arguments schema from the command reference."}}}
```

## axis_delete

Operation: `axis.delete`.

Delete one construction axis (axis and grid GUI misclick locks do not block MCP) and its saved anchor bindings from the shared MCP document. Physical construction geometry remains in place. Uses exact revision and stable idempotency_key; poll operation_get. Main is unchanged.

```json
{"type":"object","additionalProperties":false,"required":["protocol_version","request_id","idempotency_key","operation","project_id","mcp_version_id","expected_snapshot_version","expected_restore_generation","expected_document_hash","arguments"],"properties":{"protocol_version":{"type":"integer","enum":[1]},"request_id":{"type":"string","minLength":1,"maxLength":128},"idempotency_key":{"type":"string","minLength":1,"maxLength":128},"operation":{"type":"string","enum":["axis.delete"]},"project_id":{"type":"string","minLength":1,"maxLength":255},"mcp_version_id":{"type":"string","pattern":"^[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}$"},"expected_snapshot_version":{"type":"integer","minimum":1},"expected_restore_generation":{"type":"integer","minimum":1},"expected_document_hash":{"type":"string","pattern":"^[a-f0-9]{64}$"},"arguments":{"description":"Use the exact axis.delete arguments schema from the command reference."}}}
```

## axis_update

Operation: `axis.update`.

Edit an existing axis by its exact object_id. Supports label, coordinate in metres, custom angle, locked, construction_lock_enabled, explicit bindings and adjacent spacing. bindings replaces the axis graph with existing object_id/anchor_id pairs, measuring offsets from current geometry; [] detaches all. Read saved construction_bindings first. Anchor IDs: Wall/Foundation baseline.start or baseline.end; Column center; Stair start; Slab outer.<vertex index> or hole.<hole index>.<vertex index>; Roof mass.<mass id>.<vertex id> (footprint outer.<vertex index>). Use saved object geometry and exact IDs, never invent anchors. A coordinate change moves only saved bound anchors through shared GUI geometry and dependent Room/host checks. spacing={from_axis_id,distance:{value,unit:"m"}} uses GUI adjacent-interval composition, preserving other intervals. Do not combine coordinate and spacing. Disabling construction lock detaches bindings; enabling captures current aligned anchors. Axis and axis grid locks are GUI misclick guards only: edits apply through them and keep the lock flags; change locked only when the user asks. Use the latest exact revision, stable idempotency_key, and poll operation_get. Main is unchanged.

```json
{"type":"object","additionalProperties":false,"required":["protocol_version","request_id","idempotency_key","operation","project_id","mcp_version_id","expected_snapshot_version","expected_restore_generation","expected_document_hash","arguments"],"properties":{"protocol_version":{"type":"integer","enum":[1]},"request_id":{"type":"string","minLength":1,"maxLength":128},"idempotency_key":{"type":"string","minLength":1,"maxLength":128},"operation":{"type":"string","enum":["axis.update"]},"project_id":{"type":"string","minLength":1,"maxLength":255},"mcp_version_id":{"type":"string","pattern":"^[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}$"},"expected_snapshot_version":{"type":"integer","minimum":1},"expected_restore_generation":{"type":"integer","minimum":1},"expected_document_hash":{"type":"string","pattern":"^[a-f0-9]{64}$"},"arguments":{"description":"Use the exact axis.update arguments schema from the command reference."}}}
```

## catalog_type_create

Operation: `catalog.type.create`.

Create a project-local custom type using family wall, foundation or opening. Wall: name, description, role, metre thickness, currency_code, exact recipe_code and positive complete_unit_price; price_basis is derived. Foundation: name, description, kind, wall_component/footing_component/blinding_component (nullable width/height in metres), currency_code and complete_unit_price_per_m3. Concrete is fixed; zero is the existing unpriced placeholder. Read saved definitions in project_get.document.editor.wall_types or foundation_types. Poll operation_get for the stable type ID and use kind custom in wall_type or foundation_type. Type deletion is unsupported.

```json
{"type":"object","additionalProperties":false,"required":["protocol_version","request_id","idempotency_key","operation","project_id","mcp_version_id","expected_snapshot_version","expected_restore_generation","expected_document_hash","arguments"],"properties":{"protocol_version":{"type":"integer","enum":[1]},"request_id":{"type":"string","minLength":1,"maxLength":128},"idempotency_key":{"type":"string","minLength":1,"maxLength":128},"operation":{"type":"string","enum":["catalog.type.create"]},"project_id":{"type":"string","minLength":1,"maxLength":255},"mcp_version_id":{"type":"string","pattern":"^[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}$"},"expected_snapshot_version":{"type":"integer","minimum":1},"expected_restore_generation":{"type":"integer","minimum":1},"expected_document_hash":{"type":"string","pattern":"^[a-f0-9]{64}$"},"arguments":{"description":"Use the exact catalog.type.create arguments schema from the command reference."}}}
```

## catalog_type_update

Operation: `catalog.type.update`.

Edit a saved project-local Wall or Foundation type using exact object_id and family wall or foundation. Omitted fields are preserved; Foundation component null explicitly removes that component. Existing GUI owners update all bound instances on every Level, retaining host and axis guards. Wall recipe changes require a new positive complete_unit_price; Foundation price is complete_unit_price_per_m3 and zero keeps the GUI unpriced semantics. Fixed concrete and derived values are readonly. Read definitions and affected objects after Save. Built-in type editing and deletion are unsupported. Reuse the idempotency key on retries.

```json
{"type":"object","additionalProperties":false,"required":["protocol_version","request_id","idempotency_key","operation","project_id","mcp_version_id","expected_snapshot_version","expected_restore_generation","expected_document_hash","arguments"],"properties":{"protocol_version":{"type":"integer","enum":[1]},"request_id":{"type":"string","minLength":1,"maxLength":128},"idempotency_key":{"type":"string","minLength":1,"maxLength":128},"operation":{"type":"string","enum":["catalog.type.update"]},"project_id":{"type":"string","minLength":1,"maxLength":255},"mcp_version_id":{"type":"string","pattern":"^[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}$"},"expected_snapshot_version":{"type":"integer","minimum":1},"expected_restore_generation":{"type":"integer","minimum":1},"expected_document_hash":{"type":"string","pattern":"^[a-f0-9]{64}$"},"arguments":{"description":"Use the exact catalog.type.update arguments schema from the command reference."}}}
```

## column_create

Operation: `column.create`.

Expose the existing Column create action in the shared MCP document. Use exact saved IDs, explicit units and revision, then poll operation_get. Derived geometry and transforms are unsupported.

```json
{"type":"object","additionalProperties":false,"required":["protocol_version","request_id","idempotency_key","operation","project_id","mcp_version_id","expected_snapshot_version","expected_restore_generation","expected_document_hash","arguments"],"properties":{"protocol_version":{"type":"integer","enum":[1]},"request_id":{"type":"string","minLength":1,"maxLength":128},"idempotency_key":{"type":"string","minLength":1,"maxLength":128},"operation":{"type":"string","enum":["column.create"]},"project_id":{"type":"string","minLength":1,"maxLength":255},"mcp_version_id":{"type":"string","pattern":"^[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}$"},"expected_snapshot_version":{"type":"integer","minimum":1},"expected_restore_generation":{"type":"integer","minimum":1},"expected_document_hash":{"type":"string","pattern":"^[a-f0-9]{64}$"},"arguments":{"description":"Use the exact column.create arguments schema from the command reference."}}}
```

## column_delete

Operation: `column.delete`.

Expose the existing Column delete action in the shared MCP document. Use exact saved IDs, explicit units and revision, then poll operation_get. Derived geometry and transforms are unsupported.

```json
{"type":"object","additionalProperties":false,"required":["protocol_version","request_id","idempotency_key","operation","project_id","mcp_version_id","expected_snapshot_version","expected_restore_generation","expected_document_hash","arguments"],"properties":{"protocol_version":{"type":"integer","enum":[1]},"request_id":{"type":"string","minLength":1,"maxLength":128},"idempotency_key":{"type":"string","minLength":1,"maxLength":128},"operation":{"type":"string","enum":["column.delete"]},"project_id":{"type":"string","minLength":1,"maxLength":255},"mcp_version_id":{"type":"string","pattern":"^[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}$"},"expected_snapshot_version":{"type":"integer","minimum":1},"expected_restore_generation":{"type":"integer","minimum":1},"expected_document_hash":{"type":"string","pattern":"^[a-f0-9]{64}$"},"arguments":{"description":"Use the exact column.delete arguments schema from the command reference."}}}
```

## column_update

Operation: `column.update`.

Expose the existing Column update action in the shared MCP document. Use exact saved IDs, explicit units and revision, then poll operation_get. Derived geometry and transforms are unsupported.

```json
{"type":"object","additionalProperties":false,"required":["protocol_version","request_id","idempotency_key","operation","project_id","mcp_version_id","expected_snapshot_version","expected_restore_generation","expected_document_hash","arguments"],"properties":{"protocol_version":{"type":"integer","enum":[1]},"request_id":{"type":"string","minLength":1,"maxLength":128},"idempotency_key":{"type":"string","minLength":1,"maxLength":128},"operation":{"type":"string","enum":["column.update"]},"project_id":{"type":"string","minLength":1,"maxLength":255},"mcp_version_id":{"type":"string","pattern":"^[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}$"},"expected_snapshot_version":{"type":"integer","minimum":1},"expected_restore_generation":{"type":"integer","minimum":1},"expected_document_hash":{"type":"string","pattern":"^[a-f0-9]{64}$"},"arguments":{"description":"Use the exact column.update arguments schema from the command reference."}}}
```

## door_create

Operation: `door.create`.

Create a hosted Door using an exact opening preset ID and a Wall or Foundation host. Custom size requires explicit width. Level is inherited from the host.

```json
{"type":"object","additionalProperties":false,"required":["protocol_version","request_id","idempotency_key","operation","project_id","mcp_version_id","expected_snapshot_version","expected_restore_generation","expected_document_hash","arguments"],"properties":{"protocol_version":{"type":"integer","enum":[1]},"request_id":{"type":"string","minLength":1,"maxLength":128},"idempotency_key":{"type":"string","minLength":1,"maxLength":128},"operation":{"type":"string","enum":["door.create"]},"project_id":{"type":"string","minLength":1,"maxLength":255},"mcp_version_id":{"type":"string","pattern":"^[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}$"},"expected_snapshot_version":{"type":"integer","minimum":1},"expected_restore_generation":{"type":"integer","minimum":1},"expected_document_hash":{"type":"string","pattern":"^[a-f0-9]{64}$"},"arguments":{"description":"Use the exact door.create arguments schema from the command reference."}}}
```

## door_delete

Operation: `door.delete`.

Delete one hosted Door through the existing editor deletion lifecycle.

```json
{"type":"object","additionalProperties":false,"required":["protocol_version","request_id","idempotency_key","operation","project_id","mcp_version_id","expected_snapshot_version","expected_restore_generation","expected_document_hash","arguments"],"properties":{"protocol_version":{"type":"integer","enum":[1]},"request_id":{"type":"string","minLength":1,"maxLength":128},"idempotency_key":{"type":"string","minLength":1,"maxLength":128},"operation":{"type":"string","enum":["door.delete"]},"project_id":{"type":"string","minLength":1,"maxLength":255},"mcp_version_id":{"type":"string","pattern":"^[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}$"},"expected_snapshot_version":{"type":"integer","minimum":1},"expected_restore_generation":{"type":"integer","minimum":1},"expected_document_hash":{"type":"string","pattern":"^[a-f0-9]{64}$"},"arguments":{"description":"Use the exact door.delete arguments schema from the command reference."}}}
```

## door_update

Operation: `door.update`.

Edit a hosted Door using existing GUI settings or host/center_ratio/side. Enable custom size before changing dimensions. Derived geometry is read-only.

```json
{"type":"object","additionalProperties":false,"required":["protocol_version","request_id","idempotency_key","operation","project_id","mcp_version_id","expected_snapshot_version","expected_restore_generation","expected_document_hash","arguments"],"properties":{"protocol_version":{"type":"integer","enum":[1]},"request_id":{"type":"string","minLength":1,"maxLength":128},"idempotency_key":{"type":"string","minLength":1,"maxLength":128},"operation":{"type":"string","enum":["door.update"]},"project_id":{"type":"string","minLength":1,"maxLength":255},"mcp_version_id":{"type":"string","pattern":"^[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}$"},"expected_snapshot_version":{"type":"integer","minimum":1},"expected_restore_generation":{"type":"integer","minimum":1},"expected_document_hash":{"type":"string","pattern":"^[a-f0-9]{64}$"},"arguments":{"description":"Use the exact door.update arguments schema from the command reference."}}}
```

## dravit_guide

Operation: `guide.read`.

Read the pinned Dravit authoring skill without local filesystem access. Start with overview and protocol. Load the relevant commands-* schema section, structure-recipes or catalog-recipes and examples-* for exact requests for every supported object family and action. Use operation on command/example collections and optional example_id to retrieve a bounded excerpt. native-tools maps registered calls, availability records unsupported workflows; workflow, verification, spatial-reasoning and human-use explain modeling and evidence. Returns all available_sections, exact version, draft/release status, checksums and compatibility. This delivers instructions, not client installation. Keep expected_version and expected_content_sha256 for subsequent sections within a modelling stage; on version_conflict finish or stop the stage before loading a new guide. Draft is unreleased and available only when explicitly enabled by the server. No project is selected or changed.

```json
{"type":"object","additionalProperties":false,"properties":{"section":{"type":"string","enum":["overview","workflow","verification","spatial-reasoning","human-use","protocol","native-tools","availability","commands-structure","commands-openings","commands-roof","commands-circulation","commands-interior","commands-site","commands-pipes","commands-generic","commands-workflows","structure-recipes","catalog-recipes","examples-structure","examples-catalog","examples-workflows","examples-protocol"],"default":"overview"},"expected_version":{"type":"string","minLength":1,"maxLength":64},"expected_content_sha256":{"type":"string","pattern":"^[a-f0-9]{64}$"},"operation":{"type":"string","pattern":"^[a-z][a-z0-9_.]{0,127}$","description":"Select one exact dotted operation from a commands-* or examples-structure/catalog/workflows section. Prefer this to loading an entire command catalog."},"example_id":{"type":"string","minLength":1,"maxLength":128,"description":"With operation on an examples section, select one exact example ID returned by that collection."}}}
```

## editor_sessions

Operation: `editor.sessions`.

Read short-lived advisory context published by your own open MCP editor windows for an explicit project, MCP version and exact saved revision. First omit window_id to list windows without selection. Select a window explicitly, then repeat with that window_id to read its saved-model selection, Level, view and client-reported readiness. Never choose the last-active/focused window automatically. No editor commands run. Context is not authorization, proof of Reverb delivery, or an image; gestures and nested selections may be unknown. Expired, closed-copy and stale-revision contexts are unavailable.

```json
{"type":"object","additionalProperties":false,"required":["protocol_version","request_id","operation","project_id","arguments"],"properties":{"protocol_version":{"type":"integer","enum":[1]},"request_id":{"type":"string","minLength":1,"maxLength":128},"operation":{"type":"string","enum":["editor.sessions"]},"project_id":{"type":"string","minLength":1,"maxLength":255},"arguments":{"type":"object","additionalProperties":false,"required":["revision"],"properties":{"revision":{"type":"object","additionalProperties":false,"required":["project_id","mcp_version_id","snapshot_version","restore_generation","document_hash"],"properties":{"project_id":{"type":"string","minLength":1,"maxLength":255},"mcp_version_id":{"type":"string","format":"uuid"},"snapshot_version":{"type":"integer","minimum":1},"restore_generation":{"type":"integer","minimum":1},"document_hash":{"type":"string","pattern":"^[a-f0-9]{64}$"}}},"window_id":{"type":"string","format":"uuid","description":"An explicit window ID from editor.sessions. Omit only to list windows without selection; never auto-select a focused or last-active window."}}}}}
```

## foundation_create

Operation: `foundation.create`.

Expose the existing Foundation create action in the shared MCP document. Section is owned by a built-in or custom Foundation type; quantities are derived. Use exact saved Level/type IDs and metre units. Poll operation_get. Transform and independent section editing are unsupported.

```json
{"type":"object","additionalProperties":false,"required":["protocol_version","request_id","idempotency_key","operation","project_id","mcp_version_id","expected_snapshot_version","expected_restore_generation","expected_document_hash","arguments"],"properties":{"protocol_version":{"type":"integer","enum":[1]},"request_id":{"type":"string","minLength":1,"maxLength":128},"idempotency_key":{"type":"string","minLength":1,"maxLength":128},"operation":{"type":"string","enum":["foundation.create"]},"project_id":{"type":"string","minLength":1,"maxLength":255},"mcp_version_id":{"type":"string","pattern":"^[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}$"},"expected_snapshot_version":{"type":"integer","minimum":1},"expected_restore_generation":{"type":"integer","minimum":1},"expected_document_hash":{"type":"string","pattern":"^[a-f0-9]{64}$"},"arguments":{"description":"Use the exact foundation.create arguments schema from the command reference."}}}
```

## foundation_delete

Operation: `foundation.delete`.

Expose the existing Foundation delete action in the shared MCP document. Section is owned by a built-in or custom Foundation type; quantities are derived. Use exact saved Level/type IDs and metre units. Poll operation_get. Transform and independent section editing are unsupported.

```json
{"type":"object","additionalProperties":false,"required":["protocol_version","request_id","idempotency_key","operation","project_id","mcp_version_id","expected_snapshot_version","expected_restore_generation","expected_document_hash","arguments"],"properties":{"protocol_version":{"type":"integer","enum":[1]},"request_id":{"type":"string","minLength":1,"maxLength":128},"idempotency_key":{"type":"string","minLength":1,"maxLength":128},"operation":{"type":"string","enum":["foundation.delete"]},"project_id":{"type":"string","minLength":1,"maxLength":255},"mcp_version_id":{"type":"string","pattern":"^[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}$"},"expected_snapshot_version":{"type":"integer","minimum":1},"expected_restore_generation":{"type":"integer","minimum":1},"expected_document_hash":{"type":"string","pattern":"^[a-f0-9]{64}$"},"arguments":{"description":"Use the exact foundation.delete arguments schema from the command reference."}}}
```

## foundation_update

Operation: `foundation.update`.

Expose the existing Foundation update action in the shared MCP document. Section is owned by a built-in or custom Foundation type; quantities are derived. Use exact saved Level/type IDs and metre units. Poll operation_get. Transform and independent section editing are unsupported.

```json
{"type":"object","additionalProperties":false,"required":["protocol_version","request_id","idempotency_key","operation","project_id","mcp_version_id","expected_snapshot_version","expected_restore_generation","expected_document_hash","arguments"],"properties":{"protocol_version":{"type":"integer","enum":[1]},"request_id":{"type":"string","minLength":1,"maxLength":128},"idempotency_key":{"type":"string","minLength":1,"maxLength":128},"operation":{"type":"string","enum":["foundation.update"]},"project_id":{"type":"string","minLength":1,"maxLength":255},"mcp_version_id":{"type":"string","pattern":"^[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}$"},"expected_snapshot_version":{"type":"integer","minimum":1},"expected_restore_generation":{"type":"integer","minimum":1},"expected_document_hash":{"type":"string","pattern":"^[a-f0-9]{64}$"},"arguments":{"description":"Use the exact foundation.update arguments schema from the command reference."}}}
```

## level_create

Operation: `level.create`.

Create one level from a label and an elevation in metres. The first level must be Level 0 at zero elevation. Returns its stable level ID. Existing dependent elements follow the same rules as GUI authoring. Uses only the exact shared MCP version from mcp_session_start. Send the latest revision/hash and a stable idempotency_key. Main is unchanged.

```json
{"type":"object","additionalProperties":false,"required":["protocol_version","request_id","idempotency_key","operation","project_id","mcp_version_id","expected_snapshot_version","expected_restore_generation","expected_document_hash","arguments"],"properties":{"protocol_version":{"type":"integer","enum":[1]},"request_id":{"type":"string","minLength":1,"maxLength":128},"idempotency_key":{"type":"string","minLength":1,"maxLength":128},"operation":{"type":"string","enum":["level.create"]},"project_id":{"type":"string","minLength":1,"maxLength":255},"mcp_version_id":{"type":"string","pattern":"^[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}$"},"expected_snapshot_version":{"type":"integer","minimum":1},"expected_restore_generation":{"type":"integer","minimum":1},"expected_document_hash":{"type":"string","pattern":"^[a-f0-9]{64}$"},"arguments":{"description":"Use the exact level.create arguments schema from the command reference."}}}
```

## level_delete

Operation: `level.delete`.

Delete one Level by stable object_id; its GUI misclick lock does not block MCP. Direct Home/Base owners must first be reassigned; secondary upper constraints detach while preserving authored geometry. Pipe datum guards are the same as GUI. Uses only the exact shared MCP revision/idempotency_key; poll operation_get. Main is unchanged.

```json
{"type":"object","additionalProperties":false,"required":["protocol_version","request_id","idempotency_key","operation","project_id","mcp_version_id","expected_snapshot_version","expected_restore_generation","expected_document_hash","arguments"],"properties":{"protocol_version":{"type":"integer","enum":[1]},"request_id":{"type":"string","minLength":1,"maxLength":128},"idempotency_key":{"type":"string","minLength":1,"maxLength":128},"operation":{"type":"string","enum":["level.delete"]},"project_id":{"type":"string","minLength":1,"maxLength":255},"mcp_version_id":{"type":"string","pattern":"^[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}$"},"expected_snapshot_version":{"type":"integer","minimum":1},"expected_restore_generation":{"type":"integer","minimum":1},"expected_document_hash":{"type":"string","pattern":"^[a-f0-9]{64}$"},"arguments":{"description":"Use the exact level.delete arguments schema from the command reference."}}}
```

## level_update

Operation: `level.update`.

Update a level label, elevation in metres or locked flag. Bound elements and pipe nodes follow the common GUI level rules. Level locks are GUI misclick guards only: edits apply to locked Levels and keep their locked flag; change locked only when the user asks. Uses only the exact shared MCP version from mcp_session_start. Send the latest revision/hash and a stable idempotency_key. Main is unchanged.

```json
{"type":"object","additionalProperties":false,"required":["protocol_version","request_id","idempotency_key","operation","project_id","mcp_version_id","expected_snapshot_version","expected_restore_generation","expected_document_hash","arguments"],"properties":{"protocol_version":{"type":"integer","enum":[1]},"request_id":{"type":"string","minLength":1,"maxLength":128},"idempotency_key":{"type":"string","minLength":1,"maxLength":128},"operation":{"type":"string","enum":["level.update"]},"project_id":{"type":"string","minLength":1,"maxLength":255},"mcp_version_id":{"type":"string","pattern":"^[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}$"},"expected_snapshot_version":{"type":"integer","minimum":1},"expected_restore_generation":{"type":"integer","minimum":1},"expected_document_hash":{"type":"string","pattern":"^[a-f0-9]{64}$"},"arguments":{"description":"Use the exact level.update arguments schema from the command reference."}}}
```

## mcp_session_start

Operation: `mcp.session.start`.

Start or join the one shared MCP work version of a project. Call this before reading or changing its model. Returns the exact work-version ID and a separate 2D/3D editor URL. The main project is unchanged. Repeated starts join the same saved work; after a user closes a version an explicit new start joins a fresh copy.

```json
{"type":"object","additionalProperties":false,"required":["project_id"],"properties":{"project_id":{"type":"string","minLength":1,"maxLength":255}}}
```

## object_get

Operation: `object.get`.

Read one saved object by stable object_id with actual bindings and parameters. For a Roof without parameters.masses, use exact existing mass and boundary IDs from derived.roof_authoring_context.masses. This read-only GUI authoring context does not change saved parameters, document or revision; null means unavailable. For a profiled Water Heater, derived.pipe_authoring_context provides the verified catalog, exact cold_in port position/direction/frame, occupied state and terminal_center used by pipe.route.create. Pipe network parameters expose saved graph IDs and parent_id is the PlumbingSystem. Missing spatial facts are explicitly unknown.

```json
{"type":"object","additionalProperties":false,"required":["protocol_version","request_id","operation","project_id","arguments"],"properties":{"protocol_version":{"type":"integer","enum":[1]},"request_id":{"type":"string","minLength":1,"maxLength":128},"operation":{"type":"string","enum":["object.get"]},"project_id":{"type":"string","minLength":1,"maxLength":255},"arguments":{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255},"kind":{"type":"string","minLength":1,"maxLength":255}}}}}
```

## objects_list

Operation: `objects.list`.

Read saved objects, levels, axes and pipe networks in stable ID order. Filter by kind, parent_id or level_id; follow next_cursor only with the same filters and revision.

```json
{"type":"object","additionalProperties":false,"required":["protocol_version","request_id","operation","project_id","arguments"],"properties":{"protocol_version":{"type":"integer","enum":[1]},"request_id":{"type":"string","minLength":1,"maxLength":128},"operation":{"type":"string","enum":["objects.list"]},"project_id":{"type":"string","minLength":1,"maxLength":255},"arguments":{"type":"object","additionalProperties":false,"properties":{"limit":{"type":"integer","minimum":1,"maximum":100,"default":25},"cursor":{"type":"string","minLength":1,"maxLength":4096},"kind":{"type":"string","minLength":1,"maxLength":255},"parent_id":{"type":"string","minLength":1,"maxLength":255},"level_id":{"type":"string","minLength":1,"maxLength":255}}}}}
```

## operation_get

Operation: `operation.get`.

Read a durable command or preview result using its operation_id. A succeeded preview includes a model-readable PNG and its exact revision/visible/omitted IDs. Only the originating connection can read it, while its project and work version remain accessible. A succeeded result confirms a database commit; it does not claim editor delivery.

```json
{"type":"object","additionalProperties":false,"required":["operation_id"],"properties":{"operation_id":{"type":"string","minLength":1,"maxLength":255}}}
```

## project_batch

Operation: `project.batch`.

Apply an ordered small batch of supported axis/Level/Wall/Room/Foundation/Column/Slab/Stair/Railing/Roof/Door/Window, Generic Shape/Group, Interior and Site/Exterior family operations, existing Pipe WP1 route/endpoint/roll/delete commands plus object.duplicate/delete/material.assign, project.settings.update (length_unit only), project.save and custom Wall/Foundation/Opening type commands with one atomic Save in the exact MCP version. Generic Shape/Group support create/update/transform/delete; Group update changes only its name, and object.ungroup releases existing Group children. Each entry has operation, arguments and optional local_id on creates and object.duplicate. project_create is a separate account tool, unavailable in batches. Use {"local_id":"name"} in object_id, level_id, top_level_id, room_id, host_wall_id, host_fence_id, provider_object_id, network_id or custom wall_type.id/foundation_type.id to refer to an earlier create. Generic Group object_ids accepts ordered stable Shape IDs or earlier generic_shape.create local references. Group-target operations accept earlier generic_group.create references. Nested batches and other commands are unsupported. Any failure rolls back the whole stage. Poll operation_get; local_object_ids maps surviving aliases to saved stable IDs. Reuse the idempotency key on retry.

```json
{"type":"object","additionalProperties":false,"required":["protocol_version","request_id","idempotency_key","operation","project_id","mcp_version_id","expected_snapshot_version","expected_restore_generation","expected_document_hash","arguments"],"properties":{"protocol_version":{"type":"integer","enum":[1]},"request_id":{"type":"string","minLength":1,"maxLength":128},"idempotency_key":{"type":"string","minLength":1,"maxLength":128},"operation":{"type":"string","enum":["project.batch"]},"project_id":{"type":"string","minLength":1,"maxLength":255},"mcp_version_id":{"type":"string","pattern":"^[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}$"},"expected_snapshot_version":{"type":"integer","minimum":1},"expected_restore_generation":{"type":"integer","minimum":1},"expected_document_hash":{"type":"string","pattern":"^[a-f0-9]{64}$"},"arguments":{"description":"Use the exact project.batch arguments schema from the command reference."}}}
```

## project_create

Operation: `project.create`.

Create a new standard project in the connected paid account and atomically start its shared MCP work version. Account project quotas and permissions apply. Pass name, request_id and idempotency_key only; no existing project or model revision is required. Reuse the same key and exact name after transport failure; retries return the original creation revision and never create another project. Read current state if that revision was edited later. A deleted or closed work version is not recreated by a retry. This account operation is unavailable inside project_batch.

```json
{"type":"object","additionalProperties":false,"required":["request_id","idempotency_key","name"],"properties":{"request_id":{"type":"string","minLength":1,"maxLength":128},"idempotency_key":{"type":"string","minLength":1,"maxLength":128},"name":{"type":"string","minLength":1,"maxLength":255}}}
```

## project_get

Operation: `project.get`.

Read the complete saved project and revision. Set include_document=false for a bounded summary; use objects_list for large models.

```json
{"type":"object","additionalProperties":false,"required":["protocol_version","request_id","operation","project_id","arguments"],"properties":{"protocol_version":{"type":"integer","enum":[1]},"request_id":{"type":"string","minLength":1,"maxLength":128},"operation":{"type":"string","enum":["project.get"]},"project_id":{"type":"string","minLength":1,"maxLength":255},"arguments":{"type":"object","additionalProperties":false,"properties":{"include_document":{"type":"boolean","default":true}}}}}
```

## project_validate

Operation: `project.validate`.

Read existing validation results for the exact current saved MCP revision without changing the document. Returns original semantic material/geometry-binding diagnostics and RequiredMaterial/MissingCalculationResult rule messages, statuses, references and suggested fixes. Those binding owners inspect semantic objects only. object_results separately delivers saved Column/Stair/Door/Window statuses/messages and the existing current GUI Door/Window host/own-parameter checks, without renderer or full hydration. requires_review is never upgraded to pass. The full coverage matrix explicitly reports parser-admission-only, authoring-guard-only, missing-input unknown and unavailable unsupported checks on every page, including when no issues exist. Parser acceptance and opening modelling status are not collision, support, engineering or Window-purpose approval. No routes, clearance facts, thresholds, profiles, new checks, calculations, overlays or repairs are invented. Supply the complete saved revision; revoked/deleted/stale targets fail, and access plus revision are rechecked after evaluation, including cached results. Repeated pages reuse original owner results for up to 60 seconds for that exact revision. Issues and object_results share limit/cursor pagination; follow next_cursor even if issues is empty. Report/record IDs are deterministic and bound to the validation contract. This bounded read is synchronous; no operation polling is needed. Use existing supported commands for corrections, then request the new saved revision.

```json
{"type":"object","additionalProperties":false,"required":["revision"],"properties":{"revision":{"type":"object","additionalProperties":false,"required":["project_id","mcp_version_id","snapshot_version","restore_generation","document_hash"],"properties":{"project_id":{"type":"string","minLength":1,"maxLength":255},"mcp_version_id":{"type":"string","format":"uuid"},"snapshot_version":{"type":"integer","minimum":1},"restore_generation":{"type":"integer","minimum":1},"document_hash":{"type":"string","pattern":"^[a-f0-9]{64}$"}}},"limit":{"type":"integer","minimum":1,"maximum":100,"default":25,"description":"Maximum original issue/object-result records on this page. Every page includes the entire coverage matrix."},"cursor":{"type":["string","null"],"minLength":1,"maxLength":8192,"description":"Opaque next_cursor from this exact report revision. Other tool, project or MCP-version cursors are rejected."}}}
```

## project_view

Operation: `project.view`.

Queue a real Top, Front, Back, Left, Right or 3D image of the exact current MCP revision. Pass the complete revision and explicit saved level_id from project_get. Save invalidates older artifacts and jobs. Top uses the chosen working plane; 3D shows that Level and lower Levels. Use the saved Room Level for Room focus. object_ids isolate existing owners; clip crops Top/3D only. Side supports existing Column, Door, Foundation, Railing, Roof, Slab, Stair, Wall, Window, Axis and Level owners. Catalog Side and Room Side/3D are unsupported. Pipe network, segment, fitting and node support Top/Front/3D; ports have no independent glyph. Mixed selections report omissions; exclusive unsupported focus returns not_supported. Optional filters use existing display categories, shown-through Level and copied Top underlays. camera selects existing isometric/perspective 3D framing. No navigation or visibility is saved. Copied underlays use separate reference_sources receipts; inherited IFC context reports preview_delivery_unsupported. Roof nested geometry is observed through its parent Roof; independent nested focus and validator overlays are unsupported. Poll operation_get for a PNG with exact revision, options and visible/omitted IDs. Omitted IDs never prove absence; multiple applicable views are needed for visual checks.

```json
{"type":"object","additionalProperties":false,"required":["revision","view","level_id"],"properties":{"revision":{"type":"object","additionalProperties":false,"required":["project_id","mcp_version_id","snapshot_version","restore_generation","document_hash"],"properties":{"project_id":{"type":"string","minLength":1,"maxLength":255},"mcp_version_id":{"type":"string","format":"uuid"},"snapshot_version":{"type":"integer","minimum":1},"restore_generation":{"type":"integer","minimum":1},"document_hash":{"type":"string","pattern":"^[a-f0-9]{64}$"}}},"view":{"type":"string","enum":["top","front","back","left","right","3d"],"description":"Top and the four actual orthographic editor views, or 3D. Side renders existing architectural families, Axis and Level; Pipe only Front. Catalog/Room Side and Room 3D are not supported. Omitted IDs are not evidence of absence."},"object_ids":{"type":"array","maxItems":100,"uniqueItems":true,"items":{"type":"string","minLength":1,"maxLength":255}},"level_id":{"type":"string","minLength":1,"maxLength":255,"description":"Required active working Level ID from this exact revision document.editor.levels. Top uses its working plane; 3D shows this Level and lower Levels. Never omit, invent or substitute a Level."},"camera":{"type":["object","null"],"additionalProperties":false,"required":["azimuth_degrees","elevation_degrees"],"description":"3D only. Uses the existing isometric or perspective camera and shared framing. Other views reject a non-null camera.","properties":{"azimuth_degrees":{"type":"number","minimum":-360,"maximum":360},"elevation_degrees":{"type":"number","minimum":1,"maximum":89},"projection":{"type":"string","enum":["isometric","perspective"],"default":"isometric"}}},"filters":{"type":"object","additionalProperties":false,"description":"Existing editor display categories and optional shown-through Level. Defaults show all categories. 3D always also applies the mandatory active Level and lower Levels.","properties":{"exterior_visible":{"type":"boolean","default":true},"generic_visible":{"type":"boolean","default":true},"interior_visible":{"type":"boolean","default":true},"underlays_visible":{"type":"boolean","default":true,"description":"Include copied reference underlays using their existing Top-only owner. A false value hides reference backgrounds without changing saved visibility."},"maximum_level_id":{"type":["string","null"],"minLength":1,"maxLength":255,"default":null}}},"clip":{"type":["object","null"],"description":"Existing preview crop in model XY metres for Top and horizontal XZ for 3D. Side views reject a non-null crop. This does not save user navigation.","additionalProperties":false,"required":["min_x","min_y","max_x","max_y"],"properties":{"min_x":{"type":"number","minimum":-1000000,"maximum":1000000},"min_y":{"type":"number","minimum":-1000000,"maximum":1000000},"max_x":{"type":"number","minimum":-1000000,"maximum":1000000},"max_y":{"type":"number","minimum":-1000000,"maximum":1000000}}}}}
```

## projects_list

Operation: `projects.list`.

Find projects currently available to the connected account, including projects created or shared after connection. Returns IDs, names and current edit access, without documents. Follow next_page; de-duplicate IDs if projects change between pages.

```json
{"type":"object","additionalProperties":false,"properties":{"page":{"type":"integer","minimum":1,"maximum":10000}}}
```

## railing_create

Operation: `railing.create`.

Create one horizontal open or closed Railing on an explicit Level from metre vertices. Uses an existing four-preset assembly. Returned vertices have stable IDs.

```json
{"type":"object","additionalProperties":false,"required":["protocol_version","request_id","idempotency_key","operation","project_id","mcp_version_id","expected_snapshot_version","expected_restore_generation","expected_document_hash","arguments"],"properties":{"protocol_version":{"type":"integer","enum":[1]},"request_id":{"type":"string","minLength":1,"maxLength":128},"idempotency_key":{"type":"string","minLength":1,"maxLength":128},"operation":{"type":"string","enum":["railing.create"]},"project_id":{"type":"string","minLength":1,"maxLength":255},"mcp_version_id":{"type":"string","pattern":"^[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}$"},"expected_snapshot_version":{"type":"integer","minimum":1},"expected_restore_generation":{"type":"integer","minimum":1},"expected_document_hash":{"type":"string","pattern":"^[a-f0-9]{64}$"},"arguments":{"description":"Use the exact railing.create arguments schema from the command reference."}}}
```

## railing_delete

Operation: `railing.delete`.

Delete one standalone Railing using the existing GUI deletion owner.

```json
{"type":"object","additionalProperties":false,"required":["protocol_version","request_id","idempotency_key","operation","project_id","mcp_version_id","expected_snapshot_version","expected_restore_generation","expected_document_hash","arguments"],"properties":{"protocol_version":{"type":"integer","enum":[1]},"request_id":{"type":"string","minLength":1,"maxLength":128},"idempotency_key":{"type":"string","minLength":1,"maxLength":128},"operation":{"type":"string","enum":["railing.delete"]},"project_id":{"type":"string","minLength":1,"maxLength":255},"mcp_version_id":{"type":"string","pattern":"^[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}$"},"expected_snapshot_version":{"type":"integer","minimum":1},"expected_restore_generation":{"type":"integer","minimum":1},"expected_document_hash":{"type":"string","pattern":"^[a-f0-9]{64}$"},"arguments":{"description":"Use the exact railing.delete arguments schema from the command reference."}}}
```

## railing_update

Operation: `railing.update`.

Edit one Railing through settings or vertex_move/vertex_insert/vertex_remove. vertex_insert addresses the edge starting at vertex_id. Minimum vertex removal deletes the Railing, exactly as GUI. Whole-object transform and changing closed are unsupported.

```json
{"type":"object","additionalProperties":false,"required":["protocol_version","request_id","idempotency_key","operation","project_id","mcp_version_id","expected_snapshot_version","expected_restore_generation","expected_document_hash","arguments"],"properties":{"protocol_version":{"type":"integer","enum":[1]},"request_id":{"type":"string","minLength":1,"maxLength":128},"idempotency_key":{"type":"string","minLength":1,"maxLength":128},"operation":{"type":"string","enum":["railing.update"]},"project_id":{"type":"string","minLength":1,"maxLength":255},"mcp_version_id":{"type":"string","pattern":"^[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}$"},"expected_snapshot_version":{"type":"integer","minimum":1},"expected_restore_generation":{"type":"integer","minimum":1},"expected_document_hash":{"type":"string","pattern":"^[a-f0-9]{64}$"},"arguments":{"description":"Use the exact railing.update arguments schema from the command reference."}}}
```

## roof_create

Operation: `roof.create`.

Create one Roof from a closed footprint on an explicit saved Level using existing GUI presets, including custom (Custom planes; first plane from the footprint), optional wall_closure_preset {kind material|assembly, id} and the shared envelope owner. Lengths are metres; pitch is degrees.

```json
{"type":"object","additionalProperties":false,"required":["protocol_version","request_id","idempotency_key","operation","project_id","mcp_version_id","expected_snapshot_version","expected_restore_generation","expected_document_hash","arguments"],"properties":{"protocol_version":{"type":"integer","enum":[1]},"request_id":{"type":"string","minLength":1,"maxLength":128},"idempotency_key":{"type":"string","minLength":1,"maxLength":128},"operation":{"type":"string","enum":["roof.create"]},"project_id":{"type":"string","minLength":1,"maxLength":255},"mcp_version_id":{"type":"string","pattern":"^[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}$"},"expected_snapshot_version":{"type":"integer","minimum":1},"expected_restore_generation":{"type":"integer","minimum":1},"expected_document_hash":{"type":"string","pattern":"^[a-f0-9]{64}$"},"arguments":{"description":"Use the exact roof.create arguments schema from the command reference."}}}
```

## roof_delete

Operation: `roof.delete`.

Delete one Roof with the existing envelope owner, including the ordinary dependent Wall and Room reconciliation.

```json
{"type":"object","additionalProperties":false,"required":["protocol_version","request_id","idempotency_key","operation","project_id","mcp_version_id","expected_snapshot_version","expected_restore_generation","expected_document_hash","arguments"],"properties":{"protocol_version":{"type":"integer","enum":[1]},"request_id":{"type":"string","minLength":1,"maxLength":128},"idempotency_key":{"type":"string","minLength":1,"maxLength":128},"operation":{"type":"string","enum":["roof.delete"]},"project_id":{"type":"string","minLength":1,"maxLength":255},"mcp_version_id":{"type":"string","pattern":"^[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}$"},"expected_snapshot_version":{"type":"integer","minimum":1},"expected_restore_generation":{"type":"integer","minimum":1},"expected_document_hash":{"type":"string","pattern":"^[a-f0-9]{64}$"},"arguments":{"description":"Use the exact roof.delete arguments schema from the command reference."}}}
```

## roof_update

Operation: `roof.update`.

Edit Roof through existing GUI actions: settings, boundary_overhang/closure/role/to_gable, mass_add/delete/pitch/generator, face_pitch, ridge_rotate/end_condition/end_pitch, apex_auto/point/height/uniform_pitch/reference_eave, dormer_create/settings/delete, fronton_settings, roof_window_create/settings/delete, custom_plane_add/offset/delete. settings also changes primitive-only roof_type, slope_direction (flat/shed) and ridge_orientation (gable) and wall_closure_preset. Custom planes: add a slope polygon (new slope uses the Roof pitch; first edge is pivot), set a plane pivot_offset or delete a plane; one plane must remain. Adjacent slopes must meet at one height, otherwise the existing Roof representation is invalid and not drawn; verify with project_view. Primitive-only settings and custom_plane_* apply only to a primitive Roof (GUI-created presets or MCP custom); MCP roof_create stores other presets as semantic. Any exact boundary/mass/face/hosted action converts a primitive or Custom planes Roof to semantic, as the GUI does, after which those primitive controls are unavailable. Read saved mass, boundary, dormer and roof-window IDs from this Roof with object_get. Face actions use semantic {kind, face_index/end_index/boundary_edge_id}; tool_describe provides closed schemas. All lengths use metres; apex height is relative to outer datum. Creation uses existing placement defaults; edit hosted objects by their saved IDs. Null overhang restores inheritance; null rectangular_window clears that opening; nullable material IDs clear bindings. The last mass requires roof_delete. Unsupported topology is rejected atomically; footprint replacement/transforms are unavailable.

```json
{"type":"object","additionalProperties":false,"required":["protocol_version","request_id","idempotency_key","operation","project_id","mcp_version_id","expected_snapshot_version","expected_restore_generation","expected_document_hash","arguments"],"properties":{"protocol_version":{"type":"integer","enum":[1]},"request_id":{"type":"string","minLength":1,"maxLength":128},"idempotency_key":{"type":"string","minLength":1,"maxLength":128},"operation":{"type":"string","enum":["roof.update"]},"project_id":{"type":"string","minLength":1,"maxLength":255},"mcp_version_id":{"type":"string","pattern":"^[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}$"},"expected_snapshot_version":{"type":"integer","minimum":1},"expected_restore_generation":{"type":"integer","minimum":1},"expected_document_hash":{"type":"string","pattern":"^[a-f0-9]{64}$"},"arguments":{"description":"Use the exact roof.update arguments schema from the command reference."}}}
```

## room_create

Operation: `room.create`.

Create a logical Top-only Room on an explicit existing Level from 3 to 1000 metre vertices. Optional name, hex fill_color, partial finishes and complete attic_envelope. Finish choices use exact surface preset codes; null clears a surface and heating is independent. Attic requires a valid Roof on the Room Level and ordered positive metre headroom thresholds. Set snap_to_boundaries=true to use the same physical wall-face/slab-edge snapping and durable boundary bindings as GUI, restricted to that Level. This creates a Room boundary; it does not build or move walls. Uses the exact shared MCP revision and stable idempotency_key; poll operation_get. Main is unchanged.

```json
{"type":"object","additionalProperties":false,"required":["protocol_version","request_id","idempotency_key","operation","project_id","mcp_version_id","expected_snapshot_version","expected_restore_generation","expected_document_hash","arguments"],"properties":{"protocol_version":{"type":"integer","enum":[1]},"request_id":{"type":"string","minLength":1,"maxLength":128},"idempotency_key":{"type":"string","minLength":1,"maxLength":128},"operation":{"type":"string","enum":["room.create"]},"project_id":{"type":"string","minLength":1,"maxLength":255},"mcp_version_id":{"type":"string","pattern":"^[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}$"},"expected_snapshot_version":{"type":"integer","minimum":1},"expected_restore_generation":{"type":"integer","minimum":1},"expected_document_hash":{"type":"string","pattern":"^[a-f0-9]{64}$"},"arguments":{"description":"Use the exact room.create arguments schema from the command reference."}}}
```

## room_delete

Operation: `room.delete`.

Delete one logical Room by stable object_id. Existing room-owned catalog objects are detached using GUI ownership rules and keep their physical placement. Walls remain. Uses only the exact shared MCP revision/idempotency_key; poll operation_get. Main is unchanged.

```json
{"type":"object","additionalProperties":false,"required":["protocol_version","request_id","idempotency_key","operation","project_id","mcp_version_id","expected_snapshot_version","expected_restore_generation","expected_document_hash","arguments"],"properties":{"protocol_version":{"type":"integer","enum":[1]},"request_id":{"type":"string","minLength":1,"maxLength":128},"idempotency_key":{"type":"string","minLength":1,"maxLength":128},"operation":{"type":"string","enum":["room.delete"]},"project_id":{"type":"string","minLength":1,"maxLength":255},"mcp_version_id":{"type":"string","pattern":"^[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}$"},"expected_snapshot_version":{"type":"integer","minimum":1},"expected_restore_generation":{"type":"integer","minimum":1},"expected_document_hash":{"type":"string","pattern":"^[a-f0-9]{64}$"},"arguments":{"description":"Use the exact room.delete arguments schema from the command reference."}}}
```

## room_update

Operation: `room.update`.

Update Room by stable object_id: name, hex fill_color, level_id, metre vertices, partial finishes or complete attic_envelope. Omitted values stay unchanged. New vertices or a new Level rebuild boundary bindings; snap_to_boundaries defaults to false for that edit. Name/fill/finishes/attic-only edits preserve boundary bindings. A Level change detaches contained catalog items and invalid attic relations using GUI rules. This changes logical zoning; widen a physical room by changing its bound walls through wall_update/project_batch, then reread its Room and same-Level image. Uses the exact shared MCP revision/idempotency_key; poll operation_get. Finish presets are surface-specific; null clears one finish, false disables heating. attic_envelope=null disables analysis; a supplied intent must match a valid Roof on the final Room Level and the exact profile with ordered positive metre thresholds. Derived metrics remain read-only.

```json
{"type":"object","additionalProperties":false,"required":["protocol_version","request_id","idempotency_key","operation","project_id","mcp_version_id","expected_snapshot_version","expected_restore_generation","expected_document_hash","arguments"],"properties":{"protocol_version":{"type":"integer","enum":[1]},"request_id":{"type":"string","minLength":1,"maxLength":128},"idempotency_key":{"type":"string","minLength":1,"maxLength":128},"operation":{"type":"string","enum":["room.update"]},"project_id":{"type":"string","minLength":1,"maxLength":255},"mcp_version_id":{"type":"string","pattern":"^[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}$"},"expected_snapshot_version":{"type":"integer","minimum":1},"expected_restore_generation":{"type":"integer","minimum":1},"expected_document_hash":{"type":"string","pattern":"^[a-f0-9]{64}$"},"arguments":{"description":"Use the exact room.update arguments schema from the command reference."}}}
```

## slab_create

Operation: `slab.create`.

Expose the existing Slab create action in the shared MCP document. Use exact saved IDs, explicit units and revision, then poll operation_get. Derived geometry and transforms are unsupported.

```json
{"type":"object","additionalProperties":false,"required":["protocol_version","request_id","idempotency_key","operation","project_id","mcp_version_id","expected_snapshot_version","expected_restore_generation","expected_document_hash","arguments"],"properties":{"protocol_version":{"type":"integer","enum":[1]},"request_id":{"type":"string","minLength":1,"maxLength":128},"idempotency_key":{"type":"string","minLength":1,"maxLength":128},"operation":{"type":"string","enum":["slab.create"]},"project_id":{"type":"string","minLength":1,"maxLength":255},"mcp_version_id":{"type":"string","pattern":"^[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}$"},"expected_snapshot_version":{"type":"integer","minimum":1},"expected_restore_generation":{"type":"integer","minimum":1},"expected_document_hash":{"type":"string","pattern":"^[a-f0-9]{64}$"},"arguments":{"description":"Use the exact slab.create arguments schema from the command reference."}}}
```

## slab_delete

Operation: `slab.delete`.

Expose the existing Slab delete action in the shared MCP document. Use exact saved IDs, explicit units and revision, then poll operation_get. Derived geometry and transforms are unsupported.

```json
{"type":"object","additionalProperties":false,"required":["protocol_version","request_id","idempotency_key","operation","project_id","mcp_version_id","expected_snapshot_version","expected_restore_generation","expected_document_hash","arguments"],"properties":{"protocol_version":{"type":"integer","enum":[1]},"request_id":{"type":"string","minLength":1,"maxLength":128},"idempotency_key":{"type":"string","minLength":1,"maxLength":128},"operation":{"type":"string","enum":["slab.delete"]},"project_id":{"type":"string","minLength":1,"maxLength":255},"mcp_version_id":{"type":"string","pattern":"^[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}$"},"expected_snapshot_version":{"type":"integer","minimum":1},"expected_restore_generation":{"type":"integer","minimum":1},"expected_document_hash":{"type":"string","pattern":"^[a-f0-9]{64}$"},"arguments":{"description":"Use the exact slab.delete arguments schema from the command reference."}}}
```

## slab_update

Operation: `slab.update`.

Update a saved Slab through one existing GUI action: settings (Level, offset, reference plane, thickness, assembly/material or name), boundary (outer vertices), boundary_vertex_insert (edge_index and point), boundary_vertex_remove (vertex_index), or opening_add (vertices). Indices start at zero; removing a triangle vertex deletes the Slab. Assembly applies its preset before explicit overrides. Existing Stair openings reconcile automatically. Manual hole edit/delete, generated opening writes and transforms are unsupported. Use metre units and exact revision, then poll operation_get.

```json
{"type":"object","additionalProperties":false,"required":["protocol_version","request_id","idempotency_key","operation","project_id","mcp_version_id","expected_snapshot_version","expected_restore_generation","expected_document_hash","arguments"],"properties":{"protocol_version":{"type":"integer","enum":[1]},"request_id":{"type":"string","minLength":1,"maxLength":128},"idempotency_key":{"type":"string","minLength":1,"maxLength":128},"operation":{"type":"string","enum":["slab.update"]},"project_id":{"type":"string","minLength":1,"maxLength":255},"mcp_version_id":{"type":"string","pattern":"^[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}$"},"expected_snapshot_version":{"type":"integer","minimum":1},"expected_restore_generation":{"type":"integer","minimum":1},"expected_document_hash":{"type":"string","pattern":"^[a-f0-9]{64}$"},"arguments":{"description":"Use the exact slab.update arguments schema from the command reference."}}}
```

## stair_create

Operation: `stair.create`.

Create a Flight or Spiral Stair using existing GUI settings. start is the lower center; direction_point sets ascent direction, not length. The solver owns steps and automatic Slab openings.

```json
{"type":"object","additionalProperties":false,"required":["protocol_version","request_id","idempotency_key","operation","project_id","mcp_version_id","expected_snapshot_version","expected_restore_generation","expected_document_hash","arguments"],"properties":{"protocol_version":{"type":"integer","enum":[1]},"request_id":{"type":"string","minLength":1,"maxLength":128},"idempotency_key":{"type":"string","minLength":1,"maxLength":128},"operation":{"type":"string","enum":["stair.create"]},"project_id":{"type":"string","minLength":1,"maxLength":255},"mcp_version_id":{"type":"string","pattern":"^[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}$"},"expected_snapshot_version":{"type":"integer","minimum":1},"expected_restore_generation":{"type":"integer","minimum":1},"expected_document_hash":{"type":"string","pattern":"^[a-f0-9]{64}$"},"arguments":{"description":"Use the exact stair.create arguments schema from the command reference."}}}
```

## stair_delete

Operation: `stair.delete`.

Delete one Stair and its generated Slab openings using the existing GUI deletion owner. Manual Slab openings remain.

```json
{"type":"object","additionalProperties":false,"required":["protocol_version","request_id","idempotency_key","operation","project_id","mcp_version_id","expected_snapshot_version","expected_restore_generation","expected_document_hash","arguments"],"properties":{"protocol_version":{"type":"integer","enum":[1]},"request_id":{"type":"string","minLength":1,"maxLength":128},"idempotency_key":{"type":"string","minLength":1,"maxLength":128},"operation":{"type":"string","enum":["stair.delete"]},"project_id":{"type":"string","minLength":1,"maxLength":255},"mcp_version_id":{"type":"string","pattern":"^[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}$"},"expected_snapshot_version":{"type":"integer","minimum":1},"expected_restore_generation":{"type":"integer","minimum":1},"expected_document_hash":{"type":"string","pattern":"^[a-f0-9]{64}$"},"arguments":{"description":"Use the exact stair.delete arguments schema from the command reference."}}}
```

## stair_transform

Operation: `stair.transform`.

Move and rotate a Stair using the existing GUI catalog transform. center is the plan bounding-box center in metres and rotation is absolute degrees. Automatic Slab openings follow.

```json
{"type":"object","additionalProperties":false,"required":["protocol_version","request_id","idempotency_key","operation","project_id","mcp_version_id","expected_snapshot_version","expected_restore_generation","expected_document_hash","arguments"],"properties":{"protocol_version":{"type":"integer","enum":[1]},"request_id":{"type":"string","minLength":1,"maxLength":128},"idempotency_key":{"type":"string","minLength":1,"maxLength":128},"operation":{"type":"string","enum":["stair.transform"]},"project_id":{"type":"string","minLength":1,"maxLength":255},"mcp_version_id":{"type":"string","pattern":"^[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}$"},"expected_snapshot_version":{"type":"integer","minimum":1},"expected_restore_generation":{"type":"integer","minimum":1},"expected_document_hash":{"type":"string","pattern":"^[a-f0-9]{64}$"},"arguments":{"description":"Use the exact stair.transform arguments schema from the command reference."}}}
```

## stair_update

Operation: `stair.update`.

Edit Stair through action settings, turn_add, turn_set, turn_remove or turn_rebalance. Turns apply only to Flight. Profile, material, width and Spiral direction retain GUI coupling. Derived geometry is read-only.

```json
{"type":"object","additionalProperties":false,"required":["protocol_version","request_id","idempotency_key","operation","project_id","mcp_version_id","expected_snapshot_version","expected_restore_generation","expected_document_hash","arguments"],"properties":{"protocol_version":{"type":"integer","enum":[1]},"request_id":{"type":"string","minLength":1,"maxLength":128},"idempotency_key":{"type":"string","minLength":1,"maxLength":128},"operation":{"type":"string","enum":["stair.update"]},"project_id":{"type":"string","minLength":1,"maxLength":255},"mcp_version_id":{"type":"string","pattern":"^[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}$"},"expected_snapshot_version":{"type":"integer","minimum":1},"expected_restore_generation":{"type":"integer","minimum":1},"expected_document_hash":{"type":"string","pattern":"^[a-f0-9]{64}$"},"arguments":{"description":"Use the exact stair.update arguments schema from the command reference."}}}
```

## tool_describe

Operation: `tool.describe`.

Describe exact schemas and explicit workflow limitations. B8 document workflows through project_batch: project.settings.update (display length_unit only), project.save, object.duplicate (explicit level_id), object.delete, object.material.assign. Existing account/main-only imports, underlay writes, drawings, exports, estimates, saved versions and browser-local sessions return unsupported descriptors with reasons and no executable schema. Generic, Interior, Site/Exterior and Pipe WP1 operations run through project_batch. Generic Shape supports create/update/transform/delete; Generic Group supports create, name-only update, transform, delete and object.ungroup. Shapes are box/cylinder/sphere/wedge; group membership editing and nested groups are unsupported. Pipe operations: pipe.route.create, pipe.node.update, pipe.fitting.update and pipe.network.delete; there is no arbitrary graph CRUD. Site families: Terrain, Pavement, Pool, Fence/Access, Vegetation, Canopy, Transport and outdoor furniture. Pavement/Fence/Access whole-object transforms are unsupported; use their existing editing operations. Closed schemas publish exact presets and existing product limits.

```json
{"type":"object","additionalProperties":false,"required":["protocol_version","request_id","operation","project_id","arguments"],"properties":{"protocol_version":{"type":"integer","enum":[1]},"request_id":{"type":"string","minLength":1,"maxLength":128},"operation":{"type":"string","enum":["tool.describe"]},"project_id":{"type":"string","minLength":1,"maxLength":255},"arguments":{"type":"object","additionalProperties":false,"required":["operation"],"properties":{"operation":{"type":"string","minLength":1,"maxLength":128,"enum":["armchair.create","armchair.update","armchair.transform","armchair.delete","bathtub.create","bathtub.update","bathtub.transform","bathtub.delete","bed.create","bed.update","bed.transform","bed.delete","chair.create","chair.update","chair.transform","chair.delete","column.create","column.update","column.transform","column.delete","door.create","door.update","door.transform","door.delete","drum_kit.create","drum_kit.update","drum_kit.transform","drum_kit.delete","exterior_bench.create","exterior_bench.update","exterior_bench.transform","exterior_bench.delete","exterior_canopy.create","exterior_canopy.update","exterior_canopy.transform","exterior_canopy.delete","exterior_chair.create","exterior_chair.update","exterior_chair.transform","exterior_chair.delete","exterior_sun_lounger.create","exterior_sun_lounger.update","exterior_sun_lounger.transform","exterior_sun_lounger.delete","exterior_table.create","exterior_table.update","exterior_table.transform","exterior_table.delete","exterior_transport.create","exterior_transport.update","exterior_transport.transform","exterior_transport.delete","exterior_umbrella.create","exterior_umbrella.update","exterior_umbrella.transform","exterior_umbrella.delete","exterior_waste_bin.create","exterior_waste_bin.update","exterior_waste_bin.transform","exterior_waste_bin.delete","fence.create","fence.update","fence.transform","fence.delete","fence_access.create","fence_access.update","fence_access.transform","fence_access.delete","floating_shelf.create","floating_shelf.update","floating_shelf.transform","floating_shelf.delete","foundation.create","foundation.update","foundation.transform","foundation.delete","generic_group.create","generic_group.update","generic_group.transform","generic_group.delete","generic_shape.create","generic_shape.update","generic_shape.transform","generic_shape.delete","grand_piano.create","grand_piano.update","grand_piano.transform","grand_piano.delete","gym_accessory.create","gym_accessory.update","gym_accessory.transform","gym_accessory.delete","gym_cardio.create","gym_cardio.update","gym_cardio.transform","gym_cardio.delete","gym_strength.create","gym_strength.update","gym_strength.transform","gym_strength.delete","gym_wall_mirror.create","gym_wall_mirror.update","gym_wall_mirror.transform","gym_wall_mirror.delete","kitchen_module.create","kitchen_module.update","kitchen_module.transform","kitchen_module.delete","office_chair.create","office_chair.update","office_chair.transform","office_chair.delete","office_desk.create","office_desk.update","office_desk.transform","office_desk.delete","pavement.create","pavement.update","pavement.transform","pavement.delete","pool.create","pool.update","pool.transform","pool.delete","railing.create","railing.update","railing.transform","railing.delete","refrigerator.create","refrigerator.update","refrigerator.transform","refrigerator.delete","roof.create","roof.update","roof.transform","roof.delete","room.create","room.update","room.transform","room.delete","shower_cabin.create","shower_cabin.update","shower_cabin.transform","shower_cabin.delete","sink.create","sink.update","sink.transform","sink.delete","slab.create","slab.update","slab.transform","slab.delete","sofa.create","sofa.update","sofa.transform","sofa.delete","stair.create","stair.update","stair.transform","stair.delete","table.create","table.update","table.transform","table.delete","television.create","television.update","television.transform","television.delete","terrain.create","terrain.update","terrain.transform","terrain.delete","toilet.create","toilet.update","toilet.transform","toilet.delete","upright_piano.create","upright_piano.update","upright_piano.transform","upright_piano.delete","vegetation.create","vegetation.update","vegetation.transform","vegetation.delete","wall.create","wall.update","wall.transform","wall.delete","wardrobe.create","wardrobe.update","wardrobe.transform","wardrobe.delete","washing_machine.create","washing_machine.update","washing_machine.transform","washing_machine.delete","water_heater.create","water_heater.update","water_heater.transform","water_heater.delete","window.create","window.update","window.transform","window.delete","axis.create","axis.update","axis.delete","level.create","level.update","level.delete","pipe.route.create","pipe.node.create","pipe.node.update","pipe.node.delete","pipe.segment.create","pipe.segment.update","pipe.segment.delete","pipe.fitting.create","pipe.fitting.update","pipe.fitting.delete","pipe.connection.create","pipe.connection.update","pipe.connection.delete","pipe.network.delete","project.save","project.rename","project.create","project.delete","project.share","object.duplicate","object.delete","object.material.assign","project.material.assign","project.batch","project.undo","import.ifc","export.model","drawing.create","drawing.update","drawing.delete","drawing.export","estimate.calculate","saved_version.create","saved_version.restore","saved_version.delete","underlay.create","underlay.update","underlay.delete","project.settings.update","catalog.type.create","catalog.type.update","catalog.type.delete","pipe.catalog.import","pipe.catalog.verify","object.group","object.ungroup","object.lock","project.get","objects.list","object.get","catalog.list","tool.describe","operation.get","editor.sessions","mcp.session.start","editor.bind","project.view","project.validate","editor.tool.select","editor.catalog.open","editor.selection.update","editor.view.update","editor.visibility.update","editor.theme.update","editor.viewport.fit","editor.history.undo","editor.history.redo","editor.clipboard.copy","editor.clipboard.cut","editor.clipboard.paste","editor.help.open","editor.navigation.open","editor.mcp.accept"]}}}}}
```

## wall_create

Operation: `wall.create`.

Create one wall from a baseline in project XY metres, home level_id, base_offset, height and exact wall_type kind/id from the project catalog, plus an optional name. The Wall type defines thickness. Returns its stable ID. Omitted top_constraint creates an unconnected top. Optional top_constraint uses existing GUI modes for next Level or Roof underside, controlling roof_id and metre clearance, and can affect joined walls. Read tool_describe first. Uses only the exact shared MCP version from mcp_session_start. Send the latest revision/hash and a stable idempotency_key. Main is unchanged.

```json
{"type":"object","additionalProperties":false,"required":["protocol_version","request_id","idempotency_key","operation","project_id","mcp_version_id","expected_snapshot_version","expected_restore_generation","expected_document_hash","arguments"],"properties":{"protocol_version":{"type":"integer","enum":[1]},"request_id":{"type":"string","minLength":1,"maxLength":128},"idempotency_key":{"type":"string","minLength":1,"maxLength":128},"operation":{"type":"string","enum":["wall.create"]},"project_id":{"type":"string","minLength":1,"maxLength":255},"mcp_version_id":{"type":"string","pattern":"^[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}$"},"expected_snapshot_version":{"type":"integer","minimum":1},"expected_restore_generation":{"type":"integer","minimum":1},"expected_document_hash":{"type":"string","pattern":"^[a-f0-9]{64}$"},"arguments":{"description":"Use the exact wall.create arguments schema from the command reference."}}}
```

## wall_delete

Operation: `wall.delete`.

Delete one wall and its hosted door/window objects and material bindings. Read the wall first. Uses only the exact shared MCP version from mcp_session_start. Send the latest revision/hash and a stable idempotency_key. Main is unchanged.

```json
{"type":"object","additionalProperties":false,"required":["protocol_version","request_id","idempotency_key","operation","project_id","mcp_version_id","expected_snapshot_version","expected_restore_generation","expected_document_hash","arguments"],"properties":{"protocol_version":{"type":"integer","enum":[1]},"request_id":{"type":"string","minLength":1,"maxLength":128},"idempotency_key":{"type":"string","minLength":1,"maxLength":128},"operation":{"type":"string","enum":["wall.delete"]},"project_id":{"type":"string","minLength":1,"maxLength":255},"mcp_version_id":{"type":"string","pattern":"^[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}$"},"expected_snapshot_version":{"type":"integer","minimum":1},"expected_restore_generation":{"type":"integer","minimum":1},"expected_document_hash":{"type":"string","pattern":"^[a-f0-9]{64}$"},"arguments":{"description":"Use the exact wall.delete arguments schema from the command reference."}}}
```

## wall_transform

Operation: `wall.transform`.

Translate a wall in project XY metres and/or rotate it in degrees about its baseline start, then translate. Hosted openings keep their wall-relative placement. Read the object first. Uses only the exact shared MCP version from mcp_session_start. Send the latest revision/hash and a stable idempotency_key. Main is unchanged.

```json
{"type":"object","additionalProperties":false,"required":["protocol_version","request_id","idempotency_key","operation","project_id","mcp_version_id","expected_snapshot_version","expected_restore_generation","expected_document_hash","arguments"],"properties":{"protocol_version":{"type":"integer","enum":[1]},"request_id":{"type":"string","minLength":1,"maxLength":128},"idempotency_key":{"type":"string","minLength":1,"maxLength":128},"operation":{"type":"string","enum":["wall.transform"]},"project_id":{"type":"string","minLength":1,"maxLength":255},"mcp_version_id":{"type":"string","pattern":"^[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}$"},"expected_snapshot_version":{"type":"integer","minimum":1},"expected_restore_generation":{"type":"integer","minimum":1},"expected_document_hash":{"type":"string","pattern":"^[a-f0-9]{64}$"},"arguments":{"description":"Use the exact wall.transform arguments schema from the command reference."}}}
```

## wall_update

Operation: `wall.update`.

Update an existing wall: name, height, baseline, baseline_alignment, level_id, base_offset, wall_type or top_constraint. Top modes, Roof choice and metre clearance use the GUI owner for the entire joined Wall network; next Level/fallback are derived. Heights and offsets are metres relative to the home level. Changing base_offset preserves the top elevation. Thickness is defined only by wall_type, as in the GUI; there is no independent thickness override. Read tool_describe and the object first. Uses only the exact shared MCP version from mcp_session_start. Send the latest revision/hash and a stable idempotency_key. Main is unchanged.

```json
{"type":"object","additionalProperties":false,"required":["protocol_version","request_id","idempotency_key","operation","project_id","mcp_version_id","expected_snapshot_version","expected_restore_generation","expected_document_hash","arguments"],"properties":{"protocol_version":{"type":"integer","enum":[1]},"request_id":{"type":"string","minLength":1,"maxLength":128},"idempotency_key":{"type":"string","minLength":1,"maxLength":128},"operation":{"type":"string","enum":["wall.update"]},"project_id":{"type":"string","minLength":1,"maxLength":255},"mcp_version_id":{"type":"string","pattern":"^[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}$"},"expected_snapshot_version":{"type":"integer","minimum":1},"expected_restore_generation":{"type":"integer","minimum":1},"expected_document_hash":{"type":"string","pattern":"^[a-f0-9]{64}$"},"arguments":{"description":"Use the exact wall.update arguments schema from the command reference."}}}
```

## window_create

Operation: `window.create`.

Create a hosted Window using an exact opening preset ID and a Wall or Foundation host. Custom size requires explicit width. Level is inherited from the host.

```json
{"type":"object","additionalProperties":false,"required":["protocol_version","request_id","idempotency_key","operation","project_id","mcp_version_id","expected_snapshot_version","expected_restore_generation","expected_document_hash","arguments"],"properties":{"protocol_version":{"type":"integer","enum":[1]},"request_id":{"type":"string","minLength":1,"maxLength":128},"idempotency_key":{"type":"string","minLength":1,"maxLength":128},"operation":{"type":"string","enum":["window.create"]},"project_id":{"type":"string","minLength":1,"maxLength":255},"mcp_version_id":{"type":"string","pattern":"^[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}$"},"expected_snapshot_version":{"type":"integer","minimum":1},"expected_restore_generation":{"type":"integer","minimum":1},"expected_document_hash":{"type":"string","pattern":"^[a-f0-9]{64}$"},"arguments":{"description":"Use the exact window.create arguments schema from the command reference."}}}
```

## window_delete

Operation: `window.delete`.

Delete one hosted Window through the existing editor deletion lifecycle.

```json
{"type":"object","additionalProperties":false,"required":["protocol_version","request_id","idempotency_key","operation","project_id","mcp_version_id","expected_snapshot_version","expected_restore_generation","expected_document_hash","arguments"],"properties":{"protocol_version":{"type":"integer","enum":[1]},"request_id":{"type":"string","minLength":1,"maxLength":128},"idempotency_key":{"type":"string","minLength":1,"maxLength":128},"operation":{"type":"string","enum":["window.delete"]},"project_id":{"type":"string","minLength":1,"maxLength":255},"mcp_version_id":{"type":"string","pattern":"^[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}$"},"expected_snapshot_version":{"type":"integer","minimum":1},"expected_restore_generation":{"type":"integer","minimum":1},"expected_document_hash":{"type":"string","pattern":"^[a-f0-9]{64}$"},"arguments":{"description":"Use the exact window.delete arguments schema from the command reference."}}}
```

## window_update

Operation: `window.update`.

Edit a hosted Window using existing GUI settings or host/center_ratio/side. Enable custom size before changing dimensions. Derived geometry is read-only.

```json
{"type":"object","additionalProperties":false,"required":["protocol_version","request_id","idempotency_key","operation","project_id","mcp_version_id","expected_snapshot_version","expected_restore_generation","expected_document_hash","arguments"],"properties":{"protocol_version":{"type":"integer","enum":[1]},"request_id":{"type":"string","minLength":1,"maxLength":128},"idempotency_key":{"type":"string","minLength":1,"maxLength":128},"operation":{"type":"string","enum":["window.update"]},"project_id":{"type":"string","minLength":1,"maxLength":255},"mcp_version_id":{"type":"string","pattern":"^[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}$"},"expected_snapshot_version":{"type":"integer","minimum":1},"expected_restore_generation":{"type":"integer","minimum":1},"expected_document_hash":{"type":"string","pattern":"^[a-f0-9]{64}$"},"arguments":{"description":"Use the exact window.update arguments schema from the command reference."}}}
```

