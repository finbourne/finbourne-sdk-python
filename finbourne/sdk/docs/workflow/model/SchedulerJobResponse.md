# SchedulerJobResponse

Readonly configuration for a Worker that calls a Scheduler job
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **type** | **str** | Optional | The type of worker |
| **job_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.SchedulerJobResponse import SchedulerJobResponse

instance = SchedulerJobResponse(
    type="...",  # optional — The type of worker
    job_id=ResourceId(...)  # optional
)
```

- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

