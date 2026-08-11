# GetCounterpartyAgreementResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **value** | [CounterpartyAgreement](CounterpartyAgreement.md) | Optional | *No description available.* |
| **failed** | [Dict[str, ErrorDetail]](ErrorDetail.md) | Optional | The counterparty agreement that could not be retrieved along with a reason for failure. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.GetCounterpartyAgreementResponse import GetCounterpartyAgreementResponse

instance = GetCounterpartyAgreementResponse(
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    value=CounterpartyAgreement(...),  # optional
    failed=ErrorDetail(...),  # optional — The counterparty agreement that could not be retrieved along with a reason for failure.
    links=[]  # optional
)
```

- [CounterpartyAgreement](CounterpartyAgreement.md)
- [ErrorDetail](ErrorDetail.md) — used in `failed`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

