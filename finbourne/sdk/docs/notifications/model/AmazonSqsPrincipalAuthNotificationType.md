# AmazonSqsPrincipalAuthNotificationType

The information required to create or update an AWS SQS notification with principal authentication
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **type** | **str** | Required | The type of delivery mechanism for this notification |
| **body** | **str** | Required | The body of the Amazon Queue Message |
| **queue_url_ref** | **str** | Required | Reference to queue url from Configuration Store |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.notifications.models.AmazonSqsPrincipalAuthNotificationType import AmazonSqsPrincipalAuthNotificationType

instance = AmazonSqsPrincipalAuthNotificationType(
    type="...",  # required — The type of delivery mechanism for this notification
    body="...",  # required — The body of the Amazon Queue Message
    queue_url_ref="..."  # required — Reference to queue url from Configuration Store
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

