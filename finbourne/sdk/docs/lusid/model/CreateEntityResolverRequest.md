# CreateEntityResolverRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **entity_type** | **str** | Required | The entity type that a specific resolution configuration is applicable to (e.g. Instrument). |
| **description** | **str** | Optional | Describes what this specific identifier order is used for. |
| **identifier_matching_order** | [List[IdentifierForResolution]](IdentifierForResolution.md) | Required | Ordered collection of related identifier keys that are used to define which identifier takes priority in resolving an entity. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CreateEntityResolverRequest import CreateEntityResolverRequest

instance = CreateEntityResolverRequest(
    id=ResourceId(...),  # required
    entity_type="...",  # required — The entity type that a specific resolution configuration is applicable to (e.g. Instrument).
    description="...",  # optional — Describes what this specific identifier order is used for.
    identifier_matching_order=[]  # required — Ordered collection of related identifier keys that are used to define which identifier takes priority in resolving an entity.
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [IdentifierForResolution](IdentifierForResolution.md) — used in `identifier_matching_order`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

