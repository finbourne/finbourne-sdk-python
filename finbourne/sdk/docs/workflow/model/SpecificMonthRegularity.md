# SpecificMonthRegularity

Specific Month Regularity
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **frequency** | **int** | Required | The frequency of the Specific Month Regularity. For example, a value of 2 indicates every 2 months |
| **days_of_month** | **List[int]** | Required | Days of the month. For example, to specify the 1st and 15th of every month, set DaysOfMonth to [1, 15] |
| **type** | **str** | Required | The type of Date Regularity |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.SpecificMonthRegularity import SpecificMonthRegularity

instance = SpecificMonthRegularity(
    frequency=0,  # required — The frequency of the Specific Month Regularity. For example, a value of 2 indicates every 2 months
    days_of_month=,  # required — Days of the month. For example, to specify the 1st and 15th of every month, set DaysOfMonth to [1, 15]
    type="..."  # required — The type of Date Regularity
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

