# PostingModuleRequest

A Posting Module request definition
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **code** | **str** | Required | The code of the Posting Module. |
| **display_name** | **str** | Required | The name of the Posting Module. |
| **description** | **str** | Optional | A description for the Posting Module. |
| **rules** | [List[PostingModuleRule]](PostingModuleRule.md) | Optional | The Posting Rules that apply for the Posting Module. Rules are evaluated in the order they occur in this collection. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PostingModuleRequest import PostingModuleRequest

instance = PostingModuleRequest(
    code="...",  # required — The code of the Posting Module.
    display_name="...",  # required — The name of the Posting Module.
    description="...",  # optional — A description for the Posting Module.
    rules=[]  # optional — The Posting Rules that apply for the Posting Module. Rules are evaluated in the order they occur in this collection.
)
```

- [PostingModuleRule](PostingModuleRule.md) — used in `rules`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

