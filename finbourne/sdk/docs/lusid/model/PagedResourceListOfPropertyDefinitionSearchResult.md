# PagedResourceListOfPropertyDefinitionSearchResult

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **next_page** | **str** | Optional | *No description available.* |
| **previous_page** | **str** | Optional | *No description available.* |
| **values** | [List[PropertyDefinitionSearchResult]](PropertyDefinitionSearchResult.md) | Required | *No description available.* |
| **href** | **str** | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PagedResourceListOfPropertyDefinitionSearchResult import PagedResourceListOfPropertyDefinitionSearchResult

instance = PagedResourceListOfPropertyDefinitionSearchResult(
    next_page="...",  # optional
    previous_page="...",  # optional
    values=[],  # required
    href="...",  # optional
    links=[]  # optional
)
```

- [PropertyDefinitionSearchResult](PropertyDefinitionSearchResult.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

