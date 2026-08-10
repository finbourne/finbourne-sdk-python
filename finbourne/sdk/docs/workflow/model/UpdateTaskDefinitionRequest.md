# UpdateTaskDefinitionRequest

Contains required info to update a Task Definition
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **display_name** | **str** | Required | Human readable name |
| **description** | **str** | Optional | Human readable description |
| **states** | [../model/List[TaskStateDefinition]](TaskStateDefinition.md) | Required | The states this Task Definition operates over |
| **field_schema** | [../model/List[TaskFieldDefinition]](TaskFieldDefinition.md) | Optional | Defines the fields associated with this Task |
| **initial_state** | [../model/InitialState](InitialState.md) | Required | *No description available.* |
| **triggers** | [../model/List[TransitionTriggerDefinition]](TransitionTriggerDefinition.md) | Optional | Triggers |
| **transitions** | [../model/List[TaskTransitionDefinition]](TaskTransitionDefinition.md) | Optional | Transitions |
| **actions** | [../model/List[ActionDefinition]](ActionDefinition.md) | Optional | Actions |
| **properties** | [../model/Dict[str, PerpetualProperty]](PerpetualProperty.md) | Optional | The properties to set on the Task Definition, keyed by property key. Optional. A null property value deletes the property. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.UpdateTaskDefinitionRequest import UpdateTaskDefinitionRequest

instance = UpdateTaskDefinitionRequest(
    display_name="...",  # required — Human readable name
    description="...",  # optional — Human readable description
    states=[],  # required — The states this Task Definition operates over
    field_schema=[],  # optional — Defines the fields associated with this Task
    initial_state=InitialState(...),  # required
    triggers=[],  # optional — Triggers
    transitions=[],  # optional — Transitions
    actions=[],  # optional — Actions
    properties=PerpetualProperty(...)  # optional — The properties to set on the Task Definition, keyed by property key. Optional. A null property value deletes the property.
)
```

- [TaskStateDefinition](TaskStateDefinition.md) — used in `states`
- [TaskFieldDefinition](TaskFieldDefinition.md) — used in `field_schema`
- [InitialState](InitialState.md)
- [TransitionTriggerDefinition](TransitionTriggerDefinition.md) — used in `triggers`
- [TaskTransitionDefinition](TaskTransitionDefinition.md) — used in `transitions`
- [ActionDefinition](ActionDefinition.md) — used in `actions`
- [PerpetualProperty](PerpetualProperty.md) — used in `properties`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

