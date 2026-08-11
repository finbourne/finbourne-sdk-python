# GetQuotesResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **values** | [Dict[str, Quote]](Quote.md) | Optional | The quotes which have been successfully retrieved. |
| **not_found** | [Dict[str, ErrorDetail]](ErrorDetail.md) | Optional | The quotes that could not be found along with a reason why. |
| **failed** | [Dict[str, ErrorDetail]](ErrorDetail.md) | Optional | The quotes that could not be retrieved due to an error along with a reason for their failure. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.GetQuotesResponse import GetQuotesResponse

instance = GetQuotesResponse(
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    values=Quote(...),  # optional — The quotes which have been successfully retrieved.
    not_found=ErrorDetail(...),  # optional — The quotes that could not be found along with a reason why.
    failed=ErrorDetail(...),  # optional — The quotes that could not be retrieved due to an error along with a reason for their failure.
    links=[]  # optional
)
```

- [Quote](Quote.md) — used in `values`
- [ErrorDetail](ErrorDetail.md) — used in `not_found`
- [ErrorDetail](ErrorDetail.md) — used in `failed`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

