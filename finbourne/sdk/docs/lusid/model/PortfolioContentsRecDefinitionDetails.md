# PortfolioContentsRecDefinitionDetails

A definition reconciling the contents of LUSID portfolios on at least one side, with a relational dataset  permitted on the other.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **left_portfolio_sources** | [List[RecDefSource]](RecDefSource.md) | Required | The portfolios, portfolio groups and funds contributing to the left side. Empty when the left side draws on relational data instead, which requires every ruleset to declare relational data for that side. Both sides cannot be empty. |
| **right_portfolio_sources** | [List[RecDefSource]](RecDefSource.md) | Required | The portfolios, portfolio groups and funds contributing to the right side. Empty when the right side draws on relational data instead, which requires every ruleset to declare relational data for that side. Both sides cannot be empty. |
| **valuation_recipes** | [RecDefRecipeIds](RecDefRecipeIds.md) | Optional | *No description available.* |
| **currencies** | [RecDefCurrencies](RecDefCurrencies.md) | Optional | *No description available.* |
| **rulesets** | [List[RecDefRuleset]](RecDefRuleset.md) | Required | The types of reconciliation included in the group, each naming the matching ruleset that drives it. At least one entry is required, and each rec type may appear at most once. |
| **definition_type** | **str** | Required | What this definition reconciles, and so which shape of details it carries. PortfolioContents and External are supported; LusidEntity is not yet. Available values: PortfolioContents, LusidEntity, External. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PortfolioContentsRecDefinitionDetails import PortfolioContentsRecDefinitionDetails

instance = PortfolioContentsRecDefinitionDetails(
    left_portfolio_sources=[],  # required — The portfolios, portfolio groups and funds contributing to the left side. Empty when the left side draws on relational data instead, which requires every ruleset to declare relational data for that side. Both sides cannot be empty.
    right_portfolio_sources=[],  # required — The portfolios, portfolio groups and funds contributing to the right side. Empty when the right side draws on relational data instead, which requires every ruleset to declare relational data for that side. Both sides cannot be empty.
    valuation_recipes=RecDefRecipeIds(...),  # optional
    currencies=RecDefCurrencies(...),  # optional
    rulesets=[],  # required — The types of reconciliation included in the group, each naming the matching ruleset that drives it. At least one entry is required, and each rec type may appear at most once.
    definition_type="..."  # required — What this definition reconciles, and so which shape of details it carries. PortfolioContents and External are supported; LusidEntity is not yet. Available values: PortfolioContents, LusidEntity, External.
)
```


## Related Models

- [RecDefSource](RecDefSource.md) — used in `left_portfolio_sources`
- [RecDefSource](RecDefSource.md) — used in `right_portfolio_sources`
- [RecDefRecipeIds](RecDefRecipeIds.md)
- [RecDefCurrencies](RecDefCurrencies.md)
- [RecDefRuleset](RecDefRuleset.md) — used in `rulesets`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

