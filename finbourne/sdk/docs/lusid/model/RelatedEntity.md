# RelatedEntity

Information about the other related entity in the relationship
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **entity_type** | **str** | Required | The type of the entity. |
| **entity_id** | **Dict[str, Optional[str]]** | Required | The identifier of the other related entity in the relationship. It contains &#39;scope&#39; and &#39;code&#39; as keys for identifiers of a Portfolio or Portfolio Group, or &#39;idTypeScope&#39;, &#39;idTypeCode&#39;, &#39;code&#39; as keys for identifiers of a Person or Legal entity, or &#39;scope&#39;, &#39;identifierType&#39;, &#39;identifierValue&#39; as keys for identifiers of an Instrument |
| **display_name** | **str** | Required | The display name of the entity. |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | The properties of the entity. This field is empty until further notice. |
| **scope** | **str** | Optional | The scope of the identifier |
| **lusid_unique_id** | [LusidUniqueId](LusidUniqueId.md) | Optional | *No description available.* |
| **identifiers** | [List[EntityIdentifier]](EntityIdentifier.md) | Required | The identifiers of the related entity in the relationship. |
| **href** | **str** | Optional | The link to the entity. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RelatedEntity import RelatedEntity

instance = RelatedEntity(
    entity_type="...",  # required — The type of the entity.
    entity_id=,  # required — The identifier of the other related entity in the relationship. It contains &#39;scope&#39; and &#39;code&#39; as keys for identifiers of a Portfolio or Portfolio Group, or &#39;idTypeScope&#39;, &#39;idTypeCode&#39;, &#39;code&#39; as keys for identifiers of a Person or Legal entity, or &#39;scope&#39;, &#39;identifierType&#39;, &#39;identifierValue&#39; as keys for identifiers of an Instrument
    display_name="...",  # required — The display name of the entity.
    properties=ModelProperty(...),  # optional — The properties of the entity. This field is empty until further notice.
    scope="...",  # optional — The scope of the identifier
    lusid_unique_id=LusidUniqueId(...),  # optional
    identifiers=[],  # required — The identifiers of the related entity in the relationship.
    href="..."  # optional — The link to the entity.
)
```

- [ModelProperty](ModelProperty.md) — used in `properties`
- [LusidUniqueId](LusidUniqueId.md)
- [EntityIdentifier](EntityIdentifier.md) — used in `identifiers`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

