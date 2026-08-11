# CustomEntityDefinition

Representation of Custom Entity Definition on LUSID API
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **entity_type_name** | **str** | Required | The name provided when the custom entity type was created. This has been prefixed with “~” and returned as “entityType”, which is the identifier for the custom entity type. |
| **display_name** | **str** | Required | A display label for the custom entity type. |
| **description** | **str** | Optional | A description for the custom entity type. |
| **entity_type** | **str** | Required | The identifier for the custom entity type, derived from the “entityTypeName” provided on creation. |
| **field_schema** | [List[CustomEntityFieldDefinition]](CustomEntityFieldDefinition.md) | Required | The description of the fields on the custom entity type. |
| **version** | [Version](Version.md) | Required | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CustomEntityDefinition import CustomEntityDefinition

instance = CustomEntityDefinition(
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    entity_type_name="...",  # required — The name provided when the custom entity type was created. This has been prefixed with “~” and returned as “entityType”, which is the identifier for the custom entity type.
    display_name="...",  # required — A display label for the custom entity type.
    description="...",  # optional — A description for the custom entity type.
    entity_type="...",  # required — The identifier for the custom entity type, derived from the “entityTypeName” provided on creation.
    field_schema=[],  # required — The description of the fields on the custom entity type.
    version=Version(...),  # required
    links=[]  # optional
)
```

- [CustomEntityFieldDefinition](CustomEntityFieldDefinition.md) — used in `field_schema`
- [Version](Version.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

