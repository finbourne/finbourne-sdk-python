# AccessControlledResource

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **application** | **str** | Optional | *No description available.* |
| **name** | **str** | Optional | *No description available.* |
| **description** | **str** | Optional | *No description available.* |
| **actions** | [List[AccessControlledAction]](AccessControlledAction.md) | Optional | *No description available.* |
| **identifier_parts** | [List[AccessControlledResourceIdentifierPartSchemaAttribute]](AccessControlledResourceIdentifierPartSchemaAttribute.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.luminesce.models.AccessControlledResource import AccessControlledResource

instance = AccessControlledResource(
    application="...",  # optional
    name="...",  # optional
    description="...",  # optional
    actions=[],  # optional
    identifier_parts=[]  # optional
)
```

- [AccessControlledAction](AccessControlledAction.md)
- [AccessControlledResourceIdentifierPartSchemaAttribute](AccessControlledResourceIdentifierPartSchemaAttribute.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

