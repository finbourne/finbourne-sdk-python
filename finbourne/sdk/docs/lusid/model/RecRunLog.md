# RecRunLog

One rec type's run history within a rec instance: its most recent runs, and the total number of runs those  were taken from.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **run_count** | **int** | Required | The total number of runs of this rec type, which is not necessarily the number returned. A value greater than ten means runs has been truncated; the runs beyond it remain retrievable from previousRuns on the rec type&#39;s result set. |
| **runs** | [List[RecRunLogEntry]](RecRunLogEntry.md) | Required | The ten most recent runs of this rec type, ordered by run number descending, so the current run is always the first entry. Exactly one entry has a null supersededAsAt. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RecRunLog import RecRunLog

instance = RecRunLog(
    run_count=0,  # required — The total number of runs of this rec type, which is not necessarily the number returned. A value greater than ten means runs has been truncated; the runs beyond it remain retrievable from previousRuns on the rec type&#39;s result set.
    runs=[]  # required — The ten most recent runs of this rec type, ordered by run number descending, so the current run is always the first entry. Exactly one entry has a null supersededAsAt.
)
```

- [RecRunLogEntry](RecRunLogEntry.md) — used in `runs`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

