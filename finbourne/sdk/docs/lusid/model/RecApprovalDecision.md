# RecApprovalDecision

An entry in the append-only log of approver decisions.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **approval_code** | **str** | Required | The approval slot this decision satisfies. Must match a required approval code. |
| **decision** | **str** | Required | The decision made. Available values: Approve, RequestRevisions. |
| **reason** | **str** | Optional | Rationale for the decision. |
| **user_id** | **str** | Required | The approver who made the decision. |
| **as_at_decided** | **datetime** | Required | The asAt datetime at which the decision was made. |
| **as_at_superseded** | **datetime** | Optional | The asAt datetime at which this entry was superseded. Null when it is the current standing entry. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RecApprovalDecision import RecApprovalDecision

instance = RecApprovalDecision(
    approval_code="...",  # required — The approval slot this decision satisfies. Must match a required approval code.
    decision="...",  # required — The decision made. Available values: Approve, RequestRevisions.
    reason="...",  # optional — Rationale for the decision.
    user_id="...",  # required — The approver who made the decision.
    as_at_decided=datetime.now(),  # required — The asAt datetime at which the decision was made.
    as_at_superseded=datetime.now()  # optional — The asAt datetime at which this entry was superseded. Null when it is the current standing entry.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

