# WeightedInstrumentInLineLookupIdentifiers

External market codes and identifiers for the equity, e.g. IBM.  Required for valuation via SimpleStatic (look-up pricing).  Valuation will not succeed without a matching quote.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **lusid_instrument_id** | **str** | Optional | *No description available.* |
| **isin** | **str** | Optional | *No description available.* |
| **sedol** | **str** | Optional | *No description available.* |
| **cusip** | **str** | Optional | *No description available.* |
| **client_internal** | **str** | Optional | *No description available.* |
| **figi** | **str** | Optional | *No description available.* |
| **ric** | **str** | Optional | *No description available.* |
| **quote_perm_id** | **str** | Optional | *No description available.* |
| **red_code** | **str** | Optional | *No description available.* |
| **bbgid** | **str** | Optional | *No description available.* |
| **ice_code** | **str** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.WeightedInstrumentInLineLookupIdentifiers import WeightedInstrumentInLineLookupIdentifiers

instance = WeightedInstrumentInLineLookupIdentifiers(
    lusid_instrument_id="...",  # optional
    isin="...",  # optional
    sedol="...",  # optional
    cusip="...",  # optional
    client_internal="...",  # optional
    figi="...",  # optional
    ric="...",  # optional
    quote_perm_id="...",  # optional
    red_code="...",  # optional
    bbgid="...",  # optional
    ice_code="..."  # optional
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

