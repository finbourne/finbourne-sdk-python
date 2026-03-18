# CorporateActionTransitionComponentRequest

A single transition component request, when grouped with other transition component requests a corporate action  transition request is formed.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **instrument_identifiers** | **Dict[str, Optional[str]]** | Required | Unique instrument identifiers |
| **units_factor** | **float** | Required | The factor to scale units by |
| **cost_factor** | **float** | Required | The factor to scale cost by |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CorporateActionTransitionComponentRequest import CorporateActionTransitionComponentRequest

instance = CorporateActionTransitionComponentRequest(
    instrument_identifiers=,  # required — Unique instrument identifiers
    units_factor=0.0,  # required — The factor to scale units by
    cost_factor=0.0  # required — The factor to scale cost by
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

