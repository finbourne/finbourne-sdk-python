# RecOpenExceptionCounts

Counts for results that are exceptions with an Open status.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **total** | **int** | Required | The total number of results in this category. |
| **by_result_type** | [../model/RecExceptionCountByResultType](RecExceptionCountByResultType.md) | Required | *No description available.* |
| **by_review_status** | [../model/RecResultCountByReviewStatus](RecResultCountByReviewStatus.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RecOpenExceptionCounts import RecOpenExceptionCounts

instance = RecOpenExceptionCounts(
    total=0,  # required — The total number of results in this category.
    by_result_type=RecExceptionCountByResultType(...),  # required
    by_review_status=RecResultCountByReviewStatus(...)  # required
)
```

- [RecExceptionCountByResultType](RecExceptionCountByResultType.md)
- [RecResultCountByReviewStatus](RecResultCountByReviewStatus.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

