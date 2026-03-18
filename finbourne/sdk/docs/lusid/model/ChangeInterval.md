# ChangeInterval

Defines a change that occured for an entity
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **as_at_modified** | **datetime** | Optional | The date/time of the change. |
| **user_id_modified** | **str** | Optional | The unique identifier of the user that made the change. |
| **request_id_modified** | **str** | Optional | The unique identifier of the request that the changes were part of. |
| **reason_modified** | **str** | Optional | The reason for an entity modification. |
| **as_at_version_number** | **int** | Optional | The version number for the entity (the entity was created at version 1). This may refer to the version number of a changed related entity, not a change for the entity itself. |
| **staged_modification_id_modified** | **str** | Optional | The id of the staged modification that was approved. Will be null if the change didn&#39;t come from a staged modification. |
| **action** | **str** | Optional | The action performed on the field. |
| **attribute_name** | **str** | Optional | The name of the field or property that has been changed. |
| **previous_value** | [PropertyValue](PropertyValue.md) | Optional | *No description available.* |
| **new_value** | [PropertyValue](PropertyValue.md) | Optional | *No description available.* |
| **effective_range** | [EffectiveRange](EffectiveRange.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ChangeInterval import ChangeInterval

instance = ChangeInterval(
    as_at_modified=datetime.now(),  # optional — The date/time of the change.
    user_id_modified="...",  # optional — The unique identifier of the user that made the change.
    request_id_modified="...",  # optional — The unique identifier of the request that the changes were part of.
    reason_modified="...",  # optional — The reason for an entity modification.
    as_at_version_number=0,  # optional — The version number for the entity (the entity was created at version 1). This may refer to the version number of a changed related entity, not a change for the entity itself.
    staged_modification_id_modified="...",  # optional — The id of the staged modification that was approved. Will be null if the change didn&#39;t come from a staged modification.
    action="...",  # optional — The action performed on the field.
    attribute_name="...",  # optional — The name of the field or property that has been changed.
    previous_value=PropertyValue(...),  # optional
    new_value=PropertyValue(...),  # optional
    effective_range=EffectiveRange(...)  # optional
)
```

- [PropertyValue](PropertyValue.md)
- [PropertyValue](PropertyValue.md)
- [EffectiveRange](EffectiveRange.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

