# OrderGraphPlacementExecutionSynopsis

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **quantity** | **float** | Required | Total number of units executed. |
| **details** | [List[OrderGraphPlacementExecutionDetail]](OrderGraphPlacementExecutionDetail.md) | Required | Identifiers info for each execution against this placement. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.OrderGraphPlacementExecutionSynopsis import OrderGraphPlacementExecutionSynopsis

instance = OrderGraphPlacementExecutionSynopsis(
    quantity=0.0,  # required — Total number of units executed.
    details=[]  # required — Identifiers info for each execution against this placement.
)
```

- [OrderGraphPlacementExecutionDetail](OrderGraphPlacementExecutionDetail.md) — used in `details`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

