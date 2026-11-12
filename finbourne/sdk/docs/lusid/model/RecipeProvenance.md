# RecipeProvenance

The recipe a fund valuation was priced with, and where it came from. Absent when the fund has no portfolios  at the effective date, as nothing is priced and no recipe is resolved.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **recipe_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **source** | **str** | Optional | Where the recipe came from. &#39;NavType&#39; when it is the recipe on the nominated NAV type&#39;s definition;  &#39;Request&#39; when the request named a recipeId that replaced it for pricing in that request only. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RecipeProvenance import RecipeProvenance

instance = RecipeProvenance(
    recipe_id=ResourceId(...),  # optional
    source="..."  # optional — Where the recipe came from. &#39;NavType&#39; when it is the recipe on the nominated NAV type&#39;s definition;  &#39;Request&#39; when the request named a recipeId that replaced it for pricing in that request only.
)
```


## Related Models

- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

