# AllocationEventEqualisation

The terms of a subsequent close an Equalisation Allocation Event applies: the booked prior calls to equalise, the  partners admitted, and how interest, excess and profit and loss are treated.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **prior_call_ids** | [List[ResourceId]](ResourceId.md) | Required | The booked capital calls to equalise, and any earlier equalisation on the same map whose catch-up the admitted partners must also be brought level with. Each must be booked, on the same allocation map and in the same currency. |
| **new_investor_record_ids** | **List[str]** | Required | The investor records admitted at this close. Each must be on the register with its commitment at the event date. |
| **interest_rate** | **float** | Optional | The simple annual rate of equalisation interest the admitted partners pay on each catch-up from the prior call&#39;s due date to the event date. Defaults to 0.08. |
| **day_count_convention** | **str** | Optional | The day count of the equalisation interest: ACT/365 or ACT/360. Defaults to ACT/365. |
| **interest_on_fees** | **bool** | Optional | Whether equalisation interest is also charged on the management fee catch-ups, from each fee&#39;s due date. Defaults to false. |
| **treatment** | **str** | Optional | How the existing partners&#39; excess is returned: ReturnOfExcess restores it to their uncalled commitment; RecallableDistribution distributes it as recallable capital. Defaults to ReturnOfExcess. Available values: ReturnOfExcess, RecallableDistribution. |
| **pnl** | **str** | Optional | Whether profit and loss already allocated is re-trued between partners with no cash so each holds its post-close share (ReTrue), or the equalisation is kept to capital (CapitalOnly). Defaults to ReTrue. Available values: ReTrue, CapitalOnly. |
| **fee_catch_ups** | [List[AllocationEventEqualisationFeeCatchUp]](AllocationEventEqualisationFeeCatchUp.md) | Optional | The management fees each admitted partner owes from the first fee date to the close, including any stub period, as explicit amounts. Paid to the manager and allocated to that partner only. |
| **marks** | [List[AllocationEventEqualisationMark]](AllocationEventEqualisationMark.md) | Optional | The valuation moves already allocated to the existing partners, by the member of the structure they belong to, to re-true to the admitted partners. Ignored when the profit and loss treatment is CapitalOnly. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AllocationEventEqualisation import AllocationEventEqualisation

instance = AllocationEventEqualisation(
    prior_call_ids=[],  # required — The booked capital calls to equalise, and any earlier equalisation on the same map whose catch-up the admitted partners must also be brought level with. Each must be booked, on the same allocation map and in the same currency.
    new_investor_record_ids=,  # required — The investor records admitted at this close. Each must be on the register with its commitment at the event date.
    interest_rate=0.0,  # optional — The simple annual rate of equalisation interest the admitted partners pay on each catch-up from the prior call&#39;s due date to the event date. Defaults to 0.08.
    day_count_convention="...",  # optional — The day count of the equalisation interest: ACT/365 or ACT/360. Defaults to ACT/365.
    interest_on_fees=True,  # optional — Whether equalisation interest is also charged on the management fee catch-ups, from each fee&#39;s due date. Defaults to false.
    treatment="...",  # optional — How the existing partners&#39; excess is returned: ReturnOfExcess restores it to their uncalled commitment; RecallableDistribution distributes it as recallable capital. Defaults to ReturnOfExcess. Available values: ReturnOfExcess, RecallableDistribution.
    pnl="...",  # optional — Whether profit and loss already allocated is re-trued between partners with no cash so each holds its post-close share (ReTrue), or the equalisation is kept to capital (CapitalOnly). Defaults to ReTrue. Available values: ReTrue, CapitalOnly.
    fee_catch_ups=[],  # optional — The management fees each admitted partner owes from the first fee date to the close, including any stub period, as explicit amounts. Paid to the manager and allocated to that partner only.
    marks=[]  # optional — The valuation moves already allocated to the existing partners, by the member of the structure they belong to, to re-true to the admitted partners. Ignored when the profit and loss treatment is CapitalOnly.
)
```


## Related Models

- [ResourceId](ResourceId.md) — used in `prior_call_ids`
- [AllocationEventEqualisationFeeCatchUp](AllocationEventEqualisationFeeCatchUp.md) — used in `fee_catch_ups`
- [AllocationEventEqualisationMark](AllocationEventEqualisationMark.md) — used in `marks`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

