# AccessControlledAction

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **description** | **str** | Required | *No description available.* |
| **action** | [ActionId](ActionId.md) | Required | *No description available.* |
| **limited_set** | [List[IdSelectorDefinition]](IdSelectorDefinition.md) | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AccessControlledAction import AccessControlledAction

instance = AccessControlledAction(
    description="...",  # required
    action=ActionId(...),  # required
    limited_set=[],  # optional
    links=[]  # optional
)
```

- [ActionId](ActionId.md)
- [IdSelectorDefinition](IdSelectorDefinition.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

