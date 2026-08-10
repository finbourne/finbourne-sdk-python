# TaskDefinition

Task Definition
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [../model/ResourceId](ResourceId.md) | Required | *No description available.* |
| **version** | [../model/VersionInfo](VersionInfo.md) | Optional | *No description available.* |
| **display_name** | **str** | Required | Human readable name |
| **description** | **str** | Optional | Human readable description |
| **states** | [../model/List[TaskStateDefinition]](TaskStateDefinition.md) | Required | The states this Task Definition operates over |
| **field_schema** | [../model/List[TaskFieldDefinition]](TaskFieldDefinition.md) | Optional | The Fields that this Task Definition operates on |
| **initial_state** | [../model/InitialState](InitialState.md) | Required | *No description available.* |
| **triggers** | [../model/List[TransitionTriggerDefinition]](TransitionTriggerDefinition.md) | Optional | The Triggers for State transition |
| **actions** | [../model/List[ActionDefinitionResponse]](ActionDefinitionResponse.md) | Optional | The Actions of this Task - executed after a Transition completion |
| **transitions** | [../model/List[TaskTransitionDefinition]](TaskTransitionDefinition.md) | Optional | The Transitions between States |
| **properties** | [../model/Dict[str, PerpetualProperty]](PerpetualProperty.md) | Optional | The properties of the Task Definition, keyed by property key. Only populated when set on the request (Create/Update) or when property keys are requested (Get/List). |


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
    transitions=[],  # optional — The Transitions between States
    properties=PerpetualProperty(...)  # optional — The properties of the Task Definition, keyed by property key. Only populated when set on the request (Create/Update) or when property keys are requested (Get/List).
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
- [PerpetualProperty](PerpetualProperty.md) — used in `properties`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

