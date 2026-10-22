# Site command reference

Read [protocol](protocol.md) for the full tool envelope and revision handling. These are exact inner `arguments` schemas, not top-level tool calls. All listed operations can be submitted through `project_batch`; a dedicated native tool exists only when listed in [native tools](native-tools.md). Schemas include every writable field, unit, enum, limit, null/reset and union branch. `required` applies to its enclosing object; choose exactly one `oneOf` branch. Omission preserves an existing setting on update unless the relevant recipe states otherwise. Read current `tool_describe` if the server differs from this snapshot.

Batch reference overrides are generated from the real batch schema: only `reference_paths` additionally accept `{"local_id":"alias"}`; `[]` means array elements. A non-null `local_id_pattern` permits an entry alias, null forbids it. The [protocol compatibility table](protocol.md#batch-reference-compatibility) applies. Other fields remain unchanged.

Examples and prerequisites: [construction and roofs](structure-recipes.md), [interior, site, pipes and groups](catalog-recipes.md), [structural examples](examples-structure.json), [catalog examples](examples-catalog.json), [workflow examples](examples-workflows.json).

- [exterior_bench.create](#exterior_benchcreate)
- [exterior_bench.delete](#exterior_benchdelete)
- [exterior_bench.transform](#exterior_benchtransform)
- [exterior_bench.update](#exterior_benchupdate)
- [exterior_canopy.create](#exterior_canopycreate)
- [exterior_canopy.delete](#exterior_canopydelete)
- [exterior_canopy.transform](#exterior_canopytransform)
- [exterior_canopy.update](#exterior_canopyupdate)
- [exterior_chair.create](#exterior_chaircreate)
- [exterior_chair.delete](#exterior_chairdelete)
- [exterior_chair.transform](#exterior_chairtransform)
- [exterior_chair.update](#exterior_chairupdate)
- [exterior_sun_lounger.create](#exterior_sun_loungercreate)
- [exterior_sun_lounger.delete](#exterior_sun_loungerdelete)
- [exterior_sun_lounger.transform](#exterior_sun_loungertransform)
- [exterior_sun_lounger.update](#exterior_sun_loungerupdate)
- [exterior_table.create](#exterior_tablecreate)
- [exterior_table.delete](#exterior_tabledelete)
- [exterior_table.transform](#exterior_tabletransform)
- [exterior_table.update](#exterior_tableupdate)
- [exterior_transport.create](#exterior_transportcreate)
- [exterior_transport.delete](#exterior_transportdelete)
- [exterior_transport.transform](#exterior_transporttransform)
- [exterior_transport.update](#exterior_transportupdate)
- [exterior_umbrella.create](#exterior_umbrellacreate)
- [exterior_umbrella.delete](#exterior_umbrelladelete)
- [exterior_umbrella.transform](#exterior_umbrellatransform)
- [exterior_umbrella.update](#exterior_umbrellaupdate)
- [exterior_waste_bin.create](#exterior_waste_bincreate)
- [exterior_waste_bin.delete](#exterior_waste_bindelete)
- [exterior_waste_bin.transform](#exterior_waste_bintransform)
- [exterior_waste_bin.update](#exterior_waste_binupdate)
- [fence.create](#fencecreate)
- [fence.delete](#fencedelete)
- [fence.update](#fenceupdate)
- [fence_access.create](#fence_accesscreate)
- [fence_access.delete](#fence_accessdelete)
- [fence_access.update](#fence_accessupdate)
- [pavement.create](#pavementcreate)
- [pavement.delete](#pavementdelete)
- [pavement.update](#pavementupdate)
- [pool.create](#poolcreate)
- [pool.delete](#pooldelete)
- [pool.transform](#pooltransform)
- [pool.update](#poolupdate)
- [terrain.create](#terraincreate)
- [terrain.delete](#terraindelete)
- [terrain.transform](#terraintransform)
- [terrain.update](#terrainupdate)
- [vegetation.create](#vegetationcreate)
- [vegetation.delete](#vegetationdelete)
- [vegetation.transform](#vegetationtransform)
- [vegetation.update](#vegetationupdate)

## exterior_bench.create

<!-- operation:exterior_bench.create -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["level_id","center"],"properties":{"level_id":{"type":"string","minLength":1},"name":{"type":"string","maxLength":120},"base_offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"length":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"depth":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"overall_height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"seat_height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"center":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["level_id"],"local_id_pattern":"^[a-z][a-z0-9_]{0,63}$"}
```

## exterior_bench.delete

<!-- operation:exterior_bench.delete -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## exterior_bench.transform

<!-- operation:exterior_bench.transform -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1},"center":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## exterior_bench.update

<!-- operation:exterior_bench.update -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1},"level_id":{"type":"string","minLength":1},"name":{"type":"string","maxLength":120},"base_offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"length":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"depth":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"overall_height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"seat_height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","level_id"],"local_id_pattern":null}
```

## exterior_canopy.create

<!-- operation:exterior_canopy.create -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["level_id","center"],"properties":{"level_id":{"type":"string","minLength":1},"name":{"type":"string","maxLength":120},"base_offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"canopy_type":{"type":"string","enum":["tensioned_fabric","dense_edge_slats","sparse_rafters_with_glass"]},"length":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"overall_height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"center":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["level_id"],"local_id_pattern":"^[a-z][a-z0-9_]{0,63}$"}
```

## exterior_canopy.delete

<!-- operation:exterior_canopy.delete -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## exterior_canopy.transform

<!-- operation:exterior_canopy.transform -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1},"center":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## exterior_canopy.update

<!-- operation:exterior_canopy.update -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1},"level_id":{"type":"string","minLength":1},"name":{"type":"string","maxLength":120},"base_offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"canopy_type":{"type":"string","enum":["tensioned_fabric","dense_edge_slats","sparse_rafters_with_glass"]},"length":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"overall_height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","level_id"],"local_id_pattern":null}
```

## exterior_chair.create

<!-- operation:exterior_chair.create -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["level_id","center"],"properties":{"level_id":{"type":"string","minLength":1},"name":{"type":"string","maxLength":120},"base_offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"depth":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"overall_height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"seat_height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"center":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["level_id"],"local_id_pattern":"^[a-z][a-z0-9_]{0,63}$"}
```

## exterior_chair.delete

<!-- operation:exterior_chair.delete -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## exterior_chair.transform

<!-- operation:exterior_chair.transform -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1},"center":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## exterior_chair.update

<!-- operation:exterior_chair.update -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1},"level_id":{"type":"string","minLength":1},"name":{"type":"string","maxLength":120},"base_offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"depth":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"overall_height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"seat_height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","level_id"],"local_id_pattern":null}
```

## exterior_sun_lounger.create

<!-- operation:exterior_sun_lounger.create -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["level_id","center"],"properties":{"level_id":{"type":"string","minLength":1},"name":{"type":"string","maxLength":120},"base_offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"length":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"deck_height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"center":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["level_id"],"local_id_pattern":"^[a-z][a-z0-9_]{0,63}$"}
```

## exterior_sun_lounger.delete

<!-- operation:exterior_sun_lounger.delete -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## exterior_sun_lounger.transform

<!-- operation:exterior_sun_lounger.transform -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1},"center":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## exterior_sun_lounger.update

<!-- operation:exterior_sun_lounger.update -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1},"level_id":{"type":"string","minLength":1},"name":{"type":"string","maxLength":120},"base_offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"length":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"deck_height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","level_id"],"local_id_pattern":null}
```

## exterior_table.create

<!-- operation:exterior_table.create -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["level_id","center"],"properties":{"level_id":{"type":"string","minLength":1},"name":{"type":"string","maxLength":120},"base_offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"top_shape":{"type":"string","enum":["rectangular","round"]},"width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"depth":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"diameter":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"center":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["level_id"],"local_id_pattern":"^[a-z][a-z0-9_]{0,63}$"}
```

## exterior_table.delete

<!-- operation:exterior_table.delete -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## exterior_table.transform

<!-- operation:exterior_table.transform -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1},"center":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## exterior_table.update

<!-- operation:exterior_table.update -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1},"level_id":{"type":"string","minLength":1},"name":{"type":"string","maxLength":120},"base_offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"top_shape":{"type":"string","enum":["rectangular","round"]},"width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"depth":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"diameter":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","level_id"],"local_id_pattern":null}
```

## exterior_transport.create

<!-- operation:exterior_transport.create -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["level_id","center"],"properties":{"level_id":{"type":"string","minLength":1},"name":{"type":"string","maxLength":120},"base_offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"form_factor":{"type":"string","enum":["bicycle","compact","sedan","wagon","hatchback","coupe","minivan","sports_car","pickup","suv","offroad"]},"color":{"type":"string","enum":["white","black","silver","graphite","red","blue","green","gold"]},"center":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["level_id"],"local_id_pattern":"^[a-z][a-z0-9_]{0,63}$"}
```

## exterior_transport.delete

<!-- operation:exterior_transport.delete -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## exterior_transport.transform

<!-- operation:exterior_transport.transform -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1},"center":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## exterior_transport.update

<!-- operation:exterior_transport.update -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1},"level_id":{"type":"string","minLength":1},"name":{"type":"string","maxLength":120},"base_offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"color":{"type":"string","enum":["white","black","silver","graphite","red","blue","green","gold"]}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","level_id"],"local_id_pattern":null}
```

## exterior_umbrella.create

<!-- operation:exterior_umbrella.create -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["level_id","center"],"properties":{"level_id":{"type":"string","minLength":1},"name":{"type":"string","maxLength":120},"base_offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"canopy_diameter":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}},"description":"Nominal minimum 1.2 m after the existing GUI project display-unit rounding and near-minimum clamping. The existing Umbrella owner validates the normalized value; no independent MCP size rules."},"pole_height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}},"description":"Nominal minimum 1.5 m after the existing GUI project display-unit rounding and near-minimum clamping. The existing Umbrella owner validates the normalized value; no independent MCP size rules."},"base_enabled":{"type":"boolean"},"center":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["level_id"],"local_id_pattern":"^[a-z][a-z0-9_]{0,63}$"}
```

## exterior_umbrella.delete

<!-- operation:exterior_umbrella.delete -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## exterior_umbrella.transform

<!-- operation:exterior_umbrella.transform -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1},"center":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## exterior_umbrella.update

<!-- operation:exterior_umbrella.update -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1},"level_id":{"type":"string","minLength":1},"name":{"type":"string","maxLength":120},"base_offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"canopy_diameter":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}},"description":"Nominal minimum 1.2 m after the existing GUI project display-unit rounding and near-minimum clamping. The existing Umbrella owner validates the normalized value; no independent MCP size rules."},"pole_height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}},"description":"Nominal minimum 1.5 m after the existing GUI project display-unit rounding and near-minimum clamping. The existing Umbrella owner validates the normalized value; no independent MCP size rules."},"base_enabled":{"type":"boolean"}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","level_id"],"local_id_pattern":null}
```

## exterior_waste_bin.create

<!-- operation:exterior_waste_bin.create -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["level_id","center"],"properties":{"level_id":{"type":"string","minLength":1},"name":{"type":"string","maxLength":120},"base_offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"form":{"type":"string","enum":["square_side_loading","round_top_loading"]},"width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"depth":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"diameter":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"center":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["level_id"],"local_id_pattern":"^[a-z][a-z0-9_]{0,63}$"}
```

## exterior_waste_bin.delete

<!-- operation:exterior_waste_bin.delete -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## exterior_waste_bin.transform

<!-- operation:exterior_waste_bin.transform -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1},"center":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## exterior_waste_bin.update

<!-- operation:exterior_waste_bin.update -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1},"level_id":{"type":"string","minLength":1},"name":{"type":"string","maxLength":120},"base_offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"form":{"type":"string","enum":["square_side_loading","round_top_loading"]},"width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"depth":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"diameter":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","level_id"],"local_id_pattern":null}
```

## fence.create

<!-- operation:fence.create -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["level_id","vertices"],"properties":{"level_id":{"type":"string","minLength":1},"vertices":{"type":"array","minItems":2,"items":{"type":"object","additionalProperties":false,"required":["id","point"],"properties":{"id":{"type":"string","minLength":1},"point":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}}}},"name":{"type":"string","maxLength":120},"fence_type":{"type":"string","enum":["masonry_plinth_horizontal_slats","composite_privacy_panels"]},"height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"maximum_post_spacing":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"base_offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"closed":{"type":"boolean"}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["level_id"],"local_id_pattern":"^[a-z][a-z0-9_]{0,63}$"}
```

## fence.delete

<!-- operation:fence.delete -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## fence.update

<!-- operation:fence.update -->

**Arguments schema**

```json
{"oneOf":[{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1},"level_id":{"type":"string","minLength":1},"name":{"type":"string","maxLength":120},"fence_type":{"type":"string","enum":["masonry_plinth_horizontal_slats","composite_privacy_panels"]},"height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"maximum_post_spacing":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"base_offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"action":{"type":"string","enum":["settings"]}}},{"type":"object","additionalProperties":false,"required":["object_id","action","vertex_id","point"],"properties":{"object_id":{"type":"string","minLength":1},"action":{"type":"string","enum":["vertex_move"]},"vertex_id":{"type":"string","minLength":1},"point":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}}}],"type":"object"}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","level_id"],"local_id_pattern":null}
```

## fence_access.create

<!-- operation:fence_access.create -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["host_fence_id","host_span_id","center_ratio","access_type"],"properties":{"host_fence_id":{"type":"string","minLength":1},"host_span_id":{"type":"string","minLength":1,"description":"Existing host span ID: span:<start_vertex_id>:<end_vertex_id>, using consecutive ordered IDs from the saved Fence parameters.vertices. A closed Fence also has the last-to-first span. Read the saved Fence after vertex edits; do not use array indices."},"center_ratio":{"type":"number","minimum":0,"maximum":1},"width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"operation_clearance_visible":{"type":"boolean"},"hinge_edge":{"type":"string","enum":["start","end"]},"swing_side":{"type":"string","enum":["a","b"]},"slide_direction":{"type":"string","enum":["start","end"]},"name":{"type":"string","maxLength":120},"access_type":{"type":"string","enum":["wicket","double_swing_gate","sliding_gate"]}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["host_fence_id"],"local_id_pattern":"^[a-z][a-z0-9_]{0,63}$"}
```

## fence_access.delete

<!-- operation:fence_access.delete -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## fence_access.update

<!-- operation:fence_access.update -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1},"width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"operation_clearance_visible":{"type":"boolean"},"hinge_edge":{"type":"string","enum":["start","end"]},"swing_side":{"type":"string","enum":["a","b"]},"slide_direction":{"type":"string","enum":["start","end"]},"name":{"type":"string","maxLength":120},"center_ratio":{"type":"number","minimum":0,"maximum":1}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## pavement.create

<!-- operation:pavement.create -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["vertices"],"properties":{"level_id":{"type":"string","minLength":1},"vertices":{"type":"array","minItems":3,"items":{"type":"object","additionalProperties":false,"required":["id","point"],"properties":{"id":{"type":"string","minLength":1},"point":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}}}},"name":{"type":"string","maxLength":120},"datum":{"type":"string","enum":["absolute","level","site_zero"]},"offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"absolute_elevation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"pavement_type":{"type":"string","enum":["asphalt","paving"]},"thickness":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"assembly_id":{"type":"string","minLength":1},"material_id":{"type":"string","minLength":1},"owner_id":{"type":"string","minLength":1}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["level_id"],"local_id_pattern":"^[a-z][a-z0-9_]{0,63}$"}
```

## pavement.delete

<!-- operation:pavement.delete -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## pavement.update

<!-- operation:pavement.update -->

**Arguments schema**

```json
{"oneOf":[{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1},"level_id":{"type":"string","minLength":1},"name":{"type":"string","maxLength":120},"datum":{"type":"string","enum":["absolute","level","site_zero"]},"offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"absolute_elevation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"pavement_type":{"type":"string","enum":["asphalt","paving"]},"thickness":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"assembly_id":{"type":"string","minLength":1},"material_id":{"type":"string","minLength":1},"action":{"type":"string","enum":["settings"]}}},{"type":"object","additionalProperties":false,"required":["object_id","action","vertex_id","point"],"properties":{"object_id":{"type":"string","minLength":1},"action":{"type":"string","enum":["vertex_move"]},"vertex_id":{"type":"string","minLength":1},"point":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}}},{"type":"object","additionalProperties":false,"required":["object_id","action","vertex_id","point"],"properties":{"object_id":{"type":"string","minLength":1},"action":{"type":"string","enum":["vertex_insert"]},"vertex_id":{"type":"string","minLength":1},"point":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}}},{"type":"object","additionalProperties":false,"required":["object_id","action","vertex_id"],"properties":{"object_id":{"type":"string","minLength":1},"action":{"type":"string","enum":["vertex_remove"]},"vertex_id":{"type":"string","minLength":1}}},{"type":"object","additionalProperties":false,"required":["object_id","action","vertex_id","radius"],"properties":{"object_id":{"type":"string","minLength":1},"action":{"type":"string","enum":["corner_radius"]},"vertex_id":{"type":"string","minLength":1},"radius":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}}},{"type":"object","additionalProperties":false,"required":["object_id","action","pavement_type"],"properties":{"object_id":{"type":"string","minLength":1},"action":{"type":"string","enum":["apply_preset"]},"pavement_type":{"type":"string","enum":["asphalt","paving"]}}},{"type":"object","additionalProperties":false,"required":["object_id","action","vertex_id","enabled"],"properties":{"object_id":{"type":"string","minLength":1},"action":{"type":"string","enum":["curb_segment"]},"vertex_id":{"type":"string","minLength":1},"enabled":{"type":"boolean"}}},{"type":"object","additionalProperties":false,"required":["object_id","action"],"properties":{"object_id":{"type":"string","minLength":1},"action":{"type":"string","enum":["curb_profile"]},"material_id":{"type":"string","minLength":1},"width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"total_height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"upstand_above_pavement":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}}}],"type":"object"}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","level_id"],"local_id_pattern":null}
```

## pool.create

<!-- operation:pool.create -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["level_id","vertices"],"properties":{"level_id":{"type":"string","minLength":1},"vertices":{"type":"array","minItems":3,"items":{"type":"object","additionalProperties":false,"required":["id","point"],"properties":{"id":{"type":"string","minLength":1},"point":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}}}},"name":{"type":"string","maxLength":120},"flat_depth":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"waterline_drop":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"interior_transition_radius":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"coping_width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"deck_width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"shell_thickness":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["level_id"],"local_id_pattern":"^[a-z][a-z0-9_]{0,63}$"}
```

## pool.delete

<!-- operation:pool.delete -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## pool.transform

<!-- operation:pool.transform -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id","translation"],"properties":{"object_id":{"type":"string","minLength":1},"translation":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## pool.update

<!-- operation:pool.update -->

**Arguments schema**

```json
{"oneOf":[{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1},"level_id":{"type":"string","minLength":1},"name":{"type":"string","maxLength":120},"flat_depth":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"waterline_drop":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"interior_transition_radius":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"coping_width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"deck_width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"shell_thickness":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"action":{"type":"string","enum":["settings"]}}},{"type":"object","additionalProperties":false,"required":["object_id","action","vertex_id","point"],"properties":{"object_id":{"type":"string","minLength":1},"action":{"type":"string","enum":["vertex_move"]},"vertex_id":{"type":"string","minLength":1},"point":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}}},{"type":"object","additionalProperties":false,"required":["object_id","action","vertex_id","point"],"properties":{"object_id":{"type":"string","minLength":1},"action":{"type":"string","enum":["vertex_insert"]},"vertex_id":{"type":"string","minLength":1},"point":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}}},{"type":"object","additionalProperties":false,"required":["object_id","action","vertex_id"],"properties":{"object_id":{"type":"string","minLength":1},"action":{"type":"string","enum":["vertex_remove"]},"vertex_id":{"type":"string","minLength":1}}},{"type":"object","additionalProperties":false,"required":["object_id","action","vertex_id","radius"],"properties":{"object_id":{"type":"string","minLength":1},"action":{"type":"string","enum":["corner_radius"]},"vertex_id":{"type":"string","minLength":1},"radius":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}}},{"type":"object","additionalProperties":false,"required":["object_id","action","vertex_id","band","width"],"properties":{"object_id":{"type":"string","minLength":1},"action":{"type":"string","enum":["edge_width"]},"vertex_id":{"type":"string","minLength":1},"band":{"type":"string","enum":["coping","deck"]},"width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}}}],"type":"object"}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","level_id"],"local_id_pattern":null}
```

## terrain.create

<!-- operation:terrain.create -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["level_id","vertices"],"properties":{"level_id":{"type":"string","minLength":1},"vertices":{"type":"array","minItems":3,"items":{"type":"object","additionalProperties":false,"required":["id","point"],"properties":{"id":{"type":"string","minLength":1},"point":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}}}},"name":{"type":"string","maxLength":120},"offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["level_id"],"local_id_pattern":"^[a-z][a-z0-9_]{0,63}$"}
```

## terrain.delete

<!-- operation:terrain.delete -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## terrain.transform

<!-- operation:terrain.transform -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id","translation"],"properties":{"object_id":{"type":"string","minLength":1},"translation":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## terrain.update

<!-- operation:terrain.update -->

**Arguments schema**

```json
{"oneOf":[{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1},"level_id":{"type":"string","minLength":1},"name":{"type":"string","maxLength":120},"offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"action":{"type":"string","enum":["settings"]}}},{"type":"object","additionalProperties":false,"required":["object_id","action","vertex_id","point"],"properties":{"object_id":{"type":"string","minLength":1},"action":{"type":"string","enum":["vertex_move"]},"vertex_id":{"type":"string","minLength":1},"point":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}}},{"type":"object","additionalProperties":false,"required":["object_id","action","vertex_id","point"],"properties":{"object_id":{"type":"string","minLength":1},"action":{"type":"string","enum":["vertex_insert"]},"vertex_id":{"type":"string","minLength":1},"point":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}}},{"type":"object","additionalProperties":false,"required":["object_id","action","vertex_id"],"properties":{"object_id":{"type":"string","minLength":1},"action":{"type":"string","enum":["vertex_remove"]},"vertex_id":{"type":"string","minLength":1}}}],"type":"object"}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","level_id"],"local_id_pattern":null}
```

## vegetation.create

<!-- operation:vegetation.create -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["level_id","center"],"properties":{"level_id":{"type":"string","minLength":1},"name":{"type":"string","maxLength":120},"base_offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"form":{"type":"string","enum":["hedge","classic_tree","spruce","palm","shrub"]},"crown_diameter":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"length":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"center":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["level_id"],"local_id_pattern":"^[a-z][a-z0-9_]{0,63}$"}
```

## vegetation.delete

<!-- operation:vegetation.delete -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## vegetation.transform

<!-- operation:vegetation.transform -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1},"center":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## vegetation.update

<!-- operation:vegetation.update -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1},"level_id":{"type":"string","minLength":1},"name":{"type":"string","maxLength":120},"base_offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"crown_diameter":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"length":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","level_id"],"local_id_pattern":null}
```

