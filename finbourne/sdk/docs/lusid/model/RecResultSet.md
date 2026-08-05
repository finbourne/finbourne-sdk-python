# RecResultSet

The collection of reconciliation results for a given rec type within a rec instance. Identified by  its rec type and instance. The latest run's data is promoted to the root; prior runs are available  via previousRuns.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **rec_type** | **str** | Required | The type of rec that this result set belongs to (e.g. Holding). Together with the rec instance, this uniquely identifies the result set. Available values: Holding, CashHolding, Valuation, InputTransaction, OutputTransaction, SettlementActivity. |
| **rec_instance** | [RecInstanceSummary](RecInstanceSummary.md) | Required | *No description available.* |
| **run_number** | **int** | Required | The run number within the instance. Increments with each re-run. |
| **run_as_at** | **datetime** | Required | The asAt datetime at which the run happened. |
| **execution** | [RecExecution](RecExecution.md) | Required | *No description available.* |
| **dates_reconciled** | [RecDatesReconciled](RecDatesReconciled.md) | Required | *No description available.* |
| **result_counts** | [RecResultCounts](RecResultCounts.md) | Required | *No description available.* |
| **review** | [RecReview](RecReview.md) | Required | *No description available.* |
| **approval_status** | **str** | Required | The position of this result set in the approval ceremony. Available values: UnderReview, PendingApproval, RevisionsRequested, Approved, NotApplicable. |
| **required_approvals** | [List[RecRequiredApproval]](RecRequiredApproval.md) | Required | The approval slots required for this result set, passed through from the rec definition&#39;s review configuration. May be empty. |
| **submissions** | [List[RecSubmission]](RecSubmission.md) | Required | An append-only log of review submissions. May be empty. |
| **decisions** | [List[RecApprovalDecision]](RecApprovalDecision.md) | Required | An append-only log of approver decisions. May be empty. |
| **previous_runs** | [List[RecSupersededRun]](RecSupersededRun.md) | Required | Prior run snapshots, each frozen at the point of re-run. Populated only when includePreviousRuns is true. |
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RecResultSet import RecResultSet

instance = RecResultSet(
    rec_type="...",  # required — The type of rec that this result set belongs to (e.g. Holding). Together with the rec instance, this uniquely identifies the result set. Available values: Holding, CashHolding, Valuation, InputTransaction, OutputTransaction, SettlementActivity.
    rec_instance=RecInstanceSummary(...),  # required
    run_number=0,  # required — The run number within the instance. Increments with each re-run.
    run_as_at=datetime.now(),  # required — The asAt datetime at which the run happened.
    execution=RecExecution(...),  # required
    dates_reconciled=RecDatesReconciled(...),  # required
    result_counts=RecResultCounts(...),  # required
    review=RecReview(...),  # required
    approval_status="...",  # required — The position of this result set in the approval ceremony. Available values: UnderReview, PendingApproval, RevisionsRequested, Approved, NotApplicable.
    required_approvals=[],  # required — The approval slots required for this result set, passed through from the rec definition&#39;s review configuration. May be empty.
    submissions=[],  # required — An append-only log of review submissions. May be empty.
    decisions=[],  # required — An append-only log of approver decisions. May be empty.
    previous_runs=[],  # required — Prior run snapshots, each frozen at the point of re-run. Populated only when includePreviousRuns is true.
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    version=Version(...),  # optional
    links=[]  # optional
)
```

- [RecInstanceSummary](RecInstanceSummary.md)
- [RecExecution](RecExecution.md)
- [RecDatesReconciled](RecDatesReconciled.md)
- [RecResultCounts](RecResultCounts.md)
- [RecReview](RecReview.md)
- [RecRequiredApproval](RecRequiredApproval.md) — used in `required_approvals`
- [RecSubmission](RecSubmission.md) — used in `submissions`
- [RecApprovalDecision](RecApprovalDecision.md) — used in `decisions`
- [RecSupersededRun](RecSupersededRun.md) — used in `previous_runs`
- [Version](Version.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

