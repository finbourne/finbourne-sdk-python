# CreateTaskDefinitionRequest

Contains required info to create a new Task Definition
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **display_name** | **str** | Required | Human readable name |
| **description** | **str** | Optional | Human readable description |
| **states** | [List[TaskStateDefinition]](TaskStateDefinition.md) | Required | The states this Task Definition operates over |
| **field_schema** | [List[TaskFieldDefinition]](TaskFieldDefinition.md) | Optional | Defines the fields associated with this Task |
| **initial_state** | [InitialState](InitialState.md) | Required | *No description available.* |
| **triggers** | [List[TransitionTriggerDefinition]](TransitionTriggerDefinition.md) | Optional | Triggers |
| **transitions** | [List[TaskTransitionDefinition]](TaskTransitionDefinition.md) | Optional | Transitions |
| **actions** | [List[ActionDefinition]](ActionDefinition.md) | Optional | Actions |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.CreateTaskDefinitionRequest import CreateTaskDefinitionRequest

instance = CreateTaskDefinitionRequest(
    id=ResourceId(...),  # required
    display_name="...",  # required — Human readable name
    description="...",  # optional — Human readable description
    states=[],  # required — The states this Task Definition operates over
    field_schema=[],  # optional — Defines the fields associated with this Task
    initial_state=InitialState(...),  # required
    triggers=[],  # optional — Triggers
    transitions=[],  # optional — Transitions
    actions=[]  # optional — Actions
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [TaskStateDefinition](TaskStateDefinition.md) — used in `states`
- [TaskFieldDefinition](TaskFieldDefinition.md) — used in `field_schema`
- [InitialState](InitialState.md)
- [TransitionTriggerDefinition](TransitionTriggerDefinition.md) — used in `triggers`
- [TaskTransitionDefinition](TaskTransitionDefinition.md) — used in `transitions`
- [ActionDefinition](ActionDefinition.md) — used in `actions`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

