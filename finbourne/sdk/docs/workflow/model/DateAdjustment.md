# DateAdjustment

A date adjustment to apply to the scheduled time of an EventHandler with a Finbourne.Workflow.WebApi.Common.Dto.Json.EventHandlers.ScheduleMatchingPattern
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **delta_days** | **int** | Required | The delta to apply to the date part of the scheduled time, in days |
| **business_day_adjustment** | **str** | Required | The Business Day Adjustment |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.DateAdjustment import DateAdjustment

instance = DateAdjustment(
    delta_days=0,  # required — The delta to apply to the date part of the scheduled time, in days
    business_day_adjustment="..."  # required — The Business Day Adjustment
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

