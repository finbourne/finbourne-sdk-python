# BatchManageCommentResponse

The response to a batch manage-comments request. Keyed by the client-supplied batch item key; each  success returns the full updated rec result.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **values** | [Dict[str, RecResult]](RecResult.md) | Required | The successfully-processed batch items, keyed by the client-supplied batch item key. |
| **failed** | [Dict[str, ErrorDetail]](ErrorDetail.md) | Optional | The failed batch items, keyed by the client-supplied batch item key. |
| **metadata** | **Dict[str, Optional[List[ResponseMetaData]]]** | Optional | Response metadata, keyed by the client-supplied batch item key. |
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.BatchManageCommentResponse import BatchManageCommentResponse

instance = BatchManageCommentResponse(
    values=RecResult(...),  # required — The successfully-processed batch items, keyed by the client-supplied batch item key.
    failed=ErrorDetail(...),  # optional — The failed batch items, keyed by the client-supplied batch item key.
    metadata=,  # optional — Response metadata, keyed by the client-supplied batch item key.
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    links=[]  # optional
)
```


## Related Models

- [RecResult](RecResult.md) — used in `values`
- [ErrorDetail](ErrorDetail.md) — used in `failed`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

