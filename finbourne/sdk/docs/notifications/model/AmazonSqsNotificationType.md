# AmazonSqsNotificationType

The information required to create or update an AWS SQS notification
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **type** | **str** | Required | The type of delivery mechanism for this notification |
| **api_key_ref** | **str** | Required | Reference to API key from Configuration Store |
| **api_secret_ref** | **str** | Required | Reference to API secret from Configuration Store |
| **body** | **str** | Required | The body of the Amazon Queue Message |
| **queue_url_ref** | **str** | Required | Reference to queue url from Configuration Store |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.notifications.models.AmazonSqsNotificationType import AmazonSqsNotificationType

instance = AmazonSqsNotificationType(
    type="...",  # required — The type of delivery mechanism for this notification
    api_key_ref="...",  # required — Reference to API key from Configuration Store
    api_secret_ref="...",  # required — Reference to API secret from Configuration Store
    body="...",  # required — The body of the Amazon Queue Message
    queue_url_ref="..."  # required — Reference to queue url from Configuration Store
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

