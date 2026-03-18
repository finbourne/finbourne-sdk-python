# RelationshipDefinition

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **relationship_definition_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **source_entity_type** | **str** | Required | The entity type of the source entity object. |
| **target_entity_type** | **str** | Required | The entity type of the target entity object. |
| **display_name** | **str** | Required | The display name of the relationship. |
| **outward_description** | **str** | Required | The description to relate source entity object and target entity object |
| **inward_description** | **str** | Required | The description to relate target entity object and source entity object |
| **life_time** | **str** | Required | Describes how the relationships can change over time. |
| **relationship_cardinality** | **str** | Required | Describes the cardinality of the relationship between source entity and target entity. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RelationshipDefinition import RelationshipDefinition

instance = RelationshipDefinition(
    version=Version(...),  # optional
    relationship_definition_id=ResourceId(...),  # required
    source_entity_type="...",  # required — The entity type of the source entity object.
    target_entity_type="...",  # required — The entity type of the target entity object.
    display_name="...",  # required — The display name of the relationship.
    outward_description="...",  # required — The description to relate source entity object and target entity object
    inward_description="...",  # required — The description to relate target entity object and source entity object
    life_time="...",  # required — Describes how the relationships can change over time.
    relationship_cardinality="...",  # required — Describes the cardinality of the relationship between source entity and target entity.
    links=[]  # optional
)
```


## Related Models

- [Version](Version.md)
- [ResourceId](ResourceId.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

