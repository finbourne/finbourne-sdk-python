# ShareClassDetails

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **lusid_instrument_id** | **str** | Optional | LUSID&#39;s internal unique instrument identifier, resolved from the share class&#39; instrument identifiers |
| **instrument_scope** | **str** | Optional | The scope in which the share class instrument lies. |
| **short_code** | **str** | Optional | The unique code within the fund for the share class instrument. |
| **dom_currency** | **str** | Optional | The domestic currency of the share class instrument |
| **instrument_active** | **bool** | Optional | If the instrument of the share class is active. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ShareClassDetails import ShareClassDetails

instance = ShareClassDetails(
    lusid_instrument_id="...",  # optional — LUSID&#39;s internal unique instrument identifier, resolved from the share class&#39; instrument identifiers
    instrument_scope="...",  # optional — The scope in which the share class instrument lies.
    short_code="...",  # optional — The unique code within the fund for the share class instrument.
    dom_currency="...",  # optional — The domestic currency of the share class instrument
    instrument_active=True  # optional — If the instrument of the share class is active.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

