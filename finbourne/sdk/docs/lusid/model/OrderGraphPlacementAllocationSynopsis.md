# OrderGraphPlacementAllocationSynopsis

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **quantity** | **float** | Required | Total number of units allocated. |
| **amount** | **float** | Optional | Total monetary value allocated, derived from the quantity and price of each allocation, in the placement&#39;s amount currency. Null where the placement has no amount, or where an allocation cannot be expressed in that currency. |
| **details** | [List[OrderGraphPlacementAllocationDetail]](OrderGraphPlacementAllocationDetail.md) | Required | Identifiers for each allocation in this placement. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.OrderGraphPlacementAllocationSynopsis import OrderGraphPlacementAllocationSynopsis

instance = OrderGraphPlacementAllocationSynopsis(
    quantity=0.0,  # required — Total number of units allocated.
    amount=0.0,  # optional — Total monetary value allocated, derived from the quantity and price of each allocation, in the placement&#39;s amount currency. Null where the placement has no amount, or where an allocation cannot be expressed in that currency.
    details=[]  # required — Identifiers for each allocation in this placement.
)
```

- [OrderGraphPlacementAllocationDetail](OrderGraphPlacementAllocationDetail.md) — used in `details`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

