# TraceDiagramNode

Represents a node within a trace diagram.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | **str** | Optional | Unique identifier of the node. |
| **display_name** | **str** | Optional | Display name of the node. |
| **level** | **int** | Optional | Depth level of the node within the diagram. |
| **parent** | **str** | Optional | Identifier of the node&#39;s parent. This is null for the root node. |
| **type** | **str** | Optional | Type classification of the node. |
| **agent_scope** | **str** | Optional | The scope of the agent. |
| **agent_version** | **int** | Optional | The version of the agent. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.insights.models.TraceDiagramNode import TraceDiagramNode

instance = TraceDiagramNode(
    id="...",  # optional — Unique identifier of the node.
    display_name="...",  # optional — Display name of the node.
    level=0,  # optional — Depth level of the node within the diagram.
    parent="...",  # optional — Identifier of the node&#39;s parent. This is null for the root node.
    type="...",  # optional — Type classification of the node.
    agent_scope="...",  # optional — The scope of the agent.
    agent_version=0  # optional — The version of the agent.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

