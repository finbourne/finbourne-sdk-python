# RecipeBlock

An atomic operation used in Recipe composer to compose a Configuration Recipe
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **value** | [RecipeValue](RecipeValue.md) | Optional | *No description available.* |
| **path** | **str** | Optional | Path of the Value that the operation is to be performed on. |
| **op** | **str** | Optional | Operation to be performed on the part of the value. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RecipeBlock import RecipeBlock

instance = RecipeBlock(
    value=RecipeValue(...),  # optional
    path="...",  # optional — Path of the Value that the operation is to be performed on.
    op="..."  # optional — Operation to be performed on the part of the value.
)
```


## Related Models

- [RecipeValue](RecipeValue.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

