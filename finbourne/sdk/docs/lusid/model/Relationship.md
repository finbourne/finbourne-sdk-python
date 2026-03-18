# Relationship

Representation of a Relationship between a requested entity with the stated entity as RelatedEntityId
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **relationship_definition_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **related_entity** | [RelatedEntity](RelatedEntity.md) | Required | *No description available.* |
| **traversal_direction** | **str** | Required | Direction of relationship between the requested entity and related entity. This can be &#39;In&#39; or &#39;Out&#39;. Read more about relationships traversal direction in LUSID Knowledge Base here https://support.lusid.com/knowledgebase/article/KA-01679. |
| **traversal_description** | **str** | Required | Description of the relationship based on relationship&#39;s traversal direction. If &#39;TraversalDirection&#39; is &#39;Out&#39;, this description would be &#39;OutwardDescription&#39; from the associated relationship definition. If &#39;TraversalDirection&#39; is &#39;In&#39;, this description would be &#39;InwardDescription&#39; from the associated relationship definition. |
| **effective_from** | **datetime** | Optional | The effective datetime from which the relationship is valid. |
| **effective_until** | **datetime** | Optional | The effective datetime until which the relationship is valid. If no future deletions are present or an effective until has not been set for the relationship, this will be indefinite and represented by the maximum date. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.Relationship import Relationship

instance = Relationship(
    version=Version(...),  # optional
    relationship_definition_id=ResourceId(...),  # required
    related_entity=RelatedEntity(...),  # required
    traversal_direction="...",  # required — Direction of relationship between the requested entity and related entity. This can be &#39;In&#39; or &#39;Out&#39;. Read more about relationships traversal direction in LUSID Knowledge Base here https://support.lusid.com/knowledgebase/article/KA-01679.
    traversal_description="...",  # required — Description of the relationship based on relationship&#39;s traversal direction. If &#39;TraversalDirection&#39; is &#39;Out&#39;, this description would be &#39;OutwardDescription&#39; from the associated relationship definition. If &#39;TraversalDirection&#39; is &#39;In&#39;, this description would be &#39;InwardDescription&#39; from the associated relationship definition.
    effective_from=datetime.now(),  # optional — The effective datetime from which the relationship is valid.
    effective_until=datetime.now()  # optional — The effective datetime until which the relationship is valid. If no future deletions are present or an effective until has not been set for the relationship, this will be indefinite and represented by the maximum date.
)
```


## Related Models

- [Version](Version.md)
- [ResourceId](ResourceId.md)
- [RelatedEntity](RelatedEntity.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

