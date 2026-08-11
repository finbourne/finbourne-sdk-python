# InstrumentDefinition

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **name** | **str** | Required | The name of the instrument. |
| **identifiers** | [Dict[str, InstrumentIdValue]](InstrumentIdValue.md) | Required | A set of identifiers that can be used to identify the instrument. At least one of these must be configured to be a unique identifier. |
| **properties** | [List[ModelProperty]](ModelProperty.md) | Optional | Set of unique instrument properties and associated values to store with the instrument. Each property must be from the &#39;Instrument&#39; domain. |
| **look_through_portfolio_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **definition** | [LusidInstrument](LusidInstrument.md) | Optional | *No description available.* |
| **settlement_cycle** | [SettlementCycle](SettlementCycle.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.InstrumentDefinition import InstrumentDefinition

instance = InstrumentDefinition(
    name="...",  # required — The name of the instrument.
    identifiers=InstrumentIdValue(...),  # required — A set of identifiers that can be used to identify the instrument. At least one of these must be configured to be a unique identifier.
    properties=[],  # optional — Set of unique instrument properties and associated values to store with the instrument. Each property must be from the &#39;Instrument&#39; domain.
    look_through_portfolio_id=ResourceId(...),  # optional
    definition=LusidInstrument(...),  # optional
    settlement_cycle=SettlementCycle(...)  # optional
)
```

- [InstrumentIdValue](InstrumentIdValue.md) — used in `identifiers`
- [ModelProperty](ModelProperty.md) — used in `properties`
- [ResourceId](ResourceId.md)
- [LusidInstrument](LusidInstrument.md)
- [SettlementCycle](SettlementCycle.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

