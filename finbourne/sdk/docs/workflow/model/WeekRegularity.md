# WeekRegularity

Week Regularity
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **frequency** | **int** | Required | The frequency of the Week Regularity. For example, a value of 2 indicates every 2 weeks |
| **days_of_week** | **List[str]** | Required | Days of the week. One or more of - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday |
| **type** | **str** | Required | The type of Date Regularity |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.WeekRegularity import WeekRegularity

instance = WeekRegularity(
    frequency=0,  # required — The frequency of the Week Regularity. For example, a value of 2 indicates every 2 weeks
    days_of_week=,  # required — Days of the week. One or more of - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday
    type="..."  # required — The type of Date Regularity
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

