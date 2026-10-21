# ResolveWithholdingTaxRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **mode** | **str** | Required | Where the dimension values come from. Raw: from Dimensions. InstrumentResolved: from the instrument, through the configuration&#39;s value sources, as in booking. Available values: Raw, InstrumentResolved. |
| **tax_country** | **str** | Required | The tax country of the holder. It is matched like any other dimension. |
| **profile_type** | **str** | Required | The profile type of the holder. It is matched like any other dimension. |
| **dimensions** | **Dict[str, Optional[str]]** | Optional | The value of each matching dimension, keyed by its field name in the rate datasets. A dimension left out is null, as in booking. taxCountry, profileType and ruleSource are not allowed here, and a name that neither dataset matches on is refused. With InstrumentResolved, a value here overrides the derived one, or gives one that the lookup cannot derive (see unresolvedDimensions in the response). |
| **wht_config** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **anomaly_dataset** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **main_dataset** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **source_priority** | **List[str]** | Optional | Optional. The source priority, most preferred first: it replaces the configuration&#39;s, or is used on its own when there is no configuration. An empty list applies no source filter. |
| **instrument_identifiers** | **Dict[str, Optional[str]]** | Optional | The identifiers of the instrument, resolved as for a transaction. Required with InstrumentResolved, not allowed with Raw. |
| **instrument_scope** | **str** | Optional | Optional. The scope to resolve the instrument in, before the default scope. Only with InstrumentResolved. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ResolveWithholdingTaxRequest import ResolveWithholdingTaxRequest

instance = ResolveWithholdingTaxRequest(
    mode="...",  # required — Where the dimension values come from. Raw: from Dimensions. InstrumentResolved: from the instrument, through the configuration&#39;s value sources, as in booking. Available values: Raw, InstrumentResolved.
    tax_country="...",  # required — The tax country of the holder. It is matched like any other dimension.
    profile_type="...",  # required — The profile type of the holder. It is matched like any other dimension.
    dimensions=,  # optional — The value of each matching dimension, keyed by its field name in the rate datasets. A dimension left out is null, as in booking. taxCountry, profileType and ruleSource are not allowed here, and a name that neither dataset matches on is refused. With InstrumentResolved, a value here overrides the derived one, or gives one that the lookup cannot derive (see unresolvedDimensions in the response).
    wht_config=ResourceId(...),  # optional
    anomaly_dataset=ResourceId(...),  # optional
    main_dataset=ResourceId(...),  # optional
    source_priority=,  # optional — Optional. The source priority, most preferred first: it replaces the configuration&#39;s, or is used on its own when there is no configuration. An empty list applies no source filter.
    instrument_identifiers=,  # optional — The identifiers of the instrument, resolved as for a transaction. Required with InstrumentResolved, not allowed with Raw.
    instrument_scope="..."  # optional — Optional. The scope to resolve the instrument in, before the default scope. Only with InstrumentResolved.
)
```

- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

