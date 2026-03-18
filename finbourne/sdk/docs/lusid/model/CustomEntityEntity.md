# CustomEntityEntity

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Required | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **entity_unique_id** | **str** | Required | The unique id of the entity. |
| **as_at_version_number** | **int** | Optional | The integer version number for the entity (the entity was created at version 1) |
| **status** | **str** | Required | The status of the entity at the current time. |
| **as_at_deleted** | **datetime** | Optional | The asAt datetime at which the entity was deleted. |
| **user_id_deleted** | **str** | Optional | The unique id of the user who deleted the entity. |
| **request_id_deleted** | **str** | Optional | The unique request id of the command that deleted the entity. |
| **effective_at_created** | **datetime** | Optional | The EffectiveAt this Entity is created, if entity does not currently exist in EffectiveAt. |
| **prevailing_custom_entity** | [CustomEntityResponse](CustomEntityResponse.md) | Optional | *No description available.* |
| **deleted_custom_entity** | [CustomEntityResponse](CustomEntityResponse.md) | Optional | *No description available.* |
| **previewed_status** | **str** | Optional | The status of the previewed entity. |
| **previewed_custom_entity** | [CustomEntityResponse](CustomEntityResponse.md) | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CustomEntityEntity import CustomEntityEntity

instance = CustomEntityEntity(
    href="...",  # required — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    entity_unique_id="...",  # required — The unique id of the entity.
    as_at_version_number=0,  # optional — The integer version number for the entity (the entity was created at version 1)
    status="...",  # required — The status of the entity at the current time.
    as_at_deleted=datetime.now(),  # optional — The asAt datetime at which the entity was deleted.
    user_id_deleted="...",  # optional — The unique id of the user who deleted the entity.
    request_id_deleted="...",  # optional — The unique request id of the command that deleted the entity.
    effective_at_created=datetime.now(),  # optional — The EffectiveAt this Entity is created, if entity does not currently exist in EffectiveAt.
    prevailing_custom_entity=CustomEntityResponse(...),  # optional
    deleted_custom_entity=CustomEntityResponse(...),  # optional
    previewed_status="...",  # optional — The status of the previewed entity.
    previewed_custom_entity=CustomEntityResponse(...),  # optional
    links=[]  # optional
)
```

- [CustomEntityResponse](CustomEntityResponse.md)
- [CustomEntityResponse](CustomEntityResponse.md)
- [CustomEntityResponse](CustomEntityResponse.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

