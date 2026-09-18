# WorkflowResponse

A Workflow
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **version** | [VersionInfo](VersionInfo.md) | Optional | *No description available.* |
| **display_name** | **str** | Required | Human readable name |
| **description** | **str** | Optional | Human readable description |
| **root_task_definition_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **workflow_structure** | [WorkflowStructure](WorkflowStructure.md) | Required | *No description available.* |
| **run_count** | **int** | Required | The number of times this Workflow has been run. Starts at 0 and increments by 1 each time a new run is instantiated. |
| **properties** | [Dict[str, PerpetualProperty]](PerpetualProperty.md) | Optional | The properties of the Workflow, keyed by property key. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.WorkflowResponse import WorkflowResponse

instance = WorkflowResponse(
    id=ResourceId(...),  # required
    version=VersionInfo(...),  # optional
    display_name="...",  # required — Human readable name
    description="...",  # optional — Human readable description
    root_task_definition_id=ResourceId(...),  # required
    workflow_structure=WorkflowStructure(...),  # required
    run_count=0,  # required — The number of times this Workflow has been run. Starts at 0 and increments by 1 each time a new run is instantiated.
    properties=PerpetualProperty(...)  # optional — The properties of the Workflow, keyed by property key.
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [VersionInfo](VersionInfo.md)
- [ResourceId](ResourceId.md)
- [WorkflowStructure](WorkflowStructure.md)
- [PerpetualProperty](PerpetualProperty.md) — used in `properties`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

