# OpenFigiData

OpenFIGI data structure
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **figi** | **str** | Required | FIGI assigned to the instrument. |
| **name** | **str** | Optional | Various attributes of the instrument |
| **ticker** | **str** | Optional | Various attributes of the instrument |
| **exchange_code** | **str** | Optional | Exchange code of the desired instrument(s) |
| **mic** | **str** | Optional | ISO market identification code(MIC) of the desired instrument(s) |
| **exchange_name** | **str** | Optional | Exchange name of the desired instrument(s) |
| **market_sector** | **str** | Optional | Market sector description of the desired instrument(s) |
| **general_security_type** | **str** | Optional | Enum-like attributes of the instrument |
| **security_type** | **str** | Optional | Enum-like attributes of the instrument |
| **security_description** | **str** | Optional | Various attributes of the instrument |
| **composite_figi** | **str** | Optional | Various attributes of the instrument |
| **share_class_figi** | **str** | Optional | Various attributes of the instrument |
| **match_type** | **str** | Optional | Type that the instrument matched against |
| **search_input** | **str** | Optional | Search input used to generate this response |
| **lusid_instrument_id** | **str** | Optional | If an instrument with this FIGI exists, the LUID of that instrument in LUSID |
| **lusid_instrument_scope** | **str** | Optional | If an instrument with this FIGI exists, the Scope of that instrument in LUSID |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.OpenFigiData import OpenFigiData

instance = OpenFigiData(
    figi="...",  # required — FIGI assigned to the instrument.
    name="...",  # optional — Various attributes of the instrument
    ticker="...",  # optional — Various attributes of the instrument
    exchange_code="...",  # optional — Exchange code of the desired instrument(s)
    mic="...",  # optional — ISO market identification code(MIC) of the desired instrument(s)
    exchange_name="...",  # optional — Exchange name of the desired instrument(s)
    market_sector="...",  # optional — Market sector description of the desired instrument(s)
    general_security_type="...",  # optional — Enum-like attributes of the instrument
    security_type="...",  # optional — Enum-like attributes of the instrument
    security_description="...",  # optional — Various attributes of the instrument
    composite_figi="...",  # optional — Various attributes of the instrument
    share_class_figi="...",  # optional — Various attributes of the instrument
    match_type="...",  # optional — Type that the instrument matched against
    search_input="...",  # optional — Search input used to generate this response
    lusid_instrument_id="...",  # optional — If an instrument with this FIGI exists, the LUID of that instrument in LUSID
    lusid_instrument_scope="..."  # optional — If an instrument with this FIGI exists, the Scope of that instrument in LUSID
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

