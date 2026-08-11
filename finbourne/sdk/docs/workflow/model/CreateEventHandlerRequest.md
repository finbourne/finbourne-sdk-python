# CreateEventHandlerRequest

Contains information for creating an Event Handler
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **display_name** | **str** | Required | Human readable name |
| **description** | **str** | Optional | Human readable description |
| **status** | **str** | Required | The current status of the event handler |
| **event_matching_pattern** | [EventMatchingPattern](EventMatchingPattern.md) | Optional | *No description available.* |
| **schedule_matching_pattern** | [ScheduleMatchingPattern](ScheduleMatchingPattern.md) | Optional | *No description available.* |
| **run_as_user_id** | [EventHandlerMapping](EventHandlerMapping.md) | Required | *No description available.* |
| **task_definition_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **task_definition_as_at** | **datetime** | Optional | AsAt of the required task definition |
| **task_activity** | [TaskActivity](TaskActivity.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.CreateEventHandlerRequest import CreateEventHandlerRequest

instance = CreateEventHandlerRequest(
    id=ResourceId(...),  # required
    display_name="...",  # required — Human readable name
    description="...",  # optional — Human readable description
    status="...",  # required — The current status of the event handler
    event_matching_pattern=EventMatchingPattern(...),  # optional
    schedule_matching_pattern=ScheduleMatchingPattern(...),  # optional
    run_as_user_id=EventHandlerMapping(...),  # required
    task_definition_id=ResourceId(...),  # required
    task_definition_as_at=datetime.now(),  # optional — AsAt of the required task definition
    task_activity=TaskActivity(...)  # required
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [EventMatchingPattern](EventMatchingPattern.md)
- [ScheduleMatchingPattern](ScheduleMatchingPattern.md)
- [EventHandlerMapping](EventHandlerMapping.md)
- [ResourceId](ResourceId.md)
- [TaskActivity](TaskActivity.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

