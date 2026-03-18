# TraceDiagramEdge

Represents an edge connecting two nodes within a trace diagram.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | **int** | Optional | Sequential identifier of the edge. |
| **node_id** | **str** | Optional | Identifier of the parent node. |
| **child_node_id** | **str** | Optional | Identifier of the child node. |
| **label** | **str** | Optional | Label displayed for the edge. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.insights.models.TraceDiagramEdge import TraceDiagramEdge

instance = TraceDiagramEdge(
    id=0,  # optional — Sequential identifier of the edge.
    node_id="...",  # optional — Identifier of the parent node.
    child_node_id="...",  # optional — Identifier of the child node.
    label="..."  # optional — Label displayed for the edge.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

