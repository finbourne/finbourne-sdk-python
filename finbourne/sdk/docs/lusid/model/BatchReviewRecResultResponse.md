# BatchReviewRecResultResponse

The response to a batch review request. Keyed by the client-supplied batch item key.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **values** | [Dict[str, BatchReviewRecResultItemResult]](BatchReviewRecResultItemResult.md) | Required | The successfully-processed batch items, keyed by the client-supplied batch item key. |
| **failed** | [Dict[str, ErrorDetail]](ErrorDetail.md) | Optional | The failed batch items, keyed by the client-supplied batch item key. |
| **metadata** | **Dict[str, Optional[List[ResponseMetaData]]]** | Optional | Response metadata, keyed by the client-supplied batch item key. |
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.BatchReviewRecResultResponse import BatchReviewRecResultResponse

instance = BatchReviewRecResultResponse(
    values=BatchReviewRecResultItemResult(...),  # required — The successfully-processed batch items, keyed by the client-supplied batch item key.
    failed=ErrorDetail(...),  # optional — The failed batch items, keyed by the client-supplied batch item key.
    metadata=,  # optional — Response metadata, keyed by the client-supplied batch item key.
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    links=[]  # optional
)
```


## Related Models

- [BatchReviewRecResultItemResult](BatchReviewRecResultItemResult.md) — used in `values`
- [ErrorDetail](ErrorDetail.md) — used in `failed`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

