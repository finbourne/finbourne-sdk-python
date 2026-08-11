# ActionDefinition

Defines the Actions for a Task
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **name** | **str** | Required | The Name of this Action |
| **run_as_user_id** | **str** | Optional | The ID of the user that this action will be performed by. If not specified, the actions will be performed by the \&quot;current user\&quot;. |
| **action_details** | [ActionDetails](ActionDetails.md) | Required | *No description available.* |
| **display_name** | **str** | Optional | The display name of this Action |
| **description** | **str** | Optional | The description of this Action |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.ActionDefinition import ActionDefinition

instance = ActionDefinition(
    name="...",  # required — The Name of this Action
    run_as_user_id="...",  # optional — The ID of the user that this action will be performed by. If not specified, the actions will be performed by the \&quot;current user\&quot;.
    action_details=ActionDetails(...),  # required
    display_name="...",  # optional — The display name of this Action
    description="..."  # optional — The description of this Action
)
```

- [ActionDetails](ActionDetails.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

