# UpdateNotificationRequest

The information required to update a notification
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **display_name** | **str** | Required | The name of the notification |
| **description** | **str** | Optional | The summary of the services provided by the notification |
| **notification_type** | [NotificationType](NotificationType.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.notifications.models.UpdateNotificationRequest import UpdateNotificationRequest

instance = UpdateNotificationRequest(
    display_name="...",  # required — The name of the notification
    description="...",  # optional — The summary of the services provided by the notification
    notification_type=NotificationType(...)  # required
)
```

- [NotificationType](NotificationType.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

