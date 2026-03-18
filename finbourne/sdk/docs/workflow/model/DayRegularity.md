# DayRegularity

Day Regularity
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **frequency** | **int** | Required | The frequency of the Day Regularity. For example, a value of 2 indicates every 2 days |
| **type** | **str** | Required | The type of Date Regularity |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.DayRegularity import DayRegularity

instance = DayRegularity(
    frequency=0,  # required — The frequency of the Day Regularity. For example, a value of 2 indicates every 2 days
    type="..."  # required — The type of Date Regularity
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

