# EntityResolver

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **entity_type** | **str** | Required | The entity type that a specific resolution configuration is applicable to (e.g. Instrument). |
| **description** | **str** | Optional | Describes what this specific identifier order is used for. |
| **identifier_matching_order** | [List[IdentifierForResolution]](IdentifierForResolution.md) | Required | Ordered collection of related identifier keys that are used to define which identifier takes priority in resolving an entity. |
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.EntityResolver import EntityResolver

instance = EntityResolver(
    id=ResourceId(...),  # required
    entity_type="...",  # required — The entity type that a specific resolution configuration is applicable to (e.g. Instrument).
    description="...",  # optional — Describes what this specific identifier order is used for.
    identifier_matching_order=[],  # required — Ordered collection of related identifier keys that are used to define which identifier takes priority in resolving an entity.
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    version=Version(...),  # optional
    links=[]  # optional
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [IdentifierForResolution](IdentifierForResolution.md) — used in `identifier_matching_order`
- [Version](Version.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

