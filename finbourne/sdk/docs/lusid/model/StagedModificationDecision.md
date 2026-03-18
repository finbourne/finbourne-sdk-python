# StagedModificationDecision

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **as_at** | **datetime** | Optional | Time the decision request is made. |
| **user_id** | **str** | Optional | ID of user that approved the request. |
| **request_id** | **str** | Optional | ID of user that made the request. |
| **decision** | **str** | Optional | The decision on the requested staged modification, can be &#39;Approve&#39; or &#39;Reject&#39;. |
| **comment** | **str** | Optional | Comment on decision. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.StagedModificationDecision import StagedModificationDecision

instance = StagedModificationDecision(
    as_at=datetime.now(),  # optional — Time the decision request is made.
    user_id="...",  # optional — ID of user that approved the request.
    request_id="...",  # optional — ID of user that made the request.
    decision="...",  # optional — The decision on the requested staged modification, can be &#39;Approve&#39; or &#39;Reject&#39;.
    comment="..."  # optional — Comment on decision.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

