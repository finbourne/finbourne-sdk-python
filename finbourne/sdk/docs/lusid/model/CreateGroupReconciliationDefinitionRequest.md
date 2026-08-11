# CreateGroupReconciliationDefinitionRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **display_name** | **str** | Required | The name of the Group Reconciliation Definition |
| **description** | **str** | Optional | The description of the Group Reconciliation Definition |
| **portfolio_entity_ids** | [GroupReconciliationDefinitionPortfolioEntityIds](GroupReconciliationDefinitionPortfolioEntityIds.md) | Required | *No description available.* |
| **recipe_ids** | [GroupReconciliationDefinitionRecipeIds](GroupReconciliationDefinitionRecipeIds.md) | Optional | *No description available.* |
| **currencies** | [GroupReconciliationDefinitionCurrencies](GroupReconciliationDefinitionCurrencies.md) | Optional | *No description available.* |
| **transaction_date_windows** | [TransactionDateWindows](TransactionDateWindows.md) | Optional | *No description available.* |
| **comparison_ruleset_ids** | [GroupReconciliationDefinitionComparisonRulesetIds](GroupReconciliationDefinitionComparisonRulesetIds.md) | Optional | *No description available.* |
| **break_code_source** | [BreakCodeSource](BreakCodeSource.md) | Optional | *No description available.* |
| **primary_schedule** | [PrimarySchedule](PrimarySchedule.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CreateGroupReconciliationDefinitionRequest import CreateGroupReconciliationDefinitionRequest

instance = CreateGroupReconciliationDefinitionRequest(
    id=ResourceId(...),  # optional
    display_name="...",  # required — The name of the Group Reconciliation Definition
    description="...",  # optional — The description of the Group Reconciliation Definition
    portfolio_entity_ids=GroupReconciliationDefinitionPortfolioEntityIds(...),  # required
    recipe_ids=GroupReconciliationDefinitionRecipeIds(...),  # optional
    currencies=GroupReconciliationDefinitionCurrencies(...),  # optional
    transaction_date_windows=TransactionDateWindows(...),  # optional
    comparison_ruleset_ids=GroupReconciliationDefinitionComparisonRulesetIds(...),  # optional
    break_code_source=BreakCodeSource(...),  # optional
    primary_schedule=PrimarySchedule(...)  # optional
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


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

