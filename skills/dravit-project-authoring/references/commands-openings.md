# Openings command reference

Read [protocol](protocol.md) for the full tool envelope and revision handling. These are exact inner `arguments` schemas, not top-level tool calls. All listed operations can be submitted through `project_batch`; a dedicated native tool exists only when listed in [native tools](native-tools.md). Schemas include every writable field, unit, enum, limit, null/reset and union branch. `required` applies to its enclosing object; choose exactly one `oneOf` branch. Omission preserves an existing setting on update unless the relevant recipe states otherwise. Read current `tool_describe` if the server differs from this snapshot.

Batch reference overrides are generated from the real batch schema: only `reference_paths` additionally accept `{"local_id":"alias"}`; `[]` means array elements. A non-null `local_id_pattern` permits an entry alias, null forbids it. The [protocol compatibility table](protocol.md#batch-reference-compatibility) applies. Other fields remain unchanged.

Examples and prerequisites: [construction and roofs](structure-recipes.md), [interior, site, pipes and groups](catalog-recipes.md), [structural examples](examples-structure.json), [catalog examples](examples-catalog.json), [workflow examples](examples-workflows.json).

- [door.create](#doorcreate)
- [door.delete](#doordelete)
- [door.update](#doorupdate)
- [window.create](#windowcreate)
- [window.delete](#windowdelete)
- [window.update](#windowupdate)

## door.create

<!-- operation:door.create -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["host_wall_id","center_ratio","side","opening_preset_id"],"properties":{"host_wall_id":{"type":"string","minLength":1,"maxLength":255},"center_ratio":{"type":"number","minimum":0,"maximum":1},"side":{"type":"string","enum":["left","right"]},"opening_preset_id":{"type":"string","minLength":1,"maxLength":255,"description":"Exact catalog ID. Built-in IDs: opening_preset.door.interior_900x2100, opening_preset.door.interior_800x2100, opening_preset.door.entry_1000x2100, opening_preset.door.garage_2500x2125, opening_preset.door.unfilled. Project-local presets: project_get.document.editor.opening_presets. Unknown/cross-kind IDs are rejected."},"size_mode":{"type":"string","enum":["preset","custom"]},"width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"frame_width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"installation_depth":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"name":{"type":"string","minLength":1,"maxLength":120,"pattern":"^[\\s\\S]*\\S[\\s\\S]*$"},"bottom_offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"operation_type":{"type":"string","enum":["single_swing","sectional_overhead"]},"configuration_type":{"type":"string","enum":["solid_timber","solid_steel","security_steel","timber_upper_glazed","steel_upper_glazed","full_glass_aluminum","full_glass_pvc"]},"sectional_state":{"type":"string","enum":["open","closed"]},"leaf_thickness":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"handle_height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"lower_panel_height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"hinge_side":{"type":"string","enum":["left","right"]},"swing_direction":{"type":"string","enum":["away_from_reference","toward_reference"]},"swing_angle":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":15,"maximum":180},"unit":{"type":"string","enum":["deg"]}}},"swing_volume_3d_visible":{"type":"boolean"}},"description":"Existing GUI opening lifecycle. Host must be a saved Wall or Foundation wall component. Level is inherited from host. Width/height require custom size mode; unfilled always uses custom size and requires width on create. Derived geometry is read-only. Dormer windows use roof.update."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["host_wall_id"],"local_id_pattern":"^[a-z][a-z0-9_]{0,63}$"}
```

## door.delete

<!-- operation:door.delete -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255}},"description":"Existing GUI opening lifecycle. Host must be a saved Wall or Foundation wall component. Level is inherited from host. Width/height require custom size mode; unfilled always uses custom size and requires width on create. Derived geometry is read-only. Dormer windows use roof.update."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## door.update

<!-- operation:door.update -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255},"host_wall_id":{"type":"string","minLength":1,"maxLength":255},"center_ratio":{"type":"number","minimum":0,"maximum":1},"side":{"type":"string","enum":["left","right"]},"opening_preset_id":{"type":"string","minLength":1,"maxLength":255,"description":"Exact catalog ID. Built-in IDs: opening_preset.door.interior_900x2100, opening_preset.door.interior_800x2100, opening_preset.door.entry_1000x2100, opening_preset.door.garage_2500x2125, opening_preset.door.unfilled. Project-local presets: project_get.document.editor.opening_presets. Unknown/cross-kind IDs are rejected."},"size_mode":{"type":"string","enum":["preset","custom"]},"width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"frame_width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"installation_depth":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"name":{"type":"string","minLength":1,"maxLength":120,"pattern":"^[\\s\\S]*\\S[\\s\\S]*$"},"bottom_offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"operation_type":{"type":"string","enum":["single_swing","sectional_overhead"]},"configuration_type":{"type":"string","enum":["solid_timber","solid_steel","security_steel","timber_upper_glazed","steel_upper_glazed","full_glass_aluminum","full_glass_pvc"]},"sectional_state":{"type":"string","enum":["open","closed"]},"leaf_thickness":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"handle_height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"lower_panel_height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"hinge_side":{"type":"string","enum":["left","right"]},"swing_direction":{"type":"string","enum":["away_from_reference","toward_reference"]},"swing_angle":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":15,"maximum":180},"unit":{"type":"string","enum":["deg"]}}},"swing_volume_3d_visible":{"type":"boolean"}},"minProperties":2,"description":"Existing GUI opening lifecycle. Host must be a saved Wall or Foundation wall component. Level is inherited from host. Width/height require custom size mode; unfilled always uses custom size and requires width on create. Derived geometry is read-only. Dormer windows use roof.update."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","host_wall_id"],"local_id_pattern":null}
```

## window.create

<!-- operation:window.create -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["host_wall_id","center_ratio","side","opening_preset_id"],"properties":{"host_wall_id":{"type":"string","minLength":1,"maxLength":255},"center_ratio":{"type":"number","minimum":0,"maximum":1},"side":{"type":"string","enum":["left","right"]},"opening_preset_id":{"type":"string","minLength":1,"maxLength":255,"description":"Exact catalog ID. Built-in IDs: opening_preset.window.two_column_1500x1400, opening_preset.window.single_900x1500, opening_preset.window.single_1200x1500, opening_preset.window.double_1200x1200, opening_preset.window.two_column_1800x1200, opening_preset.window.triple_1800x1400, opening_preset.window.three_column_2400x1500, opening_preset.window.landscape_1500x900, opening_preset.window.single_600x1200, opening_preset.window.full_height_single_900x2100, opening_preset.window.full_height_two_column_1800x2400, opening_preset.window.full_height_three_column_2400x2400, opening_preset.window.unfilled. Project-local presets: project_get.document.editor.opening_presets. Unknown/cross-kind IDs are rejected."},"size_mode":{"type":"string","enum":["preset","custom"]},"width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"frame_width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"installation_depth":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"name":{"type":"string","minLength":1,"maxLength":120,"pattern":"^[\\s\\S]*\\S[\\s\\S]*$"},"sill_height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"horizontal_sections":{"type":"integer","minimum":1,"maximum":12},"vertical_sections":{"type":"integer","minimum":1,"maximum":12},"sill_enabled":{"type":"boolean"},"sill_projection":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"profile_insets":{"type":"object","additionalProperties":false,"required":["bottom","left","right","top"],"properties":{"bottom":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"left":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"right":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"top":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}}}},"description":"Existing GUI opening lifecycle. Host must be a saved Wall or Foundation wall component. Level is inherited from host. Width/height require custom size mode; unfilled always uses custom size and requires width on create. Derived geometry is read-only. Dormer windows use roof.update."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["host_wall_id"],"local_id_pattern":"^[a-z][a-z0-9_]{0,63}$"}
```

## window.delete

<!-- operation:window.delete -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255}},"description":"Existing GUI opening lifecycle. Host must be a saved Wall or Foundation wall component. Level is inherited from host. Width/height require custom size mode; unfilled always uses custom size and requires width on create. Derived geometry is read-only. Dormer windows use roof.update."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## window.update

<!-- operation:window.update -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255},"host_wall_id":{"type":"string","minLength":1,"maxLength":255},"center_ratio":{"type":"number","minimum":0,"maximum":1},"side":{"type":"string","enum":["left","right"]},"opening_preset_id":{"type":"string","minLength":1,"maxLength":255,"description":"Exact catalog ID. Built-in IDs: opening_preset.window.two_column_1500x1400, opening_preset.window.single_900x1500, opening_preset.window.single_1200x1500, opening_preset.window.double_1200x1200, opening_preset.window.two_column_1800x1200, opening_preset.window.triple_1800x1400, opening_preset.window.three_column_2400x1500, opening_preset.window.landscape_1500x900, opening_preset.window.single_600x1200, opening_preset.window.full_height_single_900x2100, opening_preset.window.full_height_two_column_1800x2400, opening_preset.window.full_height_three_column_2400x2400, opening_preset.window.unfilled. Project-local presets: project_get.document.editor.opening_presets. Unknown/cross-kind IDs are rejected."},"size_mode":{"type":"string","enum":["preset","custom"]},"width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"frame_width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"installation_depth":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"name":{"type":"string","minLength":1,"maxLength":120,"pattern":"^[\\s\\S]*\\S[\\s\\S]*$"},"sill_height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"horizontal_sections":{"type":"integer","minimum":1,"maximum":12},"vertical_sections":{"type":"integer","minimum":1,"maximum":12},"sill_enabled":{"type":"boolean"},"sill_projection":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"profile_insets":{"type":"object","additionalProperties":false,"required":["bottom","left","right","top"],"properties":{"bottom":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"left":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"right":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"top":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}}}},"minProperties":2,"description":"Existing GUI opening lifecycle. Host must be a saved Wall or Foundation wall component. Level is inherited from host. Width/height require custom size mode; unfilled always uses custom size and requires width on create. Derived geometry is read-only. Dormer windows use roof.update."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","host_wall_id"],"local_id_pattern":null}
```

