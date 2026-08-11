# OutputTransition

A 'transition' within a corporate action, representing an output transition.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **instrument_identifiers** | **Dict[str, Optional[str]]** | Required | Unique instrument identifiers |
| **units_factor** | **float** | Required | The factor to scale units by |
| **cost_factor** | **float** | Required | The factor to scale cost by |
| **lusid_instrument_id** | **str** | Optional | LUSID&#39;s internal unique instrument identifier, resolved from the instrument identifiers *(read-only)* |
| **instrument_scope** | **str** | Optional | The scope in which the instrument lies. *(read-only)* |
| **rounding** | [RoundingConfiguration](RoundingConfiguration.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.OutputTransition import OutputTransition

instance = OutputTransition(
    instrument_identifiers=,  # required — Unique instrument identifiers
    units_factor=0.0,  # required — The factor to scale units by
    cost_factor=0.0,  # required — The factor to scale cost by
    lusid_instrument_id="...",  # optional — LUSID&#39;s internal unique instrument identifier, resolved from the instrument identifiers
    instrument_scope="...",  # optional — The scope in which the instrument lies.
    rounding=RoundingConfiguration(...)  # optional
)
```

- [RoundingConfiguration](RoundingConfiguration.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

