# DataPointVersion

The version metadata for DataPoints.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **as_at_created** | **datetime** | Optional | The asAt datetime at which the entity was first created in LUSID. |
| **user_id_created** | **str** | Optional | The unique id of the user who created the entity. |
| **request_id_created** | **str** | Optional | The unique request id of the command that created the entity. |
| **as_at_modified** | **datetime** | Optional | The asAt datetime at which the entity (including its properties) was last updated in LUSID. |
| **user_id_modified** | **str** | Optional | The unique id of the user who last updated the entity (including its properties) in LUSID. |
| **request_id_modified** | **str** | Optional | The unique request id of the command that last updated the entity (including its properties) in LUSID. |
| **as_at_version_number** | **int** | Optional | The integer version number for the entity (the entity was created at version 1) |
| **entity_unique_id** | **str** | Optional | The unique id of the entity |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.DataPointVersion import DataPointVersion

instance = DataPointVersion(
    as_at_created=datetime.now(),  # optional — The asAt datetime at which the entity was first created in LUSID.
    user_id_created="...",  # optional — The unique id of the user who created the entity.
    request_id_created="...",  # optional — The unique request id of the command that created the entity.
    as_at_modified=datetime.now(),  # optional — The asAt datetime at which the entity (including its properties) was last updated in LUSID.
    user_id_modified="...",  # optional — The unique id of the user who last updated the entity (including its properties) in LUSID.
    request_id_modified="...",  # optional — The unique request id of the command that last updated the entity (including its properties) in LUSID.
    as_at_version_number=0,  # optional — The integer version number for the entity (the entity was created at version 1)
    entity_unique_id="..."  # optional — The unique id of the entity
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

