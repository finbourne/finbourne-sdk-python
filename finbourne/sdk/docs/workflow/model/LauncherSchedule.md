# LauncherSchedule

When a Schedule Launcher starts a run of its Workflow
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **calendar_context** | **str** | Required | The name of the calendar context the schedule is read in, which must be one the Launcher declares |
| **recurrence_pattern** | [RecurrencePattern](RecurrencePattern.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.LauncherSchedule import LauncherSchedule

instance = LauncherSchedule(
    calendar_context="...",  # required — The name of the calendar context the schedule is read in, which must be one the Launcher declares
    recurrence_pattern=RecurrencePattern(...)  # required
)
```

- [RecurrencePattern](RecurrencePattern.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

