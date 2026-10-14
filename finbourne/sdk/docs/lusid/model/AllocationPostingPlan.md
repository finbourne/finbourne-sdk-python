# AllocationPostingPlan

Everything booking an Allocation Event writes, in write order: the investors' lines, the roll-ups above them and  the fund side. Returned by a dry run, so a caller sees exactly what a booking would post before it does.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **lp_side** | [List[AllocationPostingLpLine]](AllocationPostingLpLine.md) | Optional | The instrument events written on each investor&#39;s commitment line, one per component. |
| **roll_ups** | [List[AllocationPostingRollUp]](AllocationPostingRollUp.md) | Optional | The roll-ups written on each vehicle&#39;s line on the register above it, summing the lines beneath. |
| **fund_side** | [List[AllocationPostingFundLine]](AllocationPostingFundLine.md) | Optional | The transactions written on the fund&#39;s own books. |
| **counts** | [AllocationPostingCounts](AllocationPostingCounts.md) | Optional | *No description available.* |
| **warnings** | [List[AllocationEventBookingWarning]](AllocationEventBookingWarning.md) | Optional | The validation rules the booking would be allowed to proceed through under the map&#39;s policy. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AllocationPostingPlan import AllocationPostingPlan

instance = AllocationPostingPlan(
    lp_side=[],  # optional — The instrument events written on each investor&#39;s commitment line, one per component.
    roll_ups=[],  # optional — The roll-ups written on each vehicle&#39;s line on the register above it, summing the lines beneath.
    fund_side=[],  # optional — The transactions written on the fund&#39;s own books.
    counts=AllocationPostingCounts(...),  # optional
    warnings=[]  # optional — The validation rules the booking would be allowed to proceed through under the map&#39;s policy.
)
```


## Related Models

- [AllocationPostingLpLine](AllocationPostingLpLine.md) — used in `lp_side`
- [AllocationPostingRollUp](AllocationPostingRollUp.md) — used in `roll_ups`
- [AllocationPostingFundLine](AllocationPostingFundLine.md) — used in `fund_side`
- [AllocationPostingCounts](AllocationPostingCounts.md)
- [AllocationEventBookingWarning](AllocationEventBookingWarning.md) — used in `warnings`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

