# ResourceListOfGetRecipeResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **values** | [List[GetRecipeResponse]](GetRecipeResponse.md) | Required | *No description available.* |
| **href** | **str** | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |
| **next_page** | **str** | Optional | *No description available.* |
| **previous_page** | **str** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ResourceListOfGetRecipeResponse import ResourceListOfGetRecipeResponse

instance = ResourceListOfGetRecipeResponse(
    values=[],  # required
    href="...",  # optional
    links=[],  # optional
    next_page="...",  # optional
    previous_page="..."  # optional
)
```


## Related Models

- [GetRecipeResponse](GetRecipeResponse.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

