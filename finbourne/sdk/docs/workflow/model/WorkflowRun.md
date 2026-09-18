# WorkflowRun

Information about the run of the Workflow that created this Task, inherited from the root/ultimate parent Task.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | **int** | Required | The id of this run of the Workflow. Assigned once, when the run is instantiated. |
| **as_at_created** | **datetime** | Required | The version.asAtCreated of the root/ultimate parent Task of this run. |
| **completion_status** | **str** | Required | The completion status of the root/ultimate parent Task of this run: NotStarted, InProgress, or Completed. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.WorkflowRun import WorkflowRun

instance = WorkflowRun(
    id=0,  # required — The id of this run of the Workflow. Assigned once, when the run is instantiated.
    as_at_created=datetime.now(),  # required — The version.asAtCreated of the root/ultimate parent Task of this run.
    completion_status="..."  # required — The completion status of the root/ultimate parent Task of this run: NotStarted, InProgress, or Completed.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

