# ActionLog

An Action Log contains the processing history of an Action
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | **UUID** | Required | Unique identifier of the Action |
| **origin** | [ActionLogOrigin](ActionLogOrigin.md) | Required | *No description available.* |
| **action_type** | **str** | Required | The type of the Action |
| **run_as_user_id** | **str** | Optional | The ID of the user that the Action was performed by. If not specified, the actions were performed by the \&quot;current user\&quot;. |
| **logged_items** | [List[ActionLogItem]](ActionLogItem.md) | Required | The logged items for this Action |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.ActionLog import ActionLog

instance = ActionLog(
    id="...",  # required — Unique identifier of the Action
    origin=ActionLogOrigin(...),  # required
    action_type="...",  # required — The type of the Action
    run_as_user_id="...",  # optional — The ID of the user that the Action was performed by. If not specified, the actions were performed by the \&quot;current user\&quot;.
    logged_items=[]  # required — The logged items for this Action
)
```

- [ActionLogOrigin](ActionLogOrigin.md)
- [ActionLogItem](ActionLogItem.md) — used in `logged_items`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

