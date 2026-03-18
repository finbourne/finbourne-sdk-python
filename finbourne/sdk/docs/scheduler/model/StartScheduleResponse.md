# StartScheduleResponse

Response from a manual run of a schedule
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **schedule_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **job_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **run_id** | **str** | Optional | Unique RunId of the started schedule |
| **status** | **str** | Optional | Status of the started schedule |
| **result** | **str** | Optional | Link to the result of the job run when completed |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.scheduler.models.StartScheduleResponse import StartScheduleResponse

instance = StartScheduleResponse(
    schedule_id=ResourceId(...),  # optional
    job_id=ResourceId(...),  # optional
    run_id="...",  # optional — Unique RunId of the started schedule
    status="...",  # optional — Status of the started schedule
    result="..."  # optional — Link to the result of the job run when completed
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

