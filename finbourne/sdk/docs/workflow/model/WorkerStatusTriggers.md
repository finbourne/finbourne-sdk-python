# WorkerStatusTriggers

Defines triggers that will be invoked per Worker outcome
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **started** | **str** | Optional | Trigger to invoke when the Worker has Started |
| **completed_with_results** | **str** | Optional | Trigger to invoke when the Worker has Completed (with results) |
| **completed_no_results** | **str** | Optional | Trigger to invoke when the Worker has Completed (no results) |
| **failed_to_start** | **str** | Optional | Trigger to invoke when the Worker has Failed to Start |
| **failed_to_complete** | **str** | Optional | Trigger to invoke when the Worker has Failed to Complete |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.WorkerStatusTriggers import WorkerStatusTriggers

instance = WorkerStatusTriggers(
    started="...",  # optional — Trigger to invoke when the Worker has Started
    completed_with_results="...",  # optional — Trigger to invoke when the Worker has Completed (with results)
    completed_no_results="...",  # optional — Trigger to invoke when the Worker has Completed (no results)
    failed_to_start="...",  # optional — Trigger to invoke when the Worker has Failed to Start
    failed_to_complete="..."  # optional — Trigger to invoke when the Worker has Failed to Complete
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

