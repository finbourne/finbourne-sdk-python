# DeletedEntityResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **effective_from** | **datetime** | Optional | The effective datetime at which the deletion became valid. May be null in the case where multiple date times are applicable. |
| **as_at** | **datetime** | Required | The asAt datetime at which the deletion was committed to LUSID. |
| **entity_type** | **str** | Optional | The type of the entity that the deleted response applies to. |
| **entity_unique_id** | **str** | Optional | The unique Id of the entity that the deleted response applies to. |
| **staged_modifications** | [StagedModificationsInfo](StagedModificationsInfo.md) | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.DeletedEntityResponse import DeletedEntityResponse

instance = DeletedEntityResponse(
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    effective_from=datetime.now(),  # optional — The effective datetime at which the deletion became valid. May be null in the case where multiple date times are applicable.
    as_at=datetime.now(),  # required — The asAt datetime at which the deletion was committed to LUSID.
    entity_type="...",  # optional — The type of the entity that the deleted response applies to.
    entity_unique_id="...",  # optional — The unique Id of the entity that the deleted response applies to.
    staged_modifications=StagedModificationsInfo(...),  # optional
    links=[]  # optional
)
```

- [StagedModificationsInfo](StagedModificationsInfo.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

