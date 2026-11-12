# MarginRunAllocation

How far the allocation pass over a run's base calls got: whether it ran, how many calls it proposed collateral  for, and what it left out.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **status** | **str** | Required | How far the allocation pass got. One of Pending, Completed, Skipped or Failed. |
| **allocated_call_count** | **int** | Required | How many calls the pass proposed collateral for. |
| **detail** | **str** | Optional | Which calls the pass could not allocate and why, or why it failed. Null when every call that moves our collateral was allocated. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.MarginRunAllocation import MarginRunAllocation

instance = MarginRunAllocation(
    status="...",  # required — How far the allocation pass got. One of Pending, Completed, Skipped or Failed.
    allocated_call_count=0,  # required — How many calls the pass proposed collateral for.
    detail="..."  # optional — Which calls the pass could not allocate and why, or why it failed. Null when every call that moves our collateral was allocated.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

