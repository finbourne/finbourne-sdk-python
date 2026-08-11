# UpsertQuotesResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **values** | [Dict[str, Quote]](Quote.md) | Optional | The quotes which have been successfully updated or inserted. |
| **failed** | [Dict[str, ErrorDetail]](ErrorDetail.md) | Optional | The quotes that could not be updated or inserted along with a reason for their failure. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpsertQuotesResponse import UpsertQuotesResponse

instance = UpsertQuotesResponse(
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    values=Quote(...),  # optional — The quotes which have been successfully updated or inserted.
    failed=ErrorDetail(...),  # optional — The quotes that could not be updated or inserted along with a reason for their failure.
    links=[]  # optional
)
```

- [Quote](Quote.md) — used in `values`
- [ErrorDetail](ErrorDetail.md) — used in `failed`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

