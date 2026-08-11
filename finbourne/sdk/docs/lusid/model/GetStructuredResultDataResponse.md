# GetStructuredResultDataResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **values** | [Dict[str, StructuredResultData]](StructuredResultData.md) | Optional | The set of values that were successfully retrieved. |
| **failed** | [Dict[str, ErrorDetail]](ErrorDetail.md) | Optional | The set of values that could not be retrieved due along with a reason for this, e.g badly formed request. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.GetStructuredResultDataResponse import GetStructuredResultDataResponse

instance = GetStructuredResultDataResponse(
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    values=StructuredResultData(...),  # optional — The set of values that were successfully retrieved.
    failed=ErrorDetail(...),  # optional — The set of values that could not be retrieved due along with a reason for this, e.g badly formed request.
    links=[]  # optional
)
```

- [StructuredResultData](StructuredResultData.md) — used in `values`
- [ErrorDetail](ErrorDetail.md) — used in `failed`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

