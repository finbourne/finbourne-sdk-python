# RecResultSettlementActivityItem

A settlement-activity item within a rec result. Names the portfolio, the activity's instrument and the settled  transaction's resolved instrument alongside, for display.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **portfolio_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **portfolio_display_name** | **str** | Optional | The display name of the item&#39;s portfolio, as it stood at the asAt the run read its data. Null where the run did not read it. |
| **activity_id** | **str** | Optional | The settlement activity identifier. |
| **activity_instrument_scope** | **str** | Optional | The scope of the settlement activity&#39;s instrument. Null where the source does not state one. |
| **activity_lusid_instrument_id** | **str** | Optional | The LUID of the settlement activity&#39;s instrument. Null where the source does not state it. |
| **activity_instrument_name** | **str** | Optional | The name of the settlement activity&#39;s instrument, as it stood at the asAt the run read its data. Null where the run did not resolve it. |
| **transaction_id** | **str** | Optional | The transaction identifier. |
| **transaction_instrument_scope** | **str** | Optional | The scope of the transaction&#39;s resolved instrument. Null where the source does not state one. |
| **transaction_lusid_instrument_id** | **str** | Optional | The LUID of the transaction&#39;s resolved instrument. Null where the source does not state it. |
| **transaction_instrument_name** | **str** | Optional | The name of the transaction&#39;s resolved instrument, as it stood at the asAt the run read its data. Null where the run did not resolve it. |
| **settlement_instruction_id** | **str** | Optional | The settlement instruction identifier. |
| **holding_impacts** | [List[RecResultHoldingImpact]](RecResultHoldingImpact.md) | Required | The holdings, and where the source states them the tax lots, the item impacted. A distinct set ordered by holdingId then taxLotId; may be empty. An input transaction has not run the movements engine and impacts nothing yet. |
| **item_type** | **str** | Required | The polymorphic item-type discriminator: Holding, ValuedHolding, Transaction, SettlementActivity, RelationalDataPoint or the entity type of a LusidEntity rec. Names the item rather than the rec type: Holding and CashHolding recs produce Holding items, a Valuation rec produces ValuedHolding items, both transaction rec types produce Transaction items, and a relational dataset side produces RelationalDataPoint items whatever the rec type. A LusidEntity rec produces items of its entity type, for example Instrument items. Available values: SettlementActivity, Holding, Transaction, ValuedHolding, RelationalDataPoint, Instrument, LegalEntity, Portfolio. |
| **rule_and_attribute_values** | **Dict[str, Optional[str]]** | Optional | The core rule, aggregate rule and supplemental attribute values for the item, keyed by name. |
| **writeback_suggestions** | [List[WritebackSuggestion]](WritebackSuggestion.md) | Required | The writebacks suggested against this item, as configured by the matching ruleset&#39;s writebackConfigurations. Only ever populated on target-side items. Suggestions only: a user is expected to review them before acting. Required, but may be empty. *(read-only)* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RecResultSettlementActivityItem import RecResultSettlementActivityItem

instance = RecResultSettlementActivityItem(
    portfolio_id=ResourceId(...),  # required
    portfolio_display_name="...",  # optional — The display name of the item&#39;s portfolio, as it stood at the asAt the run read its data. Null where the run did not read it.
    activity_id="...",  # optional — The settlement activity identifier.
    activity_instrument_scope="...",  # optional — The scope of the settlement activity&#39;s instrument. Null where the source does not state one.
    activity_lusid_instrument_id="...",  # optional — The LUID of the settlement activity&#39;s instrument. Null where the source does not state it.
    activity_instrument_name="...",  # optional — The name of the settlement activity&#39;s instrument, as it stood at the asAt the run read its data. Null where the run did not resolve it.
    transaction_id="...",  # optional — The transaction identifier.
    transaction_instrument_scope="...",  # optional — The scope of the transaction&#39;s resolved instrument. Null where the source does not state one.
    transaction_lusid_instrument_id="...",  # optional — The LUID of the transaction&#39;s resolved instrument. Null where the source does not state it.
    transaction_instrument_name="...",  # optional — The name of the transaction&#39;s resolved instrument, as it stood at the asAt the run read its data. Null where the run did not resolve it.
    settlement_instruction_id="...",  # optional — The settlement instruction identifier.
    holding_impacts=[],  # required — The holdings, and where the source states them the tax lots, the item impacted. A distinct set ordered by holdingId then taxLotId; may be empty. An input transaction has not run the movements engine and impacts nothing yet.
    item_type="...",  # required — The polymorphic item-type discriminator: Holding, ValuedHolding, Transaction, SettlementActivity, RelationalDataPoint or the entity type of a LusidEntity rec. Names the item rather than the rec type: Holding and CashHolding recs produce Holding items, a Valuation rec produces ValuedHolding items, both transaction rec types produce Transaction items, and a relational dataset side produces RelationalDataPoint items whatever the rec type. A LusidEntity rec produces items of its entity type, for example Instrument items. Available values: SettlementActivity, Holding, Transaction, ValuedHolding, RelationalDataPoint, Instrument, LegalEntity, Portfolio.
    rule_and_attribute_values=,  # optional — The core rule, aggregate rule and supplemental attribute values for the item, keyed by name.
    writeback_suggestions=[]  # required — The writebacks suggested against this item, as configured by the matching ruleset&#39;s writebackConfigurations. Only ever populated on target-side items. Suggestions only: a user is expected to review them before acting. Required, but may be empty.
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [RecResultHoldingImpact](RecResultHoldingImpact.md) — used in `holding_impacts`
- [WritebackSuggestion](WritebackSuggestion.md) — used in `writeback_suggestions`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

