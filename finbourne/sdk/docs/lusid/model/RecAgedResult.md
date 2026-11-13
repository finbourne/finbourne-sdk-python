# RecAgedResult

A summary of a rec result in another instance, as at the stamp that first recorded it.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | **str** | Required | The id of the result within its instance, e.g. &#39;Holding-break-1&#39;. With instanceId, it fully qualifies the result. |
| **instance_id** | [RecInstanceId](RecInstanceId.md) | Required | *No description available.* |
| **run_number** | **int** | Required | The result&#39;s latest run as at the stamp that first recorded it. |
| **run_as_at** | **datetime** | Required | The asAt datetime of the result&#39;s latest run as at the stamp that first recorded it. |
| **first_run_seen** | **int** | Required | The run in which the result was first assigned its id. |
| **as_at_first_seen** | **datetime** | Required | The runAsAt of the run in which the result first appeared in its instance, the run numbered firstRunSeen. Written once: re-runs leave it unchanged. |
| **dates_reconciled** | [RecDatesReconciled](RecDatesReconciled.md) | Required | *No description available.* |
| **exception_status** | **str** | Required | The result&#39;s exception status as at the stamp that first recorded it: Open or Closed. Available values: Open, Closed. |
| **closure_type** | **str** | Optional | The result&#39;s exception closure type as at the stamp that first recorded it. Null while the exception is open. Available values: Cleared, Accepted, ForceMatched. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RecAgedResult import RecAgedResult

instance = RecAgedResult(
    id="...",  # required — The id of the result within its instance, e.g. &#39;Holding-break-1&#39;. With instanceId, it fully qualifies the result.
    instance_id=RecInstanceId(...),  # required
    run_number=0,  # required — The result&#39;s latest run as at the stamp that first recorded it.
    run_as_at=datetime.now(),  # required — The asAt datetime of the result&#39;s latest run as at the stamp that first recorded it.
    first_run_seen=0,  # required — The run in which the result was first assigned its id.
    as_at_first_seen=datetime.now(),  # required — The runAsAt of the run in which the result first appeared in its instance, the run numbered firstRunSeen. Written once: re-runs leave it unchanged.
    dates_reconciled=RecDatesReconciled(...),  # required
    exception_status="...",  # required — The result&#39;s exception status as at the stamp that first recorded it: Open or Closed. Available values: Open, Closed.
    closure_type="..."  # optional — The result&#39;s exception closure type as at the stamp that first recorded it. Null while the exception is open. Available values: Cleared, Accepted, ForceMatched.
)
```

- [RecInstanceId](RecInstanceId.md)
- [RecDatesReconciled](RecDatesReconciled.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

