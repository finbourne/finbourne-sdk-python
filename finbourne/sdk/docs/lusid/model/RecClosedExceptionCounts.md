# RecClosedExceptionCounts

Counts for results that are exceptions with a Closed status.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **total** | **int** | Required | The total number of results in this category. |
| **by_closure_type** | [../model/RecExceptionCountByClosureType](RecExceptionCountByClosureType.md) | Required | *No description available.* |
| **by_review_status** | [../model/RecResultCountByReviewStatus](RecResultCountByReviewStatus.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RecClosedExceptionCounts import RecClosedExceptionCounts

instance = RecClosedExceptionCounts(
    total=0,  # required — The total number of results in this category.
    by_closure_type=RecExceptionCountByClosureType(...),  # required
    by_review_status=RecResultCountByReviewStatus(...)  # required
)
```

- [RecExceptionCountByClosureType](RecExceptionCountByClosureType.md)
- [RecResultCountByReviewStatus](RecResultCountByReviewStatus.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

