# GroupReconciliationUserReviewBreakCode

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **break_code** | **str** | Required | The break code of the reconciliation result. |
| **user_id** | **str** | Optional | Id of the user who made a User Review input. |
| **as_at_added** | **datetime** | Optional | The timestamp of the added User Review input. |
| **as_at_invalid** | **datetime** | Optional | The timestamp when User Review input became invalid e.g. because of the different attribute values within the new run. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.GroupReconciliationUserReviewBreakCode import GroupReconciliationUserReviewBreakCode

instance = GroupReconciliationUserReviewBreakCode(
    break_code="...",  # required — The break code of the reconciliation result.
    user_id="...",  # optional — Id of the user who made a User Review input.
    as_at_added=datetime.now(),  # optional — The timestamp of the added User Review input.
    as_at_invalid=datetime.now()  # optional — The timestamp when User Review input became invalid e.g. because of the different attribute values within the new run.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

