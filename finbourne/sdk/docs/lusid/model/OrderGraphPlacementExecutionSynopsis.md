# OrderGraphPlacementExecutionSynopsis

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **quantity** | **float** | Required | Total number of units executed. |
| **amount** | **float** | Optional | Total monetary value executed, derived from the quantity and price of each execution, in the placement&#39;s amount currency. Null where the placement has no amount, or where an execution cannot be expressed in that currency. |
| **details** | [List[OrderGraphPlacementExecutionDetail]](OrderGraphPlacementExecutionDetail.md) | Required | Identifiers info for each execution against this placement. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.OrderGraphPlacementExecutionSynopsis import OrderGraphPlacementExecutionSynopsis

instance = OrderGraphPlacementExecutionSynopsis(
    quantity=0.0,  # required — Total number of units executed.
    amount=0.0,  # optional — Total monetary value executed, derived from the quantity and price of each execution, in the placement&#39;s amount currency. Null where the placement has no amount, or where an execution cannot be expressed in that currency.
    details=[]  # required — Identifiers info for each execution against this placement.
)
```

- [OrderGraphPlacementExecutionDetail](OrderGraphPlacementExecutionDetail.md) — used in `details`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

