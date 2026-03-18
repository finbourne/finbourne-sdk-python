# Instrument

A list of instruments.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **scope** | **str** | Optional | The scope in which the instrument lies. |
| **lusid_instrument_id** | **str** | Required | The unique LUSID Instrument Identifier (LUID) of the instrument. |
| **version** | [Version](Version.md) | Required | *No description available.* |
| **staged_modifications** | [StagedModificationsInfo](StagedModificationsInfo.md) | Optional | *No description available.* |
| **name** | **str** | Required | The name of the instrument. |
| **identifiers** | **Dict[str, Optional[str]]** | Required | The set of identifiers that can be used to identify the instrument. |
| **properties** | [List[ModelProperty]](ModelProperty.md) | Optional | The requested instrument properties. These will be from the &#39;Instrument&#39; domain. |
| **lookthrough_portfolio** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **instrument_definition** | [LusidInstrument](LusidInstrument.md) | Optional | *No description available.* |
| **state** | **str** | Required | The state of of the instrument at the asAt datetime of this version of the instrument definition. The available values are: Active, Inactive, Deleted |
| **asset_class** | **str** | Optional | The nominal asset class of the instrument, e.g. InterestRates, FX, Inflation, Equities, Credit, Commodities, etc. The available values are: InterestRates, FX, Inflation, Equities, Credit, Commodities, Money, Unknown |
| **dom_ccy** | **str** | Optional | The domestic currency, meaning the currency in which the instrument would typically be expected to pay cashflows, e.g. a share in AAPL being USD. |
| **relationships** | [List[Relationship]](Relationship.md) | Optional | A set of relationships associated to the instrument. |
| **settlement_cycle** | [SettlementCycle](SettlementCycle.md) | Optional | *No description available.* |
| **data_model_membership** | [DataModelMembership](DataModelMembership.md) | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.Instrument import Instrument

instance = Instrument(
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    scope="...",  # optional — The scope in which the instrument lies.
    lusid_instrument_id="...",  # required — The unique LUSID Instrument Identifier (LUID) of the instrument.
    version=Version(...),  # required
    staged_modifications=StagedModificationsInfo(...),  # optional
    name="...",  # required — The name of the instrument.
    identifiers=,  # required — The set of identifiers that can be used to identify the instrument.
    properties=[],  # optional — The requested instrument properties. These will be from the &#39;Instrument&#39; domain.
    lookthrough_portfolio=ResourceId(...),  # optional
    instrument_definition=LusidInstrument(...),  # optional
    state="...",  # required — The state of of the instrument at the asAt datetime of this version of the instrument definition. The available values are: Active, Inactive, Deleted
    asset_class="...",  # optional — The nominal asset class of the instrument, e.g. InterestRates, FX, Inflation, Equities, Credit, Commodities, etc. The available values are: InterestRates, FX, Inflation, Equities, Credit, Commodities, Money, Unknown
    dom_ccy="...",  # optional — The domestic currency, meaning the currency in which the instrument would typically be expected to pay cashflows, e.g. a share in AAPL being USD.
    relationships=[],  # optional — A set of relationships associated to the instrument.
    settlement_cycle=SettlementCycle(...),  # optional
    data_model_membership=DataModelMembership(...),  # optional
    links=[]  # optional
)
```

- [Version](Version.md)
- [StagedModificationsInfo](StagedModificationsInfo.md)
- [ModelProperty](ModelProperty.md) — used in `properties`
- [ResourceId](ResourceId.md)
- [LusidInstrument](LusidInstrument.md)
- [Relationship](Relationship.md) — used in `relationships`
- [SettlementCycle](SettlementCycle.md)
- [DataModelMembership](DataModelMembership.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

