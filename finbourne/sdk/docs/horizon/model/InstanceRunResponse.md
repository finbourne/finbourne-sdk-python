# InstanceRunResponse

Response containing details of a single run for an instance. The transaction and file figures describe the batch as it stands now, so they are reported on the latest attempt only and are null on earlier attempts of a retried run. Message explains a failed attempt and what will happen or must be done next; it is null for completed, running and queued attempts.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **run_id** | **UUID** | Required | *No description available.* |
| **reference_id** | **UUID** | Required | *No description available.* |
| **attempt** | **int** | Optional | *No description available.* |
| **start_time** | **datetime** | Required | *No description available.* |
| **end_time** | **datetime** | Optional | *No description available.* |
| **duration** | **str** | Optional | *No description available.* |
| **status** | **str** | Required | *No description available.* |
| **triggered_by** | **str** | Optional | *No description available.* |
| **total** | **int** | Optional | *No description available.* |
| **sent_count** | **int** | Optional | *No description available.* |
| **skipped_count** | **int** | Optional | *No description available.* |
| **failed_count** | **int** | Optional | *No description available.* |
| **failed_files** | **int** | Optional | *No description available.* |
| **message** | **str** | Optional | *No description available.* |
| **file_count** | **int** | Optional | The number of rows ListRunFiles returns for the run, every delivery attempt included; latest attempt only. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.InstanceRunResponse import InstanceRunResponse

instance = InstanceRunResponse(
    run_id="...",  # required
    reference_id="...",  # required
    attempt=0,  # optional
    start_time=datetime.now(),  # required
    end_time=datetime.now(),  # optional
    duration="...",  # optional
    status="...",  # required
    triggered_by="...",  # optional
    total=0,  # optional
    sent_count=0,  # optional
    skipped_count=0,  # optional
    failed_count=0,  # optional
    failed_files=0,  # optional
    message="...",  # optional
    file_count=0  # optional — The number of rows ListRunFiles returns for the run, every delivery attempt included; latest attempt only.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

