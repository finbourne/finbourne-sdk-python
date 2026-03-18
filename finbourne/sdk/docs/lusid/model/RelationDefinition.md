# RelationDefinition

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **relation_definition_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **source_entity_domain** | **str** | Optional | The entity domain of the source entity object. |
| **target_entity_domain** | **str** | Optional | The entity domain of the target entity object. |
| **display_name** | **str** | Optional | The display name of the relation. |
| **outward_description** | **str** | Optional | The description to relate source entity object and target entity object |
| **inward_description** | **str** | Optional | The description to relate target entity object and source entity object |
| **life_time** | **str** | Optional | Describes how the relations can change over time, allowed values are \&quot;Perpetual\&quot; and \&quot;TimeVariant\&quot; |
| **constraint_style** | **str** | Optional | Describes the uniqueness and cardinality for relations with a specific source entity object and relations under this definition. Allowed values are \&quot;Property\&quot; and \&quot;Collection\&quot;, defaults to \&quot;Collection\&quot; if not specified. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RelationDefinition import RelationDefinition

instance = RelationDefinition(
    version=Version(...),  # optional
    relation_definition_id=ResourceId(...),  # optional
    source_entity_domain="...",  # optional — The entity domain of the source entity object.
    target_entity_domain="...",  # optional — The entity domain of the target entity object.
    display_name="...",  # optional — The display name of the relation.
    outward_description="...",  # optional — The description to relate source entity object and target entity object
    inward_description="...",  # optional — The description to relate target entity object and source entity object
    life_time="...",  # optional — Describes how the relations can change over time, allowed values are \&quot;Perpetual\&quot; and \&quot;TimeVariant\&quot;
    constraint_style="...",  # optional — Describes the uniqueness and cardinality for relations with a specific source entity object and relations under this definition. Allowed values are \&quot;Property\&quot; and \&quot;Collection\&quot;, defaults to \&quot;Collection\&quot; if not specified.
    links=[]  # optional
)
```


## Related Models

- [Version](Version.md)
- [ResourceId](ResourceId.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

