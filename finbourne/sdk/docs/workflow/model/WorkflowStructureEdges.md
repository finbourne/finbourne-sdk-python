# WorkflowStructureEdges

The edges of a Workflow structure graph — the parent-child relationships between Task Definitions
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **child_task_definitions** | [List[ChildTaskDefinitionEdge]](ChildTaskDefinitionEdge.md) | Optional | The child Task Definition relationships |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.WorkflowStructureEdges import WorkflowStructureEdges

instance = WorkflowStructureEdges(
    child_task_definitions=[]  # optional — The child Task Definition relationships
)
```


## Related Models

- [ChildTaskDefinitionEdge](ChildTaskDefinitionEdge.md) — used in `child_task_definitions`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

