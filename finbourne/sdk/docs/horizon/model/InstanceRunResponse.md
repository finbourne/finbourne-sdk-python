# InstanceRunResponse

Response containing details of a single run for an instance.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **run_id** | **UUID** | Required | *No description available.* |
| **batch_reference_id** | **UUID** | Required | *No description available.* |
| **attempt** | **int** | Optional | *No description available.* |
| **start_time** | **datetime** | Required | *No description available.* |
| **end_time** | **datetime** | Optional | *No description available.* |
| **duration** | **str** | Optional | *No description available.* |
| **status** | **str** | Required | *No description available.* |
| **triggered_by** | **str** | Optional | *No description available.* |
| **total** | **int** | Required | *No description available.* |
| **sent_count** | **int** | Required | *No description available.* |
| **skipped_count** | **int** | Required | *No description available.* |
| **failed_count** | **int** | Required | *No description available.* |
| **failed_files** | **int** | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.InstanceRunResponse import InstanceRunResponse

instance = InstanceRunResponse(
    run_id="...",  # required
    batch_reference_id="...",  # required
    attempt=0,  # optional
    start_time=datetime.now(),  # required
    end_time=datetime.now(),  # optional
    duration="...",  # optional
    status="...",  # required
    triggered_by="...",  # optional
    total=0,  # required
    sent_count=0,  # required
    skipped_count=0,  # required
    failed_count=0,  # required
    failed_files=0  # required
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

