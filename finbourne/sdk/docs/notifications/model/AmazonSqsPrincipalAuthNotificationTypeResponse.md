# AmazonSqsPrincipalAuthNotificationTypeResponse

Holds readonly information about an AWS SQS with Principal Authentication notification
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **type** | **str** | Optional | The type of delivery mechanism for this notification |
| **body** | **str** | Optional | The body of the Amazon Queue Message |
| **queue_url_ref** | **str** | Optional | Reference to queue url from Configuration Store |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.notifications.models.AmazonSqsPrincipalAuthNotificationTypeResponse import AmazonSqsPrincipalAuthNotificationTypeResponse

instance = AmazonSqsPrincipalAuthNotificationTypeResponse(
    type="...",  # optional — The type of delivery mechanism for this notification
    body="...",  # optional — The body of the Amazon Queue Message
    queue_url_ref="..."  # optional — Reference to queue url from Configuration Store
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

