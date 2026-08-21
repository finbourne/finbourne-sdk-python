# WorkflowResultFieldsResponse

The result fields an instance returns to the Workflow task that started its run.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **instance_id** | **str** | Required | The instance these fields belong to. |
| **reports_to_workflow** | **bool** | Required | Whether this instance has an enabled RunWorkflow post-process task at all. |
| **result_fields** | [List[WorkflowResultFieldResponse]](WorkflowResultFieldResponse.md) | Required | Every distinct field declared across this instance&#39;s RunWorkflow tasks. |
| **tasks** | [List[WorkflowResultFieldsTaskResponse]](WorkflowResultFieldsTaskResponse.md) | Required | Per-task breakdown: an instance may declare different fields on success and on failure. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.WorkflowResultFieldsResponse import WorkflowResultFieldsResponse

instance = WorkflowResultFieldsResponse(
    instance_id="...",  # required — The instance these fields belong to.
    reports_to_workflow=True,  # required — Whether this instance has an enabled RunWorkflow post-process task at all.
    result_fields=[],  # required — Every distinct field declared across this instance&#39;s RunWorkflow tasks.
    tasks=[]  # required — Per-task breakdown: an instance may declare different fields on success and on failure.
)
```

- [WorkflowResultFieldResponse](WorkflowResultFieldResponse.md) — used in `result_fields`
- [WorkflowResultFieldsTaskResponse](WorkflowResultFieldsTaskResponse.md) — used in `tasks`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

