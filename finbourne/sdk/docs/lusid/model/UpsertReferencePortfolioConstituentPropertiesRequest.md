# UpsertReferencePortfolioConstituentPropertiesRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **identifiers** | **Dict[str, Optional[str]]** | Required | A set of instrument identifiers that can resolve the constituent to a unique instrument. |
| **properties** | [Dict[str, PerpetualProperty]](PerpetualProperty.md) | Required | The updated collection of properties of the constituent. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpsertReferencePortfolioConstituentPropertiesRequest import UpsertReferencePortfolioConstituentPropertiesRequest

instance = UpsertReferencePortfolioConstituentPropertiesRequest(
    identifiers=,  # required — A set of instrument identifiers that can resolve the constituent to a unique instrument.
    properties=PerpetualProperty(...)  # required — The updated collection of properties of the constituent.
)
```

- [PerpetualProperty](PerpetualProperty.md) — used in `properties`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

