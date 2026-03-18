# GroupReconciliationUserReviewComment

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **comment_text** | **str** | Required | User&#39;s comment regarding the reconciliation result. |
| **user_id** | **str** | Optional | Id of the user who made a User Review input. |
| **as_at_added** | **datetime** | Optional | The timestamp of the added User Review input. |
| **as_at_invalid** | **datetime** | Optional | The timestamp when User Review input became invalid e.g. because of the different attribute values within the new run. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.GroupReconciliationUserReviewComment import GroupReconciliationUserReviewComment

instance = GroupReconciliationUserReviewComment(
    comment_text="...",  # required — User&#39;s comment regarding the reconciliation result.
    user_id="...",  # optional — Id of the user who made a User Review input.
    as_at_added=datetime.now(),  # optional — The timestamp of the added User Review input.
    as_at_invalid=datetime.now()  # optional — The timestamp when User Review input became invalid e.g. because of the different attribute values within the new run.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

