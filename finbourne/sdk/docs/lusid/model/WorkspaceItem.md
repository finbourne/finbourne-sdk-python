# WorkspaceItem

An item stored in a workspace.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **type** | **str** | Required | The type of the workspace item. |
| **format** | **int** | Required | A simple integer format identifier. |
| **name** | **str** | Required | A workspace item&#39;s name. |
| **group** | **str** | Required | The group containing a workspace item. |
| **description** | **str** | Required | The description of a workspace item. |
| **content** | **object** | Required | The content associated with a workspace item. |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.WorkspaceItem import WorkspaceItem

instance = WorkspaceItem(
    type="...",  # required — The type of the workspace item.
    format=0,  # required — A simple integer format identifier.
    name="...",  # required — A workspace item&#39;s name.
    group="...",  # required — The group containing a workspace item.
    description="...",  # required — The description of a workspace item.
    content=,  # required — The content associated with a workspace item.
    version=Version(...),  # optional
    links=[]  # optional
)
```

- [Version](Version.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

