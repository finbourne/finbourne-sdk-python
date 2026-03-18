# CorporateActionTransitionComponent

A single transition component, when grouped with other components a corporate action transition is formed.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **instrument_scope** | **str** | Required | The scope in which the instrument lies. |
| **instrument_identifiers** | **Dict[str, Optional[str]]** | Required | Unique instrument identifiers |
| **instrument_uid** | **str** | Required | LUSID&#39;s internal unique instrument identifier, resolved from the instrument identifiers |
| **units_factor** | **float** | Required | The factor to scale units by |
| **cost_factor** | **float** | Required | The factor to scale cost by |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CorporateActionTransitionComponent import CorporateActionTransitionComponent

instance = CorporateActionTransitionComponent(
    instrument_scope="...",  # required — The scope in which the instrument lies.
    instrument_identifiers=,  # required — Unique instrument identifiers
    instrument_uid="...",  # required — LUSID&#39;s internal unique instrument identifier, resolved from the instrument identifiers
    units_factor=0.0,  # required — The factor to scale units by
    cost_factor=0.0  # required — The factor to scale cost by
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

