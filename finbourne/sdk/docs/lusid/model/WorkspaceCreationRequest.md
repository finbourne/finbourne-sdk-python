# WorkspaceCreationRequest

A request to create an empty workspace.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **name** | **str** | Required | A workspace&#39;s name. |
| **description** | **str** | Required | A friendly description for the workspace. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.WorkspaceCreationRequest import WorkspaceCreationRequest

instance = WorkspaceCreationRequest(
    name="...",  # required — A workspace&#39;s name.
    description="..."  # required — A friendly description for the workspace.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

