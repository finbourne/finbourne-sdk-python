# OrderGraphPlacementPlacementSynopsis

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **details** | [../model/List[OrderGraphPlacementChildPlacementDetail]](OrderGraphPlacementChildPlacementDetail.md) | Required | Identifiers for each child placement for this placement. |
| **quantity** | **float** | Optional | Total number of units placed. |
| **amount** | **float** | Optional | Total monetary value placed, in the block currency. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.OrderGraphPlacementPlacementSynopsis import OrderGraphPlacementPlacementSynopsis

instance = OrderGraphPlacementPlacementSynopsis(
    details=[],  # required — Identifiers for each child placement for this placement.
    quantity=0.0,  # optional — Total number of units placed.
    amount=0.0  # optional — Total monetary value placed, in the block currency.
)
```


## Related Models

- [OrderGraphPlacementChildPlacementDetail](OrderGraphPlacementChildPlacementDetail.md) — used in `details`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

