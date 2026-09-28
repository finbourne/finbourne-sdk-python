# AllocationMapResolution

The result of resolving an Allocation Map for one event: how much each investor record receives, and why.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **event_type** | **str** | Optional | The kind of allocation event that was resolved. Available values: CapitalCall, Distribution, FeeExpense, ValuationMove. |
| **amount** | **float** | Optional | The amount that was shared. |
| **currency** | **str** | Optional | The currency of the amount. |
| **basis_rule** | **str** | Optional | The basis the map applies to this event type. Available values: ValueWeighted, PropertyWeighted, FixedPercentage. |
| **basis_pool** | **float** | Optional | The sum of the basis values over the participants that share the remainder pro rata. |
| **fixed_total** | **float** | Optional | The total taken off the top by FixedPercentage exceptions before the remainder is shared. |
| **participant_count** | **int** | Optional | The number of investor records that receive a share, whether fixed or pro rata. |
| **excluded_count** | **int** | Optional | The number of investor records an exception removed from the allocation. |
| **allocations** | [List[AllocationMapAllocation]](AllocationMapAllocation.md) | Optional | The share of each investor record, including those excluded, which receive nothing. |
| **reconciles** | **bool** | Optional | Whether the allocated amounts sum exactly to the requested amount. Amounts are rounded to two decimal places with the largest-remainder method, so an amount with more decimal places does not reconcile. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AllocationMapResolution import AllocationMapResolution

instance = AllocationMapResolution(
    event_type="...",  # optional — The kind of allocation event that was resolved. Available values: CapitalCall, Distribution, FeeExpense, ValuationMove.
    amount=0.0,  # optional — The amount that was shared.
    currency="...",  # optional — The currency of the amount.
    basis_rule="...",  # optional — The basis the map applies to this event type. Available values: ValueWeighted, PropertyWeighted, FixedPercentage.
    basis_pool=0.0,  # optional — The sum of the basis values over the participants that share the remainder pro rata.
    fixed_total=0.0,  # optional — The total taken off the top by FixedPercentage exceptions before the remainder is shared.
    participant_count=0,  # optional — The number of investor records that receive a share, whether fixed or pro rata.
    excluded_count=0,  # optional — The number of investor records an exception removed from the allocation.
    allocations=[],  # optional — The share of each investor record, including those excluded, which receive nothing.
    reconciles=True  # optional — Whether the allocated amounts sum exactly to the requested amount. Amounts are rounded to two decimal places with the largest-remainder method, so an amount with more decimal places does not reconcile.
)
```

- [AllocationMapAllocation](AllocationMapAllocation.md) — used in `allocations`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

