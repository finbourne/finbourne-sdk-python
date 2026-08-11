# YearRegularity

Year Regularity
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **dates** | [List[DayOfYear]](DayOfYear.md) | Required | The dates in the year |
| **type** | **str** | Required | The type of Date Regularity |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.YearRegularity import YearRegularity

instance = YearRegularity(
    dates=[],  # required — The dates in the year
    type="..."  # required — The type of Date Regularity
)
```


## Related Models

- [DayOfYear](DayOfYear.md) — used in `dates`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

