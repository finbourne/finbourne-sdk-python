# RecResultRelationalDataItem

A relational data point item within a rec result: one row of a relational dataset. The dataset and the unique  id of the data point identify the row. All rec types use this item shape.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **relational_dataset_definition_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **relational_data_point_unique_id** | **str** | Required | The unique id of the relational data point the run read, as minted by the relational dataset store. Opaque: compare it whole, do not parse it. |
| **item_type** | **str** | Required | The polymorphic item-type discriminator: Holding, ValuedHolding, Transaction, SettlementActivity or RelationalDataPoint. Names the item rather than the rec type: Holding and CashHolding recs produce Holding items, a Valuation rec produces ValuedHolding items, both transaction rec types produce Transaction items, and a relational dataset side produces RelationalDataPoint items whatever the rec type. Available values: SettlementActivity, Holding, Transaction, ValuedHolding, RelationalDataPoint. |
| **rule_and_attribute_values** | **Dict[str, Optional[str]]** | Optional | The core rule, aggregate rule and supplemental attribute values for the item, keyed by name. |
| **writeback_suggestions** | [List[WritebackSuggestion]](WritebackSuggestion.md) | Required | The writebacks suggested against this item, as configured by the matching ruleset&#39;s writebackConfigurations. Only ever populated on target-side items. Suggestions only: a user is expected to review them before acting. Required, but may be empty. *(read-only)* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RecResultRelationalDataItem import RecResultRelationalDataItem

instance = RecResultRelationalDataItem(
    relational_dataset_definition_id=ResourceId(...),  # required
    relational_data_point_unique_id="...",  # required — The unique id of the relational data point the run read, as minted by the relational dataset store. Opaque: compare it whole, do not parse it.
    item_type="...",  # required — The polymorphic item-type discriminator: Holding, ValuedHolding, Transaction, SettlementActivity or RelationalDataPoint. Names the item rather than the rec type: Holding and CashHolding recs produce Holding items, a Valuation rec produces ValuedHolding items, both transaction rec types produce Transaction items, and a relational dataset side produces RelationalDataPoint items whatever the rec type. Available values: SettlementActivity, Holding, Transaction, ValuedHolding, RelationalDataPoint.
    rule_and_attribute_values=,  # optional — The core rule, aggregate rule and supplemental attribute values for the item, keyed by name.
    writeback_suggestions=[]  # required — The writebacks suggested against this item, as configured by the matching ruleset&#39;s writebackConfigurations. Only ever populated on target-side items. Suggestions only: a user is expected to review them before acting. Required, but may be empty.
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [WritebackSuggestion](WritebackSuggestion.md) — used in `writeback_suggestions`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

