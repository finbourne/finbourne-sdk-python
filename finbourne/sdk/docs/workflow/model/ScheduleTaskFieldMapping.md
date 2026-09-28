# ScheduleTaskFieldMapping

How a Schedule Launcher fills one field of the root task from the instant the schedule fired
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **map_from** | **str** | Required | The value the field is taken from. One of - ScheduledTime |
| **date_time_adjustment** | [DateTimeAdjustment](DateTimeAdjustment.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.ScheduleTaskFieldMapping import ScheduleTaskFieldMapping

instance = ScheduleTaskFieldMapping(
    map_from="...",  # required — The value the field is taken from. One of - ScheduledTime
    date_time_adjustment=DateTimeAdjustment(...)  # optional
)
```

- [DateTimeAdjustment](DateTimeAdjustment.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

