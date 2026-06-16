# FailedDeliveryResponse

A batch's failed deliveries returned by the list endpoint, aggregated to one row per batch. Finbourne.Horizon.Integrations.Web.Dto.Integrations.TradePublicationFramework.Response.FailedDeliveryResponse.FailedCount is the number of failed deliveries in the batch and Finbourne.Horizon.Integrations.Web.Dto.Integrations.TradePublicationFramework.Response.FailedDeliveryResponse.FailureReason is the comma-separated set of their failure reasons.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **batch_reference_id** | **str** | Required | *No description available.* |
| **run_id** | **UUID** | Required | *No description available.* |
| **run_start_time** | **datetime** | Required | *No description available.* |
| **failed_count** | **int** | Required | *No description available.* |
| **failure_reason** | **str** | Required | *No description available.* |
| **last_attempt_at** | **datetime** | Required | *No description available.* |
| **attempt_count** | **int** | Required | *No description available.* |
| **resolved** | **bool** | Required | *No description available.* |
| **resolved_at** | **datetime** | Optional | *No description available.* |
| **resolution_reason** | **str** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.FailedDeliveryResponse import FailedDeliveryResponse

instance = FailedDeliveryResponse(
    batch_reference_id="...",  # required
    run_id="...",  # required
    run_start_time=datetime.now(),  # required
    failed_count=0,  # required
    failure_reason="...",  # required
    last_attempt_at=datetime.now(),  # required
    attempt_count=0,  # required
    resolved=True,  # required
    resolved_at=datetime.now(),  # optional
    resolution_reason="..."  # optional
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

