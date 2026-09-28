# RecResultHoldingItem

A holding-shaped item within a rec result: the holding a Holding or CashHolding rec reconciled  (itemType Holding), or the one a Valuation rec valued (itemType ValuedHolding).
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **portfolio_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **holding_id** | **str** | Optional | The holding identifier, at holding level: the same id whichever granularity the holding was read at, so that items of different rec types over one holding name it alike. |
| **tax_lot_id** | **str** | Optional | The tax lot the item is, where the source row was a single lot: a lot of a position read by tax lot, or a cash commitment. Null for an aggregated position and for a cash balance. Opaque: compare it whole, do not parse it. |
| **item_type** | **str** | Required | The polymorphic item-type discriminator: Holding, ValuedHolding, Transaction or SettlementActivity. Names the item rather than the rec type: Holding and CashHolding recs produce Holding items, a Valuation rec produces ValuedHolding items, and both transaction rec types produce Transaction items. Available values: SettlementActivity, Holding, Transaction, ValuedHolding. |
| **rule_and_attribute_values** | **Dict[str, Optional[str]]** | Optional | The core rule, aggregate rule and supplemental attribute values for the item, keyed by name. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RecResultHoldingItem import RecResultHoldingItem

instance = RecResultHoldingItem(
    portfolio_id=ResourceId(...),  # required
    holding_id="...",  # optional — The holding identifier, at holding level: the same id whichever granularity the holding was read at, so that items of different rec types over one holding name it alike.
    tax_lot_id="...",  # optional — The tax lot the item is, where the source row was a single lot: a lot of a position read by tax lot, or a cash commitment. Null for an aggregated position and for a cash balance. Opaque: compare it whole, do not parse it.
    item_type="...",  # required — The polymorphic item-type discriminator: Holding, ValuedHolding, Transaction or SettlementActivity. Names the item rather than the rec type: Holding and CashHolding recs produce Holding items, a Valuation rec produces ValuedHolding items, and both transaction rec types produce Transaction items. Available values: SettlementActivity, Holding, Transaction, ValuedHolding.
    rule_and_attribute_values=  # optional — The core rule, aggregate rule and supplemental attribute values for the item, keyed by name.
)
```


## Related Models

- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

