# RecWorkflowTask

The workflow service task that instantiated a rec instance.  Minimal placeholder until the full workflow service task DTO is available.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | **str** | Optional | The identifier of the workflow service task. |
| **task_definition_id** | [../model/ResourceId](ResourceId.md) | Optional | *No description available.* |
| **state** | **str** | Optional | The current state of the workflow service task. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RecWorkflowTask import RecWorkflowTask

instance = RecWorkflowTask(
    id="...",  # optional — The identifier of the workflow service task.
    task_definition_id=ResourceId(...),  # optional
    state="..."  # optional — The current state of the workflow service task.
)
```

- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

