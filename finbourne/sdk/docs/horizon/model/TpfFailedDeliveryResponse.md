# TpfFailedDeliveryResponse

Response for bulk retry operation of failed deliveries
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **submitted** | **int** | Required | Number of batch elements submitted for retry |
| **results** | [List[TpfRetryElementResult]](TpfRetryElementResult.md) | Required | Per-element retry results |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.TpfFailedDeliveryResponse import TpfFailedDeliveryResponse

instance = TpfFailedDeliveryResponse(
    submitted=0,  # required — Number of batch elements submitted for retry
    results=[]  # required — Per-element retry results
)
```

- [TpfRetryElementResult](TpfRetryElementResult.md) — used in `results`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

