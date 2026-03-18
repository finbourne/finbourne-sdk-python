# FloatSchedule

Schedule for floating rate coupon payments.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **start_date** | **datetime** | Optional | Date from which LUSID starts generating the payment schedule. |
| **maturity_date** | **datetime** | Optional | Last date of the payment generation schedule. May not necessarily be the maturity date  of the underlying instrument (e.g. in case the instrument has multiple payment schedules). |
| **flow_conventions** | [FlowConventions](FlowConventions.md) | Optional | *No description available.* |
| **convention_name** | [FlowConventionName](FlowConventionName.md) | Optional | *No description available.* |
| **ex_dividend_days** | **int** | Optional | Optional. Number of calendar days in the ex-dividend period.  If the settlement date falls in the ex-dividend period then the coupon paid is zero and the accrued interest is negative.  If set, this must be a non-negative number.  If not set, or set to 0, then there is no ex-dividend period.                NOTE: This field is deprecated.  If you wish to set the ExDividendDays on a bond, please use the ExDividendConfiguration. |
| **index_convention_name** | [FlowConventionName](FlowConventionName.md) | Optional | *No description available.* |
| **index_conventions** | [IndexConvention](IndexConvention.md) | Optional | *No description available.* |
| **notional** | **float** | Optional | Scaling factor, the quantity outstanding on which the rate will be paid. |
| **payment_currency** | **str** | Required | Payment currency. This does not have to be the same as the nominal bond or observation/reset currency. |
| **spread** | **float** | Optional | Spread over floating rate given as a fraction. |
| **stub_type** | **str** | Optional | When a payment schedule doesn&#39;t have regular payment intervals just because of the  first and/or last coupons of the schedule, we call those irregular coupons stubs.  This configuration specifies what type of stub is used when building the schedule  Supported values are:  None &#x3D; this is a regular payment schedule with no stubs. DO NOT use it with irregular schedules or you will get incorrect and unexpected behaviour.  ShortFront &#x3D; this is an irregular payment schedule where only the first coupon is irregular, and covers a payment period that is shorter than the regular payment period.  ShortBack &#x3D; this is an irregular payment schedule where only the last coupon is irregular, and covers a payment period that is shorter than the regular payment period.  LongFront &#x3D; this is an irregular payment schedule where only the first coupon is irregular, and covers a payment period that is longer than the regular payment period.  LongBack &#x3D; this is an irregular payment schedule where only the last coupon is irregular, and covers a payment period that is longer than the regular payment period.  Both &#x3D; this is an irregular payment schedule where both the first and the last coupons are irregular, and the length of these periods is calculated based on the first coupon payment date that should have been explicitly set. |
| **ex_dividend_configuration** | [ExDividendConfiguration](ExDividendConfiguration.md) | Optional | *No description available.* |
| **compounding** | [Compounding](Compounding.md) | Optional | *No description available.* |
| **reset_convention** | **str** | Optional | Control how resets are generated relative to payment convention(s).    Supported string (enumeration) values are: [InAdvance, InArrears].  Defaults to \&quot;InAdvance\&quot; if not set. |
| **use_annualised_direct_rates** | **bool** | Optional | Flag indicating whether to use daily updated annualised interest  rates for calculating the accrued interest. Defaults to false. |
| **cap_rate** | **float** | Optional | The maximum floating rate which a cashflow can accrue. |
| **floor_rate** | **float** | Optional | The minimum floating rate which a cashflow can accrue. |
| **schedule_type** | **str** | Required | The available values are: FixedSchedule, FloatSchedule, OptionalitySchedule, StepSchedule, Exercise, FxRateSchedule, FxLinkedNotionalSchedule, BondConversionSchedule, Invalid |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FloatSchedule import FloatSchedule

instance = FloatSchedule(
    start_date=datetime.now(),  # optional — Date from which LUSID starts generating the payment schedule.
    maturity_date=datetime.now(),  # optional — Last date of the payment generation schedule. May not necessarily be the maturity date  of the underlying instrument (e.g. in case the instrument has multiple payment schedules).
    flow_conventions=FlowConventions(...),  # optional
    convention_name=FlowConventionName(...),  # optional
    ex_dividend_days=0,  # optional — Optional. Number of calendar days in the ex-dividend period.  If the settlement date falls in the ex-dividend period then the coupon paid is zero and the accrued interest is negative.  If set, this must be a non-negative number.  If not set, or set to 0, then there is no ex-dividend period.                NOTE: This field is deprecated.  If you wish to set the ExDividendDays on a bond, please use the ExDividendConfiguration.
    index_convention_name=FlowConventionName(...),  # optional
    index_conventions=IndexConvention(...),  # optional
    notional=0.0,  # optional — Scaling factor, the quantity outstanding on which the rate will be paid.
    payment_currency="...",  # required — Payment currency. This does not have to be the same as the nominal bond or observation/reset currency.
    spread=0.0,  # optional — Spread over floating rate given as a fraction.
    stub_type="...",  # optional — When a payment schedule doesn&#39;t have regular payment intervals just because of the  first and/or last coupons of the schedule, we call those irregular coupons stubs.  This configuration specifies what type of stub is used when building the schedule  Supported values are:  None &#x3D; this is a regular payment schedule with no stubs. DO NOT use it with irregular schedules or you will get incorrect and unexpected behaviour.  ShortFront &#x3D; this is an irregular payment schedule where only the first coupon is irregular, and covers a payment period that is shorter than the regular payment period.  ShortBack &#x3D; this is an irregular payment schedule where only the last coupon is irregular, and covers a payment period that is shorter than the regular payment period.  LongFront &#x3D; this is an irregular payment schedule where only the first coupon is irregular, and covers a payment period that is longer than the regular payment period.  LongBack &#x3D; this is an irregular payment schedule where only the last coupon is irregular, and covers a payment period that is longer than the regular payment period.  Both &#x3D; this is an irregular payment schedule where both the first and the last coupons are irregular, and the length of these periods is calculated based on the first coupon payment date that should have been explicitly set.
    ex_dividend_configuration=ExDividendConfiguration(...),  # optional
    compounding=Compounding(...),  # optional
    reset_convention="...",  # optional — Control how resets are generated relative to payment convention(s).    Supported string (enumeration) values are: [InAdvance, InArrears].  Defaults to \&quot;InAdvance\&quot; if not set.
    use_annualised_direct_rates=True,  # optional — Flag indicating whether to use daily updated annualised interest  rates for calculating the accrued interest. Defaults to false.
    cap_rate=0.0,  # optional — The maximum floating rate which a cashflow can accrue.
    floor_rate=0.0,  # optional — The minimum floating rate which a cashflow can accrue.
    schedule_type="..."  # required — The available values are: FixedSchedule, FloatSchedule, OptionalitySchedule, StepSchedule, Exercise, FxRateSchedule, FxLinkedNotionalSchedule, BondConversionSchedule, Invalid
)
```

- [FlowConventions](FlowConventions.md)
- [FlowConventionName](FlowConventionName.md)
- [FlowConventionName](FlowConventionName.md)
- [IndexConvention](IndexConvention.md)
- [ExDividendConfiguration](ExDividendConfiguration.md)
- [Compounding](Compounding.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

