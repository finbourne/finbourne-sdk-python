# CompleteRelationship

Representation of a relationship containing details of source and target entities, and both outward and inward descriptions.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **relationship_definition_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **source_entity** | [RelatedEntity](RelatedEntity.md) | Required | *No description available.* |
| **target_entity** | [RelatedEntity](RelatedEntity.md) | Required | *No description available.* |
| **outward_description** | **str** | Required | Description of the relationship based on relationship definition&#39;s outward description. |
| **inward_description** | **str** | Required | Description of the relationship based on relationship definition&#39;s inward description. |
| **effective_from** | **datetime** | Optional | The effective datetime from which the relationship is valid. |
| **effective_until** | **datetime** | Optional | The effective datetime to which the relationship is valid until. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CompleteRelationship import CompleteRelationship

instance = CompleteRelationship(
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    version=Version(...),  # optional
    relationship_definition_id=ResourceId(...),  # required
    source_entity=RelatedEntity(...),  # required
    target_entity=RelatedEntity(...),  # required
    outward_description="...",  # required — Description of the relationship based on relationship definition&#39;s outward description.
    inward_description="...",  # required — Description of the relationship based on relationship definition&#39;s inward description.
    effective_from=datetime.now(),  # optional — The effective datetime from which the relationship is valid.
    effective_until=datetime.now()  # optional — The effective datetime to which the relationship is valid until.
)
```

- [Version](Version.md)
- [ResourceId](ResourceId.md)
- [RelatedEntity](RelatedEntity.md)
- [RelatedEntity](RelatedEntity.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

