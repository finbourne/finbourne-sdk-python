# TaskTransitionDefinition

Defines a State change
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **from_state** | **str** | Required | The State this Transition if coming From |
| **to_state** | **str** | Required | The State this Transition is going To |
| **trigger** | **str** | Required | The Trigger for this Transition |
| **guard** | **str** | Optional | The Guard for this Transition, if any |
| **action** | **str** | Optional | The Action to invoke on successful Transition |
| **display_name** | **str** | Optional | Display name for transition |
| **description** | **str** | Optional | Description for transition |
| **guard_description** | **str** | Optional | Guard description for transition |
| **guard_condition_not_met_message** | **str** | Optional | Message when guard has not been met |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.TaskTransitionDefinition import TaskTransitionDefinition

instance = TaskTransitionDefinition(
    from_state="...",  # required — The State this Transition if coming From
    to_state="...",  # required — The State this Transition is going To
    trigger="...",  # required — The Trigger for this Transition
    guard="...",  # optional — The Guard for this Transition, if any
    action="...",  # optional — The Action to invoke on successful Transition
    display_name="...",  # optional — Display name for transition
    description="...",  # optional — Description for transition
    guard_description="...",  # optional — Guard description for transition
    guard_condition_not_met_message="..."  # optional — Message when guard has not been met
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

