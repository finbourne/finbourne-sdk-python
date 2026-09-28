# ScheduleLauncherDetailsResponse

A Schedule Launcher, which starts a run of its Workflow at the times a recurrence pattern gives
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **launcher_type** | **str** | Optional | *No description available.* |
| **schedule** | [LauncherSchedule](LauncherSchedule.md) | Optional | *No description available.* |
| **calendar_contexts** | [List[CalendarContext]](CalendarContext.md) | Optional | The named time zones and holiday calendars this Launcher works in.              Only a Schedule Launcher works in a calendar context |
| **map_task_fields** | [Dict[str, ScheduleTaskFieldMapping]](ScheduleTaskFieldMapping.md) | Optional | Fields of the root task filled from the instant the schedule fired, keyed by the field name on the root task definition |
| **run_as_user_id** | [LauncherMapping](LauncherMapping.md) | Optional | *No description available.* |
| **set_task_fields** | **Dict[str, Optional[object]]** | Optional | Fields of the root task set to a fixed value, keyed by the field name on the root task definition |
| **set_correlation_ids** | **List[str]** | Optional | Correlation IDs put on the root task as given |
| **initial_trigger** | **str** | Optional | The trigger given to the root task once it is made and all of its fields are filled, or null when the root task is left in its initial state |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.ScheduleLauncherDetailsResponse import ScheduleLauncherDetailsResponse

instance = ScheduleLauncherDetailsResponse(
    launcher_type="...",  # optional
    schedule=LauncherSchedule(...),  # optional
    calendar_contexts=[],  # optional — The named time zones and holiday calendars this Launcher works in.              Only a Schedule Launcher works in a calendar context
    map_task_fields=ScheduleTaskFieldMapping(...),  # optional — Fields of the root task filled from the instant the schedule fired, keyed by the field name on the root task definition
    run_as_user_id=LauncherMapping(...),  # optional
    set_task_fields=,  # optional — Fields of the root task set to a fixed value, keyed by the field name on the root task definition
    set_correlation_ids=,  # optional — Correlation IDs put on the root task as given
    initial_trigger="..."  # optional — The trigger given to the root task once it is made and all of its fields are filled, or null when the root task is left in its initial state
)
```

- [LauncherSchedule](LauncherSchedule.md)
- [CalendarContext](CalendarContext.md) — used in `calendar_contexts`
- [ScheduleTaskFieldMapping](ScheduleTaskFieldMapping.md) — used in `map_task_fields`
- [LauncherMapping](LauncherMapping.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

