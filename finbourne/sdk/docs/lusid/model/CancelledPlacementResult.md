# CancelledPlacementResult

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **placement_state** | [Placement](Placement.md) | Optional | *No description available.* |
| **cancelled_child_placements** | [List[ResourceId]](ResourceId.md) | Required | Child placements which have also been cancelled following cancellation of the parent |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CancelledPlacementResult import CancelledPlacementResult

instance = CancelledPlacementResult(
    placement_state=Placement(...),  # optional
    cancelled_child_placements=[]  # required — Child placements which have also been cancelled following cancellation of the parent
)
```


## Related Models

- [Placement](Placement.md)
- [ResourceId](ResourceId.md) — used in `cancelled_child_placements`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

