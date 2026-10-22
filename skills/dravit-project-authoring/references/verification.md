# Verification and repair

## Identity before judgment

Keep the complete identity tuple together: `project_id`, `mcp_version_id`, `snapshot_version`, `restore_generation`, `document_hash`. Read facts, program reports and images must describe that tuple. A view from before Save cannot verify the newer document. Recheck after any participant changes the shared version. Missing evidence stays unknown.

First read the changed object and affected hosts/neighbours. Confirm stable IDs, saved dimensions, Level/offset, host relationships, bindings, count and relevant catalog identity. For a claimed physical room expansion, inspect the changed physical boundaries and dependent objects, not only its Room polygon or label. A hidden duplicate can occupy exactly the same pixels.

## Client browser viewport

Request `project_view` using the complete saved `revision`, a specific `view` and exact saved `level_id` from `document.editor.levels`. Use the target Room's Level for Room tasks. Never substitute the first, zero, null, invented or all Levels.

Top uses that Level's working plane; 3D includes it and lower Levels. Use `object_ids`/supported crop to inspect a region while keeping that context. For an axis edit affecting multiple Levels, inspect each affected Level. Filters and camera use only published values and do not change saved navigation.

The tool synchronously returns `status: succeeded`, `operation_id: null` and `result: {viewport_url, render_location: "client", ticket_expires_at, workflow}`. It does not create a PNG, background image operation or polling target. Open `viewport_url` promptly in an agent-controlled browser that can take screenshots. Its fragment contains a single-use ticket valid for 60 seconds; exchange establishes a read-only HttpOnly cookie session for two hours for this exact project/MCP-version pair. No separate Dravit login is needed. Do not share the capability URL or substitute a public/main view. If the ticket expires before opening or the session ends, request a fresh `project_view` for the current saved revision.

Wait for `html[data-mcp-viewport-state="ready"]`, then parse the JSON `data-receipt` on `#mcp-viewport-status`. Verify all five revision fields, the requested `view` and `level_id`, `visible_object_ids`, `omitted_object_ids` and separate `reference_sources`. The loaded revision must match the completed Save receipt before its screenshot can verify that Save. After each later completed Save, reload **the same tab**, wait for readiness again, reread its receipt and inspect a new actual screenshot. This viewport has no WebSocket, Reverb, background polling or automatic refresh. Never use a prior ready state or screenshot as evidence for a newer Save. A deleted Level/object or closed MCP version is an explicit error, not permission to switch silently to another Level, a fresh version or main. For a new view/Level request another `project_view` and navigate the existing tab to its returned URL; view settings do not change the model.

If this ChatGPT or Claude environment has no browser with screenshots, visual verification is unavailable even when MCP reads and writes work. Record that limit and continue independent supported work; there is no backend PNG fallback. A URL or DOM receipt alone is not visual inspection. Do not draw a substitute image or publish the private model to work around a client limitation.

When the user asks to see a view, use the client's supported screenshot display or attachment mechanism. An assistant-inspected screenshot does not establish that it appeared in the user's message. If inline display is unavailable or unconfirmed, state that limit and provide the MCP editor link with the requested view. Say an image is shown only with actual client display evidence.

Use Top plus 3D where supported, then relevant Front/Back/Left/Right views for the question. Side coverage is family-specific: architecture/Axis/Level are available; Pipe supports Front; catalog Side and Room Side/3D are unsupported in this source contract. Roof nested geometry is observed through its parent. Exclusive unsupported focus may fail, while a mixed selection may omit objects. Omitted IDs, clipped objects, hidden filters, copied underlays and unsupported IFC preview delivery do not prove absence from the model.

The full editable editor and its current applied revision are separate evidence. A successful Save or reloaded read-only viewport does not prove that a user's open editor received Reverb. Report live editor delivery as verified only when actual monitor/session evidence establishes it.

## Program checks and unknowns

Discover current tools/resources before requesting program validation. Invoke only an advertised existing check and retain its scope, owner, inputs, rule identity, revision, measured facts, missing data, status and limitations. This skill contains no validator and never computes a hidden replacement geometry engine.

Use these evidence distinctions when writing the result; do not fabricate these as server payload fields:

| Evidence/result | What can be concluded |
|---|---|
| Saved fact or dimension | The exact read fact for that revision, not a whole project assessment |
| Program pass | Only the implemented rule with sufficient inputs and established applicability |
| Program fail/warning | Its actual finding, severity and evidence; keep warnings visible |
| `not_enough_data` / unknown | Required facts, scale, purpose, profile or current evidence are missing |
| `unsupported` / `not_supported` | Required capability or algorithm does not exist on this server |
| `not_applicable` | Scope was affirmatively established, not merely guessed from missing data |
| `requires_engineer_review` | Carry the reason forward; do not turn it into approval |
| Visual/contextual judgment | A bounded observation or recommendation, not deterministic pass/fail |

A program report may use only a subset of these states. Preserve its original result. Availability of geometry/read helpers does not establish a route, motion, ergonomic, daylight or regulatory check. An empty finding list is not proof that unsupported checks passed.

Placement/spatial recommendations are advisory MCP feedback and must not be used to block Save. Preserve existing schema and native command admission contracts. A missing support/collision rule stays unknown or unsupported; this instruction does not create a new validator.

## Human-use pass through the brief

Trace each required activity: confirmed entry → usable spaces → necessary transitions → functional position at the target. For a used upper floor, inspect the actual stair/alternative route, approaches, exit and slab opening. A Stair ID or two Level references do not establish reachability.

Check required Door/Window hosts and purpose; furniture's functional side; relevant opening/working/approach space; collisions in XYZ; affected adjacent routes. Use [spatial reasoning](spatial-reasoning.md) and [human use](human-use.md). When motion, zone, route or window-function facts/checks are absent, report that limit even if an image looks plausible. Do not infer missing dimensions by counting pixels.

## Repair and report

Repair a confirmed violation using a supported normal update/transform/delete, preserving existing IDs and user intent. Group dependent corrections into an atomic stage. If no supported repair satisfies a required brief item, explain that conflict and request the one material choice needed. Do not rename a bedroom into storage, omit a required occupant or invent a route to pass.

After repair, reread affected objects, repeat the affected available checks and fresh views, and inspect neighbouring routes/functions. Freeing a wardrobe while blocking the hall does not finish the repair. Repeated failure without new evidence calls for reassessment, not repeated blind writes.

The final result should identify the saved scope, fulfilled requirements with evidence, remaining defects, unknown/unsupported checks and any material next decision. Separate publication/client activation from model completion. Never claim a standards-compliant, engineered or wholly usable building from valid commands or an attractive render.
