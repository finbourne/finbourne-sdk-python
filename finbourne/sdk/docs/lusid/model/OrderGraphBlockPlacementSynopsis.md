# OrderGraphBlockPlacementSynopsis

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **quantity** | **float** | Optional | Total number of units placed. |
| **quantity_by_state** | **Dict[str, float]** | Optional | Total number of units placed. |
| **amount** | **float** | Optional | Total monetary value placed, in the block currency. |
| **amount_by_state** | **Dict[str, float]** | Optional | Total monetary value placed, broken down by placement state. |
| **details** | [../model/List[OrderGraphBlockPlacementDetail]](OrderGraphBlockPlacementDetail.md) | Required | Identifiers for each placement in this block. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.OrderGraphBlockPlacementSynopsis import OrderGraphBlockPlacementSynopsis

instance = OrderGraphBlockPlacementSynopsis(
    quantity=0.0,  # optional — Total number of units placed.
    quantity_by_state=,  # optional — Total number of units placed.
    amount=0.0,  # optional — Total monetary value placed, in the block currency.
    amount_by_state=,  # optional — Total monetary value placed, broken down by placement state.
    details=[]  # required — Identifiers for each placement in this block.
)
```

- [OrderGraphBlockPlacementDetail](OrderGraphBlockPlacementDetail.md) — used in `details`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

