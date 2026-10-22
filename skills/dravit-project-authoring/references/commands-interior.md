# Interior command reference

Read [protocol](protocol.md) for the full tool envelope and revision handling. These are exact inner `arguments` schemas, not top-level tool calls. All listed operations can be submitted through `project_batch`; a dedicated native tool exists only when listed in [native tools](native-tools.md). Schemas include every writable field, unit, enum, limit, null/reset and union branch. `required` applies to its enclosing object; choose exactly one `oneOf` branch. Omission preserves an existing setting on update unless the relevant recipe states otherwise. Read current `tool_describe` if the server differs from this snapshot.

Batch reference overrides are generated from the real batch schema: only `reference_paths` additionally accept `{"local_id":"alias"}`; `[]` means array elements. A non-null `local_id_pattern` permits an entry alias, null forbids it. The [protocol compatibility table](protocol.md#batch-reference-compatibility) applies. Other fields remain unchanged.

Examples and prerequisites: [construction and roofs](structure-recipes.md), [interior, site, pipes and groups](catalog-recipes.md), [structural examples](examples-structure.json), [catalog examples](examples-catalog.json), [workflow examples](examples-workflows.json).

- [armchair.create](#armchaircreate)
- [armchair.delete](#armchairdelete)
- [armchair.transform](#armchairtransform)
- [armchair.update](#armchairupdate)
- [bathtub.create](#bathtubcreate)
- [bathtub.delete](#bathtubdelete)
- [bathtub.transform](#bathtubtransform)
- [bathtub.update](#bathtubupdate)
- [bed.create](#bedcreate)
- [bed.delete](#beddelete)
- [bed.transform](#bedtransform)
- [bed.update](#bedupdate)
- [chair.create](#chaircreate)
- [chair.delete](#chairdelete)
- [chair.transform](#chairtransform)
- [chair.update](#chairupdate)
- [drum_kit.create](#drum_kitcreate)
- [drum_kit.delete](#drum_kitdelete)
- [drum_kit.transform](#drum_kittransform)
- [drum_kit.update](#drum_kitupdate)
- [floating_shelf.create](#floating_shelfcreate)
- [floating_shelf.delete](#floating_shelfdelete)
- [floating_shelf.transform](#floating_shelftransform)
- [floating_shelf.update](#floating_shelfupdate)
- [grand_piano.create](#grand_pianocreate)
- [grand_piano.delete](#grand_pianodelete)
- [grand_piano.transform](#grand_pianotransform)
- [grand_piano.update](#grand_pianoupdate)
- [gym_accessory.create](#gym_accessorycreate)
- [gym_accessory.delete](#gym_accessorydelete)
- [gym_accessory.transform](#gym_accessorytransform)
- [gym_accessory.update](#gym_accessoryupdate)
- [gym_cardio.create](#gym_cardiocreate)
- [gym_cardio.delete](#gym_cardiodelete)
- [gym_cardio.transform](#gym_cardiotransform)
- [gym_cardio.update](#gym_cardioupdate)
- [gym_strength.create](#gym_strengthcreate)
- [gym_strength.delete](#gym_strengthdelete)
- [gym_strength.transform](#gym_strengthtransform)
- [gym_strength.update](#gym_strengthupdate)
- [gym_wall_mirror.create](#gym_wall_mirrorcreate)
- [gym_wall_mirror.delete](#gym_wall_mirrordelete)
- [gym_wall_mirror.transform](#gym_wall_mirrortransform)
- [gym_wall_mirror.update](#gym_wall_mirrorupdate)
- [kitchen_module.create](#kitchen_modulecreate)
- [kitchen_module.delete](#kitchen_moduledelete)
- [kitchen_module.transform](#kitchen_moduletransform)
- [kitchen_module.update](#kitchen_moduleupdate)
- [office_chair.create](#office_chaircreate)
- [office_chair.delete](#office_chairdelete)
- [office_chair.transform](#office_chairtransform)
- [office_chair.update](#office_chairupdate)
- [office_desk.create](#office_deskcreate)
- [office_desk.delete](#office_deskdelete)
- [office_desk.transform](#office_desktransform)
- [office_desk.update](#office_deskupdate)
- [refrigerator.create](#refrigeratorcreate)
- [refrigerator.delete](#refrigeratordelete)
- [refrigerator.transform](#refrigeratortransform)
- [refrigerator.update](#refrigeratorupdate)
- [shower_cabin.create](#shower_cabincreate)
- [shower_cabin.delete](#shower_cabindelete)
- [shower_cabin.transform](#shower_cabintransform)
- [shower_cabin.update](#shower_cabinupdate)
- [sink.create](#sinkcreate)
- [sink.delete](#sinkdelete)
- [sink.transform](#sinktransform)
- [sink.update](#sinkupdate)
- [sofa.create](#sofacreate)
- [sofa.delete](#sofadelete)
- [sofa.transform](#sofatransform)
- [sofa.update](#sofaupdate)
- [table.create](#tablecreate)
- [table.delete](#tabledelete)
- [table.transform](#tabletransform)
- [table.update](#tableupdate)
- [television.create](#televisioncreate)
- [television.delete](#televisiondelete)
- [television.transform](#televisiontransform)
- [television.update](#televisionupdate)
- [toilet.create](#toiletcreate)
- [toilet.delete](#toiletdelete)
- [toilet.transform](#toilettransform)
- [toilet.update](#toiletupdate)
- [upright_piano.create](#upright_pianocreate)
- [upright_piano.delete](#upright_pianodelete)
- [upright_piano.transform](#upright_pianotransform)
- [upright_piano.update](#upright_pianoupdate)
- [wardrobe.create](#wardrobecreate)
- [wardrobe.delete](#wardrobedelete)
- [wardrobe.transform](#wardrobetransform)
- [wardrobe.update](#wardrobeupdate)
- [washing_machine.create](#washing_machinecreate)
- [washing_machine.delete](#washing_machinedelete)
- [washing_machine.transform](#washing_machinetransform)
- [washing_machine.update](#washing_machineupdate)
- [water_heater.create](#water_heatercreate)
- [water_heater.delete](#water_heaterdelete)
- [water_heater.transform](#water_heatertransform)
- [water_heater.update](#water_heaterupdate)

## armchair.create

<!-- operation:armchair.create -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["level_id","center"],"properties":{"level_id":{"type":"string","minLength":1,"maxLength":255,"description":"Exact saved Level ID. Required on create; changing it preserves the existing relative offset and derives Room membership on the target Level."},"center":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"name":{"type":"string","minLength":1,"maxLength":120,"pattern":"^(?=[\\s\\S]*\\S)[\\s\\S]+$"},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}},"width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"depth":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}},"description":"Existing Dravit armchair create owner. Submit this operation through project_batch; inspect saved object parameters after Save."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["level_id","room_id"],"local_id_pattern":"^[a-z][a-z0-9_]{0,63}$"}
```

## armchair.delete

<!-- operation:armchair.delete -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255}},"description":"Existing Dravit armchair delete owner. Submit this operation through project_batch; inspect saved object parameters after Save."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## armchair.transform

<!-- operation:armchair.transform -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}},"center":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}},"description":"Existing Dravit armchair transform owner. Submit this operation through project_batch; inspect saved object parameters after Save."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","room_id"],"local_id_pattern":null}
```

## armchair.update

<!-- operation:armchair.update -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"name":{"type":"string","minLength":1,"maxLength":120,"pattern":"^(?=[\\s\\S]*\\S)[\\s\\S]+$"},"level_id":{"type":"string","minLength":1,"maxLength":255,"description":"Exact saved Level ID. Required on create; changing it preserves the existing relative offset and derives Room membership on the target Level."},"width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"depth":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}}},"description":"Existing Dravit armchair update owner. Submit this operation through project_batch; inspect saved object parameters after Save."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","room_id","level_id"],"local_id_pattern":null}
```

## bathtub.create

<!-- operation:bathtub.create -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["level_id","center"],"properties":{"level_id":{"type":"string","minLength":1,"maxLength":255,"description":"Exact saved Level ID. Required on create; changing it preserves the existing relative offset and derives Room membership on the target Level."},"center":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"name":{"type":"string","minLength":1,"maxLength":120,"pattern":"^(?=[\\s\\S]*\\S)[\\s\\S]+$"},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}},"length":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"level_offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"installation_type":{"type":"string","enum":["built_in","panelled"]}},"description":"Existing Dravit bathtub create owner. Submit this operation through project_batch; inspect saved object parameters after Save."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["level_id","room_id"],"local_id_pattern":"^[a-z][a-z0-9_]{0,63}$"}
```

## bathtub.delete

<!-- operation:bathtub.delete -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255}},"description":"Existing Dravit bathtub delete owner. Submit this operation through project_batch; inspect saved object parameters after Save."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## bathtub.transform

<!-- operation:bathtub.transform -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}},"center":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}},"description":"Existing Dravit bathtub transform owner. Submit this operation through project_batch; inspect saved object parameters after Save."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","room_id"],"local_id_pattern":null}
```

## bathtub.update

<!-- operation:bathtub.update -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"name":{"type":"string","minLength":1,"maxLength":120,"pattern":"^(?=[\\s\\S]*\\S)[\\s\\S]+$"},"level_id":{"type":"string","minLength":1,"maxLength":255,"description":"Exact saved Level ID. Required on create; changing it preserves the existing relative offset and derives Room membership on the target Level."},"length":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"level_offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"installation_type":{"type":"string","enum":["built_in","panelled"]},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}}},"description":"Existing Dravit bathtub update owner. Submit this operation through project_batch; inspect saved object parameters after Save."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","room_id","level_id"],"local_id_pattern":null}
```

## bed.create

<!-- operation:bed.create -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["level_id","center"],"properties":{"level_id":{"type":"string","minLength":1,"maxLength":255,"description":"Exact saved Level ID. Required on create; changing it preserves the existing relative offset and derives Room membership on the target Level."},"center":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"name":{"type":"string","minLength":1,"maxLength":120,"pattern":"^(?=[\\s\\S]*\\S)[\\s\\S]+$"},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}},"bed_variant":{"type":"string","enum":["standard","bunk"]},"size_preset":{"type":"string","enum":["child","single","small_double","double","queen","king","custom"]},"width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"depth":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"ladder_side":{"type":"string","enum":["left","right"]}},"description":"Existing Dravit bed create owner. Submit this operation through project_batch; inspect saved object parameters after Save."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["level_id","room_id"],"local_id_pattern":"^[a-z][a-z0-9_]{0,63}$"}
```

## bed.delete

<!-- operation:bed.delete -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255}},"description":"Existing Dravit bed delete owner. Submit this operation through project_batch; inspect saved object parameters after Save."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## bed.transform

<!-- operation:bed.transform -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}},"center":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}},"description":"Existing Dravit bed transform owner. Submit this operation through project_batch; inspect saved object parameters after Save."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","room_id"],"local_id_pattern":null}
```

## bed.update

<!-- operation:bed.update -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"name":{"type":"string","minLength":1,"maxLength":120,"pattern":"^(?=[\\s\\S]*\\S)[\\s\\S]+$"},"level_id":{"type":"string","minLength":1,"maxLength":255,"description":"Exact saved Level ID. Required on create; changing it preserves the existing relative offset and derives Room membership on the target Level."},"bed_variant":{"type":"string","enum":["standard","bunk"]},"size_preset":{"type":"string","enum":["child","single","small_double","double","queen","king","custom"]},"width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"depth":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"ladder_side":{"type":"string","enum":["left","right"]},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}}},"description":"Existing Dravit bed update owner. Submit this operation through project_batch; inspect saved object parameters after Save."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","room_id","level_id"],"local_id_pattern":null}
```

## chair.create

<!-- operation:chair.create -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["level_id","center"],"properties":{"level_id":{"type":"string","minLength":1,"maxLength":255,"description":"Exact saved Level ID. Required on create; changing it preserves the existing relative offset and derives Room membership on the target Level."},"center":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"name":{"type":"string","minLength":1,"maxLength":120,"pattern":"^(?=[\\s\\S]*\\S)[\\s\\S]+$"},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}},"width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"depth":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"backrest_enabled":{"type":"boolean"}},"description":"Existing Dravit chair create owner. Submit this operation through project_batch; inspect saved object parameters after Save."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["level_id","room_id"],"local_id_pattern":"^[a-z][a-z0-9_]{0,63}$"}
```

## chair.delete

<!-- operation:chair.delete -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255}},"description":"Existing Dravit chair delete owner. Submit this operation through project_batch; inspect saved object parameters after Save."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## chair.transform

<!-- operation:chair.transform -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}},"center":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}},"description":"Existing Dravit chair transform owner. Submit this operation through project_batch; inspect saved object parameters after Save."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","room_id"],"local_id_pattern":null}
```

## chair.update

<!-- operation:chair.update -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"name":{"type":"string","minLength":1,"maxLength":120,"pattern":"^(?=[\\s\\S]*\\S)[\\s\\S]+$"},"level_id":{"type":"string","minLength":1,"maxLength":255,"description":"Exact saved Level ID. Required on create; changing it preserves the existing relative offset and derives Room membership on the target Level."},"width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"depth":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"backrest_enabled":{"type":"boolean"},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}}},"description":"Existing Dravit chair update owner. Submit this operation through project_batch; inspect saved object parameters after Save."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","room_id","level_id"],"local_id_pattern":null}
```

## drum_kit.create

<!-- operation:drum_kit.create -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["level_id","center"],"properties":{"level_id":{"type":"string","minLength":1,"maxLength":255,"description":"Exact saved Level ID. Required on create; changing it preserves the existing relative offset and derives Room membership on the target Level."},"center":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"name":{"type":"string","minLength":1,"maxLength":120,"pattern":"^(?=[\\s\\S]*\\S)[\\s\\S]+$"},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}},"width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"depth":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"bass_drum_diameter":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"snare_diameter":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"rack_tom_small_diameter":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"rack_tom_large_diameter":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"floor_tom_diameter":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"base_offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}},"description":"Existing Dravit drum_kit create owner. Submit this operation through project_batch; inspect saved object parameters after Save. Instrument components remain one assembly; only the listed existing parameters are authorable."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["level_id","room_id"],"local_id_pattern":"^[a-z][a-z0-9_]{0,63}$"}
```

## drum_kit.delete

<!-- operation:drum_kit.delete -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255}},"description":"Existing Dravit drum_kit delete owner. Submit this operation through project_batch; inspect saved object parameters after Save. Instrument components remain one assembly; only the listed existing parameters are authorable."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## drum_kit.transform

<!-- operation:drum_kit.transform -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}},"center":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}},"description":"Existing Dravit drum_kit transform owner. Submit this operation through project_batch; inspect saved object parameters after Save. Instrument components remain one assembly; only the listed existing parameters are authorable."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","room_id"],"local_id_pattern":null}
```

## drum_kit.update

<!-- operation:drum_kit.update -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"name":{"type":"string","minLength":1,"maxLength":120,"pattern":"^(?=[\\s\\S]*\\S)[\\s\\S]+$"},"level_id":{"type":"string","minLength":1,"maxLength":255,"description":"Exact saved Level ID. Required on create; changing it preserves the existing relative offset and derives Room membership on the target Level."},"width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"depth":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"bass_drum_diameter":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"snare_diameter":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"rack_tom_small_diameter":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"rack_tom_large_diameter":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"floor_tom_diameter":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"base_offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}}},"description":"Existing Dravit drum_kit update owner. Submit this operation through project_batch; inspect saved object parameters after Save. Instrument components remain one assembly; only the listed existing parameters are authorable."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","room_id","level_id"],"local_id_pattern":null}
```

## floating_shelf.create

<!-- operation:floating_shelf.create -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["level_id","center"],"properties":{"level_id":{"type":"string","minLength":1,"maxLength":255,"description":"Exact saved Level ID. Required on create; changing it preserves the existing relative offset and derives Room membership on the target Level."},"center":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"name":{"type":"string","minLength":1,"maxLength":120,"pattern":"^(?=[\\s\\S]*\\S)[\\s\\S]+$"},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}},"width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"depth":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"floor_offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}},"description":"Existing Dravit floating_shelf create owner. Submit this operation through project_batch; inspect saved object parameters after Save."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["level_id","room_id"],"local_id_pattern":"^[a-z][a-z0-9_]{0,63}$"}
```

## floating_shelf.delete

<!-- operation:floating_shelf.delete -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255}},"description":"Existing Dravit floating_shelf delete owner. Submit this operation through project_batch; inspect saved object parameters after Save."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## floating_shelf.transform

<!-- operation:floating_shelf.transform -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}},"center":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}},"description":"Existing Dravit floating_shelf transform owner. Submit this operation through project_batch; inspect saved object parameters after Save."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","room_id"],"local_id_pattern":null}
```

## floating_shelf.update

<!-- operation:floating_shelf.update -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"name":{"type":"string","minLength":1,"maxLength":120,"pattern":"^(?=[\\s\\S]*\\S)[\\s\\S]+$"},"level_id":{"type":"string","minLength":1,"maxLength":255,"description":"Exact saved Level ID. Required on create; changing it preserves the existing relative offset and derives Room membership on the target Level."},"width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"depth":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"floor_offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}}},"description":"Existing Dravit floating_shelf update owner. Submit this operation through project_batch; inspect saved object parameters after Save."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","room_id","level_id"],"local_id_pattern":null}
```

## grand_piano.create

<!-- operation:grand_piano.create -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["level_id","center"],"properties":{"level_id":{"type":"string","minLength":1,"maxLength":255,"description":"Exact saved Level ID. Required on create; changing it preserves the existing relative offset and derives Room membership on the target Level."},"center":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"name":{"type":"string","minLength":1,"maxLength":120,"pattern":"^(?=[\\s\\S]*\\S)[\\s\\S]+$"},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}},"width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"depth":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"lid_state":{"type":"string","enum":["closed","open"]},"bench_enabled":{"type":"boolean"},"base_offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}},"description":"Existing Dravit grand_piano create owner. Submit this operation through project_batch; inspect saved object parameters after Save. Instrument components remain one assembly; only the listed existing parameters are authorable."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["level_id","room_id"],"local_id_pattern":"^[a-z][a-z0-9_]{0,63}$"}
```

## grand_piano.delete

<!-- operation:grand_piano.delete -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255}},"description":"Existing Dravit grand_piano delete owner. Submit this operation through project_batch; inspect saved object parameters after Save. Instrument components remain one assembly; only the listed existing parameters are authorable."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## grand_piano.transform

<!-- operation:grand_piano.transform -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}},"center":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}},"description":"Existing Dravit grand_piano transform owner. Submit this operation through project_batch; inspect saved object parameters after Save. Instrument components remain one assembly; only the listed existing parameters are authorable."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","room_id"],"local_id_pattern":null}
```

## grand_piano.update

<!-- operation:grand_piano.update -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"name":{"type":"string","minLength":1,"maxLength":120,"pattern":"^(?=[\\s\\S]*\\S)[\\s\\S]+$"},"level_id":{"type":"string","minLength":1,"maxLength":255,"description":"Exact saved Level ID. Required on create; changing it preserves the existing relative offset and derives Room membership on the target Level."},"width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"depth":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"lid_state":{"type":"string","enum":["closed","open"]},"bench_enabled":{"type":"boolean"},"base_offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}}},"description":"Existing Dravit grand_piano update owner. Submit this operation through project_batch; inspect saved object parameters after Save. Instrument components remain one assembly; only the listed existing parameters are authorable."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","room_id","level_id"],"local_id_pattern":null}
```

## gym_accessory.create

<!-- operation:gym_accessory.create -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["level_id","center","configuration"],"properties":{"level_id":{"type":"string","minLength":1,"maxLength":255,"description":"Exact saved Level ID. Required on create; changing it preserves the existing relative offset and derives Room membership on the target Level."},"center":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"name":{"type":"string","minLength":1,"maxLength":120,"pattern":"^(?=[\\s\\S]*\\S)[\\s\\S]+$"},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}},"configuration":{"type":"string","enum":["dumbbell_rack","barbell_rack","plate_tree","accessory_rack","exercise_mat"]},"base_offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}},"description":"Existing Dravit gym_accessory create owner. Submit this operation through project_batch; inspect saved object parameters after Save. Configuration selects an existing catalog item on create only. Selected equipment supports name, Level, base offset and transform; dimensions and operating zones are not editable."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["level_id","room_id"],"local_id_pattern":"^[a-z][a-z0-9_]{0,63}$"}
```

## gym_accessory.delete

<!-- operation:gym_accessory.delete -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255}},"description":"Existing Dravit gym_accessory delete owner. Submit this operation through project_batch; inspect saved object parameters after Save. Configuration selects an existing catalog item on create only. Selected equipment supports name, Level, base offset and transform; dimensions and operating zones are not editable."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## gym_accessory.transform

<!-- operation:gym_accessory.transform -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}},"center":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}},"description":"Existing Dravit gym_accessory transform owner. Submit this operation through project_batch; inspect saved object parameters after Save. Configuration selects an existing catalog item on create only. Selected equipment supports name, Level, base offset and transform; dimensions and operating zones are not editable."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","room_id"],"local_id_pattern":null}
```

## gym_accessory.update

<!-- operation:gym_accessory.update -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"name":{"type":"string","minLength":1,"maxLength":120,"pattern":"^(?=[\\s\\S]*\\S)[\\s\\S]+$"},"level_id":{"type":"string","minLength":1,"maxLength":255,"description":"Exact saved Level ID. Required on create; changing it preserves the existing relative offset and derives Room membership on the target Level."},"base_offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}}},"description":"Existing Dravit gym_accessory update owner. Submit this operation through project_batch; inspect saved object parameters after Save. Configuration selects an existing catalog item on create only. Selected equipment supports name, Level, base offset and transform; dimensions and operating zones are not editable."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","room_id","level_id"],"local_id_pattern":null}
```

## gym_cardio.create

<!-- operation:gym_cardio.create -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["level_id","center","configuration"],"properties":{"level_id":{"type":"string","minLength":1,"maxLength":255,"description":"Exact saved Level ID. Required on create; changing it preserves the existing relative offset and derives Room membership on the target Level."},"center":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"name":{"type":"string","minLength":1,"maxLength":120,"pattern":"^(?=[\\s\\S]*\\S)[\\s\\S]+$"},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}},"configuration":{"type":"string","enum":["treadmill","upright_bike","recumbent_bike","elliptical","rower","stair_climber"]},"base_offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}},"description":"Existing Dravit gym_cardio create owner. Submit this operation through project_batch; inspect saved object parameters after Save. Configuration selects an existing catalog item on create only. Selected equipment supports name, Level, base offset and transform; dimensions and operating zones are not editable."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["level_id","room_id"],"local_id_pattern":"^[a-z][a-z0-9_]{0,63}$"}
```

## gym_cardio.delete

<!-- operation:gym_cardio.delete -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255}},"description":"Existing Dravit gym_cardio delete owner. Submit this operation through project_batch; inspect saved object parameters after Save. Configuration selects an existing catalog item on create only. Selected equipment supports name, Level, base offset and transform; dimensions and operating zones are not editable."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## gym_cardio.transform

<!-- operation:gym_cardio.transform -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}},"center":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}},"description":"Existing Dravit gym_cardio transform owner. Submit this operation through project_batch; inspect saved object parameters after Save. Configuration selects an existing catalog item on create only. Selected equipment supports name, Level, base offset and transform; dimensions and operating zones are not editable."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","room_id"],"local_id_pattern":null}
```

## gym_cardio.update

<!-- operation:gym_cardio.update -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"name":{"type":"string","minLength":1,"maxLength":120,"pattern":"^(?=[\\s\\S]*\\S)[\\s\\S]+$"},"level_id":{"type":"string","minLength":1,"maxLength":255,"description":"Exact saved Level ID. Required on create; changing it preserves the existing relative offset and derives Room membership on the target Level."},"base_offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}}},"description":"Existing Dravit gym_cardio update owner. Submit this operation through project_batch; inspect saved object parameters after Save. Configuration selects an existing catalog item on create only. Selected equipment supports name, Level, base offset and transform; dimensions and operating zones are not editable."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","room_id","level_id"],"local_id_pattern":null}
```

## gym_strength.create

<!-- operation:gym_strength.create -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["level_id","center","configuration"],"properties":{"level_id":{"type":"string","minLength":1,"maxLength":255,"description":"Exact saved Level ID. Required on create; changing it preserves the existing relative offset and derives Room membership on the target Level."},"center":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"name":{"type":"string","minLength":1,"maxLength":120,"pattern":"^(?=[\\s\\S]*\\S)[\\s\\S]+$"},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}},"configuration":{"type":"string","enum":["olympic_flat_bench","combo_rack","smith_rack","multi_press","lat_pulldown_low_row","dual_adjustable_pulley","adjustable_bench","linear_leg_press"]},"base_offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}},"description":"Existing Dravit gym_strength create owner. Submit this operation through project_batch; inspect saved object parameters after Save. Configuration selects an existing catalog item on create only. Selected equipment supports name, Level, base offset and transform; dimensions and operating zones are not editable."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["level_id","room_id"],"local_id_pattern":"^[a-z][a-z0-9_]{0,63}$"}
```

## gym_strength.delete

<!-- operation:gym_strength.delete -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255}},"description":"Existing Dravit gym_strength delete owner. Submit this operation through project_batch; inspect saved object parameters after Save. Configuration selects an existing catalog item on create only. Selected equipment supports name, Level, base offset and transform; dimensions and operating zones are not editable."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## gym_strength.transform

<!-- operation:gym_strength.transform -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}},"center":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}},"description":"Existing Dravit gym_strength transform owner. Submit this operation through project_batch; inspect saved object parameters after Save. Configuration selects an existing catalog item on create only. Selected equipment supports name, Level, base offset and transform; dimensions and operating zones are not editable."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","room_id"],"local_id_pattern":null}
```

## gym_strength.update

<!-- operation:gym_strength.update -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"name":{"type":"string","minLength":1,"maxLength":120,"pattern":"^(?=[\\s\\S]*\\S)[\\s\\S]+$"},"level_id":{"type":"string","minLength":1,"maxLength":255,"description":"Exact saved Level ID. Required on create; changing it preserves the existing relative offset and derives Room membership on the target Level."},"base_offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}}},"description":"Existing Dravit gym_strength update owner. Submit this operation through project_batch; inspect saved object parameters after Save. Configuration selects an existing catalog item on create only. Selected equipment supports name, Level, base offset and transform; dimensions and operating zones are not editable."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","room_id","level_id"],"local_id_pattern":null}
```

## gym_wall_mirror.create

<!-- operation:gym_wall_mirror.create -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["level_id","center"],"properties":{"level_id":{"type":"string","minLength":1,"maxLength":255,"description":"Exact saved Level ID. Required on create; changing it preserves the existing relative offset and derives Room membership on the target Level."},"center":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"name":{"type":"string","minLength":1,"maxLength":120,"pattern":"^(?=[\\s\\S]*\\S)[\\s\\S]+$"},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}},"base_offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}},"description":"Existing Dravit gym_wall_mirror create owner. Submit this operation through project_batch; inspect saved object parameters after Save. Current product has fixed mirror geometry and independent Level/center/rotation; persistent Wall host is unsupported."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["level_id","room_id"],"local_id_pattern":"^[a-z][a-z0-9_]{0,63}$"}
```

## gym_wall_mirror.delete

<!-- operation:gym_wall_mirror.delete -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255}},"description":"Existing Dravit gym_wall_mirror delete owner. Submit this operation through project_batch; inspect saved object parameters after Save. Current product has fixed mirror geometry and independent Level/center/rotation; persistent Wall host is unsupported."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## gym_wall_mirror.transform

<!-- operation:gym_wall_mirror.transform -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}},"center":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}},"description":"Existing Dravit gym_wall_mirror transform owner. Submit this operation through project_batch; inspect saved object parameters after Save. Current product has fixed mirror geometry and independent Level/center/rotation; persistent Wall host is unsupported."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","room_id"],"local_id_pattern":null}
```

## gym_wall_mirror.update

<!-- operation:gym_wall_mirror.update -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"name":{"type":"string","minLength":1,"maxLength":120,"pattern":"^(?=[\\s\\S]*\\S)[\\s\\S]+$"},"level_id":{"type":"string","minLength":1,"maxLength":255,"description":"Exact saved Level ID. Required on create; changing it preserves the existing relative offset and derives Room membership on the target Level."},"base_offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}}},"description":"Existing Dravit gym_wall_mirror update owner. Submit this operation through project_batch; inspect saved object parameters after Save. Current product has fixed mirror geometry and independent Level/center/rotation; persistent Wall host is unsupported."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","room_id","level_id"],"local_id_pattern":null}
```

## kitchen_module.create

<!-- operation:kitchen_module.create -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["level_id","center"],"properties":{"level_id":{"type":"string","minLength":1,"maxLength":255,"description":"Exact saved Level ID. Required on create; changing it preserves the existing relative offset and derives Room membership on the target Level."},"center":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"name":{"type":"string","minLength":1,"maxLength":120,"pattern":"^(?=[\\s\\S]*\\S)[\\s\\S]+$"},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}},"composition":{"type":"string","enum":["base_only","base_wall","full_height"]},"form":{"type":"string","enum":["single","double","corner"]},"base_variant":{"type":"string","enum":["cabinet","drawers","sink","cooktop","cooktop_oven","oven","dishwasher","washing_machine"]},"wall_variant":{"type":"string","enum":["cabinet","microwave","none","hood"]},"width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"base_depth":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"base_top_height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"wall_depth":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"wall_height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"wall_bottom_offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"corner_leg_a":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"corner_leg_b":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"tall_depth":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"tall_height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"tall_variant":{"type":"string","enum":["pantry","refrigerator_housing","oven_tower","oven_microwave_tower"]},"preset":{"type":"string","enum":["cabinet","drawers","sink","hob_with_oven","oven","dishwasher","washing_machine","pantry"]}},"description":"Existing Dravit kitchen_module create owner. Submit this operation through project_batch; inspect saved object parameters after Save. Fields must apply to the final composition/form. Existing cooking variants force the hood; existing axis normalization and catalog preset activation apply."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["level_id","room_id"],"local_id_pattern":"^[a-z][a-z0-9_]{0,63}$"}
```

## kitchen_module.delete

<!-- operation:kitchen_module.delete -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255}},"description":"Existing Dravit kitchen_module delete owner. Submit this operation through project_batch; inspect saved object parameters after Save. Fields must apply to the final composition/form. Existing cooking variants force the hood; existing axis normalization and catalog preset activation apply."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## kitchen_module.transform

<!-- operation:kitchen_module.transform -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}},"center":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}},"description":"Existing Dravit kitchen_module transform owner. Submit this operation through project_batch; inspect saved object parameters after Save. Fields must apply to the final composition/form. Existing cooking variants force the hood; existing axis normalization and catalog preset activation apply."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","room_id"],"local_id_pattern":null}
```

## kitchen_module.update

<!-- operation:kitchen_module.update -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"name":{"type":"string","minLength":1,"maxLength":120,"pattern":"^(?=[\\s\\S]*\\S)[\\s\\S]+$"},"level_id":{"type":"string","minLength":1,"maxLength":255,"description":"Exact saved Level ID. Required on create; changing it preserves the existing relative offset and derives Room membership on the target Level."},"composition":{"type":"string","enum":["base_only","base_wall","full_height"]},"form":{"type":"string","enum":["single","double","corner"]},"base_variant":{"type":"string","enum":["cabinet","drawers","sink","cooktop","cooktop_oven","oven","dishwasher","washing_machine"]},"wall_variant":{"type":"string","enum":["cabinet","microwave","none","hood"]},"width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"base_depth":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"base_top_height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"wall_depth":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"wall_height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"wall_bottom_offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"corner_leg_a":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"corner_leg_b":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"tall_depth":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"tall_height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"tall_variant":{"type":"string","enum":["pantry","refrigerator_housing","oven_tower","oven_microwave_tower"]},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}}},"description":"Existing Dravit kitchen_module update owner. Submit this operation through project_batch; inspect saved object parameters after Save. Fields must apply to the final composition/form. Existing cooking variants force the hood; existing axis normalization and catalog preset activation apply."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","room_id","level_id"],"local_id_pattern":null}
```

## office_chair.create

<!-- operation:office_chair.create -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["level_id","center"],"properties":{"level_id":{"type":"string","minLength":1,"maxLength":255,"description":"Exact saved Level ID. Required on create; changing it preserves the existing relative offset and derives Room membership on the target Level."},"center":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"name":{"type":"string","minLength":1,"maxLength":120,"pattern":"^(?=[\\s\\S]*\\S)[\\s\\S]+$"},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}},"chair_style":{"type":"string","enum":["ergonomic_mesh","executive_leather_wood"]},"width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"depth":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"seat_height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"backrest_height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"armrest_height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"tilt":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}},"headrest_enabled":{"type":"boolean"},"base_offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}},"description":"Existing Dravit office_chair create owner. Submit this operation through project_batch; inspect saved object parameters after Save."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["level_id","room_id"],"local_id_pattern":"^[a-z][a-z0-9_]{0,63}$"}
```

## office_chair.delete

<!-- operation:office_chair.delete -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255}},"description":"Existing Dravit office_chair delete owner. Submit this operation through project_batch; inspect saved object parameters after Save."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## office_chair.transform

<!-- operation:office_chair.transform -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}},"center":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}},"description":"Existing Dravit office_chair transform owner. Submit this operation through project_batch; inspect saved object parameters after Save."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","room_id"],"local_id_pattern":null}
```

## office_chair.update

<!-- operation:office_chair.update -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"name":{"type":"string","minLength":1,"maxLength":120,"pattern":"^(?=[\\s\\S]*\\S)[\\s\\S]+$"},"level_id":{"type":"string","minLength":1,"maxLength":255,"description":"Exact saved Level ID. Required on create; changing it preserves the existing relative offset and derives Room membership on the target Level."},"chair_style":{"type":"string","enum":["ergonomic_mesh","executive_leather_wood"]},"width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"depth":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"seat_height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"backrest_height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"armrest_height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"tilt":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}},"headrest_enabled":{"type":"boolean"},"base_offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}}},"description":"Existing Dravit office_chair update owner. Submit this operation through project_batch; inspect saved object parameters after Save."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","room_id","level_id"],"local_id_pattern":null}
```

## office_desk.create

<!-- operation:office_desk.create -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["level_id","center"],"properties":{"level_id":{"type":"string","minLength":1,"maxLength":255,"description":"Exact saved Level ID. Required on create; changing it preserves the existing relative offset and derives Room membership on the target Level."},"center":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"name":{"type":"string","minLength":1,"maxLength":120,"pattern":"^(?=[\\s\\S]*\\S)[\\s\\S]+$"},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}},"desk_setup":{"type":"string","enum":["empty","laptop_only","keyboard_mouse_single_monitor","keyboard_mouse_dual_monitor","keyboard_mouse_monitor_laptop_stand"]},"width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"depth":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"base_offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}},"description":"Existing Dravit office_desk create owner. Submit this operation through project_batch; inspect saved object parameters after Save. Desk equipment is part of the fixed desk assembly, with exact desk_setup values; its parts cannot be edited independently."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["level_id","room_id"],"local_id_pattern":"^[a-z][a-z0-9_]{0,63}$"}
```

## office_desk.delete

<!-- operation:office_desk.delete -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255}},"description":"Existing Dravit office_desk delete owner. Submit this operation through project_batch; inspect saved object parameters after Save. Desk equipment is part of the fixed desk assembly, with exact desk_setup values; its parts cannot be edited independently."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## office_desk.transform

<!-- operation:office_desk.transform -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}},"center":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}},"description":"Existing Dravit office_desk transform owner. Submit this operation through project_batch; inspect saved object parameters after Save. Desk equipment is part of the fixed desk assembly, with exact desk_setup values; its parts cannot be edited independently."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","room_id"],"local_id_pattern":null}
```

## office_desk.update

<!-- operation:office_desk.update -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"name":{"type":"string","minLength":1,"maxLength":120,"pattern":"^(?=[\\s\\S]*\\S)[\\s\\S]+$"},"level_id":{"type":"string","minLength":1,"maxLength":255,"description":"Exact saved Level ID. Required on create; changing it preserves the existing relative offset and derives Room membership on the target Level."},"desk_setup":{"type":"string","enum":["empty","laptop_only","keyboard_mouse_single_monitor","keyboard_mouse_dual_monitor","keyboard_mouse_monitor_laptop_stand"]},"width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"depth":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"base_offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}}},"description":"Existing Dravit office_desk update owner. Submit this operation through project_batch; inspect saved object parameters after Save. Desk equipment is part of the fixed desk assembly, with exact desk_setup values; its parts cannot be edited independently."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","room_id","level_id"],"local_id_pattern":null}
```

## refrigerator.create

<!-- operation:refrigerator.create -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["level_id","center"],"properties":{"level_id":{"type":"string","minLength":1,"maxLength":255,"description":"Exact saved Level ID. Required on create; changing it preserves the existing relative offset and derives Room membership on the target Level."},"center":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"name":{"type":"string","minLength":1,"maxLength":120,"pattern":"^(?=[\\s\\S]*\\S)[\\s\\S]+$"},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}},"preset":{"type":"string","enum":["standard_bottom_freezer","side_by_side"]},"width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"depth":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}},"description":"Existing Dravit refrigerator create owner. Submit this operation through project_batch; inspect saved object parameters after Save."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["level_id","room_id"],"local_id_pattern":"^[a-z][a-z0-9_]{0,63}$"}
```

## refrigerator.delete

<!-- operation:refrigerator.delete -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255}},"description":"Existing Dravit refrigerator delete owner. Submit this operation through project_batch; inspect saved object parameters after Save."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## refrigerator.transform

<!-- operation:refrigerator.transform -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}},"center":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}},"description":"Existing Dravit refrigerator transform owner. Submit this operation through project_batch; inspect saved object parameters after Save."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","room_id"],"local_id_pattern":null}
```

## refrigerator.update

<!-- operation:refrigerator.update -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"name":{"type":"string","minLength":1,"maxLength":120,"pattern":"^(?=[\\s\\S]*\\S)[\\s\\S]+$"},"level_id":{"type":"string","minLength":1,"maxLength":255,"description":"Exact saved Level ID. Required on create; changing it preserves the existing relative offset and derives Room membership on the target Level."},"preset":{"type":"string","enum":["standard_bottom_freezer","side_by_side"]},"width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"depth":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}}},"description":"Existing Dravit refrigerator update owner. Submit this operation through project_batch; inspect saved object parameters after Save."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","room_id","level_id"],"local_id_pattern":null}
```

## shower_cabin.create

<!-- operation:shower_cabin.create -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["level_id","center"],"properties":{"level_id":{"type":"string","minLength":1,"maxLength":255,"description":"Exact saved Level ID. Required on create; changing it preserves the existing relative offset and derives Room membership on the target Level."},"center":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"name":{"type":"string","minLength":1,"maxLength":120,"pattern":"^(?=[\\s\\S]*\\S)[\\s\\S]+$"},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}},"width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"depth":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"level_offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"installation_type":{"type":"string","enum":["built_in","freestanding"]}},"description":"Existing Dravit shower_cabin create owner. Submit this operation through project_batch; inspect saved object parameters after Save."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["level_id","room_id"],"local_id_pattern":"^[a-z][a-z0-9_]{0,63}$"}
```

## shower_cabin.delete

<!-- operation:shower_cabin.delete -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255}},"description":"Existing Dravit shower_cabin delete owner. Submit this operation through project_batch; inspect saved object parameters after Save."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## shower_cabin.transform

<!-- operation:shower_cabin.transform -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}},"center":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}},"description":"Existing Dravit shower_cabin transform owner. Submit this operation through project_batch; inspect saved object parameters after Save."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","room_id"],"local_id_pattern":null}
```

## shower_cabin.update

<!-- operation:shower_cabin.update -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"name":{"type":"string","minLength":1,"maxLength":120,"pattern":"^(?=[\\s\\S]*\\S)[\\s\\S]+$"},"level_id":{"type":"string","minLength":1,"maxLength":255,"description":"Exact saved Level ID. Required on create; changing it preserves the existing relative offset and derives Room membership on the target Level."},"width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"depth":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"level_offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"installation_type":{"type":"string","enum":["built_in","freestanding"]},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}}},"description":"Existing Dravit shower_cabin update owner. Submit this operation through project_batch; inspect saved object parameters after Save."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","room_id","level_id"],"local_id_pattern":null}
```

## sink.create

<!-- operation:sink.create -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["level_id","center"],"properties":{"level_id":{"type":"string","minLength":1,"maxLength":255,"description":"Exact saved Level ID. Required on create; changing it preserves the existing relative offset and derives Room membership on the target Level."},"center":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"name":{"type":"string","minLength":1,"maxLength":120,"pattern":"^(?=[\\s\\S]*\\S)[\\s\\S]+$"},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}},"width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"depth":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"installation_height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}},"description":"Existing Dravit sink create owner. Submit this operation through project_batch; inspect saved object parameters after Save."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["level_id","room_id"],"local_id_pattern":"^[a-z][a-z0-9_]{0,63}$"}
```

## sink.delete

<!-- operation:sink.delete -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255}},"description":"Existing Dravit sink delete owner. Submit this operation through project_batch; inspect saved object parameters after Save."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## sink.transform

<!-- operation:sink.transform -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}},"center":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}},"description":"Existing Dravit sink transform owner. Submit this operation through project_batch; inspect saved object parameters after Save."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","room_id"],"local_id_pattern":null}
```

## sink.update

<!-- operation:sink.update -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"name":{"type":"string","minLength":1,"maxLength":120,"pattern":"^(?=[\\s\\S]*\\S)[\\s\\S]+$"},"level_id":{"type":"string","minLength":1,"maxLength":255,"description":"Exact saved Level ID. Required on create; changing it preserves the existing relative offset and derives Room membership on the target Level."},"width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"depth":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"installation_height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}}},"description":"Existing Dravit sink update owner. Submit this operation through project_batch; inspect saved object parameters after Save."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","room_id","level_id"],"local_id_pattern":null}
```

## sofa.create

<!-- operation:sofa.create -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["level_id","center"],"properties":{"level_id":{"type":"string","minLength":1,"maxLength":255,"description":"Exact saved Level ID. Required on create; changing it preserves the existing relative offset and derives Room membership on the target Level."},"center":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"name":{"type":"string","minLength":1,"maxLength":120,"pattern":"^(?=[\\s\\S]*\\S)[\\s\\S]+$"},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}},"preset":{"type":"string","enum":["two-seat","three-seat","corner"]},"width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"depth":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}},"description":"Existing Dravit sofa create owner. Submit this operation through project_batch; inspect saved object parameters after Save."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["level_id","room_id"],"local_id_pattern":"^[a-z][a-z0-9_]{0,63}$"}
```

## sofa.delete

<!-- operation:sofa.delete -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255}},"description":"Existing Dravit sofa delete owner. Submit this operation through project_batch; inspect saved object parameters after Save."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## sofa.transform

<!-- operation:sofa.transform -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}},"center":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}},"description":"Existing Dravit sofa transform owner. Submit this operation through project_batch; inspect saved object parameters after Save."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","room_id"],"local_id_pattern":null}
```

## sofa.update

<!-- operation:sofa.update -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"name":{"type":"string","minLength":1,"maxLength":120,"pattern":"^(?=[\\s\\S]*\\S)[\\s\\S]+$"},"level_id":{"type":"string","minLength":1,"maxLength":255,"description":"Exact saved Level ID. Required on create; changing it preserves the existing relative offset and derives Room membership on the target Level."},"preset":{"type":"string","enum":["two-seat","three-seat","corner"]},"width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"depth":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}}},"description":"Existing Dravit sofa update owner. Submit this operation through project_batch; inspect saved object parameters after Save."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","room_id","level_id"],"local_id_pattern":null}
```

## table.create

<!-- operation:table.create -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["level_id","center"],"properties":{"level_id":{"type":"string","minLength":1,"maxLength":255,"description":"Exact saved Level ID. Required on create; changing it preserves the existing relative offset and derives Room membership on the target Level."},"center":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"name":{"type":"string","minLength":1,"maxLength":120,"pattern":"^(?=[\\s\\S]*\\S)[\\s\\S]+$"},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}},"top_shape":{"type":"string","enum":["rectangular","round"]},"width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"depth":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}},"description":"Existing Dravit table create owner. Submit this operation through project_batch; inspect saved object parameters after Save. Round tables use equal width/depth and do not support authored rotation."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["level_id","room_id"],"local_id_pattern":"^[a-z][a-z0-9_]{0,63}$"}
```

## table.delete

<!-- operation:table.delete -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255}},"description":"Existing Dravit table delete owner. Submit this operation through project_batch; inspect saved object parameters after Save. Round tables use equal width/depth and do not support authored rotation."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## table.transform

<!-- operation:table.transform -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}},"center":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}},"description":"Existing Dravit table transform owner. Submit this operation through project_batch; inspect saved object parameters after Save. Round tables use equal width/depth and do not support authored rotation."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","room_id"],"local_id_pattern":null}
```

## table.update

<!-- operation:table.update -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"name":{"type":"string","minLength":1,"maxLength":120,"pattern":"^(?=[\\s\\S]*\\S)[\\s\\S]+$"},"level_id":{"type":"string","minLength":1,"maxLength":255,"description":"Exact saved Level ID. Required on create; changing it preserves the existing relative offset and derives Room membership on the target Level."},"top_shape":{"type":"string","enum":["rectangular","round"]},"width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}},"depth":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}},"description":"Existing Dravit table update owner. Submit this operation through project_batch; inspect saved object parameters after Save. Round tables use equal width/depth and do not support authored rotation."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","room_id","level_id"],"local_id_pattern":null}
```

## television.create

<!-- operation:television.create -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["level_id","center"],"properties":{"level_id":{"type":"string","minLength":1,"maxLength":255,"description":"Exact saved Level ID. Required on create; changing it preserves the existing relative offset and derives Room membership on the target Level."},"center":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"name":{"type":"string","minLength":1,"maxLength":120,"pattern":"^(?=[\\s\\S]*\\S)[\\s\\S]+$"},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}},"installation_type":{"type":"string","enum":["wall_mounted","on_cabinet"]},"diagonal_inches":{"type":"integer","enum":[43,50,55,65,75,85]},"wall_floor_offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"cabinet_width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"cabinet_depth":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"cabinet_height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}},"description":"Existing Dravit television create owner. Submit this operation through project_batch; inspect saved object parameters after Save."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["level_id","room_id"],"local_id_pattern":"^[a-z][a-z0-9_]{0,63}$"}
```

## television.delete

<!-- operation:television.delete -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255}},"description":"Existing Dravit television delete owner. Submit this operation through project_batch; inspect saved object parameters after Save."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## television.transform

<!-- operation:television.transform -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}},"center":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}},"description":"Existing Dravit television transform owner. Submit this operation through project_batch; inspect saved object parameters after Save."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","room_id"],"local_id_pattern":null}
```

## television.update

<!-- operation:television.update -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"name":{"type":"string","minLength":1,"maxLength":120,"pattern":"^(?=[\\s\\S]*\\S)[\\s\\S]+$"},"level_id":{"type":"string","minLength":1,"maxLength":255,"description":"Exact saved Level ID. Required on create; changing it preserves the existing relative offset and derives Room membership on the target Level."},"installation_type":{"type":"string","enum":["wall_mounted","on_cabinet"]},"diagonal_inches":{"type":"integer","enum":[43,50,55,65,75,85]},"wall_floor_offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"cabinet_width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"cabinet_depth":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"cabinet_height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}}},"description":"Existing Dravit television update owner. Submit this operation through project_batch; inspect saved object parameters after Save."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","room_id","level_id"],"local_id_pattern":null}
```

## toilet.create

<!-- operation:toilet.create -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["level_id","center"],"properties":{"level_id":{"type":"string","minLength":1,"maxLength":255,"description":"Exact saved Level ID. Required on create; changing it preserves the existing relative offset and derives Room membership on the target Level."},"center":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"name":{"type":"string","minLength":1,"maxLength":120,"pattern":"^(?=[\\s\\S]*\\S)[\\s\\S]+$"},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}},"length":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"installation_height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"installation_type":{"type":"string","enum":["close_coupled","wall_hung"]}},"description":"Existing Dravit toilet create owner. Submit this operation through project_batch; inspect saved object parameters after Save."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["level_id","room_id"],"local_id_pattern":"^[a-z][a-z0-9_]{0,63}$"}
```

## toilet.delete

<!-- operation:toilet.delete -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255}},"description":"Existing Dravit toilet delete owner. Submit this operation through project_batch; inspect saved object parameters after Save."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## toilet.transform

<!-- operation:toilet.transform -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}},"center":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}},"description":"Existing Dravit toilet transform owner. Submit this operation through project_batch; inspect saved object parameters after Save."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","room_id"],"local_id_pattern":null}
```

## toilet.update

<!-- operation:toilet.update -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"name":{"type":"string","minLength":1,"maxLength":120,"pattern":"^(?=[\\s\\S]*\\S)[\\s\\S]+$"},"level_id":{"type":"string","minLength":1,"maxLength":255,"description":"Exact saved Level ID. Required on create; changing it preserves the existing relative offset and derives Room membership on the target Level."},"length":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"installation_height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"installation_type":{"type":"string","enum":["close_coupled","wall_hung"]},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}}},"description":"Existing Dravit toilet update owner. Submit this operation through project_batch; inspect saved object parameters after Save."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","room_id","level_id"],"local_id_pattern":null}
```

## upright_piano.create

<!-- operation:upright_piano.create -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["level_id","center"],"properties":{"level_id":{"type":"string","minLength":1,"maxLength":255,"description":"Exact saved Level ID. Required on create; changing it preserves the existing relative offset and derives Room membership on the target Level."},"center":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"name":{"type":"string","minLength":1,"maxLength":120,"pattern":"^(?=[\\s\\S]*\\S)[\\s\\S]+$"},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}},"width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"depth":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"bench_enabled":{"type":"boolean"},"base_offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}},"description":"Existing Dravit upright_piano create owner. Submit this operation through project_batch; inspect saved object parameters after Save. Instrument components remain one assembly; only the listed existing parameters are authorable."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["level_id","room_id"],"local_id_pattern":"^[a-z][a-z0-9_]{0,63}$"}
```

## upright_piano.delete

<!-- operation:upright_piano.delete -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255}},"description":"Existing Dravit upright_piano delete owner. Submit this operation through project_batch; inspect saved object parameters after Save. Instrument components remain one assembly; only the listed existing parameters are authorable."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## upright_piano.transform

<!-- operation:upright_piano.transform -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}},"center":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}},"description":"Existing Dravit upright_piano transform owner. Submit this operation through project_batch; inspect saved object parameters after Save. Instrument components remain one assembly; only the listed existing parameters are authorable."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","room_id"],"local_id_pattern":null}
```

## upright_piano.update

<!-- operation:upright_piano.update -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"name":{"type":"string","minLength":1,"maxLength":120,"pattern":"^(?=[\\s\\S]*\\S)[\\s\\S]+$"},"level_id":{"type":"string","minLength":1,"maxLength":255,"description":"Exact saved Level ID. Required on create; changing it preserves the existing relative offset and derives Room membership on the target Level."},"width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"depth":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"bench_enabled":{"type":"boolean"},"base_offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}}},"description":"Existing Dravit upright_piano update owner. Submit this operation through project_batch; inspect saved object parameters after Save. Instrument components remain one assembly; only the listed existing parameters are authorable."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","room_id","level_id"],"local_id_pattern":null}
```

## wardrobe.create

<!-- operation:wardrobe.create -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["level_id","center"],"properties":{"level_id":{"type":"string","minLength":1,"maxLength":255,"description":"Exact saved Level ID. Required on create; changing it preserves the existing relative offset and derives Room membership on the target Level."},"center":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"name":{"type":"string","minLength":1,"maxLength":120,"pattern":"^(?=[\\s\\S]*\\S)[\\s\\S]+$"},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}},"width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"depth":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"section_count":{"type":"integer","minimum":1,"maximum":12},"doors_enabled":{"type":"boolean"},"catalog_preset":{"type":"string","enum":["wardrobe","open_shelving"]}},"description":"Existing Dravit wardrobe create owner. Submit this operation through project_batch; inspect saved object parameters after Save."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["level_id","room_id"],"local_id_pattern":"^[a-z][a-z0-9_]{0,63}$"}
```

## wardrobe.delete

<!-- operation:wardrobe.delete -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255}},"description":"Existing Dravit wardrobe delete owner. Submit this operation through project_batch; inspect saved object parameters after Save."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## wardrobe.transform

<!-- operation:wardrobe.transform -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}},"center":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}},"description":"Existing Dravit wardrobe transform owner. Submit this operation through project_batch; inspect saved object parameters after Save."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","room_id"],"local_id_pattern":null}
```

## wardrobe.update

<!-- operation:wardrobe.update -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"name":{"type":"string","minLength":1,"maxLength":120,"pattern":"^(?=[\\s\\S]*\\S)[\\s\\S]+$"},"level_id":{"type":"string","minLength":1,"maxLength":255,"description":"Exact saved Level ID. Required on create; changing it preserves the existing relative offset and derives Room membership on the target Level."},"width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"depth":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"section_count":{"type":"integer","minimum":1,"maximum":12},"doors_enabled":{"type":"boolean"},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}}},"description":"Existing Dravit wardrobe update owner. Submit this operation through project_batch; inspect saved object parameters after Save."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","room_id","level_id"],"local_id_pattern":null}
```

## washing_machine.create

<!-- operation:washing_machine.create -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["level_id","center"],"properties":{"level_id":{"type":"string","minLength":1,"maxLength":255,"description":"Exact saved Level ID. Required on create; changing it preserves the existing relative offset and derives Room membership on the target Level."},"center":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"name":{"type":"string","minLength":1,"maxLength":120,"pattern":"^(?=[\\s\\S]*\\S)[\\s\\S]+$"},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}},"loading_type":{"type":"string","enum":["front","top"]},"width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"depth":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"floor_offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}},"description":"Existing Dravit washing_machine create owner. Submit this operation through project_batch; inspect saved object parameters after Save."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["level_id","room_id"],"local_id_pattern":"^[a-z][a-z0-9_]{0,63}$"}
```

## washing_machine.delete

<!-- operation:washing_machine.delete -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255}},"description":"Existing Dravit washing_machine delete owner. Submit this operation through project_batch; inspect saved object parameters after Save."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## washing_machine.transform

<!-- operation:washing_machine.transform -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}},"center":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}},"description":"Existing Dravit washing_machine transform owner. Submit this operation through project_batch; inspect saved object parameters after Save."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","room_id"],"local_id_pattern":null}
```

## washing_machine.update

<!-- operation:washing_machine.update -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"name":{"type":"string","minLength":1,"maxLength":120,"pattern":"^(?=[\\s\\S]*\\S)[\\s\\S]+$"},"level_id":{"type":"string","minLength":1,"maxLength":255,"description":"Exact saved Level ID. Required on create; changing it preserves the existing relative offset and derives Room membership on the target Level."},"loading_type":{"type":"string","enum":["front","top"]},"width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"depth":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"floor_offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}}},"description":"Existing Dravit washing_machine update owner. Submit this operation through project_batch; inspect saved object parameters after Save."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","room_id","level_id"],"local_id_pattern":null}
```

## water_heater.create

<!-- operation:water_heater.create -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["level_id","center"],"properties":{"level_id":{"type":"string","minLength":1,"maxLength":255,"description":"Exact saved Level ID. Required on create; changing it preserves the existing relative offset and derives Room membership on the target Level."},"center":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"name":{"type":"string","minLength":1,"maxLength":120,"pattern":"^(?=[\\s\\S]*\\S)[\\s\\S]+$"},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}},"width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"depth":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"floor_offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"connector_profile":{"type":["object","null"],"additionalProperties":false,"required":["catalog_version","profile_id"],"properties":{"catalog_version":{"type":"string","minLength":1,"maxLength":255},"profile_id":{"type":"string","minLength":1,"maxLength":255}},"description":"Omit to preserve, null to clear an unbound profile. Current immutable catalog_version: neutral_pipe.wp1.2026-07-19.v1; profile_id: object_connector.water_heater.g1_2_flat.v1. Existing saved pinned versions remain explicit. Connected Pipe providers must be disconnected before identity/geometry changes."}},"description":"Existing Dravit water_heater create owner. Submit this operation through project_batch; inspect saved object parameters after Save."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["level_id","room_id"],"local_id_pattern":"^[a-z][a-z0-9_]{0,63}$"}
```

## water_heater.delete

<!-- operation:water_heater.delete -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255}},"description":"Existing Dravit water_heater delete owner. Submit this operation through project_batch; inspect saved object parameters after Save."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## water_heater.transform

<!-- operation:water_heater.transform -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}},"center":{"type":"object","additionalProperties":false,"required":["x","y","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}},"description":"Existing Dravit water_heater transform owner. Submit this operation through project_batch; inspect saved object parameters after Save."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","room_id"],"local_id_pattern":null}
```

## water_heater.update

<!-- operation:water_heater.update -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1,"maxLength":255},"room_id":{"type":"string","minLength":1,"maxLength":255,"description":"Optional exact saved Room context assertion on this Level. Membership is derived by the existing center-containment owner; this field never overrides it."},"name":{"type":"string","minLength":1,"maxLength":120,"pattern":"^(?=[\\s\\S]*\\S)[\\s\\S]+$"},"level_id":{"type":"string","minLength":1,"maxLength":255,"description":"Exact saved Level ID. Required on create; changing it preserves the existing relative offset and derives Room membership on the target Level."},"width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"depth":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"floor_offset":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["m"]}}},"connector_profile":{"type":["object","null"],"additionalProperties":false,"required":["catalog_version","profile_id"],"properties":{"catalog_version":{"type":"string","minLength":1,"maxLength":255},"profile_id":{"type":"string","minLength":1,"maxLength":255}},"description":"Omit to preserve, null to clear an unbound profile. Current immutable catalog_version: neutral_pipe.wp1.2026-07-19.v1; profile_id: object_connector.water_heater.g1_2_flat.v1. Existing saved pinned versions remain explicit. Connected Pipe providers must be disconnected before identity/geometry changes."},"rotation":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}}},"description":"Existing Dravit water_heater update owner. Submit this operation through project_batch; inspect saved object parameters after Save."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","room_id","level_id"],"local_id_pattern":null}
```

