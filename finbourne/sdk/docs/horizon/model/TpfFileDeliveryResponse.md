# TpfFileDeliveryResponse

Response model for TPF file delivery search results
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **run_id** | **str** | Optional | *No description available.* |
| **run_start_time** | **datetime** | Optional | *No description available.* |
| **file_name** | **str** | Required | *No description available.* |
| **generated_at** | **datetime** | Required | *No description available.* |
| **row_count** | **int** | Required | *No description available.* |
| **file_hash** | **str** | Optional | *No description available.* |
| **destination_type** | **str** | Required | *No description available.* |
| **destination_path** | **str** | Optional | *No description available.* |
| **destination_status** | **str** | Required | *No description available.* |
| **destination_error** | **str** | Optional | *No description available.* |
| **destination_name** | **str** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.TpfFileDeliveryResponse import TpfFileDeliveryResponse

instance = TpfFileDeliveryResponse(
    run_id="...",  # optional
    run_start_time=datetime.now(),  # optional
    file_name="...",  # required
    generated_at=datetime.now(),  # required
    row_count=0,  # required
    file_hash="...",  # optional
    destination_type="...",  # required
    destination_path="...",  # optional
    destination_status="...",  # required
    destination_error="...",  # optional
    destination_name="..."  # optional
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

