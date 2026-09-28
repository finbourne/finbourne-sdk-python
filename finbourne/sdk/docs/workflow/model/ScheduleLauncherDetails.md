# ScheduleLauncherDetails

A Launcher that starts a run of its Workflow at the times a recurrence pattern gives, and can fill date and time fields of the root task from the instant it fired
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **launcher_type** | **str** | Required | *No description available.* |
| **schedule** | [LauncherSchedule](LauncherSchedule.md) | Required | *No description available.* |
| **calendar_contexts** | [List[CalendarContext]](CalendarContext.md) | Optional | The named time zones and holiday calendars this Launcher works in.              Only a Schedule Launcher works in a calendar context |
| **map_task_fields** | [Dict[str, ScheduleTaskFieldMapping]](ScheduleTaskFieldMapping.md) | Optional | Fields of the root task filled from the instant the schedule fired, keyed by the field name on the root task definition |
| **run_as_user_id** | [LauncherMapping](LauncherMapping.md) | Required | *No description available.* |
| **set_task_fields** | **Dict[str, Optional[object]]** | Optional | Fields of the root task set to a fixed value, keyed by the field name on the root task definition |
| **set_correlation_ids** | **List[str]** | Optional | Correlation IDs put on the root task as given |
| **initial_trigger** | **str** | Optional | The trigger given to the root task once it is made and all of its fields are filled. When it is left out the root task is left in its initial state |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.ScheduleLauncherDetails import ScheduleLauncherDetails

instance = ScheduleLauncherDetails(
    launcher_type="...",  # required
    schedule=LauncherSchedule(...),  # required
    calendar_contexts=[],  # optional — The named time zones and holiday calendars this Launcher works in.              Only a Schedule Launcher works in a calendar context
    map_task_fields=ScheduleTaskFieldMapping(...),  # optional — Fields of the root task filled from the instant the schedule fired, keyed by the field name on the root task definition
    run_as_user_id=LauncherMapping(...),  # required
    set_task_fields=,  # optional — Fields of the root task set to a fixed value, keyed by the field name on the root task definition
    set_correlation_ids=,  # optional — Correlation IDs put on the root task as given
    initial_trigger="..."  # optional — The trigger given to the root task once it is made and all of its fields are filled. When it is left out the root task is left in its initial state
)
```

- [LauncherSchedule](LauncherSchedule.md)
- [CalendarContext](CalendarContext.md) — used in `calendar_contexts`
- [ScheduleTaskFieldMapping](ScheduleTaskFieldMapping.md) — used in `map_task_fields`
- [LauncherMapping](LauncherMapping.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

