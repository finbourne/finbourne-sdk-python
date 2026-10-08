# RecRequestedResultRevision

A result flagged for re-review as part of a Request Revisions decision.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **rec_result_id** | **str** | Required | The id of the result to flag for re-review, as carried on the result itself, e.g. &#39;break-3&#39;. Resolved within the run this result set is for. |
| **comment_text** | **str** | Optional | An optional per-result comment added to the result&#39;s user comments. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RecRequestedResultRevision import RecRequestedResultRevision

instance = RecRequestedResultRevision(
    rec_result_id="...",  # required — The id of the result to flag for re-review, as carried on the result itself, e.g. &#39;break-3&#39;. Resolved within the run this result set is for.
    comment_text="..."  # optional — An optional per-result comment added to the result&#39;s user comments.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

