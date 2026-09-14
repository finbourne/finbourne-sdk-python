# RecInstance

The expanded view of a rec instance: its identity, lifecycle status, lock state, closed periods  (for Closed Period windows) and, per rec type, the time-series of runs in that rec type's run log.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [RecInstanceId](RecInstanceId.md) | Required | *No description available.* |
| **rec_definition_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **rec_definition_display_name** | **str** | Required | The display name of the rec definition the rec was instantiated for, as it stood as-at instantiation. Not re-synchronised if the definition is later renamed. |
| **as_at_instantiated** | **datetime** | Required | The asAt datetime at which the instance was first created. |
| **status** | **str** | Required | The instance-level lifecycle rollup. Available values: Running, Failures, ReviewAndApproval, AllApproved, Locked. |
| **as_at_locked** | **datetime** | Optional | The wall-clock time the lock action was performed. Null when the instance has not been locked. |
| **dates_locked** | [RecDatesReconciled](RecDatesReconciled.md) | Optional | *No description available.* |
| **closed_periods** | [RecClosedPeriods](RecClosedPeriods.md) | Optional | *No description available.* |
| **run_logs** | [Dict[str, RecRunLog]](RecRunLog.md) | Required | The instance&#39;s run history, keyed by rec type. Contains an entry for each rec type that has produced a result set, so a run appears only once it has completed or failed. Empty while the instance&#39;s first run is still in flight. |
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
    rec_definition_display_name="...",  # required — The display name of the rec definition the rec was instantiated for, as it stood as-at instantiation. Not re-synchronised if the definition is later renamed.
    as_at_instantiated=datetime.now(),  # required — The asAt datetime at which the instance was first created.
    status="...",  # required — The instance-level lifecycle rollup. Available values: Running, Failures, ReviewAndApproval, AllApproved, Locked.
    as_at_locked=datetime.now(),  # optional — The wall-clock time the lock action was performed. Null when the instance has not been locked.
    dates_locked=RecDatesReconciled(...),  # optional
    closed_periods=RecClosedPeriods(...),  # optional
    run_logs=RecRunLog(...),  # required — The instance&#39;s run history, keyed by rec type. Contains an entry for each rec type that has produced a result set, so a run appears only once it has completed or failed. Empty while the instance&#39;s first run is still in flight.
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
- [RecRunLog](RecRunLog.md) — used in `run_logs`
- [Version](Version.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

