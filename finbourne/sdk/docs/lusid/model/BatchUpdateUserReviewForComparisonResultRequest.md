# BatchUpdateUserReviewForComparisonResultRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **comparison_result_id** | **str** | Required | Comparison result identifier, encoded value for core attribute results, aggregate attribute results, reconciliation type and run instanceId. |
| **user_review_add** | [GroupReconciliationUserReviewAdd](GroupReconciliationUserReviewAdd.md) | Optional | *No description available.* |
| **user_review_remove** | [GroupReconciliationUserReviewRemove](GroupReconciliationUserReviewRemove.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.BatchUpdateUserReviewForComparisonResultRequest import BatchUpdateUserReviewForComparisonResultRequest

instance = BatchUpdateUserReviewForComparisonResultRequest(
    comparison_result_id="...",  # required — Comparison result identifier, encoded value for core attribute results, aggregate attribute results, reconciliation type and run instanceId.
    user_review_add=GroupReconciliationUserReviewAdd(...),  # optional
    user_review_remove=GroupReconciliationUserReviewRemove(...)  # optional
)
```

- [GroupReconciliationUserReviewAdd](GroupReconciliationUserReviewAdd.md)
- [GroupReconciliationUserReviewRemove](GroupReconciliationUserReviewRemove.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

