# SmsNotificationTypeResponse

Holds readonly information about an SMS notification
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **type** | **str** | Optional | The type of delivery mechanism for this notification |
| **body** | **str** | Optional | The body of the SMS |
| **recipients** | **List[str]** | Optional | The phone numbers to which the SMS will be sent to (E.164 format) |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.notifications.models.SmsNotificationTypeResponse import SmsNotificationTypeResponse

instance = SmsNotificationTypeResponse(
    type="...",  # optional — The type of delivery mechanism for this notification
    body="...",  # optional — The body of the SMS
    recipients=  # optional — The phone numbers to which the SMS will be sent to (E.164 format)
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

