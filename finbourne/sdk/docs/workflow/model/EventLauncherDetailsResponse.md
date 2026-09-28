# EventLauncherDetailsResponse

A read only Event Launcher, which starts a run of its Workflow when a matching platform event arrives
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **launcher_type** | **str** | Optional | *No description available.* |
| **event_matching_pattern** | [LauncherEventMatchingPattern](LauncherEventMatchingPattern.md) | Optional | *No description available.* |
| **map_task_fields** | [Dict[str, EventTaskFieldMapping]](EventTaskFieldMapping.md) | Optional | Fields of the root task filled from the event, keyed by the field name on the root task definition |
| **map_correlation_ids** | [List[CorrelationIdMapping]](CorrelationIdMapping.md) | Optional | Correlation IDs of the root task filled from the event |
| **run_as_user_id** | [LauncherMapping](LauncherMapping.md) | Optional | *No description available.* |
| **set_task_fields** | **Dict[str, Optional[object]]** | Optional | Fields of the root task set to a fixed value, keyed by the field name on the root task definition |
| **set_correlation_ids** | **List[str]** | Optional | Correlation IDs put on the root task as given |
| **initial_trigger** | **str** | Optional | The trigger given to the root task once it is made and all of its fields are filled, or null when the root task is left in its initial state |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.EventLauncherDetailsResponse import EventLauncherDetailsResponse

instance = EventLauncherDetailsResponse(
    launcher_type="...",  # optional
    event_matching_pattern=LauncherEventMatchingPattern(...),  # optional
    map_task_fields=EventTaskFieldMapping(...),  # optional — Fields of the root task filled from the event, keyed by the field name on the root task definition
    map_correlation_ids=[],  # optional — Correlation IDs of the root task filled from the event
    run_as_user_id=LauncherMapping(...),  # optional
    set_task_fields=,  # optional — Fields of the root task set to a fixed value, keyed by the field name on the root task definition
    set_correlation_ids=,  # optional — Correlation IDs put on the root task as given
    initial_trigger="..."  # optional — The trigger given to the root task once it is made and all of its fields are filled, or null when the root task is left in its initial state
)
```

- [LauncherEventMatchingPattern](LauncherEventMatchingPattern.md)
- [EventTaskFieldMapping](EventTaskFieldMapping.md) — used in `map_task_fields`
- [CorrelationIdMapping](CorrelationIdMapping.md) — used in `map_correlation_ids`
- [LauncherMapping](LauncherMapping.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

