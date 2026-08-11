# GroupReconciliationAggregateAttributeRule

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **left** | [GroupReconciliationAggregateComparisonRuleOperand](GroupReconciliationAggregateComparisonRuleOperand.md) | Required | *No description available.* |
| **right** | [GroupReconciliationAggregateComparisonRuleOperand](GroupReconciliationAggregateComparisonRuleOperand.md) | Required | *No description available.* |
| **tolerance** | [GroupReconciliationComparisonRuleTolerance](GroupReconciliationComparisonRuleTolerance.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.GroupReconciliationAggregateAttributeRule import GroupReconciliationAggregateAttributeRule

instance = GroupReconciliationAggregateAttributeRule(
    left=GroupReconciliationAggregateComparisonRuleOperand(...),  # required
    right=GroupReconciliationAggregateComparisonRuleOperand(...),  # required
    tolerance=GroupReconciliationComparisonRuleTolerance(...)  # optional
)
```


## Related Models

- [GroupReconciliationAggregateComparisonRuleOperand](GroupReconciliationAggregateComparisonRuleOperand.md)
- [GroupReconciliationAggregateComparisonRuleOperand](GroupReconciliationAggregateComparisonRuleOperand.md)
- [GroupReconciliationComparisonRuleTolerance](GroupReconciliationComparisonRuleTolerance.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

