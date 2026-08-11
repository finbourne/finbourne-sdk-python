# CreateNewTaskActivityResponse

Read only Create new task response
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **type** | **str** | Optional | Type of task activity |
| **initial_trigger** | **str** | Optional | Trigger to supply to all tasks to be made |
| **correlation_ids** | [List[EventHandlerMapping]](EventHandlerMapping.md) | Optional | The event to correlation ID mappings |
| **task_fields** | [Dict[str, FieldMapping]](FieldMapping.md) | Optional | The event to task field mappings |
| **schedule_dependent_task_fields** | [Dict[str, ScheduledTimeAdjustment]](ScheduledTimeAdjustment.md) | Optional | The Schedule dependent task field mappings. Only relevant if a Finbourne.Workflow.WebApi.Common.Dto.Json.EventHandlers.ScheduleMatchingPattern is specified |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.CreateNewTaskActivityResponse import CreateNewTaskActivityResponse

instance = CreateNewTaskActivityResponse(
    type="...",  # optional — Type of task activity
    initial_trigger="...",  # optional — Trigger to supply to all tasks to be made
    correlation_ids=[],  # optional — The event to correlation ID mappings
    task_fields=FieldMapping(...),  # optional — The event to task field mappings
    schedule_dependent_task_fields=ScheduledTimeAdjustment(...)  # optional — The Schedule dependent task field mappings. Only relevant if a Finbourne.Workflow.WebApi.Common.Dto.Json.EventHandlers.ScheduleMatchingPattern is specified
)
```

- [EventHandlerMapping](EventHandlerMapping.md) — used in `correlation_ids`
- [FieldMapping](FieldMapping.md) — used in `task_fields`
- [ScheduledTimeAdjustment](ScheduledTimeAdjustment.md) — used in `schedule_dependent_task_fields`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

