# WorkspacePermittedItemActions

The workspace item actions a user is permitted to perform within a workspace.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **read_item** | **bool** | Optional | Whether the user is permitted to read workspace items. |
| **add_item** | **bool** | Optional | Whether the user is permitted to add workspace items. |
| **update_item** | **bool** | Optional | Whether the user is permitted to update workspace items. |
| **delete_item** | **bool** | Optional | Whether the user is permitted to delete workspace items. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.WorkspacePermittedItemActions import WorkspacePermittedItemActions

instance = WorkspacePermittedItemActions(
    read_item=True,  # optional — Whether the user is permitted to read workspace items.
    add_item=True,  # optional — Whether the user is permitted to add workspace items.
    update_item=True,  # optional — Whether the user is permitted to update workspace items.
    delete_item=True  # optional — Whether the user is permitted to delete workspace items.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

