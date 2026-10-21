# TriggerNextTaskAction

Defines a Trigger Next Task Action
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **type** | **str** | Required | Type name for this Action |
| **default_trigger** | **str** | Optional | Trigger sent to the next task when this task has no nextTaskInitialTrigger of its own |
| **fallback_actions** | [TriggerNextTaskFallbackActions](TriggerNextTaskFallbackActions.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.TriggerNextTaskAction import TriggerNextTaskAction

instance = TriggerNextTaskAction(
    type="...",  # required — Type name for this Action
    default_trigger="...",  # optional — Trigger sent to the next task when this task has no nextTaskInitialTrigger of its own
    fallback_actions=TriggerNextTaskFallbackActions(...)  # optional
)
```

- [TriggerNextTaskFallbackActions](TriggerNextTaskFallbackActions.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

