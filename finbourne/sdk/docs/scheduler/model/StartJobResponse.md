# StartJobResponse

Response from starting a job
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **job_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **run_id** | **str** | Optional | Unique RunId of the started job run |
| **status** | **str** | Optional | Link to the status of the started job |
| **result** | **str** | Optional | Link to the result of the job run when completed |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.scheduler.models.StartJobResponse import StartJobResponse

instance = StartJobResponse(
    job_id=ResourceId(...),  # optional
    run_id="...",  # optional — Unique RunId of the started job run
    status="...",  # optional — Link to the status of the started job
    result="..."  # optional — Link to the result of the job run when completed
)
```


## Related Models

- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

