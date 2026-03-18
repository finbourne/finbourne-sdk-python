# NotificationStatus

The status object of a notification
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **result** | **str** | Optional | The status of the notification |
| **last_updated** | **datetime** | Optional | The time at which the notification status was last updated |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.notifications.models.NotificationStatus import NotificationStatus

instance = NotificationStatus(
    result="...",  # optional — The status of the notification
    last_updated=datetime.now()  # optional — The time at which the notification status was last updated
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

