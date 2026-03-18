# CustomEntityProperties

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Required | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **entity_type** | **str** | Required | The type of custom entity this is. |
| **identifiers** | [List[CustomEntityId]](CustomEntityId.md) | Required | The identifiers the custom entity will be upserted with. |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | The properties that decorate the custom entity. |
| **version** | [Version](Version.md) | Required | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CustomEntityProperties import CustomEntityProperties

instance = CustomEntityProperties(
    href="...",  # required — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    entity_type="...",  # required — The type of custom entity this is.
    identifiers=[],  # required — The identifiers the custom entity will be upserted with.
    properties=ModelProperty(...),  # optional — The properties that decorate the custom entity.
    version=Version(...),  # required
    links=[]  # optional
)
```

- [CustomEntityId](CustomEntityId.md) — used in `identifiers`
- [ModelProperty](ModelProperty.md) — used in `properties`
- [Version](Version.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

