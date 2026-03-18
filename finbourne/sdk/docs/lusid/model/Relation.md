# Relation

Representation of a Relation between a requested entity with the stated entity as RelationedEntityId
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **relation_definition_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **related_entity_id** | **Dict[str, Optional[str]]** | Required | *No description available.* |
| **traversal_direction** | **str** | Required | *No description available.* |
| **traversal_description** | **str** | Required | *No description available.* |
| **effective_from** | **datetime** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.Relation import Relation

instance = Relation(
    version=Version(...),  # optional
    relation_definition_id=ResourceId(...),  # required
    related_entity_id=,  # required
    traversal_direction="...",  # required
    traversal_description="...",  # required
    effective_from=datetime.now()  # optional
)
```


## Related Models

- [Version](Version.md)
- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

