# RecipeComposer

Recipe composer is an object used to dynamically compose Configuration Recipe from atomic operations.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **scope** | **str** | Required | The scope used when updating or inserting the Recipe Composer. |
| **code** | **str** | Required | User given string name (code) to identify the recipe. |
| **operations** | [List[RecipeBlock]](RecipeBlock.md) | Optional | Atomic operations used to compose a Configuration Recipe. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RecipeComposer import RecipeComposer

instance = RecipeComposer(
    scope="...",  # required — The scope used when updating or inserting the Recipe Composer.
    code="...",  # required — User given string name (code) to identify the recipe.
    operations=[]  # optional — Atomic operations used to compose a Configuration Recipe.
)
```

- [RecipeBlock](RecipeBlock.md) — used in `operations`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

