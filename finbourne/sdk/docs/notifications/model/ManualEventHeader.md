# ManualEventHeader

The header of the manual event
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **event_type** | **str** | Optional | The event type of the manual event *(read-only)* |
| **timestamp** | **datetime** | Optional | The timestamp of the manual event |
| **user_id** | **str** | Optional | The user ID of the manual event |
| **request_id** | **str** | Optional | The request ID of the manual event |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.notifications.models.ManualEventHeader import ManualEventHeader

instance = ManualEventHeader(
    event_type="...",  # optional — The event type of the manual event
    timestamp=datetime.now(),  # optional — The timestamp of the manual event
    user_id="...",  # optional — The user ID of the manual event
    request_id="..."  # optional — The request ID of the manual event
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

