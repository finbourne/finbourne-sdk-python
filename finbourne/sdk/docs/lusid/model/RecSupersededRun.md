# RecSupersededRun

A prior run snapshot, frozen at the point of re-run. Has the same shape as the root-level run  fields on the result set, plus the asAt at which the run was superseded.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **run_number** | **int** | Required | The run number within the instance. Increments with each re-run. |
| **run_as_at** | **datetime** | Required | The asAt datetime at which the run happened. |
| **superseded_as_at** | **datetime** | Required | The asAt datetime at which this run was superseded by a subsequent run. |
| **execution** | [../model/RecExecution](RecExecution.md) | Required | *No description available.* |
| **dates_reconciled** | [../model/RecDatesReconciled](RecDatesReconciled.md) | Required | *No description available.* |
| **result_counts** | [../model/RecResultCounts](RecResultCounts.md) | Required | *No description available.* |
| **review** | [../model/RecReview](RecReview.md) | Required | *No description available.* |
| **approval_status** | **str** | Required | The position of this result set in the approval ceremony. Available values: UnderReview, PendingApproval, RevisionsRequested, Approved, NotApplicable. |
| **required_approvals** | [../model/List[RecRequiredApproval]](RecRequiredApproval.md) | Required | The approval slots required for this result set, passed through from the rec definition&#39;s review configuration. May be empty. |
| **submissions** | [../model/List[RecSubmission]](RecSubmission.md) | Required | An append-only log of review submissions. May be empty. |
| **decisions** | [../model/List[RecApprovalDecision]](RecApprovalDecision.md) | Required | An append-only log of approver decisions. May be empty. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RecSupersededRun import RecSupersededRun

instance = RecSupersededRun(
    run_number=0,  # required — The run number within the instance. Increments with each re-run.
    run_as_at=datetime.now(),  # required — The asAt datetime at which the run happened.
    superseded_as_at=datetime.now(),  # required — The asAt datetime at which this run was superseded by a subsequent run.
    execution=RecExecution(...),  # required
    dates_reconciled=RecDatesReconciled(...),  # required
    result_counts=RecResultCounts(...),  # required
    review=RecReview(...),  # required
    approval_status="...",  # required — The position of this result set in the approval ceremony. Available values: UnderReview, PendingApproval, RevisionsRequested, Approved, NotApplicable.
    required_approvals=[],  # required — The approval slots required for this result set, passed through from the rec definition&#39;s review configuration. May be empty.
    submissions=[],  # required — An append-only log of review submissions. May be empty.
    decisions=[]  # required — An append-only log of approver decisions. May be empty.
)
```

- [RecExecution](RecExecution.md)
- [RecDatesReconciled](RecDatesReconciled.md)
- [RecResultCounts](RecResultCounts.md)
- [RecReview](RecReview.md)
- [RecRequiredApproval](RecRequiredApproval.md) — used in `required_approvals`
- [RecSubmission](RecSubmission.md) — used in `submissions`
- [RecApprovalDecision](RecApprovalDecision.md) — used in `decisions`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

