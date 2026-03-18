# FundValuationSchedule

Specification object for the valuation schedule, how do we determine which days we wish to perform a valuation upon.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **effective_from** | **str** | Optional | If present, the EffectiveFrom and EffectiveAt dates are interpreted as a range of dates for which to perform a valuation.  In this case, valuation is calculated for the portfolio(s) for each business day in the given range. |
| **effective_at** | **str** | Optional | The market data time, i.e. the time to run the valuation request effective of. |
| **diary_entry** | **str** | Optional | The diary entry to use for the valuation schedule. This is used to determine the date on which the valuation should be performed. |
| **variant** | **str** | Optional | The diary entry variant to use, together with the diary entry to be used for the valuation schedule. |
| **tenor** | **str** | Optional | Tenor, e.g \&quot;1D\&quot;, \&quot;1M\&quot; to be used in generating the date schedule when effectiveFrom and effectiveAt are both given and are not the same. |
| **roll_convention** | **str** | Optional | When Tenor is given and is \&quot;1M\&quot; or longer, this specifies the rule which should be used to generate the date schedule.  For example, \&quot;EndOfMonth\&quot; to generate end of month dates, or \&quot;1\&quot; to specify the first day of the applicable month. |
| **holiday_calendars** | **List[str]** | Optional | The holiday calendar(s) that should be used in determining the date schedule.  Holiday calendar(s) are supplied by their names, for example, \&quot;CoppClark\&quot;.  Note that when the calendars are not available (e.g. when the user has insufficient permissions),  a recipe setting will be used to determine whether the whole batch should then fail or whether the calendar not being available should simply be ignored. |
| **valuation_date_times** | **List[str]** | Optional | If given, this is the exact set of dates on which to perform a valuation. This will replace/override all other specified values if given. |
| **business_day_convention** | **str** | Optional | When Tenor is given and is not equal to \&quot;1D\&quot;, there may be cases where \&quot;date + tenor\&quot; land on non-business days around month end.  In that case, the BusinessDayConvention, e.g. modified following \&quot;MF\&quot; would be applied to determine the next GBD. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FundValuationSchedule import FundValuationSchedule

instance = FundValuationSchedule(
    effective_from="...",  # optional — If present, the EffectiveFrom and EffectiveAt dates are interpreted as a range of dates for which to perform a valuation.  In this case, valuation is calculated for the portfolio(s) for each business day in the given range.
    effective_at="...",  # optional — The market data time, i.e. the time to run the valuation request effective of.
    diary_entry="...",  # optional — The diary entry to use for the valuation schedule. This is used to determine the date on which the valuation should be performed.
    variant="...",  # optional — The diary entry variant to use, together with the diary entry to be used for the valuation schedule.
    tenor="...",  # optional — Tenor, e.g \&quot;1D\&quot;, \&quot;1M\&quot; to be used in generating the date schedule when effectiveFrom and effectiveAt are both given and are not the same.
    roll_convention="...",  # optional — When Tenor is given and is \&quot;1M\&quot; or longer, this specifies the rule which should be used to generate the date schedule.  For example, \&quot;EndOfMonth\&quot; to generate end of month dates, or \&quot;1\&quot; to specify the first day of the applicable month.
    holiday_calendars=,  # optional — The holiday calendar(s) that should be used in determining the date schedule.  Holiday calendar(s) are supplied by their names, for example, \&quot;CoppClark\&quot;.  Note that when the calendars are not available (e.g. when the user has insufficient permissions),  a recipe setting will be used to determine whether the whole batch should then fail or whether the calendar not being available should simply be ignored.
    valuation_date_times=,  # optional — If given, this is the exact set of dates on which to perform a valuation. This will replace/override all other specified values if given.
    business_day_convention="..."  # optional — When Tenor is given and is not equal to \&quot;1D\&quot;, there may be cases where \&quot;date + tenor\&quot; land on non-business days around month end.  In that case, the BusinessDayConvention, e.g. modified following \&quot;MF\&quot; would be applied to determine the next GBD.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

