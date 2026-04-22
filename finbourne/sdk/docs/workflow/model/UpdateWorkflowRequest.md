# UpdateWorkflowRequest

Contains required info to update an existing Workflow
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **display_name** | **str** | Required | Human readable name |
| **description** | **str** | Optional | Human readable description |
| **root_task_definition_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.UpdateWorkflowRequest import UpdateWorkflowRequest

instance = UpdateWorkflowRequest(
    display_name="...",  # required — Human readable name
    description="...",  # optional — Human readable description
    root_task_definition_id=ResourceId(...)  # required
)
```

- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

