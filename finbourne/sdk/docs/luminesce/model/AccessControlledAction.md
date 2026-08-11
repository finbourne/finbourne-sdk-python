# AccessControlledAction

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **description** | **str** | Optional | *No description available.* |
| **action** | [ActionId](ActionId.md) | Optional | *No description available.* |
| **limited_set** | [List[IdSelectorDefinition]](IdSelectorDefinition.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.luminesce.models.AccessControlledAction import AccessControlledAction

instance = AccessControlledAction(
    description="...",  # optional
    action=ActionId(...),  # optional
    limited_set=[]  # optional
)
```

- [ActionId](ActionId.md)
- [IdSelectorDefinition](IdSelectorDefinition.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

