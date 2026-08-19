# MatchingRuleset

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **display_name** | **str** | Required | The name of the matching ruleset. |
| **rec_type** | **str** | Required | The type of reconciliation to perform. Available values: Holding, CashHolding, Valuation, InputTransaction, OutputTransaction, SettlementActivity. |
| **dataset_schemas** | [RecDatasetSchemas](RecDatasetSchemas.md) | Required | *No description available.* |
| **filters** | [GroupReconciliationFilters](GroupReconciliationFilters.md) | Optional | *No description available.* |
| **core_rules** | [List[CoreMatchingRule]](CoreMatchingRule.md) | Required | The core comparison rules evaluated as derivation formulae against each side of the reconciliation. |
| **aggregate_rules** | [List[AggregateMatchingRule]](AggregateMatchingRule.md) | Required | The aggregate comparison rules evaluated as derivation formulae against values on each side of the reconciliation and operation to aggregate those values. |
| **core_tolerances** | [List[ToleranceBase]](ToleranceBase.md) | Optional | Tolerance configurations applied to core rule matching, in the specified order. |
| **aggregate_tolerances** | [List[ToleranceBase]](ToleranceBase.md) | Optional | Tolerance configurations applied to aggregate rule matching. |
| **allow_partial_matching** | **bool** | Optional | Whether to permit partial matches when applying rules. |
| **supplemental_attributes** | [List[SupplementalAttribute]](SupplementalAttribute.md) | Optional | Supplemental attributes that decorate reconciliation results with additional values without participating in the reconciliation itself. |
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.MatchingRuleset import MatchingRuleset

instance = MatchingRuleset(
    id=ResourceId(...),  # required
    display_name="...",  # required — The name of the matching ruleset.
    rec_type="...",  # required — The type of reconciliation to perform. Available values: Holding, CashHolding, Valuation, InputTransaction, OutputTransaction, SettlementActivity.
    dataset_schemas=RecDatasetSchemas(...),  # required
    filters=GroupReconciliationFilters(...),  # optional
    core_rules=[],  # required — The core comparison rules evaluated as derivation formulae against each side of the reconciliation.
    aggregate_rules=[],  # required — The aggregate comparison rules evaluated as derivation formulae against values on each side of the reconciliation and operation to aggregate those values.
    core_tolerances=[],  # optional — Tolerance configurations applied to core rule matching, in the specified order.
    aggregate_tolerances=[],  # optional — Tolerance configurations applied to aggregate rule matching.
    allow_partial_matching=True,  # optional — Whether to permit partial matches when applying rules.
    supplemental_attributes=[],  # optional — Supplemental attributes that decorate reconciliation results with additional values without participating in the reconciliation itself.
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    version=Version(...),  # optional
    links=[]  # optional
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [RecDatasetSchemas](RecDatasetSchemas.md)
- [GroupReconciliationFilters](GroupReconciliationFilters.md)
- [CoreMatchingRule](CoreMatchingRule.md) — used in `core_rules`
- [AggregateMatchingRule](AggregateMatchingRule.md) — used in `aggregate_rules`
- [ToleranceBase](ToleranceBase.md) — used in `core_tolerances`
- [ToleranceBase](ToleranceBase.md) — used in `aggregate_tolerances`
- [SupplementalAttribute](SupplementalAttribute.md) — used in `supplemental_attributes`
- [Version](Version.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

