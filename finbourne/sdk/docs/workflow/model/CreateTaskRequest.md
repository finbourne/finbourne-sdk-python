# CreateTaskRequest

Contains required info to create a new Task
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **task_definition_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **correlation_ids** | **List[str]** | Optional | A set of guid identifiers that allow correlation across the application tier |
| **fields** | [List[TaskInstanceField]](TaskInstanceField.md) | Optional | Fields and their initial values - should correspond with the Task Definition field schema |
| **stacking_key** | **str** | Optional | The key for the Stack that this Task should be added to |
| **workflow_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.CreateTaskRequest import CreateTaskRequest

instance = CreateTaskRequest(
    task_definition_id=ResourceId(...),  # optional
    correlation_ids=,  # optional — A set of guid identifiers that allow correlation across the application tier
    fields=[],  # optional — Fields and their initial values - should correspond with the Task Definition field schema
    stacking_key="...",  # optional — The key for the Stack that this Task should be added to
    workflow_id=ResourceId(...)  # optional
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [TaskInstanceField](TaskInstanceField.md) — used in `fields`
- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

