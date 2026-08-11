# AccessControlledResource

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **application** | **str** | Optional | *No description available.* |
| **name** | **str** | Optional | *No description available.* |
| **description** | **str** | Required | *No description available.* |
| **actions** | [List[AccessControlledAction]](AccessControlledAction.md) | Required | *No description available.* |
| **identifier_parts** | [List[IdentifierPartSchema]](IdentifierPartSchema.md) | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.notifications.models.AccessControlledResource import AccessControlledResource

instance = AccessControlledResource(
    application="...",  # optional
    name="...",  # optional
    description="...",  # required
    actions=[],  # required
    identifier_parts=[],  # optional
    links=[]  # optional
)
```

- [AccessControlledAction](AccessControlledAction.md)
- [IdentifierPartSchema](IdentifierPartSchema.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

