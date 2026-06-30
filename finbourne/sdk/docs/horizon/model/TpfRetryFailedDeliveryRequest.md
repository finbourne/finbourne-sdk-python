# TpfRetryFailedDeliveryRequest

Request to retry failed deliveries for multiple batch elements. The integration instance identifier is supplied via the route, not the body.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **batch_element_reference_ids** | **List[str]** | Required | Batch element reference identifiers to retry. No regex pattern is required as batch element IDs are vendor-defined strings with varying formats. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.TpfRetryFailedDeliveryRequest import TpfRetryFailedDeliveryRequest

instance = TpfRetryFailedDeliveryRequest(
    batch_element_reference_ids=  # required — Batch element reference identifiers to retry. No regex pattern is required as batch element IDs are vendor-defined strings with varying formats.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

