# OrderGraphBlockPlacementSynopsis

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **quantity** | **float** | Required | Total number of units placed. |
| **quantity_by_state** | **Dict[str, float]** | Optional | Total number of units placed. |
| **details** | [List[OrderGraphBlockPlacementDetail]](OrderGraphBlockPlacementDetail.md) | Required | Identifiers for each placement in this block. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.OrderGraphBlockPlacementSynopsis import OrderGraphBlockPlacementSynopsis

instance = OrderGraphBlockPlacementSynopsis(
    quantity=0.0,  # required — Total number of units placed.
    quantity_by_state=,  # optional — Total number of units placed.
    details=[]  # required — Identifiers for each placement in this block.
)
```

- [OrderGraphBlockPlacementDetail](OrderGraphBlockPlacementDetail.md) — used in `details`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

