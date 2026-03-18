# UpsertRecipeRequest

A recipe that is to be stored in the recipe structured data store.  Only one of these must be present.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **configuration_recipe** | [ConfigurationRecipe](ConfigurationRecipe.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpsertRecipeRequest import UpsertRecipeRequest

instance = UpsertRecipeRequest(
    configuration_recipe=ConfigurationRecipe(...)  # optional
)
```


## Related Models

- [ConfigurationRecipe](ConfigurationRecipe.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

