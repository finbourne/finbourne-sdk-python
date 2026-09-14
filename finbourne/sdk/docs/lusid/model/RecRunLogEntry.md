# RecRunLogEntry

A summary of a single run of a single rec type within an instance's run log, carrying the per-run outcome  detail the grouped-by-instance overview renders. Every entry comes off a result set, so only a run that has  completed or failed appears: a run still in flight is not logged until it lands.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **run_number** | **int** | Required | The run number within the instance. Increments with each re-run. |
| **run_as_at** | **datetime** | Required | The asAt datetime at which the run happened. |
| **superseded_as_at** | **datetime** | Optional | The asAt datetime at which this run was superseded by a subsequent run. |
| **dates_reconciled** | [RecDatesReconciled](RecDatesReconciled.md) | Required | *No description available.* |
| **execution** | [RecExecution](RecExecution.md) | Required | *No description available.* |
| **approval_status** | **str** | Required | The position of this result set in the approval ceremony. Available values: UnderReview, PendingApproval, RevisionsRequested, Approved, NotApplicable. |
| **result_counts** | [RecResultCounts](RecResultCounts.md) | Optional | *No description available.* |
| **review** | [RecReview](RecReview.md) | Optional | *No description available.* |
| **rec_result_set_href** | **str** | Required | The specific Uniform Resource Identifier (URI) of the full rec result set this run belongs to. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RecRunLogEntry import RecRunLogEntry

instance = RecRunLogEntry(
    run_number=0,  # required — The run number within the instance. Increments with each re-run.
    run_as_at=datetime.now(),  # required — The asAt datetime at which the run happened.
    superseded_as_at=datetime.now(),  # optional — The asAt datetime at which this run was superseded by a subsequent run.
    dates_reconciled=RecDatesReconciled(...),  # required
    execution=RecExecution(...),  # required
    approval_status="...",  # required — The position of this result set in the approval ceremony. Available values: UnderReview, PendingApproval, RevisionsRequested, Approved, NotApplicable.
    result_counts=RecResultCounts(...),  # optional
    review=RecReview(...),  # optional
    rec_result_set_href="..."  # required — The specific Uniform Resource Identifier (URI) of the full rec result set this run belongs to.
)
```

- [RecDatesReconciled](RecDatesReconciled.md)
- [RecExecution](RecExecution.md)
- [RecResultCounts](RecResultCounts.md)
- [RecReview](RecReview.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

