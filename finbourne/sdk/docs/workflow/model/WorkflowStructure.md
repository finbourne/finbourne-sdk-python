# WorkflowStructure

Describes the structure of a Workflow as a graph of Task Definitions
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **nodes** | [WorkflowStructureNodes](WorkflowStructureNodes.md) | Optional | *No description available.* |
| **edges** | [WorkflowStructureEdges](WorkflowStructureEdges.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.WorkflowStructure import WorkflowStructure

instance = WorkflowStructure(
    nodes=WorkflowStructureNodes(...),  # optional
    edges=WorkflowStructureEdges(...)  # optional
)
```


## Related Models

- [WorkflowStructureNodes](WorkflowStructureNodes.md)
- [WorkflowStructureEdges](WorkflowStructureEdges.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

