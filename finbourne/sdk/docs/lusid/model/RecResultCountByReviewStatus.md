# RecResultCountByReviewStatus

Result counts broken down by review status.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **required** | **int** | Required | The number of results with review status Required. |
| **not_required** | **int** | Required | The number of results with review status Not Required. |
| **reviewed** | **int** | Required | The number of results with review status Reviewed. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RecResultCountByReviewStatus import RecResultCountByReviewStatus

instance = RecResultCountByReviewStatus(
    required=0,  # required — The number of results with review status Required.
    not_required=0,  # required — The number of results with review status Not Required.
    reviewed=0  # required — The number of results with review status Reviewed.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

