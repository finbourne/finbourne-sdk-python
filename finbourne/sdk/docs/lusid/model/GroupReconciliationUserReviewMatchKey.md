# GroupReconciliationUserReviewMatchKey

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **match_key** | **str** | Required | The match key of the reconciliation result. |
| **user_id** | **str** | Optional | Id of the user who made a User Review input. |
| **as_at_added** | **datetime** | Optional | The timestamp of the added User Review input. |
| **as_at_invalid** | **datetime** | Optional | The timestamp when User Review input became invalid e.g. because of the different attribute values within the new run. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.GroupReconciliationUserReviewMatchKey import GroupReconciliationUserReviewMatchKey

instance = GroupReconciliationUserReviewMatchKey(
    match_key="...",  # required — The match key of the reconciliation result.
    user_id="...",  # optional — Id of the user who made a User Review input.
    as_at_added=datetime.now(),  # optional — The timestamp of the added User Review input.
    as_at_invalid=datetime.now()  # optional — The timestamp when User Review input became invalid e.g. because of the different attribute values within the new run.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

