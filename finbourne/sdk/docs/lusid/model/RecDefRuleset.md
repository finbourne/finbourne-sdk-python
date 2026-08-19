# RecDefRuleset

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **rec_type** | **str** | Required | The type of reconciliation this entry configures. Must be valid for the definitionType, and must match the reconciliationType of the referenced matching ruleset. Available values: Holding, CashHolding, Valuation, InputTransaction, OutputTransaction, SettlementActivity. |
| **matching_ruleset_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **relational_data_filter** | **str** | Optional | Selects the slice of the relational dataset this definition draws from, e.g. \&quot;custodian eq &#39;NT&#39;\&quot;. Only permitted when the referenced ruleset declares a relational side, and combined with AND at run time with that ruleset&#39;s own filter for the side. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RecDefRuleset import RecDefRuleset

instance = RecDefRuleset(
    rec_type="...",  # required — The type of reconciliation this entry configures. Must be valid for the definitionType, and must match the reconciliationType of the referenced matching ruleset. Available values: Holding, CashHolding, Valuation, InputTransaction, OutputTransaction, SettlementActivity.
    matching_ruleset_id=ResourceId(...),  # required
    relational_data_filter="..."  # optional — Selects the slice of the relational dataset this definition draws from, e.g. \&quot;custodian eq &#39;NT&#39;\&quot;. Only permitted when the referenced ruleset declares a relational side, and combined with AND at run time with that ruleset&#39;s own filter for the side.
)
```

- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

