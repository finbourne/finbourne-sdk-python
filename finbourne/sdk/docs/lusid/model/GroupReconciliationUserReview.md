# GroupReconciliationUserReview

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **break_codes** | [List[GroupReconciliationUserReviewBreakCode]](GroupReconciliationUserReviewBreakCode.md) | Optional | A list of break codes shared between the reconciliation runs of the same run instance and result hash. |
| **match_keys** | [List[GroupReconciliationUserReviewMatchKey]](GroupReconciliationUserReviewMatchKey.md) | Optional | A list of match keys shared between the reconciliation runs of the same run instance and result hash. |
| **comments** | [List[GroupReconciliationUserReviewComment]](GroupReconciliationUserReviewComment.md) | Optional | A list of comments shared between the reconciliation runs of the same run instance and result hash. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.GroupReconciliationUserReview import GroupReconciliationUserReview

instance = GroupReconciliationUserReview(
    break_codes=[],  # optional — A list of break codes shared between the reconciliation runs of the same run instance and result hash.
    match_keys=[],  # optional — A list of match keys shared between the reconciliation runs of the same run instance and result hash.
    comments=[]  # optional — A list of comments shared between the reconciliation runs of the same run instance and result hash.
)
```


## Related Models

- [GroupReconciliationUserReviewBreakCode](GroupReconciliationUserReviewBreakCode.md) — used in `break_codes`
- [GroupReconciliationUserReviewMatchKey](GroupReconciliationUserReviewMatchKey.md) — used in `match_keys`
- [GroupReconciliationUserReviewComment](GroupReconciliationUserReviewComment.md) — used in `comments`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

