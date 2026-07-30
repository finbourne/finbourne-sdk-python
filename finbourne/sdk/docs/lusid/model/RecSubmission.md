# RecSubmission

An entry in the append-only log of review submissions.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **user_id** | **str** | Required | The user who submitted the review. |
| **comment_text** | **str** | Optional | An optional comment from the submitter. |
| **as_at_submitted** | **datetime** | Required | The asAt datetime at which the submission was made. |
| **as_at_superseded** | **datetime** | Optional | The asAt datetime at which this entry was superseded. Null when it is the current standing entry. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RecSubmission import RecSubmission

instance = RecSubmission(
    user_id="...",  # required — The user who submitted the review.
    comment_text="...",  # optional — An optional comment from the submitter.
    as_at_submitted=datetime.now(),  # required — The asAt datetime at which the submission was made.
    as_at_superseded=datetime.now()  # optional — The asAt datetime at which this entry was superseded. Null when it is the current standing entry.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

