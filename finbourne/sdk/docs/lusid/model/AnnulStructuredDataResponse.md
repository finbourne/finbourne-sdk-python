# AnnulStructuredDataResponse

The response to a request to annul (delete) a set of structured data from Lusid. This might have been for market data or some other structured entity.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **values** | **Dict[str, datetime]** | Optional | The set of values that were removed. |
| **failed** | [Dict[str, ErrorDetail]](ErrorDetail.md) | Optional | The set of values where removal failed, with a description as to why that is the case, e.g. badly formed request |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AnnulStructuredDataResponse import AnnulStructuredDataResponse

instance = AnnulStructuredDataResponse(
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    values=,  # optional — The set of values that were removed.
    failed=ErrorDetail(...),  # optional — The set of values where removal failed, with a description as to why that is the case, e.g. badly formed request
    links=[]  # optional
)
```

- [ErrorDetail](ErrorDetail.md) — used in `failed`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

