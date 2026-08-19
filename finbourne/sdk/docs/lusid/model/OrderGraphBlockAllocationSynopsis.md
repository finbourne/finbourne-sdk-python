# OrderGraphBlockAllocationSynopsis

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **quantity** | **float** | Required | Total number of units allocated. |
| **amount** | **float** | Optional | Total monetary value allocated, derived from the quantity and price of each allocation. |
| **details** | [List[OrderGraphBlockAllocationDetail]](OrderGraphBlockAllocationDetail.md) | Required | Identifiers for each allocation in this block. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.OrderGraphBlockAllocationSynopsis import OrderGraphBlockAllocationSynopsis

instance = OrderGraphBlockAllocationSynopsis(
    quantity=0.0,  # required — Total number of units allocated.
    amount=0.0,  # optional — Total monetary value allocated, derived from the quantity and price of each allocation.
    details=[]  # required — Identifiers for each allocation in this block.
)
```

- [OrderGraphBlockAllocationDetail](OrderGraphBlockAllocationDetail.md) — used in `details`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

