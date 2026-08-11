# Notification

A notification object
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **notification_id** | **str** | Required | The identifier of the notification |
| **display_name** | **str** | Required | The name of the notification |
| **description** | **str** | Optional | The summary of the services provided by the notification |
| **notification_type** | [NotificationTypeResponse](NotificationTypeResponse.md) | Required | *No description available.* |
| **created_at** | **datetime** | Required | The time at which the subscription was made |
| **user_id_created** | **str** | Required | The user who made the subscription |
| **modified_at** | **datetime** | Required | The time at which the subscription was last modified |
| **user_id_modified** | **str** | Required | The user who last modified the subscription |
| **href** | **str** | Optional | A URI for retrieving this notification |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.notifications.models.Notification import Notification

instance = Notification(
    notification_id="...",  # required — The identifier of the notification
    display_name="...",  # required — The name of the notification
    description="...",  # optional — The summary of the services provided by the notification
    notification_type=NotificationTypeResponse(...),  # required
    created_at=datetime.now(),  # required — The time at which the subscription was made
    user_id_created="...",  # required — The user who made the subscription
    modified_at=datetime.now(),  # required — The time at which the subscription was last modified
    user_id_modified="...",  # required — The user who last modified the subscription
    href="..."  # optional — A URI for retrieving this notification
)
```

- [NotificationTypeResponse](NotificationTypeResponse.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

