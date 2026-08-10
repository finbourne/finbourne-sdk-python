# RecInstanceSummary

A lightweight view of the rec instance, nested on each result set. It carries the instance-level  status, which is how a result set surfaces the instance's running/locked state to the dashboard.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [../model/RecInstanceId](RecInstanceId.md) | Required | *No description available.* |
| **rec_definition_id** | [../model/ResourceId](ResourceId.md) | Required | *No description available.* |
| **as_at_instantiated** | **datetime** | Required | The asAt datetime at which the instance was first created. |
| **workflow_task_instantiated** | [../model/RecWorkflowTask](RecWorkflowTask.md) | Optional | *No description available.* |
| **status** | **str** | Required | The instance-level lifecycle rollup. Available values: Running, Failures, ReviewAndApproval, AllApproved, Locked. |
| **as_at_locked** | **datetime** | Optional | The wall-clock time the lock action was performed. Null when the instance has not been locked. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RecInstanceSummary import RecInstanceSummary

instance = RecInstanceSummary(
    id=RecInstanceId(...),  # required
    rec_definition_id=ResourceId(...),  # required
    as_at_instantiated=datetime.now(),  # required — The asAt datetime at which the instance was first created.
    workflow_task_instantiated=RecWorkflowTask(...),  # optional
    status="...",  # required — The instance-level lifecycle rollup. Available values: Running, Failures, ReviewAndApproval, AllApproved, Locked.
    as_at_locked=datetime.now()  # optional — The wall-clock time the lock action was performed. Null when the instance has not been locked.
)
```


## Related Models

- [RecInstanceId](RecInstanceId.md)
- [ResourceId](ResourceId.md)
- [RecWorkflowTask](RecWorkflowTask.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

