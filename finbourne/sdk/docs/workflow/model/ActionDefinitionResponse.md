# ActionDefinitionResponse

Defines the Actions for a Task in a read-only form
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **name** | **str** | Optional | The Name of this Action |
| **run_as_user_id** | **str** | Optional | The ID of the user that this action will be performed by. If not specified, the actions will be performed by the \&quot;current user\&quot;. |
| **action_details** | [ActionDetailsResponse](ActionDetailsResponse.md) | Optional | *No description available.* |
| **display_name** | **str** | Optional | Schema for the Action |
| **description** | **str** | Optional | Schema for the Action |
| **category** | **str** | Optional | Schema for the Action |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.ActionDefinitionResponse import ActionDefinitionResponse

instance = ActionDefinitionResponse(
    name="...",  # optional — The Name of this Action
    run_as_user_id="...",  # optional — The ID of the user that this action will be performed by. If not specified, the actions will be performed by the \&quot;current user\&quot;.
    action_details=ActionDetailsResponse(...),  # optional
    display_name="...",  # optional — Schema for the Action
    description="...",  # optional — Schema for the Action
    category="..."  # optional — Schema for the Action
)
```

- [ActionDetailsResponse](ActionDetailsResponse.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

