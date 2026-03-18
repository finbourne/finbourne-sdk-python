# McpToolResponse

The response representation of an MCP tool
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **scope** | **str** | Optional | The scope of the MCP tool |
| **code** | **str** | Optional | The code of the MCP tool |
| **name** | **str** | Optional | The name of the MCP tool |
| **version** | **int** | Optional | The version number of this MCP tool |
| **title** | **str** | Optional | The title of the MCP tool |
| **description** | **str** | Optional | The description of the MCP tool |
| **destructive** | **bool** | Optional | Whether the tool is destructive |
| **idempotent** | **bool** | Optional | Whether the tool is idempotent |
| **open_world** | **bool** | Optional | Whether the tool operates in open world |
| **read_only** | **bool** | Optional | Whether the tool is read-only |
| **parameters** | [List[McpToolParameter]](McpToolParameter.md) | Optional | The parameters for this MCP tool |
| **payload_type** | **str** | Optional | The type of payload (Luminesce or Scheduler) |
| **luminesce_payload** | [McpToolLuminescePayload](McpToolLuminescePayload.md) | Optional | *No description available.* |
| **scheduler_payload** | [McpToolSchedulerPayload](McpToolSchedulerPayload.md) | Optional | *No description available.* |
| **created_at** | **datetime** | Optional | When the MCP tool was created |
| **created_by** | **str** | Optional | Who created the MCP tool |
| **updated_at** | **datetime** | Optional | When the MCP tool was last updated |
| **updated_by** | **str** | Optional | Who last updated the MCP tool |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.identity.models.McpToolResponse import McpToolResponse

instance = McpToolResponse(
    scope="...",  # optional — The scope of the MCP tool
    code="...",  # optional — The code of the MCP tool
    name="...",  # optional — The name of the MCP tool
    version=0,  # optional — The version number of this MCP tool
    title="...",  # optional — The title of the MCP tool
    description="...",  # optional — The description of the MCP tool
    destructive=True,  # optional — Whether the tool is destructive
    idempotent=True,  # optional — Whether the tool is idempotent
    open_world=True,  # optional — Whether the tool operates in open world
    read_only=True,  # optional — Whether the tool is read-only
    parameters=[],  # optional — The parameters for this MCP tool
    payload_type="...",  # optional — The type of payload (Luminesce or Scheduler)
    luminesce_payload=McpToolLuminescePayload(...),  # optional
    scheduler_payload=McpToolSchedulerPayload(...),  # optional
    created_at=datetime.now(),  # optional — When the MCP tool was created
    created_by="...",  # optional — Who created the MCP tool
    updated_at=datetime.now(),  # optional — When the MCP tool was last updated
    updated_by="..."  # optional — Who last updated the MCP tool
)
```

- [McpToolParameter](McpToolParameter.md) — used in `parameters`
- [McpToolLuminescePayload](McpToolLuminescePayload.md)
- [McpToolSchedulerPayload](McpToolSchedulerPayload.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

