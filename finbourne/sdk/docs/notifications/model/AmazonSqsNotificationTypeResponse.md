# AmazonSqsNotificationTypeResponse

Holds readonly information about an AWS SQS notification
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **type** | **str** | Optional | The type of delivery mechanism for this notification |
| **api_key_ref** | **str** | Optional | Reference to API key from Configuration Store |
| **api_secret_ref** | **str** | Optional | Reference to API secret from Configuration Store |
| **body** | **str** | Optional | The body of the Amazon Queue Message |
| **queue_url_ref** | **str** | Optional | Reference to queue url from Configuration Store |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.notifications.models.AmazonSqsNotificationTypeResponse import AmazonSqsNotificationTypeResponse

instance = AmazonSqsNotificationTypeResponse(
    type="...",  # optional — The type of delivery mechanism for this notification
    api_key_ref="...",  # optional — Reference to API key from Configuration Store
    api_secret_ref="...",  # optional — Reference to API secret from Configuration Store
    body="...",  # optional — The body of the Amazon Queue Message
    queue_url_ref="..."  # optional — Reference to queue url from Configuration Store
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

