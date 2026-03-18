# ChangeItem

Defines a change that occured to a Task
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **as_at_modified** | **datetime** | Required | The AsAt time of the change |
| **user_id_modified** | **str** | Required | The User ID that performed the change |
| **request_id_modified** | **str** | Required | The Request ID of the request that caused the change |
| **as_at_version_number** | **int** | Required | The AsAt Version number |
| **action** | **str** | Required | The Action that resulted in the change |
| **attribute_name** | **str** | Required | The name of the attribute that has been change |
| **previous_value** | **object** | Optional | The value of the attribute prior to the change |
| **new_value** | **object** | Required | The value of the attribute following the change |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.ChangeItem import ChangeItem

instance = ChangeItem(
    as_at_modified=datetime.now(),  # required — The AsAt time of the change
    user_id_modified="...",  # required — The User ID that performed the change
    request_id_modified="...",  # required — The Request ID of the request that caused the change
    as_at_version_number=0,  # required — The AsAt Version number
    action="...",  # required — The Action that resulted in the change
    attribute_name="...",  # required — The name of the attribute that has been change
    previous_value=,  # optional — The value of the attribute prior to the change
    new_value=  # required — The value of the attribute following the change
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

