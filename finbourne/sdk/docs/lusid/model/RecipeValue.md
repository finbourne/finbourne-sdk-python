# RecipeValue

Recipe value represents a data that is then used to perform an atomic operation which is then used in composition of Configuration Recipe.  This object either includes the data itself (in json form or as simple string) or is a reference where the data can be obtained from (from a Configuration Recipe say).  Only one field is to be populated.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **as_json** | **str** | Optional | Field to allow providing a potentially complex json value. |
| **as_string** | **str** | Optional | For simple value, a single input value, note complex nested objects are not allowed here. |
| **from_recipe** | [FromRecipe](FromRecipe.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RecipeValue import RecipeValue

instance = RecipeValue(
    as_json="...",  # optional — Field to allow providing a potentially complex json value.
    as_string="...",  # optional — For simple value, a single input value, note complex nested objects are not allowed here.
    from_recipe=FromRecipe(...)  # optional
)
```

- [FromRecipe](FromRecipe.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

