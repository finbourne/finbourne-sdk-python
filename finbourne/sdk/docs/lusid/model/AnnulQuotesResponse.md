# AnnulQuotesResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **values** | **Dict[str, datetime]** | Optional | The quotes which have been successfully deleted along with the asAt datetime at which the deletion was committed to LUSID. |
| **failed** | [Dict[str, ErrorDetail]](ErrorDetail.md) | Optional | The quotes that could not be deleted along with a reason for their failure. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AnnulQuotesResponse import AnnulQuotesResponse

instance = AnnulQuotesResponse(
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    values=,  # optional — The quotes which have been successfully deleted along with the asAt datetime at which the deletion was committed to LUSID.
    failed=ErrorDetail(...),  # optional — The quotes that could not be deleted along with a reason for their failure.
    links=[]  # optional
)
```

- [ErrorDetail](ErrorDetail.md) — used in `failed`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

