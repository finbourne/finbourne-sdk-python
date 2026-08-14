# RecUserComment

A user-authored comment attached to a rec result. Carried forward with the result across runs.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **comment_id** | **str** | Required | System-generated GUID identifying the comment. Set once on creation. |
| **comment_text** | **str** | Required | The body of the comment. |
| **user_id** | **str** | Required | The author of the comment. |
| **as_at_created** | **datetime** | Required | The asAt time the comment was created. Set once. |
| **as_at_modified** | **datetime** | Required | The asAt time the comment was last modified. Equals asAtCreated until the first edit. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RecUserComment import RecUserComment

instance = RecUserComment(
    comment_id="...",  # required — System-generated GUID identifying the comment. Set once on creation.
    comment_text="...",  # required — The body of the comment.
    user_id="...",  # required — The author of the comment.
    as_at_created=datetime.now(),  # required — The asAt time the comment was created. Set once.
    as_at_modified=datetime.now()  # required — The asAt time the comment was last modified. Equals asAtCreated until the first edit.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

