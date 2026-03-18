# OnboardInstrumentResponse

Simplified structure converted from the LUSID UpsertInstrumentReponse
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **values** | **List[str]** | Required | The instruments which have been successfully updated or created. |
| **failed** | **Dict[str, str]** | Required | The instruments that could not be updated or created or were left unchanged without error along with a reason for their failure. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.OnboardInstrumentResponse import OnboardInstrumentResponse

instance = OnboardInstrumentResponse(
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    values=,  # required — The instruments which have been successfully updated or created.
    failed=  # required — The instruments that could not be updated or created or were left unchanged without error along with a reason for their failure.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

