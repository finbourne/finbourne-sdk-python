# WeightedInstrument

Specification for a holding or quantity of (weight for) an instrument on a given date.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **quantity** | **float** | Optional | The quantity of the instrument that is owned. |
| **holding_identifier** | **str** | Optional | Identifier for the instrument.  For a single, unique trade or transaction this can be thought of as equivalent to the transaction identifier, or  a composite of the sub-holding keys for a regular sub-holding. When there are multiple transactions sharing the same underlying instrument  such as purchase of shares on multiple dates where tax implications are different this would not be the case.    In an inlined aggregation request if this is wanted to identify a line item, it can be specified in the set of aggregation keys given on the aggregation  request that accompanies the set of weighted instruments. |
| **instrument** | [LusidInstrument](LusidInstrument.md) | Optional | *No description available.* |
| **in_line_lookup_identifiers** | [WeightedInstrumentInLineLookupIdentifiers](WeightedInstrumentInLineLookupIdentifiers.md) | Optional | *No description available.* |
| **instrument_scope** | **str** | Optional | The scope in which to resolve the instrument, if no inlined definition is provided.  If left empty, the default scope will be used. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.WeightedInstrument import WeightedInstrument

instance = WeightedInstrument(
    quantity=0.0,  # optional — The quantity of the instrument that is owned.
    holding_identifier="...",  # optional — Identifier for the instrument.  For a single, unique trade or transaction this can be thought of as equivalent to the transaction identifier, or  a composite of the sub-holding keys for a regular sub-holding. When there are multiple transactions sharing the same underlying instrument  such as purchase of shares on multiple dates where tax implications are different this would not be the case.    In an inlined aggregation request if this is wanted to identify a line item, it can be specified in the set of aggregation keys given on the aggregation  request that accompanies the set of weighted instruments.
    instrument=LusidInstrument(...),  # optional
    in_line_lookup_identifiers=WeightedInstrumentInLineLookupIdentifiers(...),  # optional
    instrument_scope="..."  # optional — The scope in which to resolve the instrument, if no inlined definition is provided.  If left empty, the default scope will be used.
)
```

- [LusidInstrument](LusidInstrument.md)
- [WeightedInstrumentInLineLookupIdentifiers](WeightedInstrumentInLineLookupIdentifiers.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

