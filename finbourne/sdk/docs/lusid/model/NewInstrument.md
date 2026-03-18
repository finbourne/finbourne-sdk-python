# NewInstrument

Set of identifiers of an existing instrument that will be the subject or distribution of a corporate action.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **instrument_identifiers** | **Dict[str, Optional[str]]** | Required | Unique instrument identifiers. |
| **lusid_instrument_id** | **str** | Optional | LUSID&#39;s internal unique instrument identifier, resolved from the instrument identifiers. *(read-only)* |
| **instrument_scope** | **str** | Optional | The scope in which the instrument lies, resolved from the instrument identifiers. *(read-only)* |
| **dom_ccy** | **str** | Optional | The domestic currency of the instrument, resolved from the instrument identifiers. *(read-only)* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.NewInstrument import NewInstrument

instance = NewInstrument(
    instrument_identifiers=,  # required — Unique instrument identifiers.
    lusid_instrument_id="...",  # optional — LUSID&#39;s internal unique instrument identifier, resolved from the instrument identifiers.
    instrument_scope="...",  # optional — The scope in which the instrument lies, resolved from the instrument identifiers.
    dom_ccy="..."  # optional — The domestic currency of the instrument, resolved from the instrument identifiers.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

