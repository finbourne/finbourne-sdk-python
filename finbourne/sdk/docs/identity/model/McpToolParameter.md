# McpToolParameter

A parameter definition for an MCP tool
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **name** | **str** | Required | The name of the parameter (identifier format) |
| **data_type** | **str** | Required | The data type of the parameter |
| **description** | **str** | Optional | A description of what the parameter is used for |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.identity.models.McpToolParameter import McpToolParameter

instance = McpToolParameter(
    name="...",  # required — The name of the parameter (identifier format)
    data_type="...",  # required — The data type of the parameter
    description="..."  # optional — A description of what the parameter is used for
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

