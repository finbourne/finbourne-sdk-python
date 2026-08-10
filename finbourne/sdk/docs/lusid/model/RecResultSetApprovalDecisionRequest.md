# RecResultSetApprovalDecisionRequest

The request for an approver to approve a submitted review or request revisions. Each call satisfies  (or rejects) one approval slot from the result set's required approvals.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **approval_code** | **str** | Required | The approval slot being decided. Must match a required approval code. |
| **decision** | **str** | Required | The decision made. Available values: Approve, RequestRevisions. |
| **reason** | **str** | Optional | Rationale for the decision. |
| **requested_result_revisions** | [../model/List[RecRequestedResultRevision]](RecRequestedResultRevision.md) | Optional | The results flagged for re-review. Only applicable when the decision is Request Revisions. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RecResultSetApprovalDecisionRequest import RecResultSetApprovalDecisionRequest

instance = RecResultSetApprovalDecisionRequest(
    approval_code="...",  # required — The approval slot being decided. Must match a required approval code.
    decision="...",  # required — The decision made. Available values: Approve, RequestRevisions.
    reason="...",  # optional — Rationale for the decision.
    requested_result_revisions=[]  # optional — The results flagged for re-review. Only applicable when the decision is Request Revisions.
)
```

- [RecRequestedResultRevision](RecRequestedResultRevision.md) — used in `requested_result_revisions`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

