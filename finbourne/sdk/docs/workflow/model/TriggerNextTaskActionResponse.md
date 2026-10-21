# TriggerNextTaskActionResponse

Trigger Next Task Action Response
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **type** | **str** | Optional | Type name for this Action |
| **default_trigger** | **str** | Optional | Trigger sent to the next task when this task has no nextTaskInitialTrigger of its own |
| **fallback_actions** | [TriggerNextTaskFallbackActionsResponse](TriggerNextTaskFallbackActionsResponse.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.TriggerNextTaskActionResponse import TriggerNextTaskActionResponse

instance = TriggerNextTaskActionResponse(
    type="...",  # optional — Type name for this Action
    default_trigger="...",  # optional — Trigger sent to the next task when this task has no nextTaskInitialTrigger of its own
    fallback_actions=TriggerNextTaskFallbackActionsResponse(...)  # optional
)
```

- [TriggerNextTaskFallbackActionsResponse](TriggerNextTaskFallbackActionsResponse.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

