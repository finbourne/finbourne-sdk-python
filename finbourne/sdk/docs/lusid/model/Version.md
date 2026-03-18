# Version

The version metadata.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **effective_from** | **datetime** | Required | The effective datetime at which this version became valid. Only applies when a single entity is being interacted with. |
| **as_at_date** | **datetime** | Required | The asAt datetime at which the data was committed to LUSID. |
| **as_at_created** | **datetime** | Optional | The asAt datetime at which the entity was first created in LUSID. |
| **user_id_created** | **str** | Optional | The unique id of the user who created the entity. |
| **request_id_created** | **str** | Optional | The unique request id of the command that created the entity. |
| **reason_created** | **str** | Optional | The reason for an entity creation. |
| **as_at_modified** | **datetime** | Optional | The asAt datetime at which the entity (including its properties) was last updated in LUSID. |
| **user_id_modified** | **str** | Optional | The unique id of the user who last updated the entity (including its properties) in LUSID. |
| **request_id_modified** | **str** | Optional | The unique request id of the command that last updated the entity (including its properties) in LUSID. |
| **reason_modified** | **str** | Optional | The reason for an entity modification. |
| **as_at_version_number** | **int** | Optional | The integer version number for the entity (the entity was created at version 1) |
| **entity_unique_id** | **str** | Optional | The unique id of the entity |
| **staged_modification_id_modified** | **str** | Optional | The ID of the staged change that resulted in the most recent modification. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.Version import Version

instance = Version(
    effective_from=datetime.now(),  # required — The effective datetime at which this version became valid. Only applies when a single entity is being interacted with.
    as_at_date=datetime.now(),  # required — The asAt datetime at which the data was committed to LUSID.
    as_at_created=datetime.now(),  # optional — The asAt datetime at which the entity was first created in LUSID.
    user_id_created="...",  # optional — The unique id of the user who created the entity.
    request_id_created="...",  # optional — The unique request id of the command that created the entity.
    reason_created="...",  # optional — The reason for an entity creation.
    as_at_modified=datetime.now(),  # optional — The asAt datetime at which the entity (including its properties) was last updated in LUSID.
    user_id_modified="...",  # optional — The unique id of the user who last updated the entity (including its properties) in LUSID.
    request_id_modified="...",  # optional — The unique request id of the command that last updated the entity (including its properties) in LUSID.
    reason_modified="...",  # optional — The reason for an entity modification.
    as_at_version_number=0,  # optional — The integer version number for the entity (the entity was created at version 1)
    entity_unique_id="...",  # optional — The unique id of the entity
    staged_modification_id_modified="..."  # optional — The ID of the staged change that resulted in the most recent modification.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

