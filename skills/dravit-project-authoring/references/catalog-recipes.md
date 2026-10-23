# Catalog, Site, Pipe and Generic authoring recipes

Use this handbook to choose an existing operation and form a valid inner batch entry. Read [protocol.md](protocol.md) for the full request envelope, revision handling and operation polling. Read [native-tools.md](native-tools.md) for exact native tool names. The examples in [examples-catalog.json](examples-catalog.json) contain `operation` and `arguments`; their `id` and `requires` are documentation metadata, not command arguments. Copy only the command fields into the request.

The worked examples are independent recipes, not one sequence to submit wholesale. They use valid fixture dimensions and illustrative saved IDs. Read `requires`, substitute current IDs and coordinates, and check the live schema before execution. An ID such as `object.furniture.bed.draft_1` is an example identity, not an allocation rule. Obtain created IDs from the completed operation or a subsequent saved read. Do not predict suffixes or reuse a deleted identity. In one ordered atomic batch, use the local-reference mechanism described in the protocol when a later command targets an earlier creation.

All lengths and XY/XYZ coordinates below use metres; angles use degrees. A quantity is `{ "value": 1.2, "unit": "m" }`, an XY point is `{ "x": 2, "y": 3, "unit": "m" }`, and an angle is `{ "value": 90, "unit": "deg" }`. Use finite numbers. An object's `center` is an absolute plan position. A transform `rotation` sets the desired orientation; it is not a rotation delta. For example, 395 degrees reads back as 35 degrees. Unknown fields, derived geometry and arbitrary catalog payloads are rejected.

## Interior lifecycle shared by all 25 families

Every family in the table supports exactly `<family>.create`, `<family>.update`, `<family>.transform` and `<family>.delete`. Use [commands-interior.md](commands-interior.md) for the exact fields. The JSON companion has all four operations for every family plus named catalog alternatives.

1. Read existing Levels and the intended Room polygon. Confirm the intended authoring context and calculate the center in project coordinates. Creation requires `level_id` and `center`; the three Gym equipment families also require `configuration`.
2. Create with optional family settings, `name`, `rotation` and `room_id`. Dravit derives Room containment from the center on that Level. `room_id` is an assertion that this result is the specified saved Room. It cannot force membership or attach an object to a Room on another Level. Omit it when placing outside Rooms.
3. Update with `object_id` and only settings supported by that family. `level_id` reassignment preserves the existing relative vertical offset and derives membership on the target Level. Do not submit `base_elevation` or write parent bindings directly. The different family offset names below are intentional.
4. Transform with `object_id`, an absolute `center`, `rotation`, or both. Room membership is recalculated; an object leaving the Room retains its Level and becomes unassigned to that Room. If including `room_id`, it must assert the new containment result.
5. Delete using only the exact `object_id`. Read back the affected saved objects and inspect the relevant views after completion. A delete removes the object's geometry as well as its object record.

`update` can also accept authored rotation for Interior families. Use `transform` when the intent is placement. Plain rename and a genuine no-op do not allocate new IDs. Family settings use existing dimensional limits and coupled geometry validation even where the transport field is simply a number. A successful schema decode alone does not establish geometric applicability.

### Interior family selection

All dimension field names in this table are literal argument keys. Optional fields may be omitted to use the existing native defaults. The JSON companion shows realistic nondefault values for every family.

| Family | What it creates and configurable behavior | Relative vertical placement |
| --- | --- | --- |
| `armchair` | Soft armchair; `width`, `depth`, `height`. | Level datum through the native family owner. |
| `bathtub` | Bath; `length`, `width`, `height`; `installation_type` is `built_in` or `panelled`. | Signed `level_offset`. |
| `bed` | `bed_variant`: `standard` or `bunk`; named `size_preset` or custom `width`, `depth`, `height`; `ladder_side`: `left` or `right`. | Native Level binding. |
| `chair` | Chair/bench geometry; `width`, `depth`, `height`, `backrest_enabled`. | Native Level binding. |
| `floating_shelf` | Shelf; `width`, `depth`, `height`. It is not a Wall-host command. | `floor_offset`. |
| `table` | `top_shape`: `rectangular` or `round`; `width`, `depth`, `height`. A round table derives equal plan dimensions. | Native Level binding. |
| `wardrobe` | Equal sections; `width`, `depth`, `height`, `section_count` (1–12), `doors_enabled`. Create-only `catalog_preset`: `wardrobe` or `open_shelving`. | Native Level binding. |
| `sofa` | `preset`: `two-seat`, `three-seat` or `corner`; `width`, `depth`, `height`. | Native Level binding. |
| `kitchen_module` | One semantic kitchen module, controlled by composition/form/fill axes described below. | Active base/wall/tall dimensions define the assembly. |
| `refrigerator` | `preset`: `standard_bottom_freezer` or `side_by_side`; `width`, `depth`, `height`. | Native Level binding. |
| `sink` | Basin; `width`, `depth`, `height`. | `installation_height`. |
| `shower_cabin` | `width`, `depth`, `height`; `installation_type`: `built_in` or `freestanding`. | Signed `level_offset`. |
| `toilet` | `length`, `width`; `installation_type`: `close_coupled` or `wall_hung`. | `installation_height`. |
| `washing_machine` | `loading_type`: `front` or `top`; `width`, `depth`, `height`. | `floor_offset`. |
| `water_heater` | `width`, `depth`, `height`; optional exact immutable `connector_profile`. Connected equipment has Pipe guards. | `floor_offset`. |
| `television` | `installation_type`: `wall_mounted` or `on_cabinet`; `diagonal_inches`: 43, 50, 55, 65, 75 or 85. Cabinet fields: `cabinet_width`, `cabinet_depth`, `cabinet_height`. | `wall_floor_offset` applies to the mounted setup. |
| `office_desk` | `desk_setup` chooses fixed equipment; `width`, `depth`, `height`. | Signed `base_offset`. |
| `office_chair` | `chair_style`: `ergonomic_mesh` or `executive_leather_wood`; `width`, `depth`, `seat_height`, `backrest_height`, `armrest_height`, `tilt` in degrees, `headrest_enabled`. | Signed `base_offset`. |
| `grand_piano` | `width`, `depth`, `height`; `lid_state`: `closed` or `open`; `bench_enabled`. | Signed `base_offset`. |
| `upright_piano` | `width`, `depth`, `height`; `bench_enabled`. | Signed `base_offset`. |
| `drum_kit` | One five-piece assembly; `width`, `depth`, `height` and five drum diameter fields. | Signed `base_offset`. |
| `gym_strength` | Required immutable `configuration` selects one of eight native machines. No arbitrary machine dimensions. | Signed `base_offset`. |
| `gym_cardio` | Required immutable `configuration` selects one of six native machines. | Signed `base_offset`. |
| `gym_accessory` | Required immutable `configuration` selects one of five native accessories. | Signed `base_offset`. |
| `gym_wall_mirror` | Native Gym mirror with fixed catalog geometry; placement and `base_offset` are exposed. No `host_wall_id` argument. | Signed `base_offset`. |

The naming of `wall_hung`, `wall_mounted` or “wall mirror” does not authorize a `host_wall_id` write. These Interior schemas expose center/Level/Room placement. Do not invent a Wall host field, elevation field, attachment rule or geometry editing operation.

For `bed`, named size presets are `child`, `single`, `small_double`, `double`, `queen` and `king`; `custom` permits authored dimensions. Explicit width/depth select a custom size. Changing standard/bunk variant changes the default height before an explicit height is applied; use a height valid for the final variant. Ladder selection belongs to the bunk use case.

For Interior `table`, round diameter is authored through width/depth and is normalized to equal dimensions; do not introduce `diameter`. The existing settings rotation owner is exposed through `table.transform` and rotation on create/update, including round tables. Geometric symmetry does not remove that command field. This differs from Exterior Umbrella, whose schema has no rotation field.

`wardrobe.create` with `catalog_preset: "open_shelving"` activates the existing Office shelving defaults, including open sections. `catalog_preset` is unavailable on update. Later section, door and dimension edits use ordinary `wardrobe.update` fields; do not change a catalog activation by adding an unsupported update key.

`office_desk.desk_setup` accepts `empty`, `laptop_only`, `keyboard_mouse_single_monitor`, `keyboard_mouse_dual_monitor` and `keyboard_mouse_monitor_laptop_stand`. The equipment belongs to the desk assembly. It is not a list of independently created monitor/laptop objects.

The `drum_kit` diameter fields are `bass_drum_diameter`, `snare_diameter`, `rack_tom_small_diameter`, `rack_tom_large_diameter` and `floor_tom_diameter`. They configure the existing complete kit; they do not create separate instruments.

Gym configurations are create-only. To choose another configuration, use the supported creation/deletion lifecycle with the user's intended scope rather than sending `configuration` on update. The finite choices are:

- `gym_strength`: `olympic_flat_bench`, `combo_rack`, `smith_rack`, `multi_press`, `lat_pulldown_low_row`, `dual_adjustable_pulley`, `adjustable_bench`, `linear_leg_press`.
- `gym_cardio`: `treadmill`, `upright_bike`, `recumbent_bike`, `elliptical`, `rower`, `stair_climber`.
- `gym_accessory`: `dumbbell_rack`, `barbell_rack`, `plate_tree`, `accessory_rack`, `exercise_mat`.

### Kitchen composition and conditional settings

A kitchen module is one assembly. Choose the final axes first and send only dimension/fill fields active for that composition:

| Final `composition` | Active settings |
| --- | --- |
| `base_only` | `base_variant`, `base_depth`, `base_top_height`, common `width` and form fields. |
| `base_wall` | Base settings plus `wall_variant`, `wall_depth`, `wall_height`, `wall_bottom_offset`. |
| `full_height` | `tall_variant`, `tall_depth`, `tall_height`, common `width` and form fields. Base and wall settings are inactive. |

`form` is `single`, `double` or `corner`; corner geometry uses `corner_leg_a` and `corner_leg_b`. `base_variant` is `cabinet`, `drawers`, `sink`, `cooktop`, `cooktop_oven`, `oven`, `dishwasher` or `washing_machine`. `wall_variant` is `cabinet`, `microwave`, `none` or `hood`. `tall_variant` is `pantry`, `refrigerator_housing`, `oven_tower` or `oven_microwave_tower`.

Create-only `preset` activates `cabinet`, `drawers`, `sink`, `hob_with_oven`, `oven`, `dishwasher`, `washing_machine` or `pantry`. Update uses axes and dimensions rather than `preset`. Cooking variants retain the existing forced hood behavior: a cooking module can resolve to `base_wall` with `wall_variant: "hood"`. Read the final saved axes rather than assuming the input is a literal unnormalized payload. An update selecting `base_only` with `wall_height`, or `full_height` with `base_depth`, is invalid even though each field is individually known.

Kitchen widths are catalog choices in metres, not arbitrary run lengths. Select the final form and fill before choosing `width`:

| Final form / fill | Accepted widths, m |
| --- | --- |
| `single`, base `cabinet`/`drawers`, or tall `pantry` | 0.3, 0.4, 0.6, 0.8 |
| `single`, base `sink` | 0.6, 0.8 |
| `single`, built-in `cooktop`/`cooktop_oven`/`oven`/`dishwasher`/`washing_machine`, or tall appliance housing/tower | 0.6 |
| `double`, base `cabinet`/`drawers`/`sink`, or `full_height` with a selected tall variant | 1.0, 1.2 |
| `corner`, base `cabinet`/`sink` only | Use `corner_leg_a` and `corner_leg_b`; each leg must be at least `base_depth`. A corner is never full-height. |

Built-in base appliances stay `single`; `double` base modules admit only `cabinet`, `drawers` and `sink`. A requested 1.7 m preparation run therefore needs separate supported modules, for example 0.3 + 0.6 + 0.8 m; a 1.4 m run can use 0.6 + 0.8 m. Place their footprints edge to edge with the same depth, rear line, rotation and worktop height. Do not create a single 1.7 m module. The kitchen-module create/update examples use the same per-module requests; an ordered `project_batch` can create the whole run.

Minimum active dimensions are `base_depth: 0.45`, `base_top_height: 0.65`, `wall_depth: 0.2`, `wall_height: 0.3`, `tall_depth: 0.45`, `tall_height: 1.5`, all metres. Wall depth cannot exceed base depth; `wall_bottom_offset` must be at least `base_top_height + 0.2`. Cooking requires `wall_variant: "hood"`; a non-cooking module cannot select that hood. These are existing owner constraints, not spatial recommendations.

### Place the current Bathroom models against the intended support

Choose the represented installation, then place its rear against the actual Wall face. The current `water_heater` is a wall-mounted vertical storage heater; `sink` is a wall-hung washbasin, not a Kitchen module; `shower_cabin` with `installation_type: "built_in"` has no rear enclosure panel and needs the intended rear Wall. Keep these models supported by a real Wall at their mounting elevation. Do not substitute proximity to a Wall baseline or center-based Room membership for that contact.

For `toilet`, distinguish the default floor-standing `close_coupled` model, normally positioned near a rear Wall, from `wall_hung`, which represents a rear wall mount and concealed tank. `washing_machine` may stand freely on its floor support. The complete `shower_cabin` variant `freestanding` does not inherit the built-in shower's mandatory rear-Wall placement. These are placement instructions for the represented catalog models, not new Save admission rules.

| Family / exact variant | Native default dimensions, metres | Vertical datum | Rear / front in unrotated local plan |
| --- | --- | --- | --- |
| `water_heater` | width 0.48, depth 0.48, body height 0.82 | `floor_offset: 1.1` places tank-body bottom at Level+1.1; connections extend below the body | rear −Y / front +Y |
| `sink` | width 0.60, depth 0.45, ceramic height 0.165 | `installation_height: 0.85` is rim height; ceramic bottom is Level+0.685 | rear −Y / front +Y |
| `shower_cabin`, `built_in` (default) | width 0.90, depth 0.90, height 2.10 | signed `level_offset: 0` | rear −Y / front +Y |
| `shower_cabin`, `freestanding` | width 0.90, depth 0.90, height 2.10 | signed `level_offset: 0` | service rear −Y / curved front enclosure |
| `toilet`, `close_coupled` (default) | length 0.65, width 0.37 | `installation_height: 0.40` is the seat datum; base=Level+installation_height−0.40 | rear −X / front +X |
| `toilet`, `wall_hung` | length 0.65, width 0.37 | same seat datum; native geometry omits the floor pedestal | rear −X / front +X |
| `washing_machine`, `front` (default) | width 0.60, depth 0.60, height 0.85 | `floor_offset: 0` | rear −Y / front +Y |
| `washing_machine`, `top` | width 0.40, depth 0.60, height 0.90 | `floor_offset: 0` | service rear −Y / front +Y |

Read saved dimensions before placing an existing object. Changing washing-machine `loading_type` reapplies that variant's dimensions before explicit dimension overrides. Sink installation height must accommodate its ceramic height. Use the exact family fields; `base_elevation` is derived, and these Interior schemas have no `host_wall_id`, Wall-snap command or persistent Wall-following relation.

`<family>.transform` sets an absolute plan `center` and/or absolute `rotation` in degrees. It does not add a displacement or angle. At rotation 0, the rear footprint midpoint is `(0, -depth/2)` for heater/basin/shower/washer; it is `(-length/2, 0)` for a toilet. For a horizontal Wall and objects facing +Y, use rotation 0 for the first group and rotation 90 for a toilet. For a vertical Wall and objects facing +X, use rotation 270 for the first group and rotation 0 for a toilet. The footprint rear is edge0 for the first group and edge3 for a toilet.

Measure from a Wall face after applying its thickness and `baseline_alignment`, not from its baseline. For a Wall baseline `(0,0)→(20,0)`, centered alignment and thickness0.25, the face toward positive Y is Y 0.125. With default dimensions, rear footprint contact therefore places a basin center at Y 0.350, built-in shower at Y 0.575, toilet at Y 0.450 with rotation 90, and washer at Y 0.425 if wall-adjacent placement is desired. A freely placed washer needs no such rear contact.

The heater's rectangular footprint describes the tank body. Its native rear bracket extends another `b = min(0.022, max(0.012, depth*0.04))` metres behind that footprint. For exact bracket-to-face contact, offset its center from the face by `depth/2+b`. Default depth 0.48 gives b 0.0192 and center Y 0.3842 against the example face, preserving the intended gap behind the tank body.

The general placement calculation is `C = F + a*n`, where F is a point on the chosen Wall face and n is the unit direction from that face into the fixture. Use a=depth/2 for the first group, a=length/2 for the toilet, and a=depth/2+b for exact heater bracket contact; choose rotation so the fixture's local front direction equals n. The face segment must cover the mounting span and its real elevation. Check openings and the remaining Wall body, including any Roof trim, instead of attaching to an absent part of a Wall.

Current fixture placement preserves the supplied center and does not provide automatic Wall snapping. Do not tell the user or another model that these commands automatically snap or create a host relationship. Read the resulting objects and inspect Top plus the relevant elevation/3D view. Center-based Room membership is useful context, not physical support proof. A connected Water Heater retains the existing Pipe provider guards.

All new placement/spatial validator findings are advisory recommendations and MCP feedback. They do not prevent Save. If Wall contact or the support geometry cannot be established, report the missing fact instead of declaring support validated. Existing schema and native authoring guards remain their existing contracts.

Use the independent `*-support-*` recipes in [examples-catalog.json](examples-catalog.json). Each has its own exact Wall, Level, default dimensions and orientation prerequisites. Create examples already use the final placement; transform examples set that absolute placement on an existing matching object. These are alternatives, not one bathroom layout to submit together.

### Water Heater profiles and connected-object guards

Select a `connector_profile` with both `catalog_version` and `profile_id`, obtained from the available immutable Pipe catalog. The demonstrated profile is `object_connector.water_heater.g1_2_flat.v1`; the example version is `neutral_pipe.wp1.2026-07-19.v1`. These are concrete example identities, not instructions to override the current catalog. Sending `connector_profile: null` clears an unconnected selection. Omitting the field preserves it.

Read `object.get` and its `derived.pipe_authoring_context` after selection. Inspect the pinned catalog identity, exact port frame/XYZ, terminal center and occupancy before routing. Catalog files, SHA values, connector topology and visual assets are provided by Dravit; do not submit their contents through command arguments.

A connected Water Heater cannot be moved, resized, have its profile cleared/replaced or be deleted while that change would invalidate its Pipe binding. A rename and a genuine no-op remain usable. Resolve the connected network through the supported Pipe lifecycle first when the requested edit requires it; never bypass the guard by editing stored projections or relationships.

## Site and Exterior: all 14 families

Use [commands-site.md](commands-site.md) for exact fields and limits. Point-based Exterior objects are owned by the root Site, with a required Level and signed `base_offset`. Their derived base elevation follows `Level elevation + base_offset`; Room containment does not reparent them. Updating the Level preserves the relative offset. Their create operation uses an absolute XY `center`; transform changes that center and, where allowed, orientation.

| Family | Supported operations | Native configuration and important conditions |
| --- | --- | --- |
| `exterior_bench` | create, update, transform, delete | `length`, `depth`, `overall_height`, `seat_height`. Seat/back dimensions must form a valid final assembly. |
| `exterior_chair` | create, update, transform, delete | `width`, `depth`, `overall_height`, `seat_height`. Native tubular chair assembly. |
| `exterior_table` | create, update, transform, delete | `top_shape`: `rectangular` uses `width`/`depth`; `round` uses `diameter`. Both use `height`. Do not combine inactive dimensions. |
| `exterior_waste_bin` | create, update, transform, delete | `form`: `square_side_loading` uses `width`/`depth`; `round_top_loading` uses `diameter`. Both use `height`. |
| `exterior_sun_lounger` | create, update, transform, delete | `length`, `width`, `deck_height`; fixed native backrest geometry. |
| `exterior_umbrella` | create, update, transform, delete | `canopy_diameter`, `pole_height`, `base_enabled`; transform supports center only. Rotation is absent. |
| `exterior_canopy` | create, update, transform, delete | `canopy_type`, `length`, `width`, `overall_height`; existing automatic perimeter supports. |
| `exterior_transport` | create, update, transform, delete | Create-only `form_factor`; `color` is editable. Runtime asset and dimensions remain catalog-owned. |
| `vegetation` | create, update, transform, delete | Create-only `form`; supported dimensions depend on the selected form. |
| `terrain` | create, update, transform, delete | Semantic polygon vertices, Level, signed `offset`; transform is XY `translation` only. |
| `pavement` | create, update, delete | Polygon, datum/catalog settings, corner and curb actions; no transform operation. |
| `pool` | create, update, transform, delete | Polygon, depth/shell/bands and corner actions; transform is XY `translation` only. |
| `fence` | create, update, delete | Open/closed semantic polyline, automatic posts and hosted access; no transform operation. |
| `fence_access` | create, update, delete | Hosted wicket or gate on an exact saved Fence span; no transform operation. |

Canopy types are `tensioned_fabric`, `dense_edge_slats` and `sparse_rafters_with_glass`. No command adds new covering types, engineering behavior or support layouts.

Transport form factors are `bicycle`, `compact`, `sedan`, `wagon`, `hatchback`, `coupe`, `minivan`, `sports_car`, `pickup`, `suv` and `offroad`. Colors are `white`, `black`, `silver`, `graphite`, `red`, `blue`, `green` and `gold`. Select the catalog form at creation and read its resulting asset reference; do not write `visual_asset_ref`, mesh data or free dimensions. Form factor cannot be changed by `exterior_transport.update`.

Vegetation forms are `hedge`, `classic_tree`, `spruce`, `palm` and `shrub`. Hedge exposes `height`, `length` and `width`; other forms expose `crown_diameter` and `height`. The form is immutable through update. Catalog-backed visual references remain Dravit-owned. A form name does not grant a polygon-authoring or botanical simulation command beyond these existing fields.

### Semantic polygon and polyline vertices

Terrain, Pavement and Pool require at least three vertices; Fence requires at least two. Each creation vertex is `{ "id": "v1", "point": { "x": 10, "y": 10, "unit": "m" } }`. Supply distinct semantic IDs and a valid nondegenerate boundary. They are not array indices. After a mutation, read the saved ordered vertices/corners before targeting a later action.

`vertex_move` identifies an existing `vertex_id` and supplies its new absolute `point`. `vertex_insert` identifies the existing vertex after which a new point is inserted; Dravit allocates the new semantic identity, so read it back. `vertex_remove` identifies the vertex to remove. To retain the object, leave a valid polygon with at least three vertices. Native lifecycle rules can delete an existing polygon when an edit collapses it: Terrain and Pavement remove the object for fewer than three vertices or supported zero-area collapse, and removing a corner from a three-corner Pool deletes that Pool. Do not assume every collapsing edit is a rejection. Read the completed outcome and object existence. A whole raw polygon replacement is not a supported update shortcut.

Each action is a separate closed update variant. Do not mix settings fields with `vertex_move`, or combine two different action shapes in one entry. For settings, `action: "settings"` is explicit and may be omitted. The JSON companion has an entry for every action on every applicable family:

| Family | Update actions |
| --- | --- |
| `terrain` | `settings`, `vertex_move`, `vertex_insert`, `vertex_remove`. |
| `pavement` | `settings`, `vertex_move`, `vertex_insert`, `vertex_remove`, `corner_radius`, `apply_preset`, `curb_segment`, `curb_profile`. |
| `pool` | `settings`, `vertex_move`, `vertex_insert`, `vertex_remove`, `corner_radius`, `edge_width`. |
| `fence` | `settings`, `vertex_move`. Insert/remove are not exposed. |

Terrain and Pool translation is a displacement `{ "x": 2, "y": -1, "unit": "m" }`, not an absolute center. It moves the existing boundary through the shared owner. These operations do not accept rotation or XYZ translation.

### Pavement datum, catalog and curb recipes

Pavement creation always needs `vertices`. Choose one coherent datum:

- `datum: "level"`: provide the exact saved `level_id` and optional signed `offset`.
- `datum: "site_zero"`: provide optional signed `offset`; omit `level_id` and `absolute_elevation`.
- `datum: "absolute"`: provide `absolute_elevation`; omit `level_id` and `offset`.

Use the same active-field rule on a settings update, based on the final datum. `absolute_elevation` is available only to absolute datum; `offset` is unavailable there. A Level ID cannot be supplied for site-zero/absolute datum. Creation can optionally use an exact `owner_id` accepted by the existing owner; read the target hierarchy rather than guessing the owner. For `site_zero`, the owner must be a root Site. For Level/absolute datum, it must be a Storey below a Building below a root Site. The default owner resolves or creates the existing semantic hierarchy as needed. A settings change to datum can rederive the owner; ownership is not a free update field.

`pavement_type` is `asphalt` or `paving`. Select only existing pavement `assembly_id`/`material_id` values from the project catalog. Surface material must be a pavement material, not a kerb material. `thickness` is a positive length. `apply_preset` reapplies native preset settings; for example, the existing asphalt preset selects its native 0.07 m thickness. A plain settings change and preset activation are distinct actions.

`corner_radius` takes `vertex_id` and a metre `radius`. `curb_segment` takes the semantic start-corner ID of the edge and `enabled: true` or `false`; it changes one edge, not an index range. `curb_profile` configures the shared curb section with optional `material_id`, positive `width`, positive `total_height` and `upstand_above_pavement`. Its material must be an available kerb material. Example catalog identities are `material.pavement.concrete_paver_preliminary`, `material.pavement.asphalt_preliminary` and `material.pavement.concrete_kerb_preliminary`; verify their availability before use.

Read saved corner IDs, enabled curb edge starts, final catalog selections, datum and elevations after completion. Recheck dependent edge settings after topology edits.

### Pool settings and edge bands

Pool uses exact `level_id` and semantic plan vertices. Settings expose `flat_depth`, `waterline_drop`, `interior_transition_radius`, `coping_width`, `deck_width` and `shell_thickness`. Use a positive depth and shell thickness and a valid coupled geometric result. `flat_depth` edits an existing flat depth profile; it is rejected for a saved sloped profile. No command authors the hidden slope-profile fields.

`corner_radius` targets one saved corner. `edge_width` targets the edge beginning at `vertex_id`, with `band: "coping"` or `"deck"` and metre `width`. It creates/changes that edge's override while the settings widths remain the defaults. The examples include both bands. Inspect the final saved profile, edge overrides and Top/3D geometry; a Pool command does not add a new hydrological or engineering calculation.

### Fence hosts and access conditions

Fence `fence_type` is `masonry_plinth_horizontal_slats` or `composite_privacy_panels`. Creation accepts `closed`; the settings update exposes `height`, `maximum_post_spacing`, Level and signed `base_offset`, while `vertex_move` edits an existing polyline point. Post positions are derived by the existing owner.

Read the saved Fence before creating access. `host_span_id` is `span:<start_vertex_id>:<end_vertex_id>` using consecutive ordered saved vertex IDs. Closed fences additionally have a last-to-first span. A valid example is `span:v1:v2` only when those exact adjacent IDs exist. Do not use a vertex index, a geometric distance or a stale span after edits.

`fence_access.create` requires `host_fence_id`, `host_span_id`, `center_ratio` (0–1) and immutable `access_type`. Choose `wicket`, `double_swing_gate` or `sliding_gate`. The host owns the access and supplies its Level/datum. Optional width/height must fit the host span and respect existing overlap/placement guards; a ratio within 0–1 alone does not prove that a gate fits.

| Access type | Applicable directional settings |
| --- | --- |
| `wicket` | `hinge_edge`: `start`/`end`; `swing_side`: `a`/`b`. |
| `double_swing_gate` | `swing_side`: `a`/`b`; no `hinge_edge` field for this type. |
| `sliding_gate` | `slide_direction`: `start`/`end`; no `hinge_edge` or `swing_side`. |

All access types expose `width`, `height`, `center_ratio`, `operation_clearance_visible` and `name` on update. Host, span and access type are not update fields. There is no separate access transform; reposition within the existing span using `center_ratio`. Read dependent hosted access after a Fence vertex edit or deletion. Do not detach hosted objects by writing parent IDs.

## Pipe WP1: route, graph reads and guarded edits

Use [commands-pipes.md](commands-pipes.md). WP1 exposes exactly four commands: `pipe.route.create`, `pipe.node.update`, `pipe.fitting.update`, `pipe.network.delete`. Segments, nodes, fittings, connector ports, connections/bindings, graph IDs, takeouts and Building/PlumbingSystem ownership are created or updated by these existing owners. There are no independent segment-create/delete, node-create/delete, connection-create/delete, network-transform or raw graph-write operations.

The supported authoring slice is a saved profiled Water Heater's free `cold_in`, `cold_water`, d20, with exact 90-degree turns and available stock lengths. Other systems/sizes, hot outlet authoring, tees/branches and joins into existing networks are unavailable. Do not approximate a requested unsupported connection with a visually similar disconnected pipe.

### Routing sequence

1. Read the current Water Heater object with `derived.pipe_authoring_context`. Confirm the profile and immutable `catalog_version`/`catalog_sha256`, `connector_key`, exact `position`, `direction`, `authoring_frame`, `terminal_center`, `occupied`, and the advertised pipe/fitting identities. A missing authoring context is a prerequisite failure, not permission to fabricate a port.
2. Confirm `occupied` is false and select an existing saved Level. `level_id` is required for routing, while each vertex uses absolute world XYZ metres. Z is not a Level-relative offset.
3. Submit `pipe.route.create` with `provider_object_id`, `connector_key: "cold_in"`, `level_id` and 1–100 `vertices`. These vertices are the subsequent route points after the derived terminal center. Do not repeat the port position as a substitute for that center. The fitting takeout makes the two positions different.
4. Use axis-aligned legs consistent with the provider's authoring frame, exact permitted turns and catalog stock. Dravit selects the pinned catalog entries and builds the graph. Do not send custom `network`, catalog, port/orientation, segment, fitting or binding structures.
5. Read the completed saved network. Record the returned network ID and its actual node, segment and fitting IDs. Inspect the full saved graph, provider binding, catalog pin and ownership, and verify Top/Side/3D as appropriate to its XYZ path.

The route example uses an unoccupied fixture with terminal center `(0, 0, 0.9615)` m, then `(1, 0, 0.9615)`, `(1, 0, 0.2)` and `(2, 0, 0.2)`. These are a valid demonstrated path for that exact heater and catalog. For another placement/rotation/profile, derive new coordinates from its current context.

### Graph reads and edits

Read the network before every edit; use exact current IDs from its semantic graph. A segment record describes the existing connection between graph nodes and the selected pipe product. A fitting record carries its exact catalog fitting/ports. Bindings connect the graph to the equipment provider and may include design requirements. These records are evidence to inspect, not command payloads to overwrite.

`pipe.node.update` moves only an existing free terminal node along its incident axis to the absolute XYZ `position`. Bound endpoints and internal turn nodes cannot be moved this way. Off-axis and out-of-stock moves are rejected. In the worked fixture, the endpoint at `(2,0,0.2)` can extend along X to `(3,0,0.2)`; changing Y as well is invalid.

`pipe.fitting.update` sets `roll` in degrees for an existing saved `fitting_id` in a `network_id`. The shared owner rotates the connected downstream branch. Read back the whole branch and endpoint positions; do not assume that only a decorative fitting mesh changed. Do not write a quaternion, raw orientation, or individual port frame.

`pipe.network.delete` removes the complete connected graph, releases the equipment port and normalizes remaining catalog references. It retains the Water Heater and semantic ownership records. Delete/recreate allocates fresh graph IDs; preserve IDs from current reads and never reconstruct them from the example names.

A failed Pipe action must leave the candidate unchanged. After a rejection, inspect the returned parameter/error, refresh the graph/context and change the requested input only within the supported slice. Do not fall back to stored-document mutation.

## Generic Shape and Group

Use [commands-generic.md](commands-generic.md). Generic objects expose their existing placement, settings, grouping and transform behavior. They do not acquire structural, material-takeoff or engineering meaning from their appearance.

`generic_shape.create` requires `shape`, `level_id` and XY `center`. Shape is `box`, `cylinder`, `sphere` or `wedge` and is immutable after creation. Optional `width`, `depth`, `height` are 0.01–1000 m; `base_offset` is signed relative to the Level. Use a six-digit hex `color`, `opacity` from 0.15 to 1, optional `name` and degree `rotation`. `cylinder_orientation` (`upright`/`side`) applies only to a cylinder.

`generic_shape.update` edits the exposed settings and requires at least one field beyond `object_id`. It cannot change `shape` or set center/rotation; use `generic_shape.transform` for those placement changes. Read back normalized values: for example `#AABBCC` becomes `#aabbcc`, and opacity 0.45678 becomes 0.4568. Level reassignment derives base elevation from the preserved signed offset.

`generic_shape.transform` requires `object_id` plus center, rotation or both. Repeating the same normalized transform is a no-op. `generic_shape.delete` removes an ungrouped shape and geometry.

### Ordered group lifecycle

1. Create/read 2–100 distinct ungrouped Generic Shapes with the same Site parent. Membership is restricted to Generic Shapes, not arbitrary Interior, Wall or Site objects. Confirm current saved IDs and intended order.
2. Call `generic_group.create` with ordered `object_ids` and optional `name`. The owner creates a group container and reparents the children, retaining their identities and geometry. Duplicate identities are invalid even when two references use different local/stable spellings that resolve to the same ID.
3. Rename via `generic_group.update` with `object_id` and required `name`. Membership replacement is not supported by update.
4. Move/rotate the assembly through `generic_group.transform`, with center, rotation or both. The group center comes from current member bounds. Rotation changes the relative child positions and orientations together. It is not a command to scale or deform the group.
5. Choose deletion scope deliberately: `generic_group.delete` deletes the container and all child shapes. `object.ungroup` removes only the container, preserving child IDs, geometry and transforms and restoring their parent ownership.

Grouped children retain supported settings such as dimensions, offset, Level, name, color and opacity. Their independent center/rotation transform, cylinder-orientation change and individual deletion are guarded. Transform the group, or ungroup first when the intended edit requires an independent child. Do not work around the guard with a parent update.

## Readback and completion evidence

For all families, use the full operation lifecycle in [verification.md](verification.md). A submitted/queued command or accepted JSON is not a saved modeling result. Wait for completion, read the current revision and exact resulting object parameters/relations, and inspect the relevant views for the intended spatial outcome.

Check the specific contract you changed: family/preset and dimensions; actual Level/Room/Site/host ownership; relative offset and derived elevation; semantic vertex IDs and edge overrides; immutable catalog identities; connected Pipe branch coordinates; or ordered Generic membership. Confirm the returned IDs remain stable across settings and transforms. For a destructive operation, confirm the precise removed and retained objects, especially hosted access, connected networks and group children. Keep conclusions limited to the checks performed.
