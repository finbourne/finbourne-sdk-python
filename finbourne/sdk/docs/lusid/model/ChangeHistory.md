# ChangeHistory

A group of changes made by the same person at the same time.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **user_id** | **str** | Required | The unique identifier of the user that made the change. |
| **modified_as_at** | **datetime** | Required | The date/time of the change. |
| **request_id** | **str** | Required | The unique identifier of the request that the changes were part of. |
| **action** | **str** | Required | The action performed on the transaction, either created, updated, or deleted. The available values are: Create, Update, Delete |
| **changes** | [List[ChangeItem]](ChangeItem.md) | Required | The collection of changes that were made. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ChangeHistory import ChangeHistory

instance = ChangeHistory(
    user_id="...",  # required — The unique identifier of the user that made the change.
    modified_as_at=datetime.now(),  # required — The date/time of the change.
    request_id="...",  # required — The unique identifier of the request that the changes were part of.
    action="...",  # required — The action performed on the transaction, either created, updated, or deleted. The available values are: Create, Update, Delete
    changes=[],  # required — The collection of changes that were made.
    links=[]  # optional
)
```

- [ChangeItem](ChangeItem.md) — used in `changes`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

