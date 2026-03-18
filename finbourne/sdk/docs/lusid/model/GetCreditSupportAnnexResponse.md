# GetCreditSupportAnnexResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **value** | [CreditSupportAnnex](CreditSupportAnnex.md) | Optional | *No description available.* |
| **failed** | [Dict[str, ErrorDetail]](ErrorDetail.md) | Optional | The credit support annex that could not be updated or inserted along with a reason for failure. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.GetCreditSupportAnnexResponse import GetCreditSupportAnnexResponse

instance = GetCreditSupportAnnexResponse(
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    value=CreditSupportAnnex(...),  # optional
    failed=ErrorDetail(...),  # optional — The credit support annex that could not be updated or inserted along with a reason for failure.
    links=[]  # optional
)
```

- [CreditSupportAnnex](CreditSupportAnnex.md)
- [ErrorDetail](ErrorDetail.md) — used in `failed`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

