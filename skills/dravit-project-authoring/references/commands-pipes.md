# Pipes command reference

Read [protocol](protocol.md) for the full tool envelope and revision handling. These are exact inner `arguments` schemas, not top-level tool calls. All listed operations can be submitted through `project_batch`; a dedicated native tool exists only when listed in [native tools](native-tools.md). Schemas include every writable field, unit, enum, limit, null/reset and union branch. `required` applies to its enclosing object; choose exactly one `oneOf` branch. Omission preserves an existing setting on update unless the relevant recipe states otherwise. Read current `tool_describe` if the server differs from this snapshot.

Batch reference overrides are generated from the real batch schema: only `reference_paths` additionally accept `{"local_id":"alias"}`; `[]` means array elements. A non-null `local_id_pattern` permits an entry alias, null forbids it. The [protocol compatibility table](protocol.md#batch-reference-compatibility) applies. Other fields remain unchanged.

Examples and prerequisites: [construction and roofs](structure-recipes.md), [interior, site, pipes and groups](catalog-recipes.md), [structural examples](examples-structure.json), [catalog examples](examples-catalog.json), [workflow examples](examples-workflows.json).

- [pipe.fitting.update](#pipefittingupdate)
- [pipe.network.delete](#pipenetworkdelete)
- [pipe.node.update](#pipenodeupdate)
- [pipe.route.create](#piperoutecreate)

## pipe.fitting.update

<!-- operation:pipe.fitting.update -->

**Arguments schema**

```json
{"type":"object","description":"Set an existing fitting roll in degrees; the shared GUI owner rotates the connected downstream branch. Exact saved IDs; no direct orientation/port writes.","additionalProperties":false,"required":["network_id","fitting_id","roll"],"properties":{"network_id":{"type":"string","minLength":1,"maxLength":255},"fitting_id":{"type":"string","minLength":1,"maxLength":255},"roll":{"type":"object","additionalProperties":false,"required":["value","unit"],"properties":{"value":{"type":"number"},"unit":{"type":"string","enum":["deg"]}}}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["network_id"],"local_id_pattern":null}
```

## pipe.network.delete

<!-- operation:pipe.network.delete -->

**Arguments schema**

```json
{"type":"object","description":"Delete the complete existing connected Pipe network. Retains equipment and semantic ownership records; releases its port and normalizes the exact remaining catalog references.","additionalProperties":false,"required":["network_id"],"properties":{"network_id":{"type":"string","minLength":1,"maxLength":255}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["network_id"],"local_id_pattern":null}
```

## pipe.node.update

<!-- operation:pipe.node.update -->

**Arguments schema**

```json
{"type":"object","description":"Move the existing free terminal node along its incident axis. Exact saved network/node IDs. Bound/internal nodes and off-axis or out-of-stock moves are rejected.","additionalProperties":false,"required":["network_id","node_id","position"],"properties":{"network_id":{"type":"string","minLength":1,"maxLength":255},"node_id":{"type":"string","minLength":1,"maxLength":255},"position":{"type":"object","additionalProperties":false,"required":["x","y","z","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"z":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["network_id"],"local_id_pattern":null}
```

## pipe.route.create

<!-- operation:pipe.route.create -->

**Arguments schema**

```json
{"type":"object","description":"Existing Pipe WP1 route from a saved profiled Water Heater cold_in. Read object.get derived.pipe_authoring_context for the exact provider and terminal centre. vertices are subsequent absolute XYZ points in metres, after that derived centre. Dravit owns catalog, IDs, fittings, ports, takeouts and Building/PlumbingSystem. Only cold_water d20 and exact 90-degree turns. No branches, existing-network joins, other systems/sizes or raw graph writes.","additionalProperties":false,"required":["provider_object_id","connector_key","level_id","vertices"],"properties":{"provider_object_id":{"type":"string","minLength":1,"maxLength":255},"connector_key":{"type":"string","enum":["cold_in"]},"level_id":{"type":"string","minLength":1,"maxLength":255},"vertices":{"type":"array","minItems":1,"maxItems":100,"items":{"type":"object","additionalProperties":false,"required":["x","y","z","unit"],"properties":{"x":{"type":"number"},"y":{"type":"number"},"z":{"type":"number"},"unit":{"type":"string","enum":["m"]}}}}}}
```

**Batch reference overrides** (generated from the actual batch schema):

```json
{"reference_paths":["provider_object_id","level_id"],"local_id_pattern":"^[a-z][a-z0-9_]{0,63}$"}
```

