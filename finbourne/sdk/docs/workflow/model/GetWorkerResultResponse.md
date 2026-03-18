# GetWorkerResultResponse

The RunWorker response
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **worker_status** | **str** | Required | The final status of the Worker |
| **results** | **List[Dict[str, object]]** | Required | Results |
| **status_detail** | **str** | Optional | Detail on the final status |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.GetWorkerResultResponse import GetWorkerResultResponse

instance = GetWorkerResultResponse(
    worker_status="...",  # required — The final status of the Worker
    results=,  # required — Results
    status_detail="..."  # optional — Detail on the final status
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

