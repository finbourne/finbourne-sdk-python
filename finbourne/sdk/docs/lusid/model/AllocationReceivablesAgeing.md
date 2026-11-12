# AllocationReceivablesAgeing

What each investor still owes on a booked capital call as of a date, and how late it is.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **as_of** | **datetime** | Optional | The date the receivables are aged as of. |
| **due_date** | **datetime** | Optional | The date the cash was due. |
| **outstanding** | **float** | Optional | What the investors still owe, looking through feeders to their LPs so a roll-up is not counted twice. |
| **receivables** | [List[AllocationReceivable]](AllocationReceivable.md) | Optional | One entry per investor record and side that was called on a register. |
| **registers** | [List[AllocationRegisterReceivable]](AllocationRegisterReceivable.md) | Optional | What each register is owed on its own lines, a feeder&#39;s roll-up included. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AllocationReceivablesAgeing import AllocationReceivablesAgeing

instance = AllocationReceivablesAgeing(
    as_of=datetime.now(),  # optional — The date the receivables are aged as of.
    due_date=datetime.now(),  # optional — The date the cash was due.
    outstanding=0.0,  # optional — What the investors still owe, looking through feeders to their LPs so a roll-up is not counted twice.
    receivables=[],  # optional — One entry per investor record and side that was called on a register.
    registers=[]  # optional — What each register is owed on its own lines, a feeder&#39;s roll-up included.
)
```

- [AllocationReceivable](AllocationReceivable.md) — used in `receivables`
- [AllocationRegisterReceivable](AllocationRegisterReceivable.md) — used in `registers`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

