# AzureServiceBusNotificationType

The information required to create or update an Azure Service Bus notification
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **type** | **str** | Required | The type of delivery mechanism for this notification |
| **namespace** | **str** | Required | Reference to namespace from Configuration Store |
| **queue_name** | **str** | Required | Reference to queue name from Configuration Store |
| **body** | **str** | Required | The body of the Azure Service Bus Message |
| **tenant_id** | **str** | Required | Reference to tenant id from Configuration Store |
| **client_id** | **str** | Required | Reference to client id from Configuration Store |
| **client_secret** | **str** | Required | Reference to client secret from Configuration Store |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.notifications.models.AzureServiceBusNotificationType import AzureServiceBusNotificationType

instance = AzureServiceBusNotificationType(
    type="...",  # required — The type of delivery mechanism for this notification
    namespace="...",  # required — Reference to namespace from Configuration Store
    queue_name="...",  # required — Reference to queue name from Configuration Store
    body="...",  # required — The body of the Azure Service Bus Message
    tenant_id="...",  # required — Reference to tenant id from Configuration Store
    client_id="...",  # required — Reference to client id from Configuration Store
    client_secret="..."  # required — Reference to client secret from Configuration Store
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

