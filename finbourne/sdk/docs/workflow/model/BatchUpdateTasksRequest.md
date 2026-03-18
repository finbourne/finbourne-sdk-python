# BatchUpdateTasksRequest

A request to update multiple Tasks
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **update_tasks** | [List[UpdateTaskWithIdAndTriggerRequest]](UpdateTaskWithIdAndTriggerRequest.md) | Optional | A Dictionary of task IDs to UpdateTaskRequest |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.BatchUpdateTasksRequest import BatchUpdateTasksRequest

instance = BatchUpdateTasksRequest(
    update_tasks=[]  # optional — A Dictionary of task IDs to UpdateTaskRequest
)
```


## Related Models

- [UpdateTaskWithIdAndTriggerRequest](UpdateTaskWithIdAndTriggerRequest.md) — used in `update_tasks`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

