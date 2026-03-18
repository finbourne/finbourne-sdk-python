# PostingModuleDetails

A posting Module request definition
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **display_name** | **str** | Required | The name of the Posting Module. |
| **description** | **str** | Optional | A description for the Posting Module. |
| **status** | **str** | Required | The Posting Module status. Can be Active or Inactive. Defaults to Active. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PostingModuleDetails import PostingModuleDetails

instance = PostingModuleDetails(
    display_name="...",  # required — The name of the Posting Module.
    description="...",  # optional — A description for the Posting Module.
    status="..."  # required — The Posting Module status. Can be Active or Inactive. Defaults to Active.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

