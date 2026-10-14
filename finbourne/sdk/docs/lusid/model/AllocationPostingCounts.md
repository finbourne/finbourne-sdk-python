# AllocationPostingCounts

How many postings a plan writes on each side.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **lp_side** | **int** | Optional | The number of instrument events on investors&#39; lines. |
| **roll_ups** | **int** | Optional | The number of roll-ups. |
| **fund_side** | **int** | Optional | The number of fund-side transactions. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AllocationPostingCounts import AllocationPostingCounts

instance = AllocationPostingCounts(
    lp_side=0,  # optional — The number of instrument events on investors&#39; lines.
    roll_ups=0,  # optional — The number of roll-ups.
    fund_side=0  # optional — The number of fund-side transactions.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

