# CreateWorkflowRequest

Contains required info to create a new Workflow
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **display_name** | **str** | Required | Human readable name |
| **description** | **str** | Optional | Human readable description |
| **root_task_definition_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **properties** | [Dict[str, PerpetualProperty]](PerpetualProperty.md) | Optional | The properties to set on the Workflow, keyed by property key. Optional. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.CreateWorkflowRequest import CreateWorkflowRequest

instance = CreateWorkflowRequest(
    id=ResourceId(...),  # required
    display_name="...",  # required — Human readable name
    description="...",  # optional — Human readable description
    root_task_definition_id=ResourceId(...),  # required
    properties=PerpetualProperty(...)  # optional — The properties to set on the Workflow, keyed by property key. Optional.
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [PerpetualProperty](PerpetualProperty.md) — used in `properties`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

