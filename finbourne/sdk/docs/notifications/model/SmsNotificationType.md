# SmsNotificationType

The information required to create or update an SMS notification
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **type** | **str** | Required | The type of delivery mechanism for this notification |
| **body** | **str** | Required | The body of the SMS |
| **recipients** | **List[str]** | Required | The phone numbers to which the SMS will be sent to (E.164 format) |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.notifications.models.SmsNotificationType import SmsNotificationType

instance = SmsNotificationType(
    type="...",  # required — The type of delivery mechanism for this notification
    body="...",  # required — The body of the SMS
    recipients=  # required — The phone numbers to which the SMS will be sent to (E.164 format)
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

