# RecInstance

The expanded view of a rec instance: its identity, lifecycle status, lock state, closed periods  (for Closed Period windows) and the time-series of runs in the run log.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [RecInstanceId](RecInstanceId.md) | Required | *No description available.* |
| **rec_definition_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **as_at_instantiated** | **datetime** | Required | The asAt datetime at which the instance was first created. |
| **status** | **str** | Required | The instance-level lifecycle rollup. Available values: Running, Failures, ReviewAndApproval, AllApproved, Locked. |
| **as_at_locked** | **datetime** | Optional | The wall-clock time the lock action was performed. Null when the instance has not been locked. |
| **dates_locked** | [RecDatesReconciled](RecDatesReconciled.md) | Optional | *No description available.* |
| **closed_periods** | [RecClosedPeriods](RecClosedPeriods.md) | Optional | *No description available.* |
| **run_log** | [List[RecRunLogEntry]](RecRunLogEntry.md) | Required | A chronologically ordered list of all runs on the instance. Always contains at least one entry. |
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RecInstance import RecInstance

instance = RecInstance(
    id=RecInstanceId(...),  # required
    rec_definition_id=ResourceId(...),  # required
    as_at_instantiated=datetime.now(),  # required — The asAt datetime at which the instance was first created.
    status="...",  # required — The instance-level lifecycle rollup. Available values: Running, Failures, ReviewAndApproval, AllApproved, Locked.
    as_at_locked=datetime.now(),  # optional — The wall-clock time the lock action was performed. Null when the instance has not been locked.
    dates_locked=RecDatesReconciled(...),  # optional
    closed_periods=RecClosedPeriods(...),  # optional
    run_log=[],  # required — A chronologically ordered list of all runs on the instance. Always contains at least one entry.
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    version=Version(...),  # optional
    links=[]  # optional
)
```


## Related Models

- [RecInstanceId](RecInstanceId.md)
- [ResourceId](ResourceId.md)
- [RecDatesReconciled](RecDatesReconciled.md)
- [RecClosedPeriods](RecClosedPeriods.md)
- [RecRunLogEntry](RecRunLogEntry.md) — used in `run_log`
- [Version](Version.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

