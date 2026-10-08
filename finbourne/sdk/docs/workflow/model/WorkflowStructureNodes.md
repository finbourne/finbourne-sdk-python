# WorkflowStructureNodes

The nodes of a Workflow structure graph — the Task Definitions and the Launchers involved
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **task_definitions** | [List[TaskDefinition]](TaskDefinition.md) | Optional | The Task Definitions that make up the nodes of this Workflow |
| **launchers** | [List[LauncherResponse]](LauncherResponse.md) | Optional | The Launchers of this Workflow, as full Launcher objects. At most the first 10 by launcher id are returned, in the same order as ListLaunchers gives by default. Inactive Launchers are included. When the Workflow has more, launchersTruncated is true and ListLaunchers returns the full set |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.WorkflowStructureNodes import WorkflowStructureNodes

instance = WorkflowStructureNodes(
    task_definitions=[],  # optional — The Task Definitions that make up the nodes of this Workflow
    launchers=[]  # optional — The Launchers of this Workflow, as full Launcher objects. At most the first 10 by launcher id are returned, in the same order as ListLaunchers gives by default. Inactive Launchers are included. When the Workflow has more, launchersTruncated is true and ListLaunchers returns the full set
)
```


## Related Models

- [TaskDefinition](TaskDefinition.md) — used in `task_definitions`
- [LauncherResponse](LauncherResponse.md) — used in `launchers`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

