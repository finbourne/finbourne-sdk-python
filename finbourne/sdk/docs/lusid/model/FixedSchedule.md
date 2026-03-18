# FixedSchedule

Schedule for fixed coupon payments
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **start_date** | **datetime** | Required | Date from which LUSID starts generating the payment schedule. |
| **maturity_date** | **datetime** | Required | Last date of the payment generation schedule. May not necessarily be the maturity date  of the underlying instrument (e.g. in case the instrument has multiple payment schedules). |
| **flow_conventions** | [FlowConventions](FlowConventions.md) | Optional | *No description available.* |
| **coupon_rate** | **float** | Optional | Coupon rate given as a fraction. |
| **convention_name** | [FlowConventionName](FlowConventionName.md) | Optional | *No description available.* |
| **ex_dividend_days** | **int** | Optional | Optional. Number of calendar days in the ex-dividend period.  If the settlement date falls in the ex-dividend period then the coupon paid is zero and the accrued interest is negative.  If set, this must be a non-negative number.  If not set, or set to 0, then there is no ex-dividend period.                NOTE: This field is deprecated.  If you wish to set the ExDividendDays on a bond, please use the ExDividendConfiguration. |
| **notional** | **float** | Optional | Scaling factor, the quantity outstanding on which the rate will be paid. |
| **payment_currency** | **str** | Required | Payment currency. This does not have to be the same as the nominal bond or observation/reset currency. |
| **stub_type** | **str** | Optional | When a payment schedule doesn&#39;t have regular payment intervals just because of the  first and/or last coupons of the schedule, we call those irregular coupons stubs.  This configuration specifies what type of stub is used when building the schedule  Supported values are:  None &#x3D; this is a regular payment schedule with no stubs. DO NOT use it with irregular schedules or you will get incorrect and unexpected behaviour.  ShortFront &#x3D; this is an irregular payment schedule where only the first coupon is irregular, and covers a payment period that is shorter than the regular payment period.  ShortBack &#x3D; this is an irregular payment schedule where only the last coupon is irregular, and covers a payment period that is shorter than the regular payment period.  LongFront &#x3D; this is an irregular payment schedule where only the first coupon is irregular, and covers a payment period that is longer than the regular payment period.  LongBack &#x3D; this is an irregular payment schedule where only the last coupon is irregular, and covers a payment period that is longer than the regular payment period.  Both &#x3D; this is an irregular payment schedule where both the first and the last coupons are irregular, and the length of these periods is calculated based on the first coupon payment date that should have been explicitly set. |
| **ex_dividend_configuration** | [ExDividendConfiguration](ExDividendConfiguration.md) | Optional | *No description available.* |
| **schedule_type** | **str** | Required | The available values are: FixedSchedule, FloatSchedule, OptionalitySchedule, StepSchedule, Exercise, FxRateSchedule, FxLinkedNotionalSchedule, BondConversionSchedule, Invalid |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FixedSchedule import FixedSchedule

instance = FixedSchedule(
    start_date=datetime.now(),  # required — Date from which LUSID starts generating the payment schedule.
    maturity_date=datetime.now(),  # required — Last date of the payment generation schedule. May not necessarily be the maturity date  of the underlying instrument (e.g. in case the instrument has multiple payment schedules).
    flow_conventions=FlowConventions(...),  # optional
    coupon_rate=0.0,  # optional — Coupon rate given as a fraction.
    convention_name=FlowConventionName(...),  # optional
    ex_dividend_days=0,  # optional — Optional. Number of calendar days in the ex-dividend period.  If the settlement date falls in the ex-dividend period then the coupon paid is zero and the accrued interest is negative.  If set, this must be a non-negative number.  If not set, or set to 0, then there is no ex-dividend period.                NOTE: This field is deprecated.  If you wish to set the ExDividendDays on a bond, please use the ExDividendConfiguration.
    notional=0.0,  # optional — Scaling factor, the quantity outstanding on which the rate will be paid.
    payment_currency="...",  # required — Payment currency. This does not have to be the same as the nominal bond or observation/reset currency.
    stub_type="...",  # optional — When a payment schedule doesn&#39;t have regular payment intervals just because of the  first and/or last coupons of the schedule, we call those irregular coupons stubs.  This configuration specifies what type of stub is used when building the schedule  Supported values are:  None &#x3D; this is a regular payment schedule with no stubs. DO NOT use it with irregular schedules or you will get incorrect and unexpected behaviour.  ShortFront &#x3D; this is an irregular payment schedule where only the first coupon is irregular, and covers a payment period that is shorter than the regular payment period.  ShortBack &#x3D; this is an irregular payment schedule where only the last coupon is irregular, and covers a payment period that is shorter than the regular payment period.  LongFront &#x3D; this is an irregular payment schedule where only the first coupon is irregular, and covers a payment period that is longer than the regular payment period.  LongBack &#x3D; this is an irregular payment schedule where only the last coupon is irregular, and covers a payment period that is longer than the regular payment period.  Both &#x3D; this is an irregular payment schedule where both the first and the last coupons are irregular, and the length of these periods is calculated based on the first coupon payment date that should have been explicitly set.
    ex_dividend_configuration=ExDividendConfiguration(...),  # optional
    schedule_type="..."  # required — The available values are: FixedSchedule, FloatSchedule, OptionalitySchedule, StepSchedule, Exercise, FxRateSchedule, FxLinkedNotionalSchedule, BondConversionSchedule, Invalid
)
```

- [FlowConventions](FlowConventions.md)
- [FlowConventionName](FlowConventionName.md)
- [ExDividendConfiguration](ExDividendConfiguration.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

