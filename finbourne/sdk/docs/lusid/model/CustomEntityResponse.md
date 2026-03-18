# CustomEntityResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **entity_type** | **str** | Required | The type of custom entity this is. |
| **version** | [Version](Version.md) | Required | *No description available.* |
| **staged_modifications** | [StagedModificationsInfo](StagedModificationsInfo.md) | Optional | *No description available.* |
| **display_name** | **str** | Required | A display label for the custom entity. |
| **description** | **str** | Optional | A description of the custom entity. |
| **identifiers** | [List[CustomEntityId]](CustomEntityId.md) | Required | The identifiers the custom entity will be upserted with. |
| **fields** | [List[CustomEntityField]](CustomEntityField.md) | Required | The fields that decorate the custom entity. |
| **relationships** | [List[Relationship]](Relationship.md) | Required | A set of relationships associated to the custom entity. |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | The properties that decorate the custom entity. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CustomEntityResponse import CustomEntityResponse

instance = CustomEntityResponse(
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    entity_type="...",  # required — The type of custom entity this is.
    version=Version(...),  # required
    staged_modifications=StagedModificationsInfo(...),  # optional
    display_name="...",  # required — A display label for the custom entity.
    description="...",  # optional — A description of the custom entity.
    identifiers=[],  # required — The identifiers the custom entity will be upserted with.
    fields=[],  # required — The fields that decorate the custom entity.
    relationships=[],  # required — A set of relationships associated to the custom entity.
    properties=ModelProperty(...),  # optional — The properties that decorate the custom entity.
    links=[]  # optional
)
```

- [Version](Version.md)
- [StagedModificationsInfo](StagedModificationsInfo.md)
- [CustomEntityId](CustomEntityId.md) — used in `identifiers`
- [CustomEntityField](CustomEntityField.md) — used in `fields`
- [Relationship](Relationship.md) — used in `relationships`
- [ModelProperty](ModelProperty.md) — used in `properties`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

