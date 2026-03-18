# GroupReconciliationComparisonRuleset

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **display_name** | **str** | Required | The name of the ruleset |
| **reconciliation_type** | **str** | Required | The type of reconciliation to perform. \&quot;Holding\&quot; | \&quot;Transaction\&quot; | \&quot;Valuation\&quot; |
| **core_attribute_rules** | [List[GroupReconciliationCoreAttributeRule]](GroupReconciliationCoreAttributeRule.md) | Required | The core comparison rules |
| **aggregate_attribute_rules** | [List[GroupReconciliationAggregateAttributeRule]](GroupReconciliationAggregateAttributeRule.md) | Required | The aggregate comparison rules |
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.GroupReconciliationComparisonRuleset import GroupReconciliationComparisonRuleset

instance = GroupReconciliationComparisonRuleset(
    id=ResourceId(...),  # required
    display_name="...",  # required — The name of the ruleset
    reconciliation_type="...",  # required — The type of reconciliation to perform. \&quot;Holding\&quot; | \&quot;Transaction\&quot; | \&quot;Valuation\&quot;
    core_attribute_rules=[],  # required — The core comparison rules
    aggregate_attribute_rules=[],  # required — The aggregate comparison rules
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    version=Version(...),  # optional
    links=[]  # optional
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [GroupReconciliationCoreAttributeRule](GroupReconciliationCoreAttributeRule.md) — used in `core_attribute_rules`
- [GroupReconciliationAggregateAttributeRule](GroupReconciliationAggregateAttributeRule.md) — used in `aggregate_attribute_rules`
- [Version](Version.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

