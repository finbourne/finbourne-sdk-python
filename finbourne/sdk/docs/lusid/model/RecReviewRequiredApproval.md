# RecReviewRequiredApproval

One approval a submitted review has to collect, and who may give it. All of a configuration's approvals are  required, they may be given in any order, and no user may give more than one of them.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **approval_code** | **str** | Required | The client-defined identifier for the approval, e.g. \&quot;Desk\&quot; or \&quot;Risk\&quot;. Each may appear at most once. |
| **description** | **str** | Optional | A human-readable label for the approval. |
| **deciding_user** | **str** | Optional | A boolean expression over the user attempting the approval, which has to hold for them to give it. They must also hold the entitlement for the decide action. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RecReviewRequiredApproval import RecReviewRequiredApproval

instance = RecReviewRequiredApproval(
    approval_code="...",  # required — The client-defined identifier for the approval, e.g. \&quot;Desk\&quot; or \&quot;Risk\&quot;. Each may appear at most once.
    description="...",  # optional — A human-readable label for the approval.
    deciding_user="..."  # optional — A boolean expression over the user attempting the approval, which has to hold for them to give it. They must also hold the entitlement for the decide action.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

