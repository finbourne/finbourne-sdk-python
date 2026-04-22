# ViewItem

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **name** | **str** | Optional | The name of the view |
| **domain** | **str** | Optional | The domain the view applies to |
| **file_path** | **str** | Optional | The full file path in the HcFs |
| **file_content** | **str** | Optional | The full file content in the HcFs. This will be needed for Upserting the view to a different domain / for use in fbn-config. |
| **last_updated_execution_id** | **UUID** | Optional | The last ExecutionId, needed to get the creating Sql out of the logs |
| **last_updated_at** | **datetime** | Optional | The last updated at time, needed to get the creating Sql out of the logs |
| **last_updated_by** | **str** | Optional | The last updated by this user |
| **created_by_user_id** | **str** | Optional | Originally created by this user |
| **notes** | **str** | Optional | Any notes around saving or whatnot |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.luminesce.models.ViewItem import ViewItem

instance = ViewItem(
    name="...",  # optional — The name of the view
    domain="...",  # optional — The domain the view applies to
    file_path="...",  # optional — The full file path in the HcFs
    file_content="...",  # optional — The full file content in the HcFs. This will be needed for Upserting the view to a different domain / for use in fbn-config.
    last_updated_execution_id="...",  # optional — The last ExecutionId, needed to get the creating Sql out of the logs
    last_updated_at=datetime.now(),  # optional — The last updated at time, needed to get the creating Sql out of the logs
    last_updated_by="...",  # optional — The last updated by this user
    created_by_user_id="...",  # optional — Originally created by this user
    notes="..."  # optional — Any notes around saving or whatnot
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

