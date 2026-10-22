# Structure command reference

Read [protocol](protocol.md) for the full tool envelope and revision handling. These are exact inner `arguments` schemas, not top-level tool calls. All listed operations can be submitted through `project_batch`; a dedicated native tool exists only when listed in [native tools](native-tools.md). Schemas include every writable field, unit, enum, limit, null/reset and union branch. `required` applies to its enclosing object; choose exactly one `oneOf` branch. Omission preserves an existing setting on update unless the relevant recipe states otherwise. Read current `tool_describe` if the server differs from this snapshot.

Batch reference overrides are generated from the real batch schema: only `reference_paths` additionally accept `{"local_id":"alias"}`; `[]` means array elements. A non-null `local_id_pattern` permits an entry alias, null forbids it. The [protocol compatibility table](protocol.md#batch-reference-compatibility) applies. Other fields remain unchanged.

Examples and prerequisites: [construction and roofs](structure-recipes.md), [interior, site, pipes and groups](catalog-recipes.md), [structural examples](examples-structure.json), [catalog examples](examples-catalog.json), [workflow examples](examples-workflows.json).

- [axis.create](#axiscreate)
- [axis.delete](#axisdelete)
- [axis.update](#axisupdate)
- [column.create](#columncreate)
- [column.delete](#columndelete)
- [column.update](#columnupdate)
- [foundation.create](#foundationcreate)
- [foundation.delete](#foundationdelete)
- [foundation.update](#foundationupdate)
- [level.create](#levelcreate)
- [level.delete](#leveldelete)
- [level.update](#levelupdate)
- [room.create](#roomcreate)
- [room.delete](#roomdelete)
- [room.update](#roomupdate)
- [slab.create](#slabcreate)
- [slab.delete](#slabdelete)
- [slab.update](#slabupdate)
- [wall.create](#wallcreate)
- [wall.delete](#walldelete)
- [wall.transform](#walltransform)
- [wall.update](#wallupdate)

## axis.create

<!-- operation:axis.create -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["orientation","coordinate"],"properties":{"orientation":{"enum":["vertical","horizontal","custom"],"type":"string"},"coordinate":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"label":{"type":"string","minLength":1,"maxLength":255,"pattern":"^[\\s\\S]*\\S[\\s\\S]*$"},"angle":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":0,"maximum":90},"unit":{"type":"string","enum":["deg"]}}}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":[],"local_id_pattern":"^[a-z][a-z0-9_]{0,63}$"}
```

## axis.delete

<!-- operation:axis.delete -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":133,"pattern":"^axis\\.[A-Za-z0-9][A-Za-z0-9._-]{0,127}$"}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## axis.update

<!-- operation:axis.update -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"minProperties":2,"properties":{"object_id":{"type":"string","minLength":1,"maxLength":133,"pattern":"^(?:axis\\.[A-Za-z0-9][A-Za-z0-9._-]{0,127}|group\\.axis_grid\\.primary)$"},"label":{"type":"string","minLength":1,"maxLength":255,"pattern":"^[\\s\\S]*\\S[\\s\\S]*$"},"coordinate":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"locked":{"type":"boolean"},"construction_lock_enabled":{"type":"boolean"},"angle":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":0,"maximum":90},"unit":{"type":"string","enum":["deg"]}}},"bindings":{"type":"array","maxItems":10000,"items":{"type":"object","additionalProperties":false,"required":["object_id","anchor_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255,"pattern":"^[a-z][a-z0-9]*(?:[._-][a-z0-9]+)*$"},"anchor_id":{"type":"string","minLength":1,"maxLength":255}}}},"spacing":{"type":"object","additionalProperties":false,"required":["from_axis_id","distance"],"properties":{"from_axis_id":{"type":"string","minLength":1,"maxLength":133,"pattern":"^axis\\.[A-Za-z0-9][A-Za-z0-9._-]{0,127}$"},"distance":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":0},"unit":{"type":"string","enum":["m"]}}}}},"group_grid":{"type":"boolean","description":"Existing Group axes action. Only object_id group.axis_grid.primary. No ungroup action exists.","enum":[true]},"all_axes_locked":{"type":"boolean","description":"Existing axis-grid checkbox: update every individual axis lock and clear the grid lock. Only object_id group.axis_grid.primary."}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## column.create

<!-- operation:column.create -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["center","level_id"],"properties":{"level_id":{"type":"string","minLength":1},"profile":{"type":"string","enum":["square","rectangle","circle"]},"width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":0,"exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"depth":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":0,"exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"diameter":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":0,"exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"base_offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}},"top_binding_mode":{"type":"string","enum":["auto","explicit","unconnected"]},"top_level_id":{"type":["string","null"],"minLength":1},"top_offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"unconnected_height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":0,"exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"pad_foundation":{"type":"object","additionalProperties":false,"required":[],"properties":{"enabled":{"type":"boolean"},"footing_length":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":0,"exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"footing_width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":0,"exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"footing_thickness":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":0,"exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"founding_depth":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":0,"exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}}},"minProperties":1},"material_id":{"type":"string","minLength":1},"name":{"type":"string","minLength":1,"maxLength":255},"center":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["level_id","top_level_id"],"local_id_pattern":"^[a-z][a-z0-9_]{0,63}$"}
```

## column.delete

<!-- operation:column.delete -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## column.update

<!-- operation:column.update -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1},"level_id":{"type":"string","minLength":1},"profile":{"type":"string","enum":["square","rectangle","circle"]},"width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":0,"exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"depth":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":0,"exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"diameter":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":0,"exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"base_offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}},"top_binding_mode":{"type":"string","enum":["auto","explicit","unconnected"]},"top_level_id":{"type":["string","null"],"minLength":1},"top_offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"unconnected_height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":0,"exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"pad_foundation":{"type":"object","additionalProperties":false,"required":[],"properties":{"enabled":{"type":"boolean"},"footing_length":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":0,"exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"footing_width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":0,"exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"footing_thickness":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":0,"exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"founding_depth":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":0,"exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}}},"minProperties":1},"material_id":{"type":"string","minLength":1},"name":{"type":"string","minLength":1,"maxLength":255}},"minProperties":2}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","level_id","top_level_id"],"local_id_pattern":null}
```

## foundation.create

<!-- operation:foundation.create -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["level_id","base_offset","baseline","foundation_type"],"properties":{"level_id":{"type":"string","minLength":1,"maxLength":255},"base_offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"baseline":{"type":"object","additionalProperties":false,"required":["start","end"],"properties":{"start":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"end":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}}},"baseline_alignment":{"type":"string","enum":["center","left","right"]},"foundation_type":{"type":"object","additionalProperties":false,"required":["kind","id"],"properties":{"kind":{"type":"string","enum":["built_in","custom"]},"id":{"type":"string","minLength":1,"maxLength":255}}}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["level_id","foundation_type.id"],"local_id_pattern":"^[a-z][a-z0-9_]{0,63}$"}
```

## foundation.delete

<!-- operation:foundation.delete -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## foundation.update

<!-- operation:foundation.update -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255},"name":{"type":"string","minLength":1,"maxLength":120},"length":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":0.08},"unit":{"type":"string","enum":["m"]}}},"level_id":{"type":"string","minLength":1,"maxLength":255},"base_offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"foundation_type":{"type":"object","additionalProperties":false,"required":["kind","id"],"properties":{"kind":{"type":"string","enum":["built_in","custom"]},"id":{"type":"string","minLength":1,"maxLength":255}}}},"minProperties":2}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","level_id","foundation_type.id"],"local_id_pattern":null}
```

## level.create

<!-- operation:level.create -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["label","elevation"],"properties":{"label":{"type":"string","minLength":1,"maxLength":255,"pattern":"^[\\s\\S]*\\S[\\s\\S]*$"},"elevation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":[],"local_id_pattern":"^[a-z][a-z0-9_]{0,63}$"}
```

## level.delete

<!-- operation:level.delete -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255,"pattern":"^[a-z][a-z0-9]*(?:[._-][a-z0-9]+)*$"}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## level.update

<!-- operation:level.update -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255,"pattern":"^[a-z][a-z0-9]*(?:[._-][a-z0-9]+)*$"},"label":{"type":"string","minLength":1,"maxLength":255,"pattern":"^[\\s\\S]*\\S[\\s\\S]*$"},"elevation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"locked":{"type":"boolean"}},"minProperties":2}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## room.create

<!-- operation:room.create -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["level_id","vertices"],"properties":{"level_id":{"type":"string","minLength":1,"maxLength":255,"pattern":"^[a-z][a-z0-9]*(?:[._-][a-z0-9]+)*$"},"vertices":{"type":"array","minItems":3,"maxItems":1000,"items":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}},"name":{"type":"string","minLength":1,"maxLength":120,"pattern":"^[\\s\\S]*\\S[\\s\\S]*$","description":"At most 120 UTF-16 code units, matching the editor and stored Room name contract."},"fill_color":{"type":"string","pattern":"^#[0-9a-fA-F]{6}$"},"snap_to_boundaries":{"type":"boolean"},"finishes":{"type":"object","additionalProperties":false,"minProperties":1,"properties":{"finish_floor":{"type":["string","null"],"enum":["laminate","solid_wood_parquet","engineered_wood","tile","tile_waterproof","carpet","vinyl_lvt","linoleum",null]},"finish_walls":{"type":["string","null"],"enum":["paint_prepared","wallpaper","tile","tile_waterproof","decorative_plaster","wood_veneer_panels","decorative_panels",null]},"finish_ceiling":{"type":["string","null"],"enum":["paint_flat","gypsum_single_level","gypsum_multilevel","mineral_grid","stretch_membrane","metal_panels","wood_panels",null]},"has_underfloor_heating":{"type":"boolean"}},"description":"Partial exact surface preset patch. Omitted choices stay unchanged, null clears one surface; heating is independent."},"attic_envelope":{"type":["object","null"],"additionalProperties":false,"required":["roof_id","profile_id","profile_mode","knee_wall_cutoff","minimum_included_headroom","average_headroom"],"description":"Complete GUI attic intent. Roof must be a valid same-Level Roof. Ordered positive metre thresholds; source-backed thresholds must match the saved profile. null disables analysis. Coverage diagnostics remain separate from authoring.","properties":{"roof_id":{"type":"string","minLength":1,"maxLength":255,"pattern":"^[a-z][a-z0-9]*(?:[._-][a-z0-9]+)*$"},"profile_id":{"type":"string","enum":["advisory_custom","pl_wt_2022_attic_room"]},"profile_mode":{"type":"string","enum":["advisory","source_backed"]},"knee_wall_cutoff":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":0},"unit":{"type":"string","enum":["m"]}}},"minimum_included_headroom":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":0},"unit":{"type":"string","enum":["m"]}}},"average_headroom":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":0},"unit":{"type":"string","enum":["m"]}}}}}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["level_id"],"local_id_pattern":"^[a-z][a-z0-9_]{0,63}$"}
```

## room.delete

<!-- operation:room.delete -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255,"pattern":"^[a-z][a-z0-9]*(?:[._-][a-z0-9]+)*$"}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## room.update

<!-- operation:room.update -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"minProperties":2,"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255,"pattern":"^[a-z][a-z0-9]*(?:[._-][a-z0-9]+)*$"},"level_id":{"type":"string","minLength":1,"maxLength":255,"pattern":"^[a-z][a-z0-9]*(?:[._-][a-z0-9]+)*$"},"vertices":{"type":"array","minItems":3,"maxItems":1000,"items":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}},"name":{"type":"string","minLength":1,"maxLength":120,"pattern":"^[\\s\\S]*\\S[\\s\\S]*$","description":"At most 120 UTF-16 code units, matching the editor and stored Room name contract."},"fill_color":{"type":"string","pattern":"^#[0-9a-fA-F]{6}$"},"snap_to_boundaries":{"type":"boolean"},"finishes":{"type":"object","additionalProperties":false,"minProperties":1,"properties":{"finish_floor":{"type":["string","null"],"enum":["laminate","solid_wood_parquet","engineered_wood","tile","tile_waterproof","carpet","vinyl_lvt","linoleum",null]},"finish_walls":{"type":["string","null"],"enum":["paint_prepared","wallpaper","tile","tile_waterproof","decorative_plaster","wood_veneer_panels","decorative_panels",null]},"finish_ceiling":{"type":["string","null"],"enum":["paint_flat","gypsum_single_level","gypsum_multilevel","mineral_grid","stretch_membrane","metal_panels","wood_panels",null]},"has_underfloor_heating":{"type":"boolean"}},"description":"Partial exact surface preset patch. Omitted choices stay unchanged, null clears one surface; heating is independent."},"attic_envelope":{"type":["object","null"],"additionalProperties":false,"required":["roof_id","profile_id","profile_mode","knee_wall_cutoff","minimum_included_headroom","average_headroom"],"description":"Complete GUI attic intent. Roof must be a valid same-Level Roof. Ordered positive metre thresholds; source-backed thresholds must match the saved profile. null disables analysis. Coverage diagnostics remain separate from authoring.","properties":{"roof_id":{"type":"string","minLength":1,"maxLength":255,"pattern":"^[a-z][a-z0-9]*(?:[._-][a-z0-9]+)*$"},"profile_id":{"type":"string","enum":["advisory_custom","pl_wt_2022_attic_room"]},"profile_mode":{"type":"string","enum":["advisory","source_backed"]},"knee_wall_cutoff":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":0},"unit":{"type":"string","enum":["m"]}}},"minimum_included_headroom":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":0},"unit":{"type":"string","enum":["m"]}}},"average_headroom":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":0},"unit":{"type":"string","enum":["m"]}}}}},"confirm_knee_walls":{"type":"boolean","description":"Invoke the existing Room knee-wall confirmation after the supplied details. Requires resolved attic analysis and creates ordinary roof-attached Walls. Repeated confirmation follows the GUI rejection.","enum":[true]}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","level_id"],"local_id_pattern":null}
```

## slab.create

<!-- operation:slab.create -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["level_id","vertices"],"properties":{"level_id":{"type":"string","minLength":1},"reference_plane":{"type":"string","enum":["top","bottom"]},"level_offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"thickness":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":0.04},"unit":{"type":"string","enum":["m"]}}},"assembly_id":{"type":"string","minLength":1},"material_id":{"type":"string","minLength":1},"name":{"type":"string","minLength":1,"maxLength":255},"vertices":{"type":"array","minItems":3,"items":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["level_id"],"local_id_pattern":"^[a-z][a-z0-9_]{0,63}$"}
```

## slab.delete

<!-- operation:slab.delete -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## slab.update

<!-- operation:slab.update -->

**Arguments schema**

```json
{"type":"object","oneOf":[{"type":"object","additionalProperties":false,"required":["object_id","action"],"properties":{"object_id":{"type":"string","minLength":1},"action":{"type":"string","enum":["settings"]},"level_id":{"type":"string","minLength":1},"reference_plane":{"type":"string","enum":["top","bottom"]},"level_offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"thickness":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":0.04},"unit":{"type":"string","enum":["m"]}}},"assembly_id":{"type":"string","minLength":1},"material_id":{"type":"string","minLength":1},"name":{"type":"string","minLength":1,"maxLength":255}},"minProperties":3},{"type":"object","additionalProperties":false,"required":["object_id","action","vertices"],"properties":{"object_id":{"type":"string","minLength":1},"action":{"type":"string","enum":["boundary"]},"vertices":{"type":"array","minItems":3,"items":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}}},"minProperties":3},{"type":"object","additionalProperties":false,"required":["object_id","action","edge_index","point"],"properties":{"object_id":{"type":"string","minLength":1},"action":{"type":"string","enum":["boundary_vertex_insert"]},"edge_index":{"type":"integer","minimum":0},"point":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}},"minProperties":3},{"type":"object","additionalProperties":false,"required":["object_id","action","vertex_index"],"properties":{"object_id":{"type":"string","minLength":1},"action":{"type":"string","enum":["boundary_vertex_remove"]},"vertex_index":{"type":"integer","minimum":0}},"minProperties":3},{"type":"object","additionalProperties":false,"required":["object_id","action","vertices"],"properties":{"object_id":{"type":"string","minLength":1},"action":{"type":"string","enum":["opening_add"]},"vertices":{"type":"array","minItems":3,"items":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}}},"minProperties":3}]}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","level_id"],"local_id_pattern":null}
```

## wall.create

<!-- operation:wall.create -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["height","baseline","level_id","base_offset","wall_type"],"properties":{"height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":0.2},"unit":{"type":"string","enum":["m"]}},"x-parameter-id":"wall.wallDrafts.WallDraftGeometry.height"},"baseline_alignment":{"type":"string","enum":["center","left","right"]},"baseline":{"type":"object","additionalProperties":false,"required":["start","end"],"properties":{"start":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"end":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}}},"level_id":{"type":"string","minLength":1,"maxLength":255,"pattern":"^[a-z][a-z0-9]*(?:[._-][a-z0-9]+)*$"},"base_offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"wall_type":{"description":"Built-in concrete wall 180 mm: {\"kind\":\"material\",\"id\":\"material.concrete.c25_fixture\"}. For a project custom type, use kind custom and an exact ID from project_get(include_document:true), document.editor.wall_types[].id. Other material/assembly references must be known catalog IDs; do not invent them.","type":"object","additionalProperties":false,"required":["kind","id"],"properties":{"kind":{"type":"string","enum":["material","assembly","custom"]},"id":{"type":"string","minLength":1,"maxLength":255,"pattern":"^[a-z][a-z0-9]*(?:[._-][a-z0-9]+)*$"}}},"top_constraint":{"type":"object","additionalProperties":false,"required":["mode"],"description":"Existing GUI top control, applied after geometry and Level edits to the joined Wall network. Next Level and fallback height are derived. Only Roof mode accepts roof_id and clearance; omitted Roof values preserve current choice or GUI defaults. roof_id:null clears the explicit choice; use unconnected to detach. Read resulting saved network after Save.","properties":{"mode":{"type":"string","enum":["unconnected","automatic_next_level","automatic_roof_underside"]},"roof_id":{"type":["string","null"],"minLength":1,"maxLength":255,"pattern":"^[a-z][a-z0-9]*(?:[._-][a-z0-9]+)*$"},"clearance":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":0},"unit":{"type":"string","enum":["m"]}}}}},"name":{"type":"string","minLength":1,"maxLength":120,"pattern":"^(?=.*\\S)[^\\r\\n\\t]+$"}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["level_id","wall_type.id"],"local_id_pattern":"^[a-z][a-z0-9_]{0,63}$"}
```

## wall.delete

<!-- operation:wall.delete -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255,"pattern":"^[a-z][a-z0-9]*(?:[._-][a-z0-9]+)*$"}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## wall.transform

<!-- operation:wall.transform -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255,"pattern":"^[a-z][a-z0-9]*(?:[._-][a-z0-9]+)*$"},"translation":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}}},"minProperties":2}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## wall.update

<!-- operation:wall.update -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255,"pattern":"^[a-z][a-z0-9]*(?:[._-][a-z0-9]+)*$"},"height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":0.2},"unit":{"type":"string","enum":["m"]}},"x-parameter-id":"wall.wallDrafts.WallDraftGeometry.height"},"baseline_alignment":{"type":"string","enum":["center","left","right"]},"baseline":{"type":"object","additionalProperties":false,"required":["start","end"],"properties":{"start":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"end":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}}},"level_id":{"type":"string","minLength":1,"maxLength":255,"pattern":"^[a-z][a-z0-9]*(?:[._-][a-z0-9]+)*$"},"base_offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"wall_type":{"description":"Built-in concrete wall 180 mm: {\"kind\":\"material\",\"id\":\"material.concrete.c25_fixture\"}. For a project custom type, use kind custom and an exact ID from project_get(include_document:true), document.editor.wall_types[].id. Other material/assembly references must be known catalog IDs; do not invent them.","type":"object","additionalProperties":false,"required":["kind","id"],"properties":{"kind":{"type":"string","enum":["material","assembly","custom"]},"id":{"type":"string","minLength":1,"maxLength":255,"pattern":"^[a-z][a-z0-9]*(?:[._-][a-z0-9]+)*$"}}},"top_constraint":{"type":"object","additionalProperties":false,"required":["mode"],"description":"Existing GUI top control, applied after geometry and Level edits to the joined Wall network. Next Level and fallback height are derived. Only Roof mode accepts roof_id and clearance; omitted Roof values preserve current choice or GUI defaults. roof_id:null clears the explicit choice; use unconnected to detach. Read resulting saved network after Save.","properties":{"mode":{"type":"string","enum":["unconnected","automatic_next_level","automatic_roof_underside"]},"roof_id":{"type":["string","null"],"minLength":1,"maxLength":255,"pattern":"^[a-z][a-z0-9]*(?:[._-][a-z0-9]+)*$"},"clearance":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":0},"unit":{"type":"string","enum":["m"]}}}}},"name":{"type":"string","minLength":1,"maxLength":120,"pattern":"^(?=.*\\S)[^\\r\\n\\t]+$"}},"minProperties":2}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","level_id","wall_type.id"],"local_id_pattern":null}
```

