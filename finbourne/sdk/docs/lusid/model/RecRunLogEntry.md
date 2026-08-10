# RecRunLogEntry

A single run within an instance's run log. All runs share the same effective dates (frozen at  instantiation); each has a different asAt, advanced on re-run.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **run_number** | **int** | Required | The run number within the instance. Increments with each re-run. |
| **run_as_at** | **datetime** | Required | The asAt datetime at which the run happened. |
| **superseded_as_at** | **datetime** | Optional | The asAt datetime at which this run was superseded by a subsequent run. |
| **dates_reconciled** | [../model/RecDatesReconciled](RecDatesReconciled.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RecRunLogEntry import RecRunLogEntry

instance = RecRunLogEntry(
    run_number=0,  # required — The run number within the instance. Increments with each re-run.
    run_as_at=datetime.now(),  # required — The asAt datetime at which the run happened.
    superseded_as_at=datetime.now(),  # optional — The asAt datetime at which this run was superseded by a subsequent run.
    dates_reconciled=RecDatesReconciled(...)  # required
)
```

- [RecDatesReconciled](RecDatesReconciled.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

