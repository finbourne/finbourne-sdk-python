# TransitionTriggerDefinition

State changes happen in response to Triggers
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **name** | **str** | Required | The key/Name of this Trigger |
| **trigger** | [TriggerSchema](TriggerSchema.md) | Required | *No description available.* |
| **display_name** | **str** | Optional | Display name for trigger |
| **description** | **str** | Optional | Description of trigger |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.TransitionTriggerDefinition import TransitionTriggerDefinition

instance = TransitionTriggerDefinition(
    name="...",  # required — The key/Name of this Trigger
    trigger=TriggerSchema(...),  # required
    display_name="...",  # optional — Display name for trigger
    description="..."  # optional — Description of trigger
)
```

- [TriggerSchema](TriggerSchema.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

