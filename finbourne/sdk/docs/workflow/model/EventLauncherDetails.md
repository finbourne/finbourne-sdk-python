# EventLauncherDetails

A Launcher that starts a run of its Workflow when a matching platform event arrives, and can fill fields and correlation IDs of the root task from that event
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **launcher_type** | **str** | Required | *No description available.* |
| **event_matching_pattern** | [LauncherEventMatchingPattern](LauncherEventMatchingPattern.md) | Required | *No description available.* |
| **map_task_fields** | [Dict[str, EventTaskFieldMapping]](EventTaskFieldMapping.md) | Optional | Fields of the root task filled from the event, keyed by the field name on the root task definition |
| **map_correlation_ids** | [List[CorrelationIdMapping]](CorrelationIdMapping.md) | Optional | Correlation IDs of the root task filled from the event |
| **run_as_user_id** | [LauncherMapping](LauncherMapping.md) | Required | *No description available.* |
| **set_task_fields** | **Dict[str, Optional[object]]** | Optional | Fields of the root task set to a fixed value, keyed by the field name on the root task definition |
| **set_correlation_ids** | **List[str]** | Optional | Correlation IDs put on the root task as given |
| **initial_trigger** | **str** | Optional | The trigger given to the root task once it is made and all of its fields are filled. When it is left out the root task is left in its initial state |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.EventLauncherDetails import EventLauncherDetails

instance = EventLauncherDetails(
    launcher_type="...",  # required
    event_matching_pattern=LauncherEventMatchingPattern(...),  # required
    map_task_fields=EventTaskFieldMapping(...),  # optional — Fields of the root task filled from the event, keyed by the field name on the root task definition
    map_correlation_ids=[],  # optional — Correlation IDs of the root task filled from the event
    run_as_user_id=LauncherMapping(...),  # required
    set_task_fields=,  # optional — Fields of the root task set to a fixed value, keyed by the field name on the root task definition
    set_correlation_ids=,  # optional — Correlation IDs put on the root task as given
    initial_trigger="..."  # optional — The trigger given to the root task once it is made and all of its fields are filled. When it is left out the root task is left in its initial state
)
```

- [LauncherEventMatchingPattern](LauncherEventMatchingPattern.md)
- [EventTaskFieldMapping](EventTaskFieldMapping.md) — used in `map_task_fields`
- [CorrelationIdMapping](CorrelationIdMapping.md) — used in `map_correlation_ids`
- [LauncherMapping](LauncherMapping.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

