# TriggerChildTasksAction

Defines a Trigger Child Tasks Action
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **type** | **str** | Required | Type name for this Action |
| **trigger** | **str** | Required | Trigger on child tasks to be invoked |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.TriggerChildTasksAction import TriggerChildTasksAction

instance = TriggerChildTasksAction(
    type="...",  # required — Type name for this Action
    trigger="..."  # required — Trigger on child tasks to be invoked
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

