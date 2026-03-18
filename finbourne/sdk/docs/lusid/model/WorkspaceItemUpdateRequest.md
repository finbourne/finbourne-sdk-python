# WorkspaceItemUpdateRequest

A request to update a workspace item.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **format** | **int** | Required | A simple integer format identifier. |
| **description** | **str** | Required | The description of a workspace item. |
| **content** | **object** | Required | The content associated with a workspace item. |
| **type** | **str** | Required | The type of the workspace item. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.WorkspaceItemUpdateRequest import WorkspaceItemUpdateRequest

instance = WorkspaceItemUpdateRequest(
    format=0,  # required — A simple integer format identifier.
    description="...",  # required — The description of a workspace item.
    content=,  # required — The content associated with a workspace item.
    type="..."  # required — The type of the workspace item.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

