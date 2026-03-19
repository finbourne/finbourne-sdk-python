# CreateGroupReconciliationComparisonRulesetRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **display_name** | **str** | Required | The name of the ruleset |
| **reconciliation_type** | **str** | Required | The type of reconciliation to perform. \&quot;Holding\&quot; | \&quot;Transaction\&quot; | \&quot;Valuation\&quot; |
| **filters** | [GroupReconciliationFilters](GroupReconciliationFilters.md) | Optional | *No description available.* |
| **core_attribute_rules** | [List[GroupReconciliationCoreAttributeRule]](GroupReconciliationCoreAttributeRule.md) | Required | The core comparison rules |
| **aggregate_attribute_rules** | [List[GroupReconciliationAggregateAttributeRule]](GroupReconciliationAggregateAttributeRule.md) | Required | The aggregate comparison rules |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CreateGroupReconciliationComparisonRulesetRequest import CreateGroupReconciliationComparisonRulesetRequest

instance = CreateGroupReconciliationComparisonRulesetRequest(
    id=ResourceId(...),  # required
    display_name="...",  # required — The name of the ruleset
    reconciliation_type="...",  # required — The type of reconciliation to perform. \&quot;Holding\&quot; | \&quot;Transaction\&quot; | \&quot;Valuation\&quot;
    filters=GroupReconciliationFilters(...),  # optional
    core_attribute_rules=[],  # required — The core comparison rules
    aggregate_attribute_rules=[]  # required — The aggregate comparison rules
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [GroupReconciliationFilters](GroupReconciliationFilters.md)
- [GroupReconciliationCoreAttributeRule](GroupReconciliationCoreAttributeRule.md) — used in `core_attribute_rules`
- [GroupReconciliationAggregateAttributeRule](GroupReconciliationAggregateAttributeRule.md) — used in `aggregate_attribute_rules`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

