# GroupReconciliationDefinition

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [../model/ResourceId](ResourceId.md) | Optional | *No description available.* |
| **display_name** | **str** | Optional | The name of the Group Reconciliation Definition |
| **description** | **str** | Optional | The description of the Group Reconciliation Definition |
| **portfolio_entity_ids** | [../model/GroupReconciliationDefinitionPortfolioEntityIds](GroupReconciliationDefinitionPortfolioEntityIds.md) | Optional | *No description available.* |
| **recipe_ids** | [../model/GroupReconciliationDefinitionRecipeIds](GroupReconciliationDefinitionRecipeIds.md) | Optional | *No description available.* |
| **currencies** | [../model/GroupReconciliationDefinitionCurrencies](GroupReconciliationDefinitionCurrencies.md) | Optional | *No description available.* |
| **transaction_date_windows** | [../model/TransactionDateWindows](TransactionDateWindows.md) | Optional | *No description available.* |
| **comparison_ruleset_ids** | [../model/GroupReconciliationDefinitionComparisonRulesetIds](GroupReconciliationDefinitionComparisonRulesetIds.md) | Optional | *No description available.* |
| **break_code_source** | [../model/BreakCodeSource](BreakCodeSource.md) | Optional | *No description available.* |
| **primary_schedule** | [../model/PrimarySchedule](PrimarySchedule.md) | Optional | *No description available.* |
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **version** | [../model/Version](Version.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.GroupReconciliationDefinition import GroupReconciliationDefinition

instance = GroupReconciliationDefinition(
    id=ResourceId(...),  # optional
    display_name="...",  # optional — The name of the Group Reconciliation Definition
    description="...",  # optional — The description of the Group Reconciliation Definition
    portfolio_entity_ids=GroupReconciliationDefinitionPortfolioEntityIds(...),  # optional
    recipe_ids=GroupReconciliationDefinitionRecipeIds(...),  # optional
    currencies=GroupReconciliationDefinitionCurrencies(...),  # optional
    transaction_date_windows=TransactionDateWindows(...),  # optional
    comparison_ruleset_ids=GroupReconciliationDefinitionComparisonRulesetIds(...),  # optional
    break_code_source=BreakCodeSource(...),  # optional
    primary_schedule=PrimarySchedule(...),  # optional
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    version=Version(...)  # optional
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [GroupReconciliationDefinitionPortfolioEntityIds](GroupReconciliationDefinitionPortfolioEntityIds.md)
- [GroupReconciliationDefinitionRecipeIds](GroupReconciliationDefinitionRecipeIds.md)
- [GroupReconciliationDefinitionCurrencies](GroupReconciliationDefinitionCurrencies.md)
- [TransactionDateWindows](TransactionDateWindows.md)
- [GroupReconciliationDefinitionComparisonRulesetIds](GroupReconciliationDefinitionComparisonRulesetIds.md)
- [BreakCodeSource](BreakCodeSource.md)
- [PrimarySchedule](PrimarySchedule.md)
- [Version](Version.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

