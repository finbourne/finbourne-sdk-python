# RelativeOffset

A relative offset back from \"now\", e.g. `{ Amount = 2, Unit = Hours }` meaning two hours before now.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **amount** | **int** | Required | The number of units to go back from now. Must be at least 1. |
| **unit** | **str** | Required | The unit of the offset. One of the Finbourne.Insights.WebApi.Dtos.Querying.RelativeTimeUnit values. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.insights.models.RelativeOffset import RelativeOffset

instance = RelativeOffset(
    amount=0,  # required — The number of units to go back from now. Must be at least 1.
    unit="..."  # required — The unit of the offset. One of the Finbourne.Insights.WebApi.Dtos.Querying.RelativeTimeUnit values.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

