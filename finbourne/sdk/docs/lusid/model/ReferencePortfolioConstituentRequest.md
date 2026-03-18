# ReferencePortfolioConstituentRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **instrument_identifiers** | **Dict[str, Optional[str]]** | Required | Unique instrument identifiers |
| **properties** | [Dict[str, PerpetualProperty]](PerpetualProperty.md) | Optional | *No description available.* |
| **weight** | **float** | Required |  |
| **currency** | **str** | Optional |  |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ReferencePortfolioConstituentRequest import ReferencePortfolioConstituentRequest

instance = ReferencePortfolioConstituentRequest(
    instrument_identifiers=,  # required — Unique instrument identifiers
    properties=PerpetualProperty(...),  # optional
    weight=0.0,  # required — 
    currency="..."  # optional — 
)
```

- [PerpetualProperty](PerpetualProperty.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

