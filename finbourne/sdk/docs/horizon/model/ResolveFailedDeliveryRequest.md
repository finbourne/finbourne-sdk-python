# ResolveFailedDeliveryRequest

Request to resolve a failed delivery without retry.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **reason** | **str** | Required | The reason for resolving the failed delivery without retrying. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.ResolveFailedDeliveryRequest import ResolveFailedDeliveryRequest

instance = ResolveFailedDeliveryRequest(
    reason="..."  # required — The reason for resolving the failed delivery without retrying.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

