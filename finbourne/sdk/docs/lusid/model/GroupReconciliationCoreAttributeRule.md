# GroupReconciliationCoreAttributeRule

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **left** | [GroupReconciliationCoreComparisonRuleOperand](GroupReconciliationCoreComparisonRuleOperand.md) | Required | *No description available.* |
| **right** | [GroupReconciliationCoreComparisonRuleOperand](GroupReconciliationCoreComparisonRuleOperand.md) | Required | *No description available.* |
| **allowable_string_mappings** | [List[GroupReconciliationComparisonRuleStringValueMap]](GroupReconciliationComparisonRuleStringValueMap.md) | Optional | The string mappings to use when comparing |
| **is_comparison_case_sensitive** | **bool** | Required | Whether the compare keys and strings mappings case sensitive or not |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.GroupReconciliationCoreAttributeRule import GroupReconciliationCoreAttributeRule

instance = GroupReconciliationCoreAttributeRule(
    left=GroupReconciliationCoreComparisonRuleOperand(...),  # required
    right=GroupReconciliationCoreComparisonRuleOperand(...),  # required
    allowable_string_mappings=[],  # optional — The string mappings to use when comparing
    is_comparison_case_sensitive=True  # required — Whether the compare keys and strings mappings case sensitive or not
)
```


## Related Models

- [GroupReconciliationCoreComparisonRuleOperand](GroupReconciliationCoreComparisonRuleOperand.md)
- [GroupReconciliationCoreComparisonRuleOperand](GroupReconciliationCoreComparisonRuleOperand.md)
- [GroupReconciliationComparisonRuleStringValueMap](GroupReconciliationComparisonRuleStringValueMap.md) — used in `allowable_string_mappings`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

