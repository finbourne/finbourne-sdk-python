# RecResultHoldingItem

A holding-shaped item within a rec result: the holding a Holding or CashHolding rec reconciled  (itemType Holding), or the one a Valuation rec valued (itemType ValuedHolding). Also holds the display names  of the portfolio and the holding's instrument.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **portfolio_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **portfolio_display_name** | **str** | Optional | The display name of the item&#39;s portfolio, as it stood at the asAt the run read its data. Null where the run did not read it. |
| **holding_id** | **str** | Optional | The holding identifier, at holding level: the same id whichever granularity the holding was read at, so that items of different rec types over one holding name it alike. |
| **tax_lot_id** | **str** | Optional | The tax lot the item is, where the source row was a single lot: a lot of a position read by tax lot, or a cash commitment. Null for an aggregated position and for a cash balance. Opaque: compare it whole, do not parse it. |
| **holding_instrument_scope** | **str** | Optional | The scope of the holding&#39;s instrument. Null where the source does not state one. |
| **holding_lusid_instrument_id** | **str** | Optional | The LUID of the holding&#39;s instrument. Null where the source does not state it. |
| **holding_instrument_name** | **str** | Optional | The name of the holding&#39;s instrument, as it stood at the asAt the run read its data. Null where the run did not resolve it. |
| **item_type** | **str** | Required | The polymorphic item-type discriminator: Holding, ValuedHolding, Transaction, SettlementActivity, RelationalDataPoint or the entity type of a LusidEntity rec. Names the item rather than the rec type: Holding and CashHolding recs produce Holding items, a Valuation rec produces ValuedHolding items, both transaction rec types produce Transaction items, and a relational dataset side produces RelationalDataPoint items whatever the rec type. A LusidEntity rec produces items of its entity type, for example Instrument items. Available values: SettlementActivity, Holding, Transaction, ValuedHolding, RelationalDataPoint, Instrument, LegalEntity, Portfolio, CustomEntity. |
| **rule_and_attribute_values** | **Dict[str, Optional[str]]** | Optional | The core rule, aggregate rule and supplemental attribute values for the item, keyed by name. |
| **writeback_suggestions** | [List[WritebackSuggestion]](WritebackSuggestion.md) | Required | The writebacks suggested against this item, as configured by the matching ruleset&#39;s writebackConfigurations. Only ever populated on target-side items. Suggestions only: a user is expected to review them before acting. Required, but may be empty. *(read-only)* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RecResultHoldingItem import RecResultHoldingItem

instance = RecResultHoldingItem(
    portfolio_id=ResourceId(...),  # required
    portfolio_display_name="...",  # optional — The display name of the item&#39;s portfolio, as it stood at the asAt the run read its data. Null where the run did not read it.
    holding_id="...",  # optional — The holding identifier, at holding level: the same id whichever granularity the holding was read at, so that items of different rec types over one holding name it alike.
    tax_lot_id="...",  # optional — The tax lot the item is, where the source row was a single lot: a lot of a position read by tax lot, or a cash commitment. Null for an aggregated position and for a cash balance. Opaque: compare it whole, do not parse it.
    holding_instrument_scope="...",  # optional — The scope of the holding&#39;s instrument. Null where the source does not state one.
    holding_lusid_instrument_id="...",  # optional — The LUID of the holding&#39;s instrument. Null where the source does not state it.
    holding_instrument_name="...",  # optional — The name of the holding&#39;s instrument, as it stood at the asAt the run read its data. Null where the run did not resolve it.
    item_type="...",  # required — The polymorphic item-type discriminator: Holding, ValuedHolding, Transaction, SettlementActivity, RelationalDataPoint or the entity type of a LusidEntity rec. Names the item rather than the rec type: Holding and CashHolding recs produce Holding items, a Valuation rec produces ValuedHolding items, both transaction rec types produce Transaction items, and a relational dataset side produces RelationalDataPoint items whatever the rec type. A LusidEntity rec produces items of its entity type, for example Instrument items. Available values: SettlementActivity, Holding, Transaction, ValuedHolding, RelationalDataPoint, Instrument, LegalEntity, Portfolio, CustomEntity.
    rule_and_attribute_values=,  # optional — The core rule, aggregate rule and supplemental attribute values for the item, keyed by name.
    writeback_suggestions=[]  # required — The writebacks suggested against this item, as configured by the matching ruleset&#39;s writebackConfigurations. Only ever populated on target-side items. Suggestions only: a user is expected to review them before acting. Required, but may be empty.
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [WritebackSuggestion](WritebackSuggestion.md) — used in `writeback_suggestions`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

