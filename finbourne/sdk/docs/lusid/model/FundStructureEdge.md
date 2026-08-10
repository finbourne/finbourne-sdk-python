# FundStructureEdge

A directed edge in a Fund Structure, defining a relationship from a feeder node to a master node share class.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **var_from** | **str** | Required | The node code of the feeder node that is the source of this relationship. |
| **to** | [../model/FundStructureEdgeTarget](FundStructureEdgeTarget.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FundStructureEdge import FundStructureEdge

instance = FundStructureEdge(
    var_from="...",  # required — The node code of the feeder node that is the source of this relationship.
    to=FundStructureEdgeTarget(...)  # required
)
```

- [FundStructureEdgeTarget](FundStructureEdgeTarget.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

