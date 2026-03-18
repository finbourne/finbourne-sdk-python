# UpdateTaskWithIdAndTriggerRequest

A request to update multiple Tasks Includes a trigger which is supplied from route in single update request
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **task_instance_id** | **str** | Optional | The ID of the task instance |
| **correlation_ids** | **List[str]** | Optional | A set of guid identifiers that allow correlation across the application tier |
| **fields** | [List[TaskInstanceField]](TaskInstanceField.md) | Optional | Defines the fields associated with the update |
| **stacking_key** | **str** | Optional | The key for the Stack that this Task should be added to |
| **trigger_name** | **str** | Optional | The trigger we want to update the task with |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.UpdateTaskWithIdAndTriggerRequest import UpdateTaskWithIdAndTriggerRequest

instance = UpdateTaskWithIdAndTriggerRequest(
    task_instance_id="...",  # optional — The ID of the task instance
    correlation_ids=,  # optional — A set of guid identifiers that allow correlation across the application tier
    fields=[],  # optional — Defines the fields associated with the update
    stacking_key="...",  # optional — The key for the Stack that this Task should be added to
    trigger_name="..."  # optional — The trigger we want to update the task with
)
```

- [TaskInstanceField](TaskInstanceField.md) — used in `fields`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

