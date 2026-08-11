# ItemAndWorkspace

An item plus its containing workspace name.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **workspace_name** | **str** | Required | A workspace&#39;s name. |
| **workspace_item** | [WorkspaceItem](WorkspaceItem.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ItemAndWorkspace import ItemAndWorkspace

instance = ItemAndWorkspace(
    workspace_name="...",  # required — A workspace&#39;s name.
    workspace_item=WorkspaceItem(...)  # required
)
```

- [WorkspaceItem](WorkspaceItem.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

