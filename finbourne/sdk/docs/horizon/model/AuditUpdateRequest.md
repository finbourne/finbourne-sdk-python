# AuditUpdateRequest

An incoming request for a Horizon Update Event
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | **str** | Required | A unique ID identifiying the source of the event |
| **user_id** | **str** | Required | A unique ID identifiying who owns the schedule |
| **scheduler_run_id** | **str** | Required | The GUID of the schedule run |
| **start_time** | **datetime** | Required | When the run was started in UTC |
| **message** | **str** | Required | A descriptive message to accompany the status |
| **process_name_override** | **str** | Optional | Optional Name for how the process appears in Data Feed Monitoring |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.AuditUpdateRequest import AuditUpdateRequest

instance = AuditUpdateRequest(
    id="...",  # required — A unique ID identifiying the source of the event
    user_id="...",  # required — A unique ID identifiying who owns the schedule
    scheduler_run_id="...",  # required — The GUID of the schedule run
    start_time=datetime.now(),  # required — When the run was started in UTC
    message="...",  # required — A descriptive message to accompany the status
    process_name_override="..."  # optional — Optional Name for how the process appears in Data Feed Monitoring
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

