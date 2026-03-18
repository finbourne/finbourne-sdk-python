# CompleteRelation

Representation of a relation containing details of source and target entities, and both outward and inward descriptions.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | *No description available.* |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **relation_definition_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **source_entity_id** | **Dict[str, Optional[str]]** | Required | *No description available.* |
| **target_entity_id** | **Dict[str, Optional[str]]** | Required | *No description available.* |
| **outward_description** | **str** | Required | *No description available.* |
| **inward_description** | **str** | Required | *No description available.* |
| **effective_from** | **datetime** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CompleteRelation import CompleteRelation

instance = CompleteRelation(
    href="...",  # optional
    version=Version(...),  # optional
    relation_definition_id=ResourceId(...),  # required
    source_entity_id=,  # required
    target_entity_id=,  # required
    outward_description="...",  # required
    inward_description="...",  # required
    effective_from=datetime.now()  # optional
)
```

- [Version](Version.md)
- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

