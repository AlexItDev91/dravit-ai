# Circulation command reference

Read [protocol](protocol.md) for the full tool envelope and revision handling. These are exact inner `arguments` schemas, not top-level tool calls. All listed operations can be submitted through `project_batch`; a dedicated native tool exists only when listed in [native tools](native-tools.md). Schemas include every writable field, unit, enum, limit, null/reset and union branch. `required` applies to its enclosing object; choose exactly one `oneOf` branch. Omission preserves an existing setting on update unless the relevant recipe states otherwise. Read current `tool_describe` if the server differs from this snapshot.

Batch reference overrides are generated from the real batch schema: only `reference_paths` additionally accept `{"local_id":"alias"}`; `[]` means array elements. A non-null `local_id_pattern` permits an entry alias, null forbids it. The [protocol compatibility table](protocol.md#batch-reference-compatibility) applies. Other fields remain unchanged.

Examples and prerequisites: [construction and roofs](structure-recipes.md), [interior, site, pipes and groups](catalog-recipes.md), [structural examples](examples-structure.json), [catalog examples](examples-catalog.json), [workflow examples](examples-workflows.json).

- [railing.create](#railingcreate)
- [railing.delete](#railingdelete)
- [railing.update](#railingupdate)
- [stair.create](#staircreate)
- [stair.delete](#stairdelete)
- [stair.transform](#stairtransform)
- [stair.update](#stairupdate)

## railing.create

<!-- operation:railing.create -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["level_id","vertices","closed"],"properties":{"level_id":{"type":"string","minLength":1},"railing_type":{"type":"string","enum":["glass_with_posts","frameless_glass","metal_vertical_balusters","timber_cross_brace"]},"height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"maximum_module_width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"base_offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"name":{"type":"string","minLength":1,"maxLength":255},"closed":{"type":"boolean"},"vertices":{"type":"array","minItems":2,"maxItems":1000,"items":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["level_id"],"local_id_pattern":"^[a-z][a-z0-9_]{0,63}$"}
```

## railing.delete

<!-- operation:railing.delete -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## railing.update

<!-- operation:railing.update -->

**Arguments schema**

```json
{"type":"object","oneOf":[{"type":"object","additionalProperties":false,"required":["object_id","action"],"properties":{"object_id":{"type":"string","minLength":1},"action":{"type":"string","enum":["settings"]},"level_id":{"type":"string","minLength":1},"railing_type":{"type":"string","enum":["glass_with_posts","frameless_glass","metal_vertical_balusters","timber_cross_brace"]},"height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"maximum_module_width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"base_offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"name":{"type":"string","minLength":1,"maxLength":255}},"minProperties":3},{"type":"object","additionalProperties":false,"required":["object_id","action","vertex_id","point"],"properties":{"object_id":{"type":"string","minLength":1},"action":{"type":"string","enum":["vertex_move"]},"vertex_id":{"type":"string","minLength":1},"point":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}}},{"type":"object","additionalProperties":false,"required":["object_id","action","vertex_id","point"],"properties":{"object_id":{"type":"string","minLength":1},"action":{"type":"string","enum":["vertex_insert"]},"vertex_id":{"type":"string","minLength":1},"point":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}}},{"type":"object","additionalProperties":false,"required":["object_id","action","vertex_id"],"properties":{"object_id":{"type":"string","minLength":1},"action":{"type":"string","enum":["vertex_remove"]},"vertex_id":{"type":"string","minLength":1}}}]}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","level_id"],"local_id_pattern":null}
```

## stair.create

<!-- operation:stair.create -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["level_id","start","direction_point"],"properties":{"level_id":{"type":"string","minLength":1},"stair_type":{"type":"string","enum":["flight","spiral"]},"base_offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"top_binding_mode":{"type":"string","enum":["auto","explicit","unconnected"]},"top_level_id":{"type":["string","null"],"minLength":1},"top_offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"unconnected_height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":0.2},"unit":{"type":"string","enum":["m"]}}},"rule_set_id":{"type":"string","enum":["ru_public_accessibility","ru_evacuation","ru_exterior_accessible","residential_ergonomic","custom"]},"preferred_riser_height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":0.05},"unit":{"type":"string","enum":["m"]}}},"tread_depth":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":0.1},"unit":{"type":"string","enum":["m"]}}},"width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":0.3},"unit":{"type":"string","enum":["m"]}}},"landing_depth":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":0.3},"unit":{"type":"string","enum":["m"]}}},"construction_type":{"type":"string","enum":["monolithic_concrete","assembled_steel"]},"material_id":{"type":"string","minLength":1},"railing_sides":{"type":"string","enum":["none","left","right","both"]},"railing_height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":0.1},"unit":{"type":"string","enum":["m"]}}},"railing_thickness":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":0.005},"unit":{"type":"string","enum":["m"]}}},"automatic_opening":{"type":"boolean"},"headroom":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":1},"unit":{"type":"string","enum":["m"]}}},"opening_clearance":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":0},"unit":{"type":"string","enum":["m"]}}},"inner_radius":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"spiral_direction":{"type":"string","enum":["clockwise","counter_clockwise"]},"central_column":{"type":"boolean"},"name":{"type":"string","minLength":1,"maxLength":255},"start":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"direction_point":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["level_id","top_level_id"],"local_id_pattern":"^[a-z][a-z0-9_]{0,63}$"}
```

## stair.delete

<!-- operation:stair.delete -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## stair.transform

<!-- operation:stair.transform -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1},"center":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}}},"minProperties":2}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## stair.update

<!-- operation:stair.update -->

**Arguments schema**

```json
{"type":"object","oneOf":[{"type":"object","additionalProperties":false,"required":["object_id","action"],"properties":{"object_id":{"type":"string","minLength":1},"action":{"type":"string","enum":["settings"]},"level_id":{"type":"string","minLength":1},"stair_type":{"type":"string","enum":["flight","spiral"]},"base_offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"top_binding_mode":{"type":"string","enum":["auto","explicit","unconnected"]},"top_level_id":{"type":["string","null"],"minLength":1},"top_offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"unconnected_height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":0.2},"unit":{"type":"string","enum":["m"]}}},"rule_set_id":{"type":"string","enum":["ru_public_accessibility","ru_evacuation","ru_exterior_accessible","residential_ergonomic","custom"]},"preferred_riser_height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":0.05},"unit":{"type":"string","enum":["m"]}}},"tread_depth":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":0.1},"unit":{"type":"string","enum":["m"]}}},"width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":0.3},"unit":{"type":"string","enum":["m"]}}},"landing_depth":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":0.3},"unit":{"type":"string","enum":["m"]}}},"construction_type":{"type":"string","enum":["monolithic_concrete","assembled_steel"]},"material_id":{"type":"string","minLength":1},"railing_sides":{"type":"string","enum":["none","left","right","both"]},"railing_height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":0.1},"unit":{"type":"string","enum":["m"]}}},"railing_thickness":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":0.005},"unit":{"type":"string","enum":["m"]}}},"automatic_opening":{"type":"boolean"},"headroom":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":1},"unit":{"type":"string","enum":["m"]}}},"opening_clearance":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":0},"unit":{"type":"string","enum":["m"]}}},"inner_radius":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"spiral_direction":{"type":"string","enum":["clockwise","counter_clockwise"]},"central_column":{"type":"boolean"},"name":{"type":"string","minLength":1,"maxLength":255}},"minProperties":3},{"type":"object","additionalProperties":false,"required":["object_id","action","after_run_index","angle","side"],"properties":{"object_id":{"type":"string","minLength":1},"action":{"type":"string","enum":["turn_add"]},"after_run_index":{"type":"integer","minimum":0},"angle":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":5},"unit":{"type":"string","enum":["deg"]}}},"side":{"type":"string","enum":["left","right"]}}},{"type":"object","additionalProperties":false,"required":["object_id","action","turn_index","angle","side"],"properties":{"object_id":{"type":"string","minLength":1},"action":{"type":"string","enum":["turn_set"]},"turn_index":{"type":"integer","minimum":0},"angle":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":5},"unit":{"type":"string","enum":["deg"]}}},"side":{"type":"string","enum":["left","right"]}}},{"type":"object","additionalProperties":false,"required":["object_id","action","turn_index"],"properties":{"object_id":{"type":"string","minLength":1},"action":{"type":"string","enum":["turn_remove"]},"turn_index":{"type":"integer","minimum":0}}},{"type":"object","additionalProperties":false,"required":["object_id","action","turn_index","incoming_riser_count"],"properties":{"object_id":{"type":"string","minLength":1},"action":{"type":"string","enum":["turn_rebalance"]},"turn_index":{"type":"integer","minimum":0},"incoming_riser_count":{"type":"integer","minimum":1}}}]}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","level_id","top_level_id"],"local_id_pattern":null}
```

