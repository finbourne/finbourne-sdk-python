# WorkflowRunResultsResponse

A run's status and the result values it published, which is what the Workflow AQS polls while it waits for an integration it started to finish.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **run_id** | **str** | Required | The run these results belong to, as returned by the execute endpoint. |
| **instance_id** | **str** | Required | The instance that ran. |
| **status** | **str** | Required | The run&#39;s status, reported exactly as the runs endpoint reports it: Queued, Started, Completed, Errored or Interrupted. A caller waiting for the run to finish is waiting for one of the last three. |
| **queued_at** | **datetime** | Optional | *No description available.* |
| **started_at** | **datetime** | Optional | *No description available.* |
| **completed_at** | **datetime** | Optional | Null until the run reaches a terminal status. |
| **attempt** | **int** | Required | Which attempt this run is, counting reruns of the same work. |
| **reports_to_workflow** | **bool** | Required | Whether this run was started by a Workflow task. False for a scheduled or file-triggered run, which publishes no results because nothing is waiting on them. |
| **results** | [List[WorkflowRunResultResponse]](WorkflowRunResultResponse.md) | Required | One entry per field the instance declares, so the shape matches what the discovery endpoint promised when the worker was created. A declared field the run never published carries a null value. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.WorkflowRunResultsResponse import WorkflowRunResultsResponse

instance = WorkflowRunResultsResponse(
    run_id="...",  # required — The run these results belong to, as returned by the execute endpoint.
    instance_id="...",  # required — The instance that ran.
    status="...",  # required — The run&#39;s status, reported exactly as the runs endpoint reports it: Queued, Started, Completed, Errored or Interrupted. A caller waiting for the run to finish is waiting for one of the last three.
    queued_at=datetime.now(),  # optional
    started_at=datetime.now(),  # optional
    completed_at=datetime.now(),  # optional — Null until the run reaches a terminal status.
    attempt=0,  # required — Which attempt this run is, counting reruns of the same work.
    reports_to_workflow=True,  # required — Whether this run was started by a Workflow task. False for a scheduled or file-triggered run, which publishes no results because nothing is waiting on them.
    results=[]  # required — One entry per field the instance declares, so the shape matches what the discovery endpoint promised when the worker was created. A declared field the run never published carries a null value.
)
```

- [WorkflowRunResultResponse](WorkflowRunResultResponse.md) — used in `results`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

