# AzureServiceBusTypeResponse

Holds readonly information about an Azure Service Bus notification
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **type** | **str** | Optional | The type of delivery mechanism for this notification |
| **namespace_ref** | **str** | Optional | Reference to namespace from Configuration Store |
| **queue_name_ref** | **str** | Optional | Reference to queue name from Configuration Store |
| **body** | **str** | Optional | The body of the Azure service bus Message |
| **tenant_id_ref** | **str** | Optional | Reference to tenant id  from Configuration Store |
| **client_id_ref** | **str** | Optional | Reference to client id from Configuration Store |
| **client_secret_ref** | **str** | Optional | Reference to client secret from Configuration Store |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.notifications.models.AzureServiceBusTypeResponse import AzureServiceBusTypeResponse

instance = AzureServiceBusTypeResponse(
    type="...",  # optional — The type of delivery mechanism for this notification
    namespace_ref="...",  # optional — Reference to namespace from Configuration Store
    queue_name_ref="...",  # optional — Reference to queue name from Configuration Store
    body="...",  # optional — The body of the Azure service bus Message
    tenant_id_ref="...",  # optional — Reference to tenant id  from Configuration Store
    client_id_ref="...",  # optional — Reference to client id from Configuration Store
    client_secret_ref="..."  # optional — Reference to client secret from Configuration Store
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

