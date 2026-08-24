# RecReview

A summary of the per-result review state across the result set.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **count_reviewed** | **int** | Required | The number of results with review status Reviewed. |
| **count_required** | **int** | Required | The number of results with review status Required. |
| **count_not_required** | **int** | Required | The number of results with review status Not Required. |
| **completion_ratio** | **float** | Optional | Reviewed / (Reviewed + Required). Is 1.0 when the denominator is zero, and null when execution failed. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RecReview import RecReview

instance = RecReview(
    count_reviewed=0,  # required — The number of results with review status Reviewed.
    count_required=0,  # required — The number of results with review status Required.
    count_not_required=0,  # required — The number of results with review status Not Required.
    completion_ratio=0.0  # optional — Reviewed / (Reviewed + Required). Is 1.0 when the denominator is zero, and null when execution failed.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

