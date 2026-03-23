# PostProcessTask

Request defining a post-processing task for an instance.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **action** | **str** | Required | The type of action to perform (Allowed: RunIntegration, RunWorkflow, TriggerEmail) |
| **target_instance** | **str** | Optional | The instance identifier to trigger (for TriggerIntegration action). |
| **trigger_on** | **str** | Required | When the task should be triggered (Allowed: OnSuccess, OnFailure, Always) |
| **parameters** | **object** | Optional | JSON parameters specific to the action type. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.PostProcessTask import PostProcessTask

instance = PostProcessTask(
    action="...",  # required — The type of action to perform (Allowed: RunIntegration, RunWorkflow, TriggerEmail)
    target_instance="...",  # optional — The instance identifier to trigger (for TriggerIntegration action).
    trigger_on="...",  # required — When the task should be triggered (Allowed: OnSuccess, OnFailure, Always)
    parameters=  # optional — JSON parameters specific to the action type.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

