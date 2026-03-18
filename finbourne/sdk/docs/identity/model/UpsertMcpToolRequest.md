# UpsertMcpToolRequest

Request to create or update an MCP tool
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **name** | **str** | Required | The name of the MCP tool (alphanumeric, underscore, and hyphen) |
| **title** | **str** | Required | The title of the MCP tool |
| **description** | **str** | Required | The description of the MCP tool |
| **destructive** | **bool** | Optional | Whether the tool is destructive |
| **idempotent** | **bool** | Optional | Whether the tool is idempotent |
| **open_world** | **bool** | Optional | Whether the tool operates in open world |
| **read_only** | **bool** | Optional | Whether the tool is read-only |
| **parameters** | [List[McpToolParameter]](McpToolParameter.md) | Optional | The parameters for this MCP tool |
| **luminesce_payload** | [McpToolLuminescePayload](McpToolLuminescePayload.md) | Optional | *No description available.* |
| **scheduler_payload** | [McpToolSchedulerPayload](McpToolSchedulerPayload.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.identity.models.UpsertMcpToolRequest import UpsertMcpToolRequest

instance = UpsertMcpToolRequest(
    name="...",  # required — The name of the MCP tool (alphanumeric, underscore, and hyphen)
    title="...",  # required — The title of the MCP tool
    description="...",  # required — The description of the MCP tool
    destructive=True,  # optional — Whether the tool is destructive
    idempotent=True,  # optional — Whether the tool is idempotent
    open_world=True,  # optional — Whether the tool operates in open world
    read_only=True,  # optional — Whether the tool is read-only
    parameters=[],  # optional — The parameters for this MCP tool
    luminesce_payload=McpToolLuminescePayload(...),  # optional
    scheduler_payload=McpToolSchedulerPayload(...)  # optional
)
```

- [McpToolParameter](McpToolParameter.md) — used in `parameters`
- [McpToolLuminescePayload](McpToolLuminescePayload.md)
- [McpToolSchedulerPayload](McpToolSchedulerPayload.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

