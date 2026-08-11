# UpdateWorkflowRequest

Contains required info to update an existing Workflow
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **display_name** | **str** | Required | Human readable name |
| **description** | **str** | Optional | Human readable description |
| **root_task_definition_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **properties** | [Dict[str, PerpetualProperty]](PerpetualProperty.md) | Optional | The properties to set on the Workflow, keyed by property key. Optional. A null property value deletes the property. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.UpdateWorkflowRequest import UpdateWorkflowRequest

instance = UpdateWorkflowRequest(
    display_name="...",  # required — Human readable name
    description="...",  # optional — Human readable description
    root_task_definition_id=ResourceId(...),  # required
    properties=PerpetualProperty(...)  # optional — The properties to set on the Workflow, keyed by property key. Optional. A null property value deletes the property.
)
```

- [ResourceId](ResourceId.md)
- [PerpetualProperty](PerpetualProperty.md) — used in `properties`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

