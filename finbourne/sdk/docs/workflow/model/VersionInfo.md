# VersionInfo

The version metadata.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **as_at_created** | **datetime** | Optional | The asAt datetime at which this entity was first created. |
| **user_id_created** | **str** | Optional | The unique id of the user who created this entity. |
| **request_id_created** | **str** | Optional | The request id of the request that created this entity. |
| **as_at_modified** | **datetime** | Optional | The asAt datetime at which this entity was last updated. |
| **user_id_modified** | **str** | Optional | The unique id of the user who last updated this entity. |
| **request_id_modified** | **str** | Optional | The request id of the request that last updated this entity. |
| **as_at_version_number** | **int** | Optional | The integer version number for this entity (the entity was created at version 1). |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.VersionInfo import VersionInfo

instance = VersionInfo(
    as_at_created=datetime.now(),  # optional — The asAt datetime at which this entity was first created.
    user_id_created="...",  # optional — The unique id of the user who created this entity.
    request_id_created="...",  # optional — The request id of the request that created this entity.
    as_at_modified=datetime.now(),  # optional — The asAt datetime at which this entity was last updated.
    user_id_modified="...",  # optional — The unique id of the user who last updated this entity.
    request_id_modified="...",  # optional — The request id of the request that last updated this entity.
    as_at_version_number=0  # optional — The integer version number for this entity (the entity was created at version 1).
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

