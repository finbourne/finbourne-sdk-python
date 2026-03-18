# CreateRecipeRequest

Specification class to request for the creation/supplementing of a configuration recipe
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **recipe_creation_market_data_scopes** | **List[str]** | Required | The scopes in which the recipe creation would look for quotes/data. |
| **recipe_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **inline_recipe** | [ConfigurationRecipe](ConfigurationRecipe.md) | Optional | *No description available.* |
| **as_at** | **datetime** | Optional | The asAt date to use |
| **effective_at** | **str** | Required | The market data time, i.e. the recipe generated will look for rules with this effectiveAt. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CreateRecipeRequest import CreateRecipeRequest

instance = CreateRecipeRequest(
    recipe_creation_market_data_scopes=,  # required — The scopes in which the recipe creation would look for quotes/data.
    recipe_id=ResourceId(...),  # optional
    inline_recipe=ConfigurationRecipe(...),  # optional
    as_at=datetime.now(),  # optional — The asAt date to use
    effective_at="..."  # required — The market data time, i.e. the recipe generated will look for rules with this effectiveAt.
)
```

- [ResourceId](ResourceId.md)
- [ConfigurationRecipe](ConfigurationRecipe.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

