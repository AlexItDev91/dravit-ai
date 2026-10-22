# Availability and unsupported workflows

This is the complete finite operation vocabulary at the reviewed schema snapshot. A reserved name is not an implemented action. For unsupported requests explain the recorded limit and continue with supported parts of the brief. Do not bypass it with a REST request or a guessed batch entry.

## armchair.create

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## armchair.delete

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## armchair.transform

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## armchair.update

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## axis.create

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-structure](commands-structure.md).

## axis.delete

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-structure](commands-structure.md).

## axis.update

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-structure](commands-structure.md).

## bathtub.create

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## bathtub.delete

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## bathtub.transform

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## bathtub.update

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## bed.create

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## bed.delete

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## bed.transform

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## bed.update

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## catalog.list

Availability: `unsupported`; batch candidate: `false`.

`adapter_not_implemented`: There is no independent catalog_list MCP query. Exact supported preset IDs and enum options are available from tool_describe; saved project-local catalogs are available in project_get. A combined paginated catalog read adapter is not implemented.

## catalog.type.create

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-workflows](commands-workflows.md).

## catalog.type.delete

Availability: `unsupported`; batch candidate: `false`.

`existing_product_owner_missing`: No existing project-facing GUI/Application mutation owner implements these vocabulary placeholders. The neutral Pipe runtime catalog is immutable. MCP must not create type deletion, catalog import or verification behavior.

## catalog.type.update

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-workflows](commands-workflows.md).

## chair.create

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## chair.delete

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## chair.transform

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## chair.update

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## column.create

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-structure](commands-structure.md).

## column.delete

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-structure](commands-structure.md).

## column.transform

Availability: `unsupported`; batch candidate: `false`.

`use_existing_edit_operation`: Column position is set at creation; existing rotation and dimensions use column.update. There is no standalone Column transform owner.

## column.update

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-structure](commands-structure.md).

## door.create

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-openings](commands-openings.md).

## door.delete

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-openings](commands-openings.md).

## door.transform

Availability: `unsupported`; batch candidate: `false`.

`use_existing_edit_operation`: Existing host-relative Door placement uses door.update host_wall_id, center_ratio and side. There is no standalone Door transform owner.

## door.update

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-openings](commands-openings.md).

## drawing.create

Availability: `unsupported`; batch candidate: `false`.

`mcp_target_isolation_missing`: Existing drawing views, sheet composition, album ordering, paper and special-sheet owners use project-wide repositories. Supplemental sheets also read main estimates and main metadata. They cannot save an MCP-only drawing or album.

## drawing.delete

Availability: `unsupported`; batch candidate: `false`.

`mcp_target_isolation_missing`: Existing drawing views, sheet composition, album ordering, paper and special-sheet owners use project-wide repositories. Supplemental sheets also read main estimates and main metadata. They cannot save an MCP-only drawing or album.

## drawing.export

Availability: `unsupported`; batch candidate: `false`.

`mcp_target_isolation_missing`: The existing queued export captures project-wide saved sheets and checks their main source during execution. Its job, cache key, operation guard and private artifacts lack MCP target identity; an MCP document must not export main sheets instead.

## drawing.update

Availability: `unsupported`; batch candidate: `false`.

`mcp_target_isolation_missing`: Existing drawing views, sheet composition, album ordering, paper and special-sheet owners use project-wide repositories. Supplemental sheets also read main estimates and main metadata. They cannot save an MCP-only drawing or album.

## drum_kit.create

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## drum_kit.delete

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## drum_kit.transform

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## drum_kit.update

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## editor.bind

Availability: `unsupported`; batch candidate: `false`.

`browser_session_binding_unsupported`: Read-only window context is available through editor.sessions with an explicit saved MCP revision and window ID. Dravit has no remote browser binding or command owner; this operation cannot select or control an active tab, camera or selection.

## editor.catalog.open

Availability: `unsupported`; batch candidate: `false`.

`browser_session_only`: This existing GUI action controls a particular editor's tools, selection, viewport or presentation. No server-owned shared browser context is defined. Explicit read/query/view arguments remain available through their supported tools.

## editor.clipboard.copy

Availability: `unsupported`; batch candidate: `false`.

`browser_session_only`: The existing clipboard owner uses browser storage, browser selection and a placement point. MCP has no server-owned clipboard or browser-selection binding. Supported explicit object duplication uses its separate document command.

## editor.clipboard.cut

Availability: `unsupported`; batch candidate: `false`.

`browser_session_only`: The existing clipboard owner uses browser storage, browser selection and a placement point. MCP has no server-owned clipboard or browser-selection binding. Supported explicit object duplication uses its separate document command.

## editor.clipboard.paste

Availability: `unsupported`; batch candidate: `false`.

`browser_session_only`: The existing clipboard owner uses browser storage, browser selection and a placement point. MCP has no server-owned clipboard or browser-selection binding. Supported explicit object duplication uses its separate document command.

## editor.help.open

Availability: `unsupported`; batch candidate: `false`.

`browser_session_only`: This existing GUI action controls a particular editor's tools, selection, viewport or presentation. No server-owned shared browser context is defined. Explicit read/query/view arguments remain available through their supported tools.

## editor.history.redo

Availability: `unsupported`; batch candidate: `false`.

`browser_session_only`: The existing undo/redo owner uses a particular browser's in-memory history checkpoints, including transient tool and selection state. The durable shared MCP session has no browser history cursor; no main saved-version restore is used as a fallback.

## editor.history.undo

Availability: `unsupported`; batch candidate: `false`.

`browser_session_only`: The existing undo/redo owner uses a particular browser's in-memory history checkpoints, including transient tool and selection state. The durable shared MCP session has no browser history cursor; no main saved-version restore is used as a fallback.

## editor.mcp.accept

Availability: `unsupported`; batch candidate: `false`.

`user_interface_only`: Accepting the shared MCP version into main is reserved for the explicit user UI workflow. Neither a grant nor a model-supplied confirmation flag permits MCP to promote, delete or restart the shared version.

## editor.navigation.open

Availability: `unsupported`; batch candidate: `false`.

`browser_session_only`: This existing GUI action controls a particular editor's tools, selection, viewport or presentation. No server-owned shared browser context is defined. Explicit read/query/view arguments remain available through their supported tools.

## editor.selection.update

Availability: `unsupported`; batch candidate: `false`.

`browser_session_only`: This existing GUI action controls a particular editor's tools, selection, viewport or presentation. No server-owned shared browser context is defined. Explicit read/query/view arguments remain available through their supported tools.

## editor.sessions

Availability: `supported`; batch candidate: `false`.

Use its [native tool](native-tools.md) and the [protocol procedure](protocol.md).

## editor.theme.update

Availability: `unsupported`; batch candidate: `false`.

`browser_session_only`: This existing GUI action controls a particular editor's tools, selection, viewport or presentation. No server-owned shared browser context is defined. Explicit read/query/view arguments remain available through their supported tools.

## editor.tool.select

Availability: `unsupported`; batch candidate: `false`.

`browser_session_only`: This existing GUI action controls a particular editor's tools, selection, viewport or presentation. No server-owned shared browser context is defined. Explicit read/query/view arguments remain available through their supported tools.

## editor.view.update

Availability: `unsupported`; batch candidate: `false`.

`browser_session_only`: This existing GUI action controls a particular editor's tools, selection, viewport or presentation. No server-owned shared browser context is defined. Explicit read/query/view arguments remain available through their supported tools.

## editor.viewport.fit

Availability: `unsupported`; batch candidate: `false`.

`browser_session_only`: This existing GUI action controls a particular editor's tools, selection, viewport or presentation. No server-owned shared browser context is defined. Explicit read/query/view arguments remain available through their supported tools.

## editor.visibility.update

Availability: `unsupported`; batch candidate: `false`.

`browser_session_only`: This existing GUI action controls a particular editor's tools, selection, viewport or presentation. No server-owned shared browser context is defined. Explicit read/query/view arguments remain available through their supported tools.

## estimate.calculate

Availability: `unsupported`; batch candidate: `false`.

`mcp_target_isolation_missing`: The existing paid launcher reserves account quota and runs the current estimate/pricing queues. Snapshot, settings, status, stored estimates, observations and cache identities are project/main-scoped. MCP cannot substitute its document or bypass these owners, quota or cache-first missing-only pricing.

## export.model

Availability: `unsupported`; batch candidate: `false`.

`mcp_target_isolation_missing`: The existing queued model export locks and captures the main document. Its request identity, operation rows, source revision, guard and artifact storage do not include an MCP target. Calling it would export main instead of the bound MCP document.

## exterior_bench.create

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-site](commands-site.md).

## exterior_bench.delete

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-site](commands-site.md).

## exterior_bench.transform

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-site](commands-site.md).

## exterior_bench.update

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-site](commands-site.md).

## exterior_canopy.create

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-site](commands-site.md).

## exterior_canopy.delete

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-site](commands-site.md).

## exterior_canopy.transform

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-site](commands-site.md).

## exterior_canopy.update

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-site](commands-site.md).

## exterior_chair.create

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-site](commands-site.md).

## exterior_chair.delete

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-site](commands-site.md).

## exterior_chair.transform

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-site](commands-site.md).

## exterior_chair.update

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-site](commands-site.md).

## exterior_sun_lounger.create

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-site](commands-site.md).

## exterior_sun_lounger.delete

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-site](commands-site.md).

## exterior_sun_lounger.transform

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-site](commands-site.md).

## exterior_sun_lounger.update

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-site](commands-site.md).

## exterior_table.create

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-site](commands-site.md).

## exterior_table.delete

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-site](commands-site.md).

## exterior_table.transform

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-site](commands-site.md).

## exterior_table.update

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-site](commands-site.md).

## exterior_transport.create

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-site](commands-site.md).

## exterior_transport.delete

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-site](commands-site.md).

## exterior_transport.transform

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-site](commands-site.md).

## exterior_transport.update

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-site](commands-site.md).

## exterior_umbrella.create

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-site](commands-site.md).

## exterior_umbrella.delete

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-site](commands-site.md).

## exterior_umbrella.transform

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-site](commands-site.md).

## exterior_umbrella.update

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-site](commands-site.md).

## exterior_waste_bin.create

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-site](commands-site.md).

## exterior_waste_bin.delete

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-site](commands-site.md).

## exterior_waste_bin.transform

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-site](commands-site.md).

## exterior_waste_bin.update

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-site](commands-site.md).

## fence.create

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-site](commands-site.md).

## fence.delete

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-site](commands-site.md).

## fence.transform

Availability: `unsupported`; batch candidate: `false`.

`use_existing_edit_operation`: The current product has no whole-object Fence or Fence Access transform. Existing Fence vertices and hosted Access settings are edited through their canonical update commands.

## fence.update

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-site](commands-site.md).

## fence_access.create

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-site](commands-site.md).

## fence_access.delete

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-site](commands-site.md).

## fence_access.transform

Availability: `unsupported`; batch candidate: `false`.

`use_existing_edit_operation`: The current product has no whole-object Fence or Fence Access transform. Existing Fence vertices and hosted Access settings are edited through their canonical update commands.

## fence_access.update

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-site](commands-site.md).

## floating_shelf.create

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## floating_shelf.delete

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## floating_shelf.transform

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## floating_shelf.update

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## foundation.create

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-structure](commands-structure.md).

## foundation.delete

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-structure](commands-structure.md).

## foundation.transform

Availability: `unsupported`; batch candidate: `false`.

`use_existing_edit_operation`: Foundation baseline editing uses foundation.update. There is no standalone Foundation transform owner.

## foundation.update

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-structure](commands-structure.md).

## generic_group.create

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-generic](commands-generic.md).

## generic_group.delete

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-generic](commands-generic.md).

## generic_group.transform

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-generic](commands-generic.md).

## generic_group.update

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-generic](commands-generic.md).

## generic_shape.create

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-generic](commands-generic.md).

## generic_shape.delete

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-generic](commands-generic.md).

## generic_shape.transform

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-generic](commands-generic.md).

## generic_shape.update

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-generic](commands-generic.md).

## grand_piano.create

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## grand_piano.delete

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## grand_piano.transform

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## grand_piano.update

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## gym_accessory.create

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## gym_accessory.delete

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## gym_accessory.transform

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## gym_accessory.update

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## gym_cardio.create

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## gym_cardio.delete

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## gym_cardio.transform

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## gym_cardio.update

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## gym_strength.create

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## gym_strength.delete

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## gym_strength.transform

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## gym_strength.update

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## gym_wall_mirror.create

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## gym_wall_mirror.delete

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## gym_wall_mirror.transform

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## gym_wall_mirror.update

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## import.ifc

Availability: `unsupported`; batch candidate: `false`.

`mcp_target_isolation_missing`: Existing IFC request, status, cancel, native import, attachment apply and conversion owners capture or commit main and share project-scoped operations, quota and approvals. Their files, jobs, receipts and cleanup have no MCP target identity. No MCP upload token or local-file-path input is admitted.

## kitchen_module.create

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## kitchen_module.delete

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## kitchen_module.transform

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## kitchen_module.update

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## level.create

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-structure](commands-structure.md).

## level.delete

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-structure](commands-structure.md).

## level.update

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-structure](commands-structure.md).

## mcp.session.start

Availability: `supported`; batch candidate: `false`.

Use its [native tool](native-tools.md) and the [protocol procedure](protocol.md).

## object.delete

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-workflows](commands-workflows.md).

## object.duplicate

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-workflows](commands-workflows.md).

## object.get

Availability: `supported`; batch candidate: `false`.

Use its [native tool](native-tools.md) and the [protocol procedure](protocol.md).

## object.group

Availability: `unsupported`; batch candidate: `false`.

`use_canonical_operation`: Existing Generic Shape grouping is exposed through generic_group.create. Use its exact supported schema and existing owner, including same-Site selection and ordered child IDs.

## object.lock

Availability: `unsupported`; batch candidate: `false`.

`existing_product_owner_missing`: No generic lock action exists for all object families. Existing Axis and Level construction locks are exposed only through axis.update and level.update; these are GUI misclick guards.

## object.material.assign

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-workflows](commands-workflows.md).

## object.ungroup

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-workflows](commands-workflows.md).

## objects.list

Availability: `supported`; batch candidate: `false`.

Use its [native tool](native-tools.md) and the [protocol procedure](protocol.md).

## office_chair.create

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## office_chair.delete

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## office_chair.transform

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## office_chair.update

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## office_desk.create

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## office_desk.delete

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## office_desk.transform

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## office_desk.update

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## operation.get

Availability: `supported`; batch candidate: `false`.

Use its [native tool](native-tools.md) and the [protocol procedure](protocol.md).

## pavement.create

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-site](commands-site.md).

## pavement.delete

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-site](commands-site.md).

## pavement.transform

Availability: `unsupported`; batch candidate: `false`.

`use_existing_edit_operation`: Existing Pavement vertex editing uses pavement.update. The current product has no whole-object Pavement transform owner.

## pavement.update

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-site](commands-site.md).

## pipe.catalog.import

Availability: `unsupported`; batch candidate: `false`.

`existing_product_owner_missing`: The neutral Pipe runtime catalog is immutable. No existing project-facing GUI/Application owner implements import or verification as a user operation; MCP must not create one.

## pipe.catalog.verify

Availability: `unsupported`; batch candidate: `false`.

`existing_product_owner_missing`: The neutral Pipe runtime catalog is immutable. No existing project-facing GUI/Application owner implements import or verification as a user operation; MCP must not create one.

## pipe.connection.create

Availability: `unsupported`; batch candidate: `false`.

`use_canonical_operation`: Pipe WP1 creates a complete route through the existing route owner, moves free endpoints, rolls fittings and deletes a network. Independent arbitrary node, segment, fitting or connection CRUD is not a user-facing product operation; these reserved IDs do not authorize a new graph engine.

## pipe.connection.delete

Availability: `unsupported`; batch candidate: `false`.

`use_canonical_operation`: Pipe WP1 creates a complete route through the existing route owner, moves free endpoints, rolls fittings and deletes a network. Independent arbitrary node, segment, fitting or connection CRUD is not a user-facing product operation; these reserved IDs do not authorize a new graph engine.

## pipe.connection.update

Availability: `unsupported`; batch candidate: `false`.

`use_canonical_operation`: Pipe WP1 creates a complete route through the existing route owner, moves free endpoints, rolls fittings and deletes a network. Independent arbitrary node, segment, fitting or connection CRUD is not a user-facing product operation; these reserved IDs do not authorize a new graph engine.

## pipe.fitting.create

Availability: `unsupported`; batch candidate: `false`.

`use_canonical_operation`: Pipe WP1 creates a complete route through the existing route owner, moves free endpoints, rolls fittings and deletes a network. Independent arbitrary node, segment, fitting or connection CRUD is not a user-facing product operation; these reserved IDs do not authorize a new graph engine.

## pipe.fitting.delete

Availability: `unsupported`; batch candidate: `false`.

`use_canonical_operation`: Pipe WP1 creates a complete route through the existing route owner, moves free endpoints, rolls fittings and deletes a network. Independent arbitrary node, segment, fitting or connection CRUD is not a user-facing product operation; these reserved IDs do not authorize a new graph engine.

## pipe.fitting.update

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-pipes](commands-pipes.md).

## pipe.network.delete

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-pipes](commands-pipes.md).

## pipe.node.create

Availability: `unsupported`; batch candidate: `false`.

`use_canonical_operation`: Pipe WP1 creates a complete route through the existing route owner, moves free endpoints, rolls fittings and deletes a network. Independent arbitrary node, segment, fitting or connection CRUD is not a user-facing product operation; these reserved IDs do not authorize a new graph engine.

## pipe.node.delete

Availability: `unsupported`; batch candidate: `false`.

`use_canonical_operation`: Pipe WP1 creates a complete route through the existing route owner, moves free endpoints, rolls fittings and deletes a network. Independent arbitrary node, segment, fitting or connection CRUD is not a user-facing product operation; these reserved IDs do not authorize a new graph engine.

## pipe.node.update

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-pipes](commands-pipes.md).

## pipe.route.create

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-pipes](commands-pipes.md).

## pipe.segment.create

Availability: `unsupported`; batch candidate: `false`.

`use_canonical_operation`: Pipe WP1 creates a complete route through the existing route owner, moves free endpoints, rolls fittings and deletes a network. Independent arbitrary node, segment, fitting or connection CRUD is not a user-facing product operation; these reserved IDs do not authorize a new graph engine.

## pipe.segment.delete

Availability: `unsupported`; batch candidate: `false`.

`use_canonical_operation`: Pipe WP1 creates a complete route through the existing route owner, moves free endpoints, rolls fittings and deletes a network. Independent arbitrary node, segment, fitting or connection CRUD is not a user-facing product operation; these reserved IDs do not authorize a new graph engine.

## pipe.segment.update

Availability: `unsupported`; batch candidate: `false`.

`use_canonical_operation`: Pipe WP1 creates a complete route through the existing route owner, moves free endpoints, rolls fittings and deletes a network. Independent arbitrary node, segment, fitting or connection CRUD is not a user-facing product operation; these reserved IDs do not authorize a new graph engine.

## pool.create

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-site](commands-site.md).

## pool.delete

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-site](commands-site.md).

## pool.transform

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-site](commands-site.md).

## pool.update

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-site](commands-site.md).

## project.batch

Availability: `supported`; batch candidate: `true`.

Use its [native tool](native-tools.md) and the [protocol procedure](protocol.md).

## project.create

Availability: `supported`; batch candidate: `false`.

Use its [native tool](native-tools.md) and the [protocol procedure](protocol.md).

## project.delete

Availability: `unsupported`; batch candidate: `false`.

`user_interface_only`: Deleting a project affects its main document and project resources. Destructive account/project actions are not admitted through MCP commands. Deleting the shared MCP version also remains a user UI action.

## project.get

Availability: `supported`; batch candidate: `false`.

Use its [native tool](native-tools.md) and the [protocol procedure](protocol.md).

## project.material.assign

Availability: `unsupported`; batch candidate: `false`.

`existing_product_owner_missing`: No existing project-wide material assignment owner exists. Use object.material.assign for an exact existing object, or room.update with its supported surface-specific finishes.

## project.rename

Availability: `unsupported`; batch candidate: `false`.

`mcp_target_isolation_missing`: The existing rename owner changes relational project metadata and main history. Common Save retains the current metadata name, and MCP promotion retains the main name. A document-only rename cannot complete this workflow.

## project.save

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-workflows](commands-workflows.md).

## project.settings.update

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-workflows](commands-workflows.md).

## project.share

Availability: `unsupported`; batch candidate: `false`.

`account_scope_unavailable`: Existing membership and public-view owners change project-wide access, invitations and access epochs. These account effects cannot be isolated to the shared MCP version.

## project.undo

Availability: `unsupported`; batch candidate: `false`.

`browser_session_only`: The existing undo/redo owner uses a particular browser's in-memory history checkpoints, including transient tool and selection state. The durable shared MCP session has no browser history cursor; no main saved-version restore is used as a fallback.

## project.validate

Availability: `supported`; batch candidate: `false`.

Use its [native tool](native-tools.md) and the [protocol procedure](protocol.md).

## project.view

Availability: `supported`; batch candidate: `false`.

Use its [native tool](native-tools.md) and the [protocol procedure](protocol.md).

## railing.create

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-circulation](commands-circulation.md).

## railing.delete

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-circulation](commands-circulation.md).

## railing.transform

Availability: `unsupported`; batch candidate: `false`.

`use_existing_edit_operation`: Existing Railing vertex editing uses railing.update actions. There is no standalone Railing transform owner.

## railing.update

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-circulation](commands-circulation.md).

## refrigerator.create

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## refrigerator.delete

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## refrigerator.transform

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## refrigerator.update

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## roof.create

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-roof](commands-roof.md).

## roof.delete

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-roof](commands-roof.md).

## roof.transform

Availability: `unsupported`; batch candidate: `false`.

`use_existing_edit_operation`: Existing Roof topology and settings use roof.update actions. There is no standalone Roof transform owner.

## roof.update

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-roof](commands-roof.md).

## room.create

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-structure](commands-structure.md).

## room.delete

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-structure](commands-structure.md).

## room.transform

Availability: `unsupported`; batch candidate: `false`.

`use_existing_edit_operation`: Existing Room polygon and Level editing uses room.update. A Room is a logical space; there is no standalone Room transform owner.

## room.update

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-structure](commands-structure.md).

## saved_version.create

Availability: `unsupported`; batch candidate: `false`.

`mcp_target_isolation_missing`: The existing owner locks main and stores its document and underlays in main saved-version history, potentially replacing the oldest backup. The shared MCP version has one current document and no separate saved-version history.

## saved_version.delete

Availability: `unsupported`; batch candidate: `false`.

`mcp_target_isolation_missing`: The existing owner removes a backup from main saved-version history. There is no target-isolated saved-version catalog for the shared MCP document.

## saved_version.restore

Availability: `unsupported`; batch candidate: `false`.

`mcp_target_isolation_missing`: The existing confirmed restore owner replaces main, advances its generation, restores underlays, prunes main activity and later backups, and publishes main restoration. Reusing it would cross the shared MCP boundary.

## shower_cabin.create

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## shower_cabin.delete

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## shower_cabin.transform

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## shower_cabin.update

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## sink.create

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## sink.delete

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## sink.transform

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## sink.update

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## slab.create

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-structure](commands-structure.md).

## slab.delete

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-structure](commands-structure.md).

## slab.transform

Availability: `unsupported`; batch candidate: `false`.

`use_existing_edit_operation`: Existing Slab boundary and hole editing uses slab.update actions. There is no standalone Slab transform owner.

## slab.update

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-structure](commands-structure.md).

## sofa.create

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## sofa.delete

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## sofa.transform

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## sofa.update

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## stair.create

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-circulation](commands-circulation.md).

## stair.delete

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-circulation](commands-circulation.md).

## stair.transform

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-circulation](commands-circulation.md).

## stair.update

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-circulation](commands-circulation.md).

## table.create

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## table.delete

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## table.transform

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## table.update

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## television.create

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## television.delete

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## television.transform

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## television.update

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## terrain.create

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-site](commands-site.md).

## terrain.delete

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-site](commands-site.md).

## terrain.transform

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-site](commands-site.md).

## terrain.update

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-site](commands-site.md).

## toilet.create

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## toilet.delete

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## toilet.transform

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## toilet.update

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## tool.describe

Availability: `supported`; batch candidate: `false`.

Use its [native tool](native-tools.md) and the [protocol procedure](protocol.md).

## underlay.create

Availability: `unsupported`; batch candidate: `false`.

`mcp_target_isolation_missing`: The existing upload/retry/processing owners read main levels and write project_underlays, project_underlay_operations, files and project broadcasts. Only copied underlay list/content reads currently support an exact MCP target.

## underlay.delete

Availability: `unsupported`; batch candidate: `false`.

`mcp_target_isolation_missing`: The existing confirmed deletion owner removes main underlay rows, schedules file removal and publishes project-wide changes. MCP underlay records currently provide read access and lifecycle pruning only.

## underlay.update

Availability: `unsupported`; batch candidate: `false`.

`mcp_target_isolation_missing`: The existing catalog mutation owner updates main underlay rows and publishes project-wide changes; delete also schedules file removal. MCP underlay records currently provide read access and lifecycle pruning only.

## upright_piano.create

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## upright_piano.delete

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## upright_piano.transform

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## upright_piano.update

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## vegetation.create

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-site](commands-site.md).

## vegetation.delete

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-site](commands-site.md).

## vegetation.transform

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-site](commands-site.md).

## vegetation.update

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-site](commands-site.md).

## wall.create

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-structure](commands-structure.md).

## wall.delete

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-structure](commands-structure.md).

## wall.transform

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-structure](commands-structure.md).

## wall.update

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-structure](commands-structure.md).

## wardrobe.create

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## wardrobe.delete

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## wardrobe.transform

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## wardrobe.update

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## washing_machine.create

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## washing_machine.delete

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## washing_machine.transform

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## washing_machine.update

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## water_heater.create

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## water_heater.delete

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## water_heater.transform

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## water_heater.update

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-interior](commands-interior.md).

## window.create

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-openings](commands-openings.md).

## window.delete

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-openings](commands-openings.md).

## window.transform

Availability: `unsupported`; batch candidate: `false`.

`use_existing_edit_operation`: Existing host-relative Window placement uses window.update host_wall_id, center_ratio and side. There is no standalone Window transform owner.

## window.update

Availability: `supported`; batch candidate: `true`.

Arguments: [commands-openings](commands-openings.md).

