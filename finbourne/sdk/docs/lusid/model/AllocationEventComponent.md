# AllocationEventComponent

One component of an Allocation Event: a part of the amount shared on its own basis and booked to its own slot.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **component** | **str** | Required | The component. For a CapitalCall one of Investment, MgmtFee, OtherFee, PartnershipExpense, OrgCost, Recall, EqualisationInterest or LatePaymentInterest; for a Distribution one of ROC, RealisedGain, Dividend, Interest, OtherIncome, CarryPaid, Withholding or ReturnOfExcess. |
| **amount** | **float** | Required | The part of the event amount this component carries, in the event currency. May be zero, in which case the component allocates nothing. |
| **origin_member_short_code** | **str** | Optional | The member of the structure the component originates from, for a basis measured per deal such as PaidInForDeal. Absent means the map&#39;s own member. |
| **waterfall_tier** | **str** | Optional | For a distribution component, the tier of the waterfall it was paid under: ReturnOfContributions, PreferredReturn, CatchUp, CarriedInterest or Residual. |
| **tax_character** | **str** | Optional | For a distribution component, the tax character of the amount: ROC, Gain, Income or Deemed. |
| **recallable_amount** | **float** | Optional | For the ROC component of a Distribution only, how much of the component the fund may call back, between zero and the component amount. Shared pro rata to each investor&#39;s ROC share. Absent means the allocation map&#39;s recall window decides. |
| **recallable_until** | **datetime** | Optional | For the ROC component of a Distribution only, the last date the recallable amount may be called back. Must not be before the event date and requires a non-zero recallable amount. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AllocationEventComponent import AllocationEventComponent

instance = AllocationEventComponent(
    component="...",  # required — The component. For a CapitalCall one of Investment, MgmtFee, OtherFee, PartnershipExpense, OrgCost, Recall, EqualisationInterest or LatePaymentInterest; for a Distribution one of ROC, RealisedGain, Dividend, Interest, OtherIncome, CarryPaid, Withholding or ReturnOfExcess.
    amount=0.0,  # required — The part of the event amount this component carries, in the event currency. May be zero, in which case the component allocates nothing.
    origin_member_short_code="...",  # optional — The member of the structure the component originates from, for a basis measured per deal such as PaidInForDeal. Absent means the map&#39;s own member.
    waterfall_tier="...",  # optional — For a distribution component, the tier of the waterfall it was paid under: ReturnOfContributions, PreferredReturn, CatchUp, CarriedInterest or Residual.
    tax_character="...",  # optional — For a distribution component, the tax character of the amount: ROC, Gain, Income or Deemed.
    recallable_amount=0.0,  # optional — For the ROC component of a Distribution only, how much of the component the fund may call back, between zero and the component amount. Shared pro rata to each investor&#39;s ROC share. Absent means the allocation map&#39;s recall window decides.
    recallable_until=datetime.now()  # optional — For the ROC component of a Distribution only, the last date the recallable amount may be called back. Must not be before the event date and requires a non-zero recallable amount.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

