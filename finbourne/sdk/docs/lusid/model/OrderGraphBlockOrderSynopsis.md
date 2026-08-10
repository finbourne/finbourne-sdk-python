# OrderGraphBlockOrderSynopsis

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **quantity** | **float** | Optional | Total number of units ordered. |
| **quantity_by_state** | **Dict[str, float]** | Optional | Total number of units placed. |
| **amount** | **float** | Optional | Total monetary value ordered, in the block currency. |
| **amount_by_state** | **Dict[str, float]** | Optional | Total monetary value ordered, broken down by order state. |
| **details** | [../model/List[OrderGraphBlockOrderDetail]](OrderGraphBlockOrderDetail.md) | Required | Identifiers and other info for each order in this block. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.OrderGraphBlockOrderSynopsis import OrderGraphBlockOrderSynopsis

instance = OrderGraphBlockOrderSynopsis(
    quantity=0.0,  # optional — Total number of units ordered.
    quantity_by_state=,  # optional — Total number of units placed.
    amount=0.0,  # optional — Total monetary value ordered, in the block currency.
    amount_by_state=,  # optional — Total monetary value ordered, broken down by order state.
    details=[]  # required — Identifiers and other info for each order in this block.
)
```

- [OrderGraphBlockOrderDetail](OrderGraphBlockOrderDetail.md) — used in `details`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

