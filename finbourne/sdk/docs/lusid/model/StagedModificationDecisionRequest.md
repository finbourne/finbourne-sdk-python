# StagedModificationDecisionRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **decision** | **str** | Required | The decision on the requested staged modification, can be &#39;Approve&#39; or &#39;Reject&#39;. |
| **comment** | **str** | Required | Comment on decision. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.StagedModificationDecisionRequest import StagedModificationDecisionRequest

instance = StagedModificationDecisionRequest(
    decision="...",  # required — The decision on the requested staged modification, can be &#39;Approve&#39; or &#39;Reject&#39;.
    comment="..."  # required — Comment on decision.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

