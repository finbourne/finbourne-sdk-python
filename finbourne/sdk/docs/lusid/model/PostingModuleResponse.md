# PostingModuleResponse

A Posting Module definition
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **posting_module_code** | **str** | Required | The code of the Posting Module. |
| **chart_of_accounts_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **display_name** | **str** | Required | The name of the Posting Module. |
| **description** | **str** | Optional | A description for the Posting Module. |
| **rules** | [List[PostingModuleRule]](PostingModuleRule.md) | Optional | The Posting Rules that apply for the Posting Module. Rules are evaluated in the order they occur in this collection. |
| **status** | **str** | Required | The Posting Module status. Can be Active, Inactive or Deleted. Defaults to Active. |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PostingModuleResponse import PostingModuleResponse

instance = PostingModuleResponse(
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    posting_module_code="...",  # required — The code of the Posting Module.
    chart_of_accounts_id=ResourceId(...),  # required
    display_name="...",  # required — The name of the Posting Module.
    description="...",  # optional — A description for the Posting Module.
    rules=[],  # optional — The Posting Rules that apply for the Posting Module. Rules are evaluated in the order they occur in this collection.
    status="...",  # required — The Posting Module status. Can be Active, Inactive or Deleted. Defaults to Active.
    version=Version(...),  # optional
    links=[]  # optional
)
```

- [ResourceId](ResourceId.md)
- [PostingModuleRule](PostingModuleRule.md) — used in `rules`
- [Version](Version.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

