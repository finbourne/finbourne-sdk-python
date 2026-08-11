# ReferencePortfolioConstituent

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **instrument_identifiers** | **Dict[str, Optional[str]]** | Optional | Unique instrument identifiers |
| **instrument_uid** | **str** | Required | LUSID&#39;s internal unique instrument identifier, resolved from the instrument identifiers |
| **currency** | **str** | Required |  |
| **properties** | [Dict[str, PerpetualProperty]](PerpetualProperty.md) | Optional | Properties associated with the constituent |
| **weight** | **float** | Required |  |
| **floating_weight** | **float** | Optional |  |
| **instrument_scope** | **str** | Optional |  |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ReferencePortfolioConstituent import ReferencePortfolioConstituent

instance = ReferencePortfolioConstituent(
    instrument_identifiers=,  # optional — Unique instrument identifiers
    instrument_uid="...",  # required — LUSID&#39;s internal unique instrument identifier, resolved from the instrument identifiers
    currency="...",  # required — 
    properties=PerpetualProperty(...),  # optional — Properties associated with the constituent
    weight=0.0,  # required — 
    floating_weight=0.0,  # optional — 
    instrument_scope="..."  # optional — 
)
```

- [PerpetualProperty](PerpetualProperty.md) — used in `properties`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

