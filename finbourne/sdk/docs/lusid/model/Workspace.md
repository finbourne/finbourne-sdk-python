# Workspace

A workspace.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **name** | **str** | Required | A workspace&#39;s name. |
| **description** | **str** | Required | A friendly description for the workspace. |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **permitted_item_actions** | [WorkspacePermittedItemActions](WorkspacePermittedItemActions.md) | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.Workspace import Workspace

instance = Workspace(
    name="...",  # required — A workspace&#39;s name.
    description="...",  # required — A friendly description for the workspace.
    version=Version(...),  # optional
    permitted_item_actions=WorkspacePermittedItemActions(...),  # optional
    links=[]  # optional
)
```

- [Version](Version.md)
- [WorkspacePermittedItemActions](WorkspacePermittedItemActions.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

