# RecMatchCounts

Counts for non-exception results (Match, Cross).
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **total** | **int** | Required | The total number of results in this category. |
| **by_result_type** | [RecMatchCountByResultType](RecMatchCountByResultType.md) | Required | *No description available.* |
| **by_review_status** | [RecResultCountByReviewStatus](RecResultCountByReviewStatus.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RecMatchCounts import RecMatchCounts

instance = RecMatchCounts(
    total=0,  # required — The total number of results in this category.
    by_result_type=RecMatchCountByResultType(...),  # required
    by_review_status=RecResultCountByReviewStatus(...)  # required
)
```

- [RecMatchCountByResultType](RecMatchCountByResultType.md)
- [RecResultCountByReviewStatus](RecResultCountByReviewStatus.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

