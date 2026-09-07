# RecReviewSubmission

When the reviewer is allowed to submit their work for approval. Omit it to let them submit at any time.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **completion_ratio_threshold** | **float** | Required | The review completion ratio a result set has to reach before it can be submitted, between 0.0 and 1.0 inclusive. |
| **auto_submit** | **bool** | Optional | Whether the system submits on the reviewer&#39;s behalf as soon as the completion ratio threshold is met, rather than waiting to be asked. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RecReviewSubmission import RecReviewSubmission

instance = RecReviewSubmission(
    completion_ratio_threshold=0.0,  # required — The review completion ratio a result set has to reach before it can be submitted, between 0.0 and 1.0 inclusive.
    auto_submit=True  # optional — Whether the system submits on the reviewer&#39;s behalf as soon as the completion ratio threshold is met, rather than waiting to be asked.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

