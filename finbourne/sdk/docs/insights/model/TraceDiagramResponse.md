# TraceDiagramResponse

Represents a trace diagram composed of nodes and edges.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **nodes** | [List[TraceDiagramNode]](TraceDiagramNode.md) | Optional | The nodes that make up the diagram. |
| **edges** | [List[TraceDiagramEdge]](TraceDiagramEdge.md) | Optional | The edges that connect the nodes in the diagram. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.insights.models.TraceDiagramResponse import TraceDiagramResponse

instance = TraceDiagramResponse(
    nodes=[],  # optional — The nodes that make up the diagram.
    edges=[]  # optional — The edges that connect the nodes in the diagram.
)
```


## Related Models

- [TraceDiagramNode](TraceDiagramNode.md) — used in `nodes`
- [TraceDiagramEdge](TraceDiagramEdge.md) — used in `edges`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

