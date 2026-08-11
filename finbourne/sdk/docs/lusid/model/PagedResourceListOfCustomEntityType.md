# PagedResourceListOfCustomEntityType

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **next_page** | **str** | Optional | *No description available.* |
| **previous_page** | **str** | Optional | *No description available.* |
| **values** | [List[CustomEntityType]](CustomEntityType.md) | Required | *No description available.* |
| **href** | **str** | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PagedResourceListOfCustomEntityType import PagedResourceListOfCustomEntityType

instance = PagedResourceListOfCustomEntityType(
    next_page="...",  # optional
    previous_page="...",  # optional
    values=[],  # required
    href="...",  # optional
    links=[]  # optional
)
```

- [CustomEntityType](CustomEntityType.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

