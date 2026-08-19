# UpdateRecDefinitionRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **display_name** | **str** | Required | The name of the rec definition. |
| **description** | **str** | Optional | A description of the rec definition. |
| **definition_type** | **str** | Required | What this definition reconciles, naming the kind of dataset that must be present on at least one side. One of: PortfolioContents, LusidEntity, RelationalData. Only PortfolioContents is currently supported. Available values: PortfolioContents, LusidEntity, RelationalData. |
| **side_names** | [RecDefSideNames](RecDefSideNames.md) | Optional | *No description available.* |
| **left_portfolio_sources** | [List[RecDefSource]](RecDefSource.md) | Optional | The portfolios, portfolio groups and funds contributing to the left side. Empty when the left side draws on relational data instead, which requires every ruleset to declare relational data for that side. Both sides cannot be empty. |
| **right_portfolio_sources** | [List[RecDefSource]](RecDefSource.md) | Optional | The portfolios, portfolio groups and funds contributing to the right side. Empty when the right side draws on relational data instead, which requires every ruleset to declare relational data for that side. Both sides cannot be empty. |
| **valuation_recipes** | [RecDefRecipeIds](RecDefRecipeIds.md) | Optional | *No description available.* |
| **currencies** | [RecDefCurrencies](RecDefCurrencies.md) | Optional | *No description available.* |
| **rulesets** | [List[RecDefRuleset]](RecDefRuleset.md) | Required | The types of reconciliation included in the group, each naming the matching ruleset that drives it. At least one entry is required, and each rec type may appear at most once. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpdateRecDefinitionRequest import UpdateRecDefinitionRequest

instance = UpdateRecDefinitionRequest(
    display_name="...",  # required — The name of the rec definition.
    description="...",  # optional — A description of the rec definition.
    definition_type="...",  # required — What this definition reconciles, naming the kind of dataset that must be present on at least one side. One of: PortfolioContents, LusidEntity, RelationalData. Only PortfolioContents is currently supported. Available values: PortfolioContents, LusidEntity, RelationalData.
    side_names=RecDefSideNames(...),  # optional
    left_portfolio_sources=[],  # optional — The portfolios, portfolio groups and funds contributing to the left side. Empty when the left side draws on relational data instead, which requires every ruleset to declare relational data for that side. Both sides cannot be empty.
    right_portfolio_sources=[],  # optional — The portfolios, portfolio groups and funds contributing to the right side. Empty when the right side draws on relational data instead, which requires every ruleset to declare relational data for that side. Both sides cannot be empty.
    valuation_recipes=RecDefRecipeIds(...),  # optional
    currencies=RecDefCurrencies(...),  # optional
    rulesets=[]  # required — The types of reconciliation included in the group, each naming the matching ruleset that drives it. At least one entry is required, and each rec type may appear at most once.
)
```

- [RecDefSideNames](RecDefSideNames.md)
- [RecDefSource](RecDefSource.md) — used in `left_portfolio_sources`
- [RecDefSource](RecDefSource.md) — used in `right_portfolio_sources`
- [RecDefRecipeIds](RecDefRecipeIds.md)
- [RecDefCurrencies](RecDefCurrencies.md)
- [RecDefRuleset](RecDefRuleset.md) — used in `rulesets`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

