# LegDefinition

Definition of the set of flow and index conventions along with other miscellaneous information required to generate an instrument leg.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **convention_name** | [FlowConventionName](FlowConventionName.md) | Optional | *No description available.* |
| **conventions** | [FlowConventions](FlowConventions.md) | Optional | *No description available.* |
| **index_convention** | [IndexConvention](IndexConvention.md) | Optional | *No description available.* |
| **index_convention_name** | [FlowConventionName](FlowConventionName.md) | Optional | *No description available.* |
| **notional_exchange_type** | **str** | Required | what type of notional exchange does the leg have    Supported string (enumeration) values are: [None, Initial, Final, Both]. |
| **pay_receive** | **str** | Required | Is the leg to be paid or received    Supported string (enumeration) values are: [Pay, Receive]. |
| **rate_or_spread** | **float** | Required | Is there either a fixed rate (non-zero) or spread to be paid over the value of the leg. |
| **reset_convention** | **str** | Optional | Control how resets are generated relative to swap payment convention(s).    Supported string (enumeration) values are: [InAdvance, InArrears].  Defaults to \&quot;InAdvance\&quot; if not set. |
| **stub_type** | **str** | Required | If a stub is required should it be at the front or back of the leg.    Supported string (enumeration) values are: [None, ShortFront, ShortBack, LongBack, LongFront, Both]. |
| **compounding** | [Compounding](Compounding.md) | Optional | *No description available.* |
| **amortisation** | [StepSchedule](StepSchedule.md) | Optional | *No description available.* |
| **first_regular_payment_date** | **datetime** | Optional | Optional payment date of the first regular coupon.  Must be greater than the StartDate.  If set, the regular coupon schedule will be built such that the first regular coupon  will end on this date. The start date of this coupon will be calculated as normal and  a stub coupon will be created from the StartDate to the start of the first regular coupon. |
| **first_coupon_type** | **str** | Optional | Optional coupon type setting for the first coupon, can be used with Stub coupons.  If set to \&quot;ProRata\&quot; (the default), the coupon year fraction is calculated as normal,  however if set to \&quot;Full\&quot; the year fraction is overwritten with the standard year fraction  for a regular ful\&quot; coupon. Note this does not use the day count convention but rather is defined  directly from the tenor (i.e. a quarterly leg will be set to 0.25).    Supported string (enumeration) values are: [ProRata, Full]. |
| **last_regular_payment_date** | **datetime** | Optional | Optional payment date of the last regular coupon.  Must be less than the Maturity date.  If set, the regular coupon schedule will be built up to this date and the final  coupon will be a stub between this date and the Maturity date. |
| **last_coupon_type** | **str** | Optional | Optional coupon type setting for the last coupon, can be used with Stub coupons.  If set to \&quot;ProRata\&quot; (the default), the coupon year fraction is calculated as normal,  however if set to \&quot;Full\&quot; the year fraction is overwritten with the standard year fraction  for a regular ful\&quot; coupon. Note this does not use the day count convention but rather is defined  directly from the tenor (i.e. a quarterly leg will be set to 0.25).    Supported string (enumeration) values are: [ProRata, Full]. |
| **fx_linked_notional_schedule** | [FxLinkedNotionalSchedule](FxLinkedNotionalSchedule.md) | Optional | *No description available.* |
| **intermediate_notional_exchange** | **bool** | Optional | Indicates whether there are intermediate notional exchanges. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.LegDefinition import LegDefinition

instance = LegDefinition(
    convention_name=FlowConventionName(...),  # optional
    conventions=FlowConventions(...),  # optional
    index_convention=IndexConvention(...),  # optional
    index_convention_name=FlowConventionName(...),  # optional
    notional_exchange_type="...",  # required — what type of notional exchange does the leg have    Supported string (enumeration) values are: [None, Initial, Final, Both].
    pay_receive="...",  # required — Is the leg to be paid or received    Supported string (enumeration) values are: [Pay, Receive].
    rate_or_spread=0.0,  # required — Is there either a fixed rate (non-zero) or spread to be paid over the value of the leg.
    reset_convention="...",  # optional — Control how resets are generated relative to swap payment convention(s).    Supported string (enumeration) values are: [InAdvance, InArrears].  Defaults to \&quot;InAdvance\&quot; if not set.
    stub_type="...",  # required — If a stub is required should it be at the front or back of the leg.    Supported string (enumeration) values are: [None, ShortFront, ShortBack, LongBack, LongFront, Both].
    compounding=Compounding(...),  # optional
    amortisation=StepSchedule(...),  # optional
    first_regular_payment_date=datetime.now(),  # optional — Optional payment date of the first regular coupon.  Must be greater than the StartDate.  If set, the regular coupon schedule will be built such that the first regular coupon  will end on this date. The start date of this coupon will be calculated as normal and  a stub coupon will be created from the StartDate to the start of the first regular coupon.
    first_coupon_type="...",  # optional — Optional coupon type setting for the first coupon, can be used with Stub coupons.  If set to \&quot;ProRata\&quot; (the default), the coupon year fraction is calculated as normal,  however if set to \&quot;Full\&quot; the year fraction is overwritten with the standard year fraction  for a regular ful\&quot; coupon. Note this does not use the day count convention but rather is defined  directly from the tenor (i.e. a quarterly leg will be set to 0.25).    Supported string (enumeration) values are: [ProRata, Full].
    last_regular_payment_date=datetime.now(),  # optional — Optional payment date of the last regular coupon.  Must be less than the Maturity date.  If set, the regular coupon schedule will be built up to this date and the final  coupon will be a stub between this date and the Maturity date.
    last_coupon_type="...",  # optional — Optional coupon type setting for the last coupon, can be used with Stub coupons.  If set to \&quot;ProRata\&quot; (the default), the coupon year fraction is calculated as normal,  however if set to \&quot;Full\&quot; the year fraction is overwritten with the standard year fraction  for a regular ful\&quot; coupon. Note this does not use the day count convention but rather is defined  directly from the tenor (i.e. a quarterly leg will be set to 0.25).    Supported string (enumeration) values are: [ProRata, Full].
    fx_linked_notional_schedule=FxLinkedNotionalSchedule(...),  # optional
    intermediate_notional_exchange=True  # optional — Indicates whether there are intermediate notional exchanges.
)
```


## Related Models

- [FlowConventionName](FlowConventionName.md)
- [FlowConventions](FlowConventions.md)
- [IndexConvention](IndexConvention.md)
- [FlowConventionName](FlowConventionName.md)
- [Compounding](Compounding.md)
- [StepSchedule](StepSchedule.md)
- [FxLinkedNotionalSchedule](FxLinkedNotionalSchedule.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

