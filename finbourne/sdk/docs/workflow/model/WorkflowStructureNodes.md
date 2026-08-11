# WorkflowStructureNodes

The nodes of a Workflow structure graph — the Task Definitions involved
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **task_definitions** | [List[TaskDefinition]](TaskDefinition.md) | Optional | The Task Definitions that make up the nodes of this Workflow |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.WorkflowStructureNodes import WorkflowStructureNodes

instance = WorkflowStructureNodes(
    task_definitions=[]  # optional — The Task Definitions that make up the nodes of this Workflow
)
```


## Related Models

- [TaskDefinition](TaskDefinition.md) — used in `task_definitions`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

