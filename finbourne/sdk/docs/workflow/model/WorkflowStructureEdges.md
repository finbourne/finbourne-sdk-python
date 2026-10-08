# WorkflowStructureEdges

The edges of a Workflow structure graph — the parent-child relationships between Task Definitions and the relationships between Launchers and the Task Definitions they start
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **child_task_definitions** | [List[ChildTaskDefinitionEdge]](ChildTaskDefinitionEdge.md) | Optional | The child Task Definition relationships |
| **launchers** | [List[LauncherEdge]](LauncherEdge.md) | Optional | The Launcher relationships. There is one entry per Launcher in nodes.launchers, in the same order |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.WorkflowStructureEdges import WorkflowStructureEdges

instance = WorkflowStructureEdges(
    child_task_definitions=[],  # optional — The child Task Definition relationships
    launchers=[]  # optional — The Launcher relationships. There is one entry per Launcher in nodes.launchers, in the same order
)
```


## Related Models

- [ChildTaskDefinitionEdge](ChildTaskDefinitionEdge.md) — used in `child_task_definitions`
- [LauncherEdge](LauncherEdge.md) — used in `launchers`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

