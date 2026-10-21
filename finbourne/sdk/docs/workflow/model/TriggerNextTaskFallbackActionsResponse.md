# TriggerNextTaskFallbackActionsResponse

Actions on the same task definition that a Trigger Next Task action runs instead of triggering the next task
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **end_of_sequence** | **str** | Optional | Run when this task has no next task to trigger |
| **next_task_error** | **str** | Optional | Run when the next task cannot be triggered, e.g. it was deleted or is not in its initial state |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.TriggerNextTaskFallbackActionsResponse import TriggerNextTaskFallbackActionsResponse

instance = TriggerNextTaskFallbackActionsResponse(
    end_of_sequence="...",  # optional — Run when this task has no next task to trigger
    next_task_error="..."  # optional — Run when the next task cannot be triggered, e.g. it was deleted or is not in its initial state
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

