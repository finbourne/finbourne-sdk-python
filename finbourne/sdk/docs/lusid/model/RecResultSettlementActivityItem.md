# RecResultSettlementActivityItem

A settlement-activity item within a rec result.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **portfolio_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **activity_id** | **str** | Optional | The settlement activity identifier. |
| **transaction_id** | **str** | Optional | The transaction identifier. |
| **settlement_instruction_id** | **str** | Optional | The settlement instruction identifier. |
| **holding_impacts** | [List[RecResultHoldingImpact]](RecResultHoldingImpact.md) | Required | The holdings, and where the source states them the tax lots, the item impacted. A distinct set ordered by holdingId then taxLotId; may be empty. An input transaction has not run the movements engine and impacts nothing yet. |
| **item_type** | **str** | Required | The polymorphic item-type discriminator: Holding, ValuedHolding, Transaction or SettlementActivity. Names the item rather than the rec type: Holding and CashHolding recs produce Holding items, a Valuation rec produces ValuedHolding items, and both transaction rec types produce Transaction items. Available values: SettlementActivity, Holding, Transaction, ValuedHolding. |
| **rule_and_attribute_values** | **Dict[str, Optional[str]]** | Optional | The core rule, aggregate rule and supplemental attribute values for the item, keyed by name. |
| **writeback_suggestions** | [List[WritebackSuggestion]](WritebackSuggestion.md) | Required | The writebacks suggested against this item, as configured by the matching ruleset&#39;s writebackConfigurations. Only ever populated on target-side items. Suggestions only: a user is expected to review them before acting. Required, but may be empty. *(read-only)* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RecResultSettlementActivityItem import RecResultSettlementActivityItem

instance = RecResultSettlementActivityItem(
    portfolio_id=ResourceId(...),  # required
    activity_id="...",  # optional — The settlement activity identifier.
    transaction_id="...",  # optional — The transaction identifier.
    settlement_instruction_id="...",  # optional — The settlement instruction identifier.
    holding_impacts=[],  # required — The holdings, and where the source states them the tax lots, the item impacted. A distinct set ordered by holdingId then taxLotId; may be empty. An input transaction has not run the movements engine and impacts nothing yet.
    item_type="...",  # required — The polymorphic item-type discriminator: Holding, ValuedHolding, Transaction or SettlementActivity. Names the item rather than the rec type: Holding and CashHolding recs produce Holding items, a Valuation rec produces ValuedHolding items, and both transaction rec types produce Transaction items. Available values: SettlementActivity, Holding, Transaction, ValuedHolding.
    rule_and_attribute_values=,  # optional — The core rule, aggregate rule and supplemental attribute values for the item, keyed by name.
    writeback_suggestions=[]  # required — The writebacks suggested against this item, as configured by the matching ruleset&#39;s writebackConfigurations. Only ever populated on target-side items. Suggestions only: a user is expected to review them before acting. Required, but may be empty.
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [RecResultHoldingImpact](RecResultHoldingImpact.md) — used in `holding_impacts`
- [WritebackSuggestion](WritebackSuggestion.md) — used in `writeback_suggestions`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

