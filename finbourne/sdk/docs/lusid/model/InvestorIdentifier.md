# InvestorIdentifier

Identification of an Investor on the LUSID API.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **investor_type** | **str** | Required | The type of the investor of the Investor Record. Can be either a Person, LegalEntity or Nominee. |
| **identifiers** | **Dict[str, Optional[str]]** | Optional | Single identifier that should target the desired person or legal entity |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.InvestorIdentifier import InvestorIdentifier

instance = InvestorIdentifier(
    investor_type="...",  # required — The type of the investor of the Investor Record. Can be either a Person, LegalEntity or Nominee.
    identifiers=  # optional — Single identifier that should target the desired person or legal entity
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

