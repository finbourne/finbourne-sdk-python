# AllocationReceivablesAgeing

What each investor still owes on a booked capital call as of a date, and how late it is.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **as_of** | **datetime** | Optional | The date the receivables are aged as of. |
| **due_date** | **datetime** | Optional | The date the cash was due. |
| **outstanding** | **float** | Optional | The total still owed across all investor records. |
| **receivables** | [List[AllocationReceivable]](AllocationReceivable.md) | Optional | One entry per investor record that was called. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AllocationReceivablesAgeing import AllocationReceivablesAgeing

instance = AllocationReceivablesAgeing(
    as_of=datetime.now(),  # optional — The date the receivables are aged as of.
    due_date=datetime.now(),  # optional — The date the cash was due.
    outstanding=0.0,  # optional — The total still owed across all investor records.
    receivables=[]  # optional — One entry per investor record that was called.
)
```

- [AllocationReceivable](AllocationReceivable.md) — used in `receivables`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

