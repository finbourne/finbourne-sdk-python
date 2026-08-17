# PikSchedule

A PikSchedule represents Payment-in-Kind features for a ComplexBond.  It works in conjunction with existing FixedSchedules or FloatSchedules to define  how interest is paid during duration of the schedule.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **start_date** | **datetime** | Required | The start date of the PIK schedule period. |
| **maturity_date** | **datetime** | Required | The end date of the PIK schedule period. |
| **is_pik_fraction_electable** | **bool** | Optional | If true, the PIK fraction is electable at each payment date.  Defaults to false. |
| **pik_fraction** | **float** | Optional | The fraction of the coupon that is paid in kind, where 0 means fully cash and 1 means fully PIK.  Required if IsPikFractionElectable is false or null. Must satisfy 0 &lt;&#x3D; pikFraction &lt;&#x3D; 1. |
| **pik_payment_type** | **str** | Optional | The type of PIK payment to be used for the duration of this schedule.  InterestCapitalisation adds the paid-in-kind portion to the bond&#39;s current face;  AdditionalSecurities settles it by delivering units of another instrument, named on each  period&#39;s PikBondInterestEvent; Electable leaves the choice to a per-period election.                Supported string (enumeration) values are: [Electable, InterestCapitalisation, AdditionalSecurities]. |
| **pik_rate** | **float** | Optional | The PIK interest rate. Must be greater than or equal to zero.  null indicates no override PIK interest rate. |
| **pik_spread** | **float** | Optional | The PIK spread to be added to the base rate for the final PIK rate.  null indicates no spread on base rate. |
| **schedule_type** | **str** | Required | Available values: FixedSchedule, FloatSchedule, OptionalitySchedule, StepSchedule, Exercise, FxRateSchedule, FxLinkedNotionalSchedule, BondConversionSchedule, PikSchedule, CommodityCalendarSchedule, Invalid, CancelSchedule. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PikSchedule import PikSchedule

instance = PikSchedule(
    start_date=datetime.now(),  # required — The start date of the PIK schedule period.
    maturity_date=datetime.now(),  # required — The end date of the PIK schedule period.
    is_pik_fraction_electable=True,  # optional — If true, the PIK fraction is electable at each payment date.  Defaults to false.
    pik_fraction=0.0,  # optional — The fraction of the coupon that is paid in kind, where 0 means fully cash and 1 means fully PIK.  Required if IsPikFractionElectable is false or null. Must satisfy 0 &lt;&#x3D; pikFraction &lt;&#x3D; 1.
    pik_payment_type="...",  # optional — The type of PIK payment to be used for the duration of this schedule.  InterestCapitalisation adds the paid-in-kind portion to the bond&#39;s current face;  AdditionalSecurities settles it by delivering units of another instrument, named on each  period&#39;s PikBondInterestEvent; Electable leaves the choice to a per-period election.                Supported string (enumeration) values are: [Electable, InterestCapitalisation, AdditionalSecurities].
    pik_rate=0.0,  # optional — The PIK interest rate. Must be greater than or equal to zero.  null indicates no override PIK interest rate.
    pik_spread=0.0,  # optional — The PIK spread to be added to the base rate for the final PIK rate.  null indicates no spread on base rate.
    schedule_type="..."  # required — Available values: FixedSchedule, FloatSchedule, OptionalitySchedule, StepSchedule, Exercise, FxRateSchedule, FxLinkedNotionalSchedule, BondConversionSchedule, PikSchedule, CommodityCalendarSchedule, Invalid, CancelSchedule.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

