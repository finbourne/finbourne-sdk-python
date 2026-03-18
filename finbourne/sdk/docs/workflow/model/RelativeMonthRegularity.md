# RelativeMonthRegularity

Relative Month Regularity
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **frequency** | **int** | Required | The frequency of the Relative Month Regularity. For example, a value of 2 indicates every 2 months |
| **days_of_week** | **List[str]** | Required | Days of the week. One or more of - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday |
| **index** | **str** | Required | Relative index in the month. One of - First, Second, Third, Fourth, Last. For example, to specify the second Tuesday of every month, set DaysOfWeek to [\&quot;Tuesday\&quot;] and Index to \&quot;Second\&quot; |
| **type** | **str** | Required | The type of Date Regularity |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.RelativeMonthRegularity import RelativeMonthRegularity

instance = RelativeMonthRegularity(
    frequency=0,  # required — The frequency of the Relative Month Regularity. For example, a value of 2 indicates every 2 months
    days_of_week=,  # required — Days of the week. One or more of - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday
    index="...",  # required — Relative index in the month. One of - First, Second, Third, Fourth, Last. For example, to specify the second Tuesday of every month, set DaysOfWeek to [\&quot;Tuesday\&quot;] and Index to \&quot;Second\&quot;
    type="..."  # required — The type of Date Regularity
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

