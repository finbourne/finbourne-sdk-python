# WorkflowStructure

Describes the structure of a Workflow as a graph of its Task Definitions and its Launchers
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **nodes** | [WorkflowStructureNodes](WorkflowStructureNodes.md) | Optional | *No description available.* |
| **edges** | [WorkflowStructureEdges](WorkflowStructureEdges.md) | Optional | *No description available.* |
| **launchers_truncated** | **bool** | Optional | True when the Workflow has more Launchers than were returned inline in nodes.launchers. Call ListLaunchers for the full set |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.WorkflowStructure import WorkflowStructure

instance = WorkflowStructure(
    nodes=WorkflowStructureNodes(...),  # optional
    edges=WorkflowStructureEdges(...),  # optional
    launchers_truncated=True  # optional — True when the Workflow has more Launchers than were returned inline in nodes.launchers. Call ListLaunchers for the full set
)
```


## Related Models

- [WorkflowStructureNodes](WorkflowStructureNodes.md)
- [WorkflowStructureEdges](WorkflowStructureEdges.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

