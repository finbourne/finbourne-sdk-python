# RunWorkerResponse

The RunWorker response
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **run_id** | **UUID** | Required | Identifies a Worker run |
| **status_detail** | **str** | Optional | Detail on the final status |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.RunWorkerResponse import RunWorkerResponse

instance = RunWorkerResponse(
    run_id="...",  # required — Identifies a Worker run
    status_detail="..."  # optional — Detail on the final status
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

