# ResolveFailedDeliveryResponse

Response from resolving the failed deliveries for a batch without retry. Resolution is batch-level, so Finbourne.Horizon.Integrations.Web.Dto.Integrations.TradePublicationFramework.Response.ResolveFailedDeliveryResponse.ResolvedCount is the number of failed deliveries marked resolved.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **batch_reference_id** | **str** | Required | *No description available.* |
| **resolved_count** | **int** | Required | *No description available.* |
| **resolved** | **bool** | Required | *No description available.* |
| **resolved_at** | **datetime** | Required | *No description available.* |
| **resolution_reason** | **str** | Required | *No description available.* |
| **message** | **str** | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.ResolveFailedDeliveryResponse import ResolveFailedDeliveryResponse

instance = ResolveFailedDeliveryResponse(
    batch_reference_id="...",  # required
    resolved_count=0,  # required
    resolved=True,  # required
    resolved_at=datetime.now(),  # required
    resolution_reason="...",  # required
    message="..."  # required
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

