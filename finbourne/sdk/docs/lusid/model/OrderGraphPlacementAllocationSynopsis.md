# OrderGraphPlacementAllocationSynopsis

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **quantity** | **float** | Required | Total number of units allocated. |
| **details** | [List[OrderGraphPlacementAllocationDetail]](OrderGraphPlacementAllocationDetail.md) | Required | Identifiers for each allocation in this placement. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.OrderGraphPlacementAllocationSynopsis import OrderGraphPlacementAllocationSynopsis

instance = OrderGraphPlacementAllocationSynopsis(
    quantity=0.0,  # required — Total number of units allocated.
    details=[]  # required — Identifiers for each allocation in this placement.
)
```

- [OrderGraphPlacementAllocationDetail](OrderGraphPlacementAllocationDetail.md) — used in `details`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

