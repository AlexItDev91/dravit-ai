# Structure, openings and Roof authoring handbook

Use this handbook to choose an existing modeling operation, its host and its editing sequence. Use [examples-structure.json](examples-structure.json) for exact inner command entries and [protocol.md](protocol.md) for the complete native MCP request envelope, atomic batches, revisions, idempotency and execution readback. An example's `id` and `requires` are guide metadata: submit only its `operation` and `arguments` inside the protocol envelope. Substitute every illustrative saved ID before execution. Examples are alternatives with individual preconditions; concatenating the whole collection would create conflicting objects.

The exact parameter contracts are in [commands-structure.md](commands-structure.md), [commands-openings.md](commands-openings.md), [commands-circulation.md](commands-circulation.md) and [commands-roof.md](commands-roof.md). Read a family schema when constructing a request or choosing an enum value. Catalog creation, duplication, generic deletion and material workflows are in [commands-workflows.md](commands-workflows.md). Native tool names and complete read requests are in [native-tools.md](native-tools.md). These references also have `dravit_guide` sections using the filename stem.

## Choose the operation and obtain its dependencies

1. Read the saved project and target objects. Record stable Level, object and catalog IDs, current revision, ownership, dimensions and actual parameters.
2. Resolve catalogs before placing their consumers. A Wall type, Foundation type, material, assembly or opening preset must exist in the correct family. Names are not IDs. To create a project-local type, follow the catalog workflow rather than inventing an ID.
3. Establish Levels before their model objects. Establish Wall/Foundation hosts before Door/Window placement, upper Slabs before Stair opening verification, and Roofs before roof-fit Walls, attic Room analysis and roof-hosted children.
4. Apply only fields allowed by the exact operation/action schema. Each `*.update` is a partial edit; it needs at least one actual field in addition to identity/action. A schema enum describes a possible value, while the existing owner's current geometry and GUI availability determine whether that value can be applied.
5. Wait for terminal execution, read the saved result and inspect every affected object. Do not report the queued command as a completed model change. Validate geometry through the available saved projections and views using [verification.md](verification.md).

Every length quantity below is `{ "value": 3.2, "unit": "m" }`; a plan point is `{ "x": 2, "y": 4, "unit": "m" }`; an angle is `{ "value": 35, "unit": "deg" }`. Convert source measurements before sending them. Project display units do not permit `cm`, `mm` or `ft` in these command fields. Existing owners still apply their project-unit rounding, angle canonicalization and geometry limits, so read the persisted number. A positive schema value that rounds to an unusable dimension can be rejected.

Do not copy derived read fields into writes. Base elevations, resolved heights, Room areas/headroom results, runtime roof faces, generated Slab openings, geometry versions, bindings and parent IDs are not writable merely because they appear in readback. The family schemas identify the supported input boundary.

## Axis and Level

### Axes, dimensions and explicit construction bindings

`axis.create` supports `vertical`, `horizontal` and `custom`. The custom orientation accepts an angle from 0 to 90 degrees. Only custom axes accept angle changes; there is no update field that converts an existing axis orientation. `coordinate` is the signed position in its reference frame, not an arbitrary XY center. Save the returned `axis.*` identity.

`axis.update` supports label, coordinate, custom angle, individual lock, construction lock, explicit bindings and spacing from another axis. Use either `coordinate` or `spacing`, never both in one command. `spacing.distance` is nonnegative; zero is valid for compatible unconstrained axes. An unavailable reference axis, invalid anchor, incompatible spacing or conflicting constraints rejects the candidate.

An axis's `locked` flag protects GUI pointer actions from misclicks. MCP can edit through that flag while preserving it. `construction_lock_enabled` instead controls whether axis movement drives bound construction. Review this distinction before changing a coordinate.

`bindings` is an explicit list of unique existing `{ object_id, anchor_id }` pairs. Setting the list measures each anchor's current signed normal offset from the axis and preserves current geometry. The next axis coordinate edit moves only saved bound anchors while retaining those offsets. Enabling construction lock and supplying `bindings: []` explicitly selects no anchors. Creating an axis or enabling the existing capture owner can capture coincident anchors; mere visual coincidence after reopening does not establish a new relationship. Use an explicit list when the intended affected set matters.

Supported construction anchors:

| Object | Exact anchor spelling | Effect of an axis move |
| --- | --- | --- |
| Wall | `baseline.start`, `baseline.end` | Moves selected baseline endpoints through existing join/geometry guards |
| Foundation | `baseline.start`, `baseline.end` | Moves selected baseline endpoints |
| Column | `center` | Moves its plan center |
| Slab | `outer.0`, `outer.1`, etc.; `hole.0.0`, etc. | Moves current boundary/hole vertices |
| Stair | `start` | Translates the existing Stair and reconciles generated openings |
| Primitive Roof | `outer.0`, etc.; `plane.0.0`, etc. for custom-plane vertices | Moves current footprint/plane vertices |
| Semantic Roof | `mass.<exact-mass-id>.<exact-vertex-id>` | Moves that mass vertex through existing geometry owners |

Indices refer to the current saved order; mass/vertex IDs come from current Roof readback. Manual geometry edits reconcile existing offsets; insertion/deletion can remap uniquely retained polygon anchors. Re-read after topology changes. A second stationary bound axis still constrains the same anchor; conflicting parallel targets fail atomically. To move construction in both X and Y through this supported path, bind the intended anchors to the relevant axes and edit their coordinates with valid resulting constraints. Do not turn this into a fictitious family `.transform`.

The grid target is exactly `group.axis_grid.primary`. Its `axis.update` accepts `group_grid: true`, `locked` and `all_axes_locked`. Grouping is a one-way existing action; `group_grid: false` is invalid. `all_axes_locked` changes individual axis flags and clears the independent grid lock. Grid-only fields must not be sent to an individual axis, nor individual geometry fields to the grid. `axis.delete` deletes an individual axis and its relation, using its exact returned ID.

Examples: `axis.create.*`, `axis.update.*`, `axis.delete` in the JSON collection.

### Levels and vertical ownership

`level.create` requires a nonblank label and absolute `elevation`. `level.update` changes label/elevation/lock. An elevation edit reconciles bound construction and can affect Pipe network identities, so a single Level edit can have several changed objects. A Level lock has the same GUI pointer-guard distinction as axis lock.

When no authoring Levels exist, create exactly `label:"Level 0"` at `elevation:{"value":0,"unit":"m"}` first. An Upper floor example requires that datum to exist already or to have been created earlier in the same ordered batch. The initial name/elevation constraint applies only to that first create. Afterwards `level.update` can rename the datum or change its elevation through the normal reconciliation guards. For a custom initial label, an ordered batch can create Level 0, rename it using the earlier Level alias and then create dependent objects. A reference to a later alias is invalid.

Do not assume that every family's `level_id` edit translates geometry identically. Foundation reassignment preserves its absolute datum when no offset is supplied. Wall height and top constraints have their own rules. Room reassignment changes logical ownership and re-evaluates boundary/attic compatibility. Supply explicit final offset and dimensions when those are the intended result.

`level.delete` requires an empty deletable Level. An occupied Level is rejected instead of silently deleting its direct owners. Reassign or delete the relevant objects first and read their result before removing the datum. Discover the real Level IDs rather than assuming `level.1` exists.

## Wall, partitions, joins and top constraints

`wall.create` requires `baseline`, `level_id`, `base_offset`, `height` and `wall_type`. A Wall's type is `{ "kind": "material" | "assembly" | "custom", "id": "<exact catalog ID>" }`. Select an existing compatible reference. The type owns thickness and role. A partition is a Wall whose selected type has partition role; there is no separate `partition.create`. Use the catalog workflow for a custom partition type. Direct `thickness`, arbitrary `role`, `host_id` and `base_elevation` fields are unavailable.

### Built-in Wall and partition choices

Partitions do not require a custom type or an invented price. Use an existing assembly with `wall_type.kind:"assembly"`; the following exact catalog IDs supply the existing role and modeling thickness. Role names are descriptive product metadata, not structural/fire/acoustic approval. If the user wants a custom construction absent here, resolve that separate specification and its required finished-price input before custom type creation.

| Exact assembly ID | Existing role | Modeling thickness (m) |
|---|---|---|
| `assembly.wall.brick.half_120` | `partition` | 0.12 |
| `assembly.wall.brick.one_250` | `structural` | 0.25 |
| `assembly.wall.brick.one_half_380` | `external` | 0.38 |
| `assembly.wall.brick.two_510` | `external` | 0.51 |
| `assembly.wall.brick.cavity_520` | `external` | 0.52 |
| `assembly.wall.aac.partition_100` | `partition` | 0.1 |
| `assembly.wall.aac.internal_150` | `internal` | 0.15 |
| `assembly.wall.aac.external_300` | `external` | 0.3 |
| `assembly.wall.cmu.partition_150` | `partition` | 0.152 |
| `assembly.wall.cmu.structural_200` | `structural` | 0.203 |
| `assembly.wall.concrete.cast_in_place_200` | `structural` | 0.2 |
| `assembly.wall.icf.above_grade_300` | `external` | 0.3 |
| `assembly.wall.drywall.single_stud_75` | `partition` | 0.075 |
| `assembly.wall.drywall.double_board_125` | `partition` | 0.125 |
| `assembly.wall.wood_frame.2x4_140` | `internal` | 0.14 |
| `assembly.wall.wood_frame.2x6_190` | `external` | 0.19 |
| `assembly.wall.sip.114` | `external` | 0.114 |
| `assembly.wall.insulated_metal_panel_100` | `facade` | 0.1 |
| `assembly.wall.precast_sandwich_277` | `external` | 0.277 |

For a 75 mm stud partition, set `wall_type:{"kind":"assembly","id":"assembly.wall.drywall.single_stud_75"}` with the ordinary required Wall placement fields. For a 100 mm AAC partition choose `assembly.wall.aac.partition_100`. These catalog-backed selections avoid creating a project-local priced type just to draw a partition. The built-in material alternative `material.concrete.c25_fixture` supplies the existing 180 mm concrete Wall; use it only when that is the intended construction.

The ordered baseline controls direction and `center`/`left`/`right` alignment. Endpoint-connected compatible Walls use the existing join owner. Create an adjoining baseline endpoint at the intended common point, or edit the existing baseline to that point. There is no public `wall.join`, join-mode parameter or independent join-geometry write. Read the resulting projections and connected IDs. A physical duplicate can reject even with reversed endpoints and opposite alignment; equal plan baselines at separate Z ranges are not automatically duplicates.

`wall.update` changes baseline/alignment, selected type, name, Level, offset, height and supported top intent. A name-only edit preserves geometry. An explicit height detaches automatic top intent unless a `top_constraint` is also supplied. An offset-only edit can preserve the old top by adjusting height. For an intentional new base and height, send both. Combined edits apply top intent after the final geometry/Level change.

`wall.transform` is supported. Its `translation` is a plan delta. Its `rotation` is an angle delta about the translated baseline start. For example, a baseline `(0,0)` to `(10,0)` translated by `(2,1)` and rotated 90 degrees becomes `(2,1)` to `(2,11)`. It is not an absolute rotation field. Baseline editing and transform still run host/join, duplicate and geometry checks.

Top modes:

| `top_constraint.mode` | Input and resulting behavior |
| --- | --- |
| `unconnected` | Use explicit/fallback height; no `roof_id` or `clearance` field is allowed |
| `automatic_next_level` | Resolve the next Level and fallback through the existing owner; do not send resolved `level_id` or `fallback_height` inside the constraint |
| `automatic_roof_underside` | Optionally select `roof_id` and nonnegative `clearance`; fit through the existing Roof underside owner |

Physical Roof intersections also trim an ordinary Wall with `unconnected` intent. The authored height remains its recovery solid; it is not a way to push the body through an intersecting Roof. Derived Top/Side/3D and masonry quantities use the same trimmed body, including joined corners and hosted opening deductions. Hiding Roof covering, rafters or the whole Roof does not remove this physical dependency. A Roof wholly below the Wall base or outside its body does not trim it. Read current diagnostics for an invalid or ambiguous explicit adaptive constraint; do not treat a failed command as a Save.

In Roof mode, omitting `roof_id` preserves the prior choice; `roof_id: null` clears the selected choice. Omitted clearance is retained; explicit zero is valid. Do not add these Roof-only keys to another mode. Joined Walls can receive the same top intent, so inspect the whole changed set. Updating/deleting a Roof can change attached Wall geometry later.

`wall.delete` uses the existing cascade. Read back hosted Door/Window objects, Room boundary bindings, material/type bindings and axis relations; do not assume only one saved record changes.

Examples: `wall.create.assembly`, `.material`, `.custom`, `.join`; `wall.update.geometry`, `.relevel`, `.top.*`; `wall.transform`; `wall.delete`.

## Room, finishes, attic analysis and knee walls

`room.create` requires a Level and a simple valid polygon of 3 to 1000 points. Name, muted fill, exact finish settings and attic intent are optional. `snap_to_boundaries: true` asks the existing owner to snap to same-Level Wall/Slab boundaries and persist physical vertex bindings. Snapping is opt-in. A Wall on another Level must not become the Room's boundary source. The Room is logical spatial markup; do not infer a constructed wall or a volume from its colored plan fill.

`room.update` changes vertices, snapping, Level, name, fill, finishes or attic intent. A name-only update retains boundary bindings. Supplying vertices, changing Level or explicitly setting snap behavior recomputes bindings; if no snap applies, the relevant entries are null. Changing/deleting a Room detaches supported catalog children while preserving their authored placement instead of deleting them.

Finish choices are surface-specific. Use their exact enum strings:

| Surface | Choices |
| --- | --- |
| `finish_floor` | `laminate`, `solid_wood_parquet`, `engineered_wood`, `tile`, `tile_waterproof`, `carpet`, `vinyl_lvt`, `linoleum` |
| `finish_walls` | `paint_prepared`, `wallpaper`, `tile`, `tile_waterproof`, `decorative_plaster`, `wood_veneer_panels`, `decorative_panels` |
| `finish_ceiling` | `paint_flat`, `gypsum_single_level`, `gypsum_multilevel`, `mineral_grid`, `stretch_membrane`, `metal_panels`, `wood_panels` |

A nonempty `finishes` object is a partial patch. Null clears the corresponding finish; `has_underfloor_heating: false` disables heating. Omitted keys retain their prior values. Do not send `finishes: null`, an empty object, material IDs or derived quantities as finish selections.

`attic_envelope` is either null to clear the whole intent or a complete object with `roof_id`, `profile_id`, `profile_mode`, `knee_wall_cutoff`, `minimum_included_headroom` and `average_headroom`. The Roof must be applicable to the Room's final Level, with ordered positive headroom thresholds accepted by the existing profile. `advisory_custom` pairs with `advisory`; `pl_wt_2022_attic_room` with `source_backed` requires its exact accepted thresholds, illustrated in the examples. A profile name does not establish general legal or engineering compliance.

Saving a valid attic intent can still leave coverage/analysis unresolved or uncovered. Read derived analysis and its issues. Never write usable floor area, calculated headroom zones or other computed outputs. For a Room Level move, clear the old attic intent in the same edit or provide a complete compatible replacement Roof intent.

`room.update` with `confirm_knee_walls: true` invokes the existing confirmation only after resolved attic analysis and available proposals. It creates ordinary roof-attached Walls. It is an action, not a boolean setting: a repeated confirmation rejects atomically. Inspect the new Wall IDs and top constraints. `room.delete` removes the Room through its existing lifecycle.

Examples: `room.create`, `room.update.boundary`, `.finishes`, `.clear-finishes`, `.attic.*`, `.confirm-knee-walls`, `.relevel-clear-attic`, `room.delete`.

## Foundation, Column and Slab

### Linear Foundation types and edits

`foundation.create` takes a Level-relative `base_offset`, an ordered baseline and an exact `{ kind, id }` type. `built_in` refers to an existing catalog preset; `custom` refers to a saved project Foundation type. Built-in reference geometry includes:

| Section | Exact built-in ID |
| --- | --- |
| T-shaped wall plus footing | `foundation.t_strip.reference_600_250` |
| Strip footing | `foundation.strip_footing.reference_600_300` |
| Foundation wall | `foundation.wall.reference_250_900` |
| Trench fill | `foundation.trench_fill.reference_500_900` |
| Grade beam | `foundation.grade_beam.reference_300_450` |
| Blinding layer | `foundation.blinding.reference_700_50` |

These are reference sections, not engineered sizing. Custom section definition belongs to `catalog.type.create/update`, not Foundation instance fields. Editing a shared custom type can update multiple Foundations across Levels; inspect consumers. The estimate unit is cubic metres of the completed construction, including the defined components, not a linear-metre catalog price.

`foundation.update` exposes name, length, Level, base offset and type assignment. Length grows from the existing baseline start along its existing direction. When changing Level without a new offset, the owner preserves the absolute datum and recalculates offset; an explicit offset applies to the final Level. There is no direct instance section/baseline rewrite, alignment update or `foundation.transform`. Existing axis endpoint bindings provide the supported construction movement path. `foundation.delete` uses the owner and removes its type relation and applicable cascade.

### Column profiles, vertical binding and pads

`column.create` requires a Level and plan center. Profiles are `square`, `rectangle` and `circle`; use width for square, width/depth for rectangle and diameter for circle. Circular rotation normalizes to zero. Material must be compatible. `column.update` edits profile/dimensions, rotation, name/material, Level/offset, top binding and pad settings. Center and derived height are not writable through update; `column.transform` is unsupported. A verified axis binding to `center` can move its plan placement.

Top binding modes are `auto`, `explicit` and `unconnected`. Auto resolves the next Level or uses unconnected height. Explicit needs a valid higher `top_level_id`; `top_offset` adjusts the top datum. For unconnected geometry, supply `unconnected_height`; `top_level_id: null` explicitly clears the target. Read resolved saved height after Level/offset changes.

`pad_foundation` is a nonempty partial settings object on the Column: `enabled`, `footing_length`, `footing_width`, `footing_thickness`, `founding_depth`. It is not an independently created Foundation. Existing dimension/section compatibility rules remain enforced. Square section changes can couple dimensions and pad extents. `enabled: false` is preserved and can be a no-op if already false. `column.delete` removes the Column through the existing owner.

### Slab datum, boundary and openings

`slab.create` needs a Level and valid simple polygon. `reference_plane: top | bottom` chooses which face lies at Level elevation plus `level_offset`. Thickness is at least 0.04 m. Material/assembly assignments must be compatible catalog references.

Every `slab.update` supplies exactly one action:

| Action | Required intent |
| --- | --- |
| `settings` | One or more supported datum, thickness, assignment or name fields |
| `boundary` | Complete replacement `vertices` |
| `boundary_vertex_insert` | Zero-based `edge_index` and the inserted `point` |
| `boundary_vertex_remove` | Zero-based `vertex_index` |
| `opening_add` | Polygon `vertices` for a manual hole |

Read boundary order before indexed actions. Removing a vertex from a triangle deletes the Slab through its owner. Every retained hole, including Stair-generated openings, must remain fully inside a new boundary. An invalid shrink is rejected, not saved with missing openings.

Manual holes and generated Stair openings have different owners. `opening_add` adds a manual polygon. Stair create/edit/transform/delete and Slab Level/settings edits reconcile generated openings while retaining manual holes. There is no `opening_delete`/manual-hole edit action in this schema and no direct `generated_openings` write. `slab.transform` is unsupported; use the supported boundary or existing verified axis anchors for geometry changes. `slab.delete` is supported.

Examples: `foundation.create.*`, `foundation.update/delete`; `column.create.*`, `column.update.*`, `column.delete`; `slab.create`, every `slab.update.*` action and `slab.delete`.

## Stair and Railing

### Flight, Spiral, turns and generated Slab openings

`stair.create` requires a Level, start point and a distinct direction point. Types are `flight` and `spiral`. Vertical binding follows `auto`, `explicit` or `unconnected`; explicit targets a valid higher Level, while null clears a top target. Available settings include preferred riser height, tread depth, width, landing depth, base/top offsets, construction/material, railing sides/height/thickness and automatic opening/headroom/clearance. The saved owner derives actual riser allocation and validation. Width and rule presets can also adjust related defaults, such as landing depth.

The finite rule presets are `ru_public_accessibility`, `ru_evacuation`, `ru_exterior_accessible`, `residential_ergonomic` and `custom`. Construction is `monolithic_concrete` or `assembled_steel`, with compatible material. These are existing product presets, not a new calculation capability or an engineering sign-off.

Spiral alone accepts `inner_radius`, `spiral_direction: clockwise | counter_clockwise` and `central_column`. Supplying these to Flight rejects, including an incompatible combined type conversion. Changing Spiral direction also swaps physical railing sides according to the existing owner. A Flight can switch type through `settings` when its complete new state is valid.

`stair.update` has five action branches:

| Action | Meaning |
| --- | --- |
| `settings` | Partial settings/type/Level edit |
| `turn_add` | Insert a Flight turn after zero-based `after_run_index`, with angle and left/right side |
| `turn_set` | Change zero-based `turn_index`, angle and side |
| `turn_rebalance` | Set incoming riser allocation for `turn_index` through `incoming_riser_count` |
| `turn_remove` | Remove the indicated Flight turn |

Turn actions require current Flight route indices and valid adjacent riser allocations. They are unavailable for Spiral. Read the route after each topology edit.

`stair.transform` supports absolute `center` and absolute `rotation`, unlike Wall's delta transform. Equivalent rotations such as 0/360 degrees can be no-ops. Transform and settings changes reconcile generated Slab openings; invalid fit rejects atomically. With `automatic_opening: false`, or on `stair.delete`, only generated holes are removed and manual holes remain. Do not write Slab generated geometry to imitate the Stair owner.

### Open and closed railings with stable vertices

`railing.create` requires a Level, vertices and `closed`. An open path needs at least two valid vertices, a closed path at least three. Types are `glass_with_posts`, `frameless_glass`, `metal_vertical_balusters` and `timber_cross_brace`. Settings include height, maximum module width, base offset and name. Read the saved vertex IDs after creation.

`railing.update` has `settings`, `vertex_move`, `vertex_insert` and `vertex_remove` actions. Vertex actions take an existing stable `vertex_id` belonging to the Railing, not an index or a new invented ID. Insert adds after the specified vertex and creates a fresh ID. Move takes a new plan point. Remove can delete the whole Railing when its minimum vertex count is crossed. Settings preserve existing vertex IDs. `closed` cannot be changed by update. There is no `railing.transform`; edit the supported vertices. `railing.delete` removes the Railing.

## Door and Window

These are hosted openings. `door.create` and `window.create` require `host_wall_id`, `center_ratio` in [0,1], `side: left | right` and an exact kind-matching `opening_preset_id`. Hosts can be existing supported Walls or compatible Foundation wall components. Despite the parameter name, the verified Foundation-host path uses the Foundation object ID. A Slab/Roof/Room is not such a host. The opening must fit the entire host width/height envelope without forbidden overlaps.

Placement ratio is measured along the ordered host baseline; side selects the host reference side. Rehost through `host_wall_id` plus current/desired ratio and side. The existing owner preserves the opening's stable child/host-opening identity while changing parent and updating host geometry. There is no separate Door/Window `level_id`, arbitrary world-center placement or `.transform`. Relevel the host through its own supported operation, or rehost to a suitable object.

After a host/ratio edit, use `object_get` or `objects_list` and inspect `derived.hosted_opening_context`. `parameters` and `project_get.document` are the exact saved payload, including projection caches that can retain an earlier center. The read-only context uses the current GUI hosted-opening resolver without changing those saved facts or the revision. For example, a host from `(10,5)` to `(10,15)` and ratio `0.36` resolves to `(10,8.6)`, even if the saved center still says `(10,7.4)`:

```json
{"object_id":"object.door.example","status":"resolved","provenance":"current_gui_hosted_opening_resolver","host_wall_id":"object.wall.example","center_ratio":0.36,"center":{"unit":"m","x":10,"y":8.6},"depth":{"unit":"m","value":0.125},"rotation_degrees":90,"validation_status":"valid_for_modeling","validation_messages":[]}
```

This is the context value inside `derived`, not a writable command. Use its center/depth/rotation only with `status: resolved`. `invalid_host` gives null placement. With an existing host, `invalid_geometry` can supply current candidate coordinates, but the candidate failed the resolver checks; inspect its messages and host before deciding a repair. Do not treat that candidate as accepted placement. Missing context is unknown. `validation_status` is this resolver's result, not a whole-project collision, clearance or usability assessment. Reread after moving the host as well as after editing the opening.

Built-in Door presets: `opening_preset.door.interior_900x2100`, `.interior_800x2100`, `.entry_1000x2100`, `.garage_2500x2125`, `.unfilled` (each suffix retains the full `opening_preset.door` prefix). Built-in Window presets have full prefix `opening_preset.window.` and these suffixes: `two_column_1500x1400`, `single_900x1500`, `single_1200x1500`, `double_1200x1200`, `two_column_1800x1200`, `triple_1800x1400`, `three_column_2400x1500`, `landscape_1500x900`, `single_600x1200`, `full_height_single_900x2100`, `full_height_two_column_1800x2400`, `full_height_three_column_2400x2400`, `unfilled`. The JSON collection has a separate complete creation entry for every built-in preset.

Project-local presets are available from the saved project's `editor.opening_presets`. Read their exact IDs, kinds and dimensions. Unknown or cross-kind IDs reject; do not synthesize preset IDs from measurements.

`size_mode: preset` follows catalog dimensions and locks associated custom size/configuration fields as the GUI does. Set `size_mode: custom` with the intended dimension edit when unlocking it. Switching back to preset mode restores that exact catalog size. Unfilled openings are custom-size voids and cannot enter preset mode; frame/leaf/glazing-only controls are unavailable. Supply zero explicitly when intended, such as `bottom_offset` for a Door.

Door single-swing custom settings include width/height, frame width, installation depth, bottom offset, configuration, leaf thickness, handle height, hinge side, swing direction, 15 to 180 degree swing angle and swing-volume visibility. Configurations are `solid_timber`, `solid_steel`, `security_steel`, `timber_upper_glazed`, `steel_upper_glazed`, `full_glass_aluminum`, `full_glass_pvc`. Lower-panel height belongs to upper-glazed configurations. To select a sectional-overhead Door, use its garage preset and `sectional_state: open | closed`; single-swing and frame-only controls are not interchangeable. Changing only swing direction can preserve the GUI's implicit hinge coupling; send an explicit hinge choice when it matters.

Window custom settings include width/height, frame width, installation depth, sill height, 1 to 12 horizontal/vertical sections, sill enablement/projection and profile insets. `profile_insets` must contain all four of `bottom`, `left`, `right`, `top`. Sill projection is unavailable while the sill is disabled. The ordinary Window schema does not expose sash-cell operations or glazing opacity; Roof fronton/Dormer schemas have their own separate supported controls.

Combine related dimensions when the intended final state is valid, for example small width/height plus a smaller frame, or Door height plus handle height. The owner validates final geometry; do not write forbidden transient values in separate commands. `door.delete` and `window.delete` remove the child and its corresponding host opening. Read both host and child status afterwards.

## Roof: first identify the representation

Do not choose roof actions only from the visual preset name. A saved Roof can be a primitive preset, a primitive `custom_planes` Roof or a semantic `masses` Roof. Read its actual parameters and current authoring context before edits.

- `roof.create` accepts `flat`, `shed`, `gable`, `hip`, `pavilion` and `custom` with a Level and polygon footprint. Common supported inputs cover datum offset, pitch, shell thickness/material, framing system/spacing/material/visibility, shell visibility, closure/knee-wall settings and name.
- Non-custom creation follows the existing semantic creation path when available; read its actual `masses`. A visual gable preset does not make primitive-only controls writable on a semantic Roof.
- Primitive `custom` creation preserves `custom_planes`. Its Add slope/plane-offset/plane-delete operations are a separate lifecycle. There is no common overhang control on selected custom-plane Roofs.
- A saved primitive Roof with no `parameters.masses` can expose the exact derived semantic authoring targets through `object_get` at `derived.roof_authoring_context.masses`. This read-only field does not change saved parameters or revision. Null means unavailable, not permission to guess IDs.

For a semantic Roof use `parameters.masses`. For a primitive Roof use the derived context for exact mass/boundary targets. Child IDs come from saved `dormers`, `roof_windows` or `custom_planes`. These are internal Roof children, not independently addressable project object IDs. After mass conversion, role changes or hosted creation, read the latest context and children again. A visible merged face can represent more than one semantic host intent; preserve the exact requested mass/edge selector instead of selecting a nearby rendered face.

### Common settings and availability

`roof.update` always requires an explicit `action`. The `settings` branch covers name, Level/offset, pitch, thickness/material, supported common overhang, framing/visibility and closure/knee-wall controls. Framing systems are `flat_joists`, `none`, `timber_rafters` and `truss_array`; the current geometry still decides compatibility. None of these fields establishes engineering verification of rafters/trusses.

Primitive-only `settings` controls are `roof_type`, `slope_direction` and `ridge_orientation`. Fall direction applies only to flat/shed; ridge orientation only to gable. Semantic Roofs reject these disabled primitive controls. Use the explicit mass/topology actions instead. Selected custom-plane Roofs reject a common overhang setting. A closure preset is available only when automatic wall closure or knee-wall generation is active. A negative offset can require disabling knee walls first; the combined command may set `knee_wall_enabled: false` before applying that offset.

Angles are canonicalized by the existing owner. Sloping semantic masses need a pitch greater than zero and less than 90 degrees after rounding; zero is valid for a plane mass. Invalid geometry, inaccessible setters and silently refused settings reject without a partial saved result. Do not write absolute base elevation, reference surface, arbitrary `vertices` inside `settings`, complete masses or runtime projections.

### Exact boundary and mass/topology actions

All entries below are `roof.update` action values and have exact examples in the JSON collection.

| Action | Target and intent |
| --- | --- |
| `boundary_overhang` | Exact `mass_id` and `boundary_edge_id`, with nonnegative quantity or null to inherit |
| `boundary_closure` | Same exact pair, `mode: automatic | none | null`; null restores inheritance |
| `mass_add` | New polygon and `generator: plane | eave_wavefront | ridge_spine | single_apex` |
| `mass_delete` | Exact mass; rejects deleting the last mass |
| `mass_pitch` | Uniform pitch on the exact mass |
| `mass_generator` | Convert the exact mass to an available generator, optionally supplying compatible pitch |
| `boundary_role` | Exact boundary and a generator-compatible role |
| `face_pitch` | Exact mass plus semantic `face` selector and pitch |
| `ridge_rotate` | Rotate the existing ridge orientation through its fixed owner; no arbitrary angle field |
| `ridge_end_condition` | Ridge mass, end index 0/1 and `gable | hip | join` |
| `ridge_end_pitch` | Ridge mass, an already-hip end index and pitch |
| `boundary_to_gable` | Convert an eligible wavefront boundary through the existing gable conversion |
| `apex_auto` | Single-apex mass; restore automatic visibility-kernel apex placement |
| `apex_point` | Single-apex mass and valid plan point inside its admissible footprint |
| `apex_height` | Single-apex mass and explicit height offset from its outer datum |
| `apex_uniform_pitch` | Single-apex mass; select uniform-pitch height policy |
| `apex_reference_eave` | Single-apex mass, exact eave edge and reference pitch |

A `ridge_spine` generator requires its existing supported footprint, such as a valid rectangle; an arbitrary triangle is not an accepted ridge mass. Conversions preserve the mass identity and footprint when supported but change the semantic topology. Do not use `mass_generator` as a substitute for `mass_pitch` on a completed identical generator. A repeated identical generator/canonical pitch can be a no-op; changing the pitch through a completed same-generator draft can reject.

Boundary roles are not independent free-form geometry controls. Plane exposes `plane_boundary`/`join` subject to existing validation; wavefront and apex boundaries require `eave`; ridge generating edges and end conditions determine its compatible eave/gable/join role. Use the ridge end action to change a ridge end condition. A schema-valid role can still be unavailable or fail geometry validation.

An exact boundary-overhang edit can convert a primitive or custom-plane Roof to semantic form as in the GUI. Once converted, primitive Type/orientation and `custom_plane_*` actions can become unavailable. Read the representation after the edit rather than continuing a stale plane-edit sequence. Roof changes also reconcile attic Rooms and roof-bound Walls; their envelope/continuity guards can reject an otherwise local-looking topology change.

### Semantic face selectors

Use these exact inner `face` objects for `face_pitch`, `dormer_create` or `roof_window_create`, together with `mass_id`:

| Generator/host | `face` |
| --- | --- |
| Plane mass | `{ "kind": "plane_mass" }` |
| Ridge generating slope | `{ "kind": "ridge_generating_face", "face_index": 0 }` (or 1) |
| Ridge hip cap | `{ "kind": "ridge_hip_cap", "end_index": 0 }` (or 1, already hip) |
| Wavefront eave slope | `{ "kind": "eave_generated_face", "boundary_edge_id": "<exact ID>" }` |
| Apex boundary slope | `{ "kind": "apex_boundary_face", "boundary_edge_id": "<exact ID>" }` |

These selectors identify semantic intent, not rendering mesh/triangle IDs. The face must actually resolve and be editable for the selected action. A horizontal plane or a face with insufficient free area is not automatically a valid Dormer/roof-window host. The JSON includes every selector shape for each of those three actions, with host preconditions.

### Choose windows for an attic

In the Dravit attic workflow, place windows in a Roof slope, a Dormer or a gable. Use `roof_window_create` for the slope, the Window settings of an existing Dormer, or `fronton_settings` for a Roof-generated gable. A real ordinary gable Wall can instead host `window.create`; check its surviving face and opening fit. Do not place ordinary Windows in the eave-side Walls just because the Level is named Attic. Identify the actual Roof, Wall orientation and physical cap, then inspect Top and a matching Side/3D view. The current validator does not provide a dedicated attic-window placement check, so a clean report does not confirm this rule. This is modeling guidance and does not add a Save restriction.

### Dormers

`dormer_create` takes an exact mass/face and optional `type: gable | triangular`. It invokes the existing default host-slot search. Read the saved new Dormer ID and accepted anchor/dimensions. A rejected search is not permission to create custom geometry.

`dormer_settings` targets `dormer_id`. Editable settings include type, front alignment (`bearing_wall`, `recessed`, `slope_setback`), anchor distances, width, eave height, overhang override and a partial nonempty Window object. Anchor input is exactly `station_along_bearing_line` and `inset_from_bearing_line` quantities. The read-only `bearing_boundary_edge_id` is not writable. These distances belong to the existing bearing-line frame; they are not world XY. Eave height follows the existing above-Level owner.

Dormer Window fields are width/height, sill height, frame width, center offset, section counts, opacity and all-four-sides profile insets. They must fit the Dormer type/contour; shrinking the Window before a triangular conversion can be necessary. `overhang: null` clears the override; zero requests zero overhang. `dormer_delete` removes the exact child. There is no Dormer rehost/transform/duplicate command in this action schema.

### Frontons

`fronton_settings` addresses a generated fronton through exact mass plus gable boundary. It cannot target an arbitrary eave, and it does not create an independent Fronton object. Set `fill_mode: wall | window`, nonnegative bottom/roof insets, a partial `window_assembly`, or `rectangular_window`.

A rectangular Window override requires width, height, center offset and sill height. `rectangular_window: null` removes the override and returns to contour fill. Window assembly supports nullable frame/glazing material and assembly IDs, frame width, opacity, section counts and sash cells. Each sash is a zero-based `{ column, row, operation }`; operations are `fixed`, `left_hung`, `right_hung`, `tilt_turn`. Explicit cells must be inside the requested grid. Shrinking a grid drops inherited out-of-range cells, but explicitly supplying invalid cells rejects. Null material/assembly IDs clear only those assignments.

### Roof Windows

`roof_window_create` takes exact mass and face, then uses the existing free-slot search. Read the new child ID from saved Roof parameters. `roof_window_settings` accepts child `window_id`, width/height, surface-frame `across_slope`/`up_slope`, frame width, nullable frame/glazing material IDs and visibility. These distances belong to the host slope, not the plan XY frame.

`visible: false` hides the Window while preserving its ID and physical opening. `roof_window_delete` removes it and the opening. `roof_window_duplicate` invokes the existing GUI slot search for the exact source child, produces a distinct child ID and can reject when no slot is available. Re-read the saved children after duplication. Host-face reparenting is not a settings field; there is no arbitrary rehost/transform operation.

### Primitive custom planes

`custom_plane_add` takes a valid polygon on a primitive custom Roof and inherits the selected Roof pitch. It is the existing Add slope action. `custom_plane_offset` targets exact `plane_id` and a signed `pivot_offset` in metres. The value is relative to the plane's pivot datum, not world Z. Negative values are permitted when the resulting geometry remains valid. `custom_plane_delete` removes a plane only if another remains.

These actions reject a semantic Roof, a non-custom primitive Roof, a missing plane or removal of the last plane. Roof-bound Wall/envelope continuity checks can reject an offset that would otherwise work on an isolated Roof. Direct arbitrary plane vertices/pitch/transform updates are not exposed by these plane actions; use only the actual fields, or existing verified axis anchors where applicable.

`roof.delete` removes the Roof through the existing lifecycle and reconciles attached Walls and attic Rooms. Read those affected objects as well as disappearance of the Roof.

## Result interpretation and unavailable manipulations

Read result identity, persisted settings and derived state separately. Use execution output and saved readback to obtain created object IDs. Internal mass, boundary, plane, Dormer and Roof Window IDs require the Roof's current readback. An update that creates a child may change the parent Roof without reporting a new top-level object. Never guess IDs such as `draft_1`, `dormer.1` or `mass.1` from a prior example.

Omitted, null, false and zero have different meanings. Only use null at explicitly nullable boundaries: Wall Roof choice, Column/Stair top target, Room attic intent and finish selections, boundary/Dormer overhang reset, boundary closure reset, Fronton rectangle/material/assembly resets and Roof Window material resets. Repeating a valid scalar setting may succeed with no changed IDs; this does not justify retrying create/confirm/duplicate actions. Repeated Room knee-wall confirmation is specifically rejected. Follow protocol idempotency rules for retries after ambiguous delivery.

The supported family-specific transforms here are `wall.transform` and `stair.transform`. There is no Axis, Level, Room, Foundation, Column, Slab, Railing, Door, Window or Roof `.transform` operation. Applicable existing axis construction bindings, Wall baselines, Room/Slab boundary edits, Railing vertex edits, hosted opening placement or exact Roof actions provide their real editing paths. Do not manufacture rotate/mirror/scale, join, split, manual-hole removal, child rehost, arbitrary topology writes or engineering calculations from a generic `.update` label. If no listed owner expresses the requested manipulation, report that precise capability as unsupported and preserve the saved model.

## Evidence boundary for this reference

This guide and examples were derived from the registered `InitialCommandCodec` operations and the shared Axis/Level/Wall/Room/Foundation/Column/Slab/Stair/Railing/Door/Window/Roof JSON command schemas, with existing owner behavior checked against the structural, axis, wall-top, room-detail/knee-wall, opening, Roof topology/hosted/custom-plane automation cases. It is an operational reference for the current interface; the generated schema references retain exact field bounds. Schema-valid example arguments still require the saved objects, catalogs and geometric preconditions stated in each example before execution.
