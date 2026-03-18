# UpdateTaskRequest

A request to update a Task
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **correlation_ids** | **List[str]** | Optional | A set of guid identifiers that allow correlation across the application tier |
| **fields** | [List[TaskInstanceField]](TaskInstanceField.md) | Optional | Defines the fields associated with the update |
| **stacking_key** | **str** | Optional | The key for the Stack that this Task should be added to |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.UpdateTaskRequest import UpdateTaskRequest

instance = UpdateTaskRequest(
    correlation_ids=,  # optional — A set of guid identifiers that allow correlation across the application tier
    fields=[],  # optional — Defines the fields associated with the update
    stacking_key="..."  # optional — The key for the Stack that this Task should be added to
)
```

- [TaskInstanceField](TaskInstanceField.md) — used in `fields`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

