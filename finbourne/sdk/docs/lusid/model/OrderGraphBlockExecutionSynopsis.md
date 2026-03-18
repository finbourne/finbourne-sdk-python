# OrderGraphBlockExecutionSynopsis

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **quantity** | **float** | Required | Total number of units executed. |
| **details** | [List[OrderGraphBlockExecutionDetail]](OrderGraphBlockExecutionDetail.md) | Required | Identifiers for each execution in this block. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.OrderGraphBlockExecutionSynopsis import OrderGraphBlockExecutionSynopsis

instance = OrderGraphBlockExecutionSynopsis(
    quantity=0.0,  # required — Total number of units executed.
    details=[]  # required — Identifiers for each execution in this block.
)
```

- [OrderGraphBlockExecutionDetail](OrderGraphBlockExecutionDetail.md) — used in `details`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

