# WorkspaceItemCreationRequest

A request to create an item in a workspace.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **format** | **int** | Required | A simple integer format identifier. |
| **name** | **str** | Required | A workspace item&#39;s name. |
| **group** | **str** | Required | The group containing a workspace item. |
| **description** | **str** | Required | The description of a workspace item. |
| **content** | **object** | Required | The content associated with a workspace item. |
| **type** | **str** | Required | The type of the workspace item. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.WorkspaceItemCreationRequest import WorkspaceItemCreationRequest

instance = WorkspaceItemCreationRequest(
    format=0,  # required — A simple integer format identifier.
    name="...",  # required — A workspace item&#39;s name.
    group="...",  # required — The group containing a workspace item.
    description="...",  # required — The description of a workspace item.
    content=,  # required — The content associated with a workspace item.
    type="..."  # required — The type of the workspace item.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

