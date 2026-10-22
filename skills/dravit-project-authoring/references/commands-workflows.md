# Workflows command reference

Read [protocol](protocol.md) for the full tool envelope and revision handling. These are exact inner `arguments` schemas, not top-level tool calls. All listed operations can be submitted through `project_batch`; a dedicated native tool exists only when listed in [native tools](native-tools.md). Schemas include every writable field, unit, enum, limit, null/reset and union branch. `required` applies to its enclosing object; choose exactly one `oneOf` branch. Omission preserves an existing setting on update unless the relevant recipe states otherwise. Read current `tool_describe` if the server differs from this snapshot.

Batch reference overrides are generated from the real batch schema: only `reference_paths` additionally accept `{"local_id":"alias"}`; `[]` means array elements. A non-null `local_id_pattern` permits an entry alias, null forbids it. The [protocol compatibility table](protocol.md#batch-reference-compatibility) applies. Other fields remain unchanged.

Examples and prerequisites: [construction and roofs](structure-recipes.md), [interior, site, pipes and groups](catalog-recipes.md), [structural examples](examples-structure.json), [catalog examples](examples-catalog.json), [workflow examples](examples-workflows.json).

- [catalog.type.create](#catalogtypecreate)
- [catalog.type.update](#catalogtypeupdate)
- [object.delete](#objectdelete)
- [object.duplicate](#objectduplicate)
- [object.material.assign](#objectmaterialassign)
- [object.ungroup](#objectungroup)
- [project.batch](#projectbatch)
- [project.save](#projectsave)
- [project.settings.update](#projectsettingsupdate)

## catalog.type.create

<!-- operation:catalog.type.create -->

**Arguments schema**

```json
{"type":"object","oneOf":[{"type":"object","additionalProperties":false,"required":["family","name","description","role","thickness","currency_code","recipe_code","complete_unit_price"],"properties":{"family":{"type":"string","enum":["wall"],"description":"Only existing project-local Wall types are supported."},"name":{"type":"string","minLength":1,"maxLength":120},"description":{"type":"string","minLength":1,"maxLength":500},"role":{"type":"string","enum":["wall","partition"]},"thickness":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":0.04,"maximum":5},"unit":{"type":"string","enum":["m"]}}},"currency_code":{"type":"string","pattern":"^[A-Za-z]{3}$"},"recipe_code":{"type":"string","enum":["BrickSolid","BrickCavity","Aac","Cmu","ReinforcedCmu","CastConcreteWall","IcfWall","Drywall","TimberFrameWall","SipWall","InsulatedMetalPanelWall","PrecastSandwichWall"],"description":"Existing Wall construction code. BrickSolid/BrickCavity/Aac/Cmu/ReinforcedCmu/CastConcreteWall use m3 (volume); others use m2 (net_area). price_basis is derived and cannot be written. When changing the code, also supply a new complete_unit_price in its finished unit."},"complete_unit_price":{"type":"number","minimum":0,"exclusiveMinimum":0,"description":"One positive finished supplied-and-installed price per unit of this exact recipe, including materials, labour and logistics."}}},{"type":"object","additionalProperties":false,"required":["family","name","description","kind","wall_component","footing_component","blinding_component","complete_unit_price_per_m3","currency_code"],"properties":{"family":{"type":"string","enum":["foundation"]},"name":{"type":"string","minLength":1,"maxLength":120},"description":{"type":"string","minLength":1,"maxLength":500},"kind":{"type":"string","enum":["blinding","foundation_wall","grade_beam","strip_footing","t_section","trench_fill"]},"wall_component":{"type":["object","null"],"additionalProperties":false,"required":["width","height"],"properties":{"width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":0,"exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":0,"exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}}}},"footing_component":{"type":["object","null"],"additionalProperties":false,"required":["width","height"],"properties":{"width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":0,"exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":0,"exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}}}},"blinding_component":{"type":["object","null"],"additionalProperties":false,"required":["width","height"],"properties":{"width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":0,"exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":0,"exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}}}},"complete_unit_price_per_m3":{"type":"number","minimum":0,"description":"One complete installed Foundation price per m3 of wall, footing and blinding combined, including materials, labour and logistics. Zero is the existing GUI unpriced value."},"currency_code":{"type":"string","pattern":"^[A-Za-z]{3}$"}}},{"type":"object","additionalProperties":false,"description":"Create a project-local Door or Window preset from one existing filled built-in preset, fixed metre dimensions and its complete installed item price. The GUI assigns the stable ID. Zero price retains the existing unpriced preset behavior. Update and delete are unavailable.","required":["family","kind","base_preset_id","name","description","width","height","currency_code","complete_unit_price"],"properties":{"family":{"type":"string","enum":["opening"]},"kind":{"type":"string","enum":["door","window"]},"base_preset_id":{"type":"string","minLength":1,"enum":["opening_preset.door.interior_900x2100","opening_preset.door.interior_800x2100","opening_preset.door.entry_1000x2100","opening_preset.door.garage_2500x2125","opening_preset.window.two_column_1500x1400","opening_preset.window.single_900x1500","opening_preset.window.single_1200x1500","opening_preset.window.double_1200x1200","opening_preset.window.two_column_1800x1200","opening_preset.window.triple_1800x1400","opening_preset.window.three_column_2400x1500","opening_preset.window.landscape_1500x900","opening_preset.window.single_600x1200","opening_preset.window.full_height_single_900x2100","opening_preset.window.full_height_two_column_1800x2400","opening_preset.window.full_height_three_column_2400x2400"]},"name":{"type":"string","minLength":1,"maxLength":255},"description":{"type":"string","minLength":1,"maxLength":500},"width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":0.1,"maximum":20},"unit":{"type":"string","enum":["m"]}}},"height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":0.1,"maximum":20},"unit":{"type":"string","enum":["m"]}}},"currency_code":{"type":"string","minLength":3,"maxLength":3,"pattern":"^[A-Za-z]{3}$"},"complete_unit_price":{"type":"number","minimum":0}}}]}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":[],"local_id_pattern":"^[a-z][a-z0-9_]{0,63}$"}
```

## catalog.type.update

<!-- operation:catalog.type.update -->

**Arguments schema**

```json
{"type":"object","oneOf":[{"type":"object","additionalProperties":false,"required":["family","object_id"],"minProperties":3,"properties":{"family":{"type":"string","enum":["wall"],"description":"Only existing project-local Wall types are supported."},"object_id":{"type":"string","pattern":"^wall_type[.]project[.][a-z0-9._-]+$"},"name":{"type":"string","minLength":1,"maxLength":120},"description":{"type":"string","minLength":1,"maxLength":500},"role":{"type":"string","enum":["wall","partition"]},"thickness":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":0.04,"maximum":5},"unit":{"type":"string","enum":["m"]}}},"currency_code":{"type":"string","pattern":"^[A-Za-z]{3}$"},"recipe_code":{"type":"string","enum":["BrickSolid","BrickCavity","Aac","Cmu","ReinforcedCmu","CastConcreteWall","IcfWall","Drywall","TimberFrameWall","SipWall","InsulatedMetalPanelWall","PrecastSandwichWall"],"description":"Existing Wall construction code. BrickSolid/BrickCavity/Aac/Cmu/ReinforcedCmu/CastConcreteWall use m3 (volume); others use m2 (net_area). price_basis is derived and cannot be written. When changing the code, also supply a new complete_unit_price in its finished unit."},"complete_unit_price":{"type":"number","minimum":0,"exclusiveMinimum":0,"description":"One positive finished supplied-and-installed price per unit of this exact recipe, including materials, labour and logistics."}}},{"type":"object","additionalProperties":false,"required":["family","object_id"],"properties":{"family":{"type":"string","enum":["foundation"]},"object_id":{"type":"string","pattern":"^foundation_type\\.project\\.[1-9][0-9]*$"},"name":{"type":"string","minLength":1,"maxLength":120},"description":{"type":"string","minLength":1,"maxLength":500},"kind":{"type":"string","enum":["blinding","foundation_wall","grade_beam","strip_footing","t_section","trench_fill"]},"wall_component":{"type":["object","null"],"additionalProperties":false,"required":["width","height"],"properties":{"width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":0,"exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":0,"exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}}}},"footing_component":{"type":["object","null"],"additionalProperties":false,"required":["width","height"],"properties":{"width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":0,"exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":0,"exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}}}},"blinding_component":{"type":["object","null"],"additionalProperties":false,"required":["width","height"],"properties":{"width":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":0,"exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}},"height":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number","minimum":0,"exclusiveMinimum":0},"unit":{"type":"string","enum":["m"]}}}}},"complete_unit_price_per_m3":{"type":"number","minimum":0,"description":"One complete installed Foundation price per m3 of wall, footing and blinding combined, including materials, labour and logistics. Zero is the existing GUI unpriced value."},"currency_code":{"type":"string","pattern":"^[A-Za-z]{3}$"}},"minProperties":3}]}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## object.delete

<!-- operation:object.delete -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"description":"Existing family-specific deletion and cascades. Grouped-child locks apply. Cannot delete projects, accounts, Site, Levels, axes or arbitrary document records.","properties":{"object_id":{"type":"string","minLength":1,"maxLength":255}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## object.duplicate

<!-- operation:object.duplicate -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id","level_id"],"description":"Existing catalog Duplicate action, including Generic Group, with its standard +0.3m/-0.3m offset. Uses the explicit saved target Level and existing Room/Site placement. Structural objects outside the GUI catalog clipboard are unsupported.","properties":{"object_id":{"type":"string","minLength":1,"maxLength":255},"level_id":{"type":"string","minLength":1,"maxLength":255}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id","level_id"],"local_id_pattern":"^[a-z][a-z0-9_]{0,63}$"}
```

## object.material.assign

<!-- operation:object.material.assign -->

**Arguments schema**

```json
{"type":"object","description":"Assign an existing material or type-compatible assembly through the available GUI Material Catalog. Available for Column, Slab or a selected object with an existing missing engineering-material issue; Wall and Foundation use their type catalogs. Slab assemblies apply their preset thickness and primary material. Roof/Stair material changes also remain available through their existing family updates. Room surface finishes use room.update.finishes.","oneOf":[{"type":"object","additionalProperties":false,"required":["object_id","material_id"],"properties":{"object_id":{"type":"string","minLength":1},"material_id":{"type":"string","minLength":1,"enum":["material.concrete.c25_fixture","material.steel.s235_fixture","material.timber.c24_fixture","material.insulation.generic_fixture","material.pavement.concrete_paver_preliminary","material.pavement.asphalt_preliminary","material.pavement.concrete_kerb_preliminary"]},"assembly_id":{"type":"string","minLength":1,"enum":["assembly.wall.brick.half_120","assembly.wall.brick.one_250","assembly.wall.brick.one_half_380","assembly.wall.brick.two_510","assembly.wall.brick.cavity_520","assembly.wall.aac.partition_100","assembly.wall.aac.internal_150","assembly.wall.aac.external_300","assembly.wall.cmu.partition_150","assembly.wall.cmu.structural_200","assembly.wall.concrete.cast_in_place_200","assembly.wall.icf.above_grade_300","assembly.wall.drywall.single_stud_75","assembly.wall.drywall.double_board_125","assembly.wall.wood_frame.2x4_140","assembly.wall.wood_frame.2x6_190","assembly.wall.sip.114","assembly.wall.insulated_metal_panel_100","assembly.wall.precast_sandwich_277","assembly.slab.concrete.cast_in_place_200","assembly.slab.precast.hollow_core_200","assembly.slab.composite.steel_deck_concrete_150","assembly.slab.timber.clt_160","assembly.slab.timber.i_joist_300","assembly.floor.basic_fixture","assembly.structural.generic_fixture"]}}},{"type":"object","additionalProperties":false,"required":["object_id","assembly_id"],"properties":{"object_id":{"type":"string","minLength":1},"material_id":{"type":"string","minLength":1,"enum":["material.concrete.c25_fixture","material.steel.s235_fixture","material.timber.c24_fixture","material.insulation.generic_fixture","material.pavement.concrete_paver_preliminary","material.pavement.asphalt_preliminary","material.pavement.concrete_kerb_preliminary"]},"assembly_id":{"type":"string","minLength":1,"enum":["assembly.wall.brick.half_120","assembly.wall.brick.one_250","assembly.wall.brick.one_half_380","assembly.wall.brick.two_510","assembly.wall.brick.cavity_520","assembly.wall.aac.partition_100","assembly.wall.aac.internal_150","assembly.wall.aac.external_300","assembly.wall.cmu.partition_150","assembly.wall.cmu.structural_200","assembly.wall.concrete.cast_in_place_200","assembly.wall.icf.above_grade_300","assembly.wall.drywall.single_stud_75","assembly.wall.drywall.double_board_125","assembly.wall.wood_frame.2x4_140","assembly.wall.wood_frame.2x6_190","assembly.wall.sip.114","assembly.wall.insulated_metal_panel_100","assembly.wall.precast_sandwich_277","assembly.slab.concrete.cast_in_place_200","assembly.slab.precast.hollow_core_200","assembly.slab.composite.steel_deck_concrete_150","assembly.slab.timber.clt_160","assembly.slab.timber.i_joist_300","assembly.floor.basic_fixture","assembly.structural.generic_fixture"]}}}]}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## object.ungroup

<!-- operation:object.ungroup -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["object_id"],"properties":{"object_id":{"type":"string","minLength":1}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["object_id"],"local_id_pattern":null}
```

## project.batch

<!-- operation:project.batch -->

The batch schema below factors its repeated command union into the other supported command references. Each item has required `operation` and `arguments`, optional `local_id` on admitted creates/duplicate, and no other fields. Read [protocol](protocol.md) for local-reference positions and atomicity.

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["commands"],"properties":{"commands":{"type":"array","minItems":1,"maxItems":32,"items":{"description":"Each entry has operation, arguments and optional local_id; arguments use the corresponding supported candidate schema. Nested batches are forbidden."}}}}
```

## project.save

<!-- operation:project.save -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"description":"Confirm the current MCP document through the existing queued Save. Every mutation already saves; unchanged documents keep the same revision. No raw document input or history."}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":[],"local_id_pattern":null}
```

## project.settings.update

<!-- operation:project.settings.update -->

**Arguments schema**

```json
{"type":"object","additionalProperties":false,"required":["length_unit"],"description":"Existing display length unit only. Physical model coordinates remain in metres. Name and geographic settings are not isolated MCP workflows.","properties":{"length_unit":{"type":"string","enum":["mm","cm","m","in","ft"]}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":[],"local_id_pattern":null}
```

