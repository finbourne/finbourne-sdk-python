# ActionLogOrigin

The Action Log Origin contains information about how the Action was created
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **task_id** | **UUID** | Optional | The Id of the Task that created this Action |
| **request_id** | **str** | Required | The request Id of the request that caused this Action to be triggered. This could be the original request that caused a sequence of Actions that resulted in this Action |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.ActionLogOrigin import ActionLogOrigin

instance = ActionLogOrigin(
    task_id="...",  # optional — The Id of the Task that created this Action
    request_id="..."  # required — The request Id of the request that caused this Action to be triggered. This could be the original request that caused a sequence of Actions that resulted in this Action
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

