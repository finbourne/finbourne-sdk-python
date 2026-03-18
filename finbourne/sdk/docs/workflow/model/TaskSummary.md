# TaskSummary

Summary of a Task created based on a Task Definition
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | **UUID** | Required | The unique id for this Task |
| **task_definition_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **task_definition_version** | [TaskDefinitionVersion](TaskDefinitionVersion.md) | Required | *No description available.* |
| **task_definition_display_name** | **str** | Required | The display name of the Task Definition used by this Task |
| **state** | **str** | Required | Current State |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.TaskSummary import TaskSummary

instance = TaskSummary(
    id="...",  # required — The unique id for this Task
    task_definition_id=ResourceId(...),  # required
    task_definition_version=TaskDefinitionVersion(...),  # required
    task_definition_display_name="...",  # required — The display name of the Task Definition used by this Task
    state="..."  # required — Current State
)
```

- [ResourceId](ResourceId.md)
- [TaskDefinitionVersion](TaskDefinitionVersion.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

