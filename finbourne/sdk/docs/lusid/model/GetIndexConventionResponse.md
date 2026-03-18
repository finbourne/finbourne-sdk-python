# GetIndexConventionResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **value** | [IndexConvention](IndexConvention.md) | Optional | *No description available.* |
| **failed** | [Dict[str, ErrorDetail]](ErrorDetail.md) | Optional | The identifiers that did not resolve to a conventions along with the nature of the failure. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.GetIndexConventionResponse import GetIndexConventionResponse

instance = GetIndexConventionResponse(
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    value=IndexConvention(...),  # optional
    failed=ErrorDetail(...),  # optional — The identifiers that did not resolve to a conventions along with the nature of the failure.
    links=[]  # optional
)
```

- [IndexConvention](IndexConvention.md)
- [ErrorDetail](ErrorDetail.md) — used in `failed`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

