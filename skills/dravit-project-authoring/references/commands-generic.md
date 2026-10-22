# Generic command reference

Read [protocol](protocol.md) for the full tool envelope and revision handling. These are exact inner `arguments` schemas, not top-level tool calls. All listed operations can be submitted through `project_batch`; a dedicated native tool exists only when listed in [native tools](native-tools.md). Schemas include every writable field, unit, enum, limit, null/reset and union branch. `required` applies to its enclosing object; choose exactly one `oneOf` branch. Omission preserves an existing setting on update unless the relevant recipe states otherwise. Read current `tool_describe` if the server differs from this snapshot.

Batch reference overrides are generated from the real batch schema: only `reference_paths` additionally accept `{"local_id":"alias"}`; `[]` means array elements. A non-null `local_id_pattern` permits an entry alias, null forbids it. The [protocol compatibility table](protocol.md#batch-reference-compatibility) applies. Other fields remain unchanged.

Examples and prerequisites: [construction and roofs](structure-recipes.md), [interior, site, pipes and groups](catalog-recipes.md), [structural examples](examples-structure.json), [catalog examples](examples-catalog.json), [workflow examples](examples-workflows.json).

- [generic_group.create](#generic_groupcreate)
- [generic_group.delete](#generic_groupdelete)
- [generic_group.transform](#generic_grouptransform)
- [generic_group.update](#generic_groupupdate)
- [generic_shape.create](#generic_shapecreate)
- [generic_shape.delete](#generic_shapedelete)
- [generic_shape.transform](#generic_shapetransform)
- [generic_shape.update](#generic_shapeupdate)

## generic_group.create

<!-- operation:generic_group.create -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_ids"],"properties":{"object_ids":{"type":"array","minItems":2,"maxItems":100,"uniqueItems":true,"items":{"type":"string","minLength":1}},"name":{"type":"string","minLength":1,"maxLength":255}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_ids[]"],"local_id_pattern":"^[a-z][a-z0-9_]{0,63}$"}
```

## generic_group.delete

<!-- operation:generic_group.delete -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## generic_group.transform

<!-- operation:generic_group.transform -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1},"center":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}}},"minProperties":2}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## generic_group.update

<!-- operation:generic_group.update -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id","name"],"properties":{"object_id":{"type":"string","minLength":1},"name":{"type":"string","minLength":1,"maxLength":255}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## generic_shape.create

<!-- operation:generic_shape.create -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["shape","level_id","center"],"properties":{"shape":{"type":"string","enum":["box","cylinder","sphere","wedge"]},"center":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"level_id":{"type":"string","minLength":1},"width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":0.01,"maximum":1000},"unit":{"type":"string","enum":["m"]}}},"depth":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":0.01,"maximum":1000},"unit":{"type":"string","enum":["m"]}}},"height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":0.01,"maximum":1000},"unit":{"type":"string","enum":["m"]}}},"base_offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"cylinder_orientation":{"type":"string","enum":["upright","side"]},"color":{"type":"string","pattern":"^#[0-9a-fA-F]{6}$"},"opacity":{"type":"number","minimum":0.15,"maximum":1},"name":{"type":"string","minLength":1,"maxLength":255},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["level_id"],"local_id_pattern":"^[a-z][a-z0-9_]{0,63}$"}
```

## generic_shape.delete

<!-- operation:generic_shape.delete -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## generic_shape.transform

<!-- operation:generic_shape.transform -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1},"center":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}}},"minProperties":2}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## generic_shape.update

<!-- operation:generic_shape.update -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1},"level_id":{"type":"string","minLength":1},"width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":0.01,"maximum":1000},"unit":{"type":"string","enum":["m"]}}},"depth":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":0.01,"maximum":1000},"unit":{"type":"string","enum":["m"]}}},"height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":0.01,"maximum":1000},"unit":{"type":"string","enum":["m"]}}},"base_offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"cylinder_orientation":{"type":"string","enum":["upright","side"]},"color":{"type":"string","pattern":"^#[0-9a-fA-F]{6}$"},"opacity":{"type":"number","minimum":0.15,"maximum":1},"name":{"type":"string","minLength":1,"maxLength":255}},"minProperties":2}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","level_id"],"local_id_pattern":null}
```

