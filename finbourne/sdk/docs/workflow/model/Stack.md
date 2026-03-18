# Stack

Information pertaining to the Tasks Stack if one is present
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **member_added_as_at** | **datetime** | Optional | When the Task was added to the Stack |
| **stack_opened_as_at** | **datetime** | Optional | When the Stack was opened |
| **stack_closed_as_at** | **datetime** | Optional | When the Stack was closed |
| **stack_membership_type** | **str** | Optional | Whether the task is the Lead task of the Stack or a Member within the Stack |
| **stack_status** | **str** | Optional | Status of the Stack (Open/Closed) |
| **lead_task_id** | **UUID** | Optional | ID of the Lead Task |
| **lead_task_state** | **str** | Optional | State of the Lead Task |
| **tasks_in_stack** | **int** | Optional | Number of Tasks in the Stack |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.Stack import Stack

instance = Stack(
    member_added_as_at=datetime.now(),  # optional — When the Task was added to the Stack
    stack_opened_as_at=datetime.now(),  # optional — When the Stack was opened
    stack_closed_as_at=datetime.now(),  # optional — When the Stack was closed
    stack_membership_type="...",  # optional — Whether the task is the Lead task of the Stack or a Member within the Stack
    stack_status="...",  # optional — Status of the Stack (Open/Closed)
    lead_task_id="...",  # optional — ID of the Lead Task
    lead_task_state="...",  # optional — State of the Lead Task
    tasks_in_stack=0  # optional — Number of Tasks in the Stack
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

