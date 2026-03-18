# Notification

Notification type
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **fire_on** | **str** | Optional | Condition for the notification *(read-only)* |
| **transport** | **str** | Optional | The type of the notification |
| **destination** | **List[str]** | Optional | Where the notification should be sent |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.scheduler.models.Notification import Notification

instance = Notification(
    fire_on="...",  # optional — Condition for the notification
    transport="...",  # optional — The type of the notification
    destination=  # optional — Where the notification should be sent
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

