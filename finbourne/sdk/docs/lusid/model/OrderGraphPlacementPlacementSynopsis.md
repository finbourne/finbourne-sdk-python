# OrderGraphPlacementPlacementSynopsis

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **details** | [List[OrderGraphPlacementChildPlacementDetail]](OrderGraphPlacementChildPlacementDetail.md) | Required | Identifiers for each child placement for this placement. |
| **quantity** | **float** | Required | Total number of units placed. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.OrderGraphPlacementPlacementSynopsis import OrderGraphPlacementPlacementSynopsis

instance = OrderGraphPlacementPlacementSynopsis(
    details=[],  # required — Identifiers for each child placement for this placement.
    quantity=0.0  # required — Total number of units placed.
)
```


## Related Models

- [OrderGraphPlacementChildPlacementDetail](OrderGraphPlacementChildPlacementDetail.md) — used in `details`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

