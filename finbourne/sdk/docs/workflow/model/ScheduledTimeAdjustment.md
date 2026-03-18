# ScheduledTimeAdjustment

Represents an adjustment to the scheduled time of an EventHandler. Only relevant for EventHandlers with a Finbourne.Workflow.WebApi.Common.Dto.Json.EventHandlers.ScheduleMatchingPattern
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **date_adjustment** | [DateAdjustment](DateAdjustment.md) | Required | *No description available.* |
| **time_adjustment** | [TimeAdjustment](TimeAdjustment.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.ScheduledTimeAdjustment import ScheduledTimeAdjustment

instance = ScheduledTimeAdjustment(
    date_adjustment=DateAdjustment(...),  # required
    time_adjustment=TimeAdjustment(...)  # required
)
```


## Related Models

- [DateAdjustment](DateAdjustment.md)
- [TimeAdjustment](TimeAdjustment.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

