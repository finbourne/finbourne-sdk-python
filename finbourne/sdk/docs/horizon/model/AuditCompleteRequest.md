# AuditCompleteRequest

An incoming request for a Horizon Complete Event
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | **str** | Required | A unique ID identifiying the source of the event |
| **user_id** | **str** | Required | A unique ID identifiying who owns the schedule |
| **scheduler_run_id** | **str** | Required | The GUID of the schedule run |
| **start_time** | **datetime** | Required | When the run was started in UTC |
| **end_time** | **datetime** | Required | When the run finished in UTC |
| **message** | **str** | Required | A descriptive message to accompany the status |
| **status** | **str** | Required | The final status of the run |
| **rows_total** | **int** | Required | The number of data rows operated on |
| **rows_succeeded** | **int** | Required | The number of data rows successfully operated on |
| **rows_failed** | **int** | Required | The number of data rows that failed to be operated on |
| **rows_ignored** | **int** | Required | The number of data rows that had no actions taken |
| **audit_files** | [List[AuditFileDetails]](AuditFileDetails.md) | Required | A list of file details for attaching to the event |
| **process_name_override** | **str** | Optional | Optional Name for how the process appears in Data Feed Monitoring |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.AuditCompleteRequest import AuditCompleteRequest

instance = AuditCompleteRequest(
    id="...",  # required — A unique ID identifiying the source of the event
    user_id="...",  # required — A unique ID identifiying who owns the schedule
    scheduler_run_id="...",  # required — The GUID of the schedule run
    start_time=datetime.now(),  # required — When the run was started in UTC
    end_time=datetime.now(),  # required — When the run finished in UTC
    message="...",  # required — A descriptive message to accompany the status
    status="...",  # required — The final status of the run
    rows_total=0,  # required — The number of data rows operated on
    rows_succeeded=0,  # required — The number of data rows successfully operated on
    rows_failed=0,  # required — The number of data rows that failed to be operated on
    rows_ignored=0,  # required — The number of data rows that had no actions taken
    audit_files=[],  # required — A list of file details for attaching to the event
    process_name_override="..."  # optional — Optional Name for how the process appears in Data Feed Monitoring
)
```

- [AuditFileDetails](AuditFileDetails.md) — used in `audit_files`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

