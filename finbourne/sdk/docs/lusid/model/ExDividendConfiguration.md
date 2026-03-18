# ExDividendConfiguration

Configure the ex-dividend periods for the instrument.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **use_business_days** | **bool** | Optional | Is the ex-dividend period counted in business days or calendar days.  Defaults to false if not set. |
| **ex_dividend_days** | **int** | Required | Number of days in the ex-dividend period.  If the settlement date falls in the ex-dividend period then the coupon paid is zero and the accrued interest is negative.  If set, this must be a non-negative number.  If not set, or set to 0, than there is no ex-dividend period. |
| **return_negative_accrued** | **bool** | Optional | Does the accrued interest go negative in the ex-dividend period, or does it go to zero.  Defaults to true if not set. |
| **apply_thirty360_pay_delay** | **bool** | Optional | Set this flag to true if the ex-dividend days represent a pay delay from the accrual end date in calendar  days under the 30/360 day count convention. The typical use case for this flag are Mortgage Backed Securities  with pay delay between 1 and 60 days, such as FreddieMac and FannieMae. If this flag is set, the useBusinessDays  setting will be ignored.  Defaults to false if not provided. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ExDividendConfiguration import ExDividendConfiguration

instance = ExDividendConfiguration(
    use_business_days=True,  # optional — Is the ex-dividend period counted in business days or calendar days.  Defaults to false if not set.
    ex_dividend_days=0,  # required — Number of days in the ex-dividend period.  If the settlement date falls in the ex-dividend period then the coupon paid is zero and the accrued interest is negative.  If set, this must be a non-negative number.  If not set, or set to 0, than there is no ex-dividend period.
    return_negative_accrued=True,  # optional — Does the accrued interest go negative in the ex-dividend period, or does it go to zero.  Defaults to true if not set.
    apply_thirty360_pay_delay=True  # optional — Set this flag to true if the ex-dividend days represent a pay delay from the accrual end date in calendar  days under the 30/360 day count convention. The typical use case for this flag are Mortgage Backed Securities  with pay delay between 1 and 60 days, such as FreddieMac and FannieMae. If this flag is set, the useBusinessDays  setting will be ignored.  Defaults to false if not provided.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

