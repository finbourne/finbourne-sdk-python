# McpToolSchedulerPayload

Payload data for a Scheduler job MCP tool
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **job_scope** | **str** | Required | The scope of the scheduler job to run |
| **job_code** | **str** | Required | The code of the scheduler job to run |
| **arguments** | **Dict[str, Optional[str]]** | Optional | Arguments to pass to the scheduler job (key-value pairs) |
| **run_as** | **str** | Optional | Optional service user identifier to run the job as (if not the current user) |
| **notifications** | [List[McpToolSchedulerNotification]](McpToolSchedulerNotification.md) | Optional | Optional additional notifications for the job |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.identity.models.McpToolSchedulerPayload import McpToolSchedulerPayload

instance = McpToolSchedulerPayload(
    job_scope="...",  # required — The scope of the scheduler job to run
    job_code="...",  # required — The code of the scheduler job to run
    arguments=,  # optional — Arguments to pass to the scheduler job (key-value pairs)
    run_as="...",  # optional — Optional service user identifier to run the job as (if not the current user)
    notifications=[]  # optional — Optional additional notifications for the job
)
```

- [McpToolSchedulerNotification](McpToolSchedulerNotification.md) — used in `notifications`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

