# TaskDefinition

Task Definition
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **version** | [VersionInfo](VersionInfo.md) | Optional | *No description available.* |
| **display_name** | **str** | Required | Human readable name |
| **description** | **str** | Optional | Human readable description |
| **states** | [List[TaskStateDefinition]](TaskStateDefinition.md) | Required | The states this Task Definition operates over |
| **field_schema** | [List[TaskFieldDefinition]](TaskFieldDefinition.md) | Optional | The Fields that this Task Definition operates on |
| **initial_state** | [InitialState](InitialState.md) | Required | *No description available.* |
| **triggers** | [List[TransitionTriggerDefinition]](TransitionTriggerDefinition.md) | Optional | The Triggers for State transition |
| **actions** | [List[ActionDefinitionResponse]](ActionDefinitionResponse.md) | Optional | The Actions of this Task - executed after a Transition completion |
| **transitions** | [List[TaskTransitionDefinition]](TaskTransitionDefinition.md) | Optional | The Transitions between States |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.TaskDefinition import TaskDefinition

instance = TaskDefinition(
    id=ResourceId(...),  # required
    version=VersionInfo(...),  # optional
    display_name="...",  # required — Human readable name
    description="...",  # optional — Human readable description
    states=[],  # required — The states this Task Definition operates over
    field_schema=[],  # optional — The Fields that this Task Definition operates on
    initial_state=InitialState(...),  # required
    triggers=[],  # optional — The Triggers for State transition
    actions=[],  # optional — The Actions of this Task - executed after a Transition completion
    transitions=[]  # optional — The Transitions between States
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [VersionInfo](VersionInfo.md)
- [TaskStateDefinition](TaskStateDefinition.md) — used in `states`
- [TaskFieldDefinition](TaskFieldDefinition.md) — used in `field_schema`
- [InitialState](InitialState.md)
- [TransitionTriggerDefinition](TransitionTriggerDefinition.md) — used in `triggers`
- [ActionDefinitionResponse](ActionDefinitionResponse.md) — used in `actions`
- [TaskTransitionDefinition](TaskTransitionDefinition.md) — used in `transitions`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

