# DateTimeAdjustment

A change applied to the date and the time of a source value, in a named calendar context.              At least one of Finbourne.Workflow.WebApi.Common.Dto.Json.Launchers.DateTimeAdjustment.DateAdjustment or Finbourne.Workflow.WebApi.Common.Dto.Json.Launchers.DateTimeAdjustment.TimeAdjustment must be given
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **calendar_context** | **str** | Optional | The name of the calendar context this change happens in, which must be one the Launcher declares. When it is left out a Schedule Launcher uses the context of its schedule |
| **date_adjustment** | [DateAdjustment](DateAdjustment.md) | Optional | *No description available.* |
| **time_adjustment** | [TimeAdjustment](TimeAdjustment.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.DateTimeAdjustment import DateTimeAdjustment

instance = DateTimeAdjustment(
    calendar_context="...",  # optional — The name of the calendar context this change happens in, which must be one the Launcher declares. When it is left out a Schedule Launcher uses the context of its schedule
    date_adjustment=DateAdjustment(...),  # optional
    time_adjustment=TimeAdjustment(...)  # optional
)
```

- [DateAdjustment](DateAdjustment.md)
- [TimeAdjustment](TimeAdjustment.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

