# Bond

LUSID representation of a Vanilla Fixed Rate Bond.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **start_date** | **datetime** | Required | The Start date of the bond, this is normally when accrual of the first coupon begins. |
| **maturity_date** | **datetime** | Required | The Maturity date of the bond, this is when the last coupon accrual period ends.  Note that while most bonds have their last payment on this date there are some cases where the final payment is the next working day. |
| **dom_ccy** | **str** | Required | The domestic currency of the instrument. This should be the same as the Currency set on the FlowConventions. |
| **flow_conventions** | [FlowConventions](FlowConventions.md) | Required | *No description available.* |
| **principal** | **float** | Required | The face-value or principal for the bond at outset.  This might be reduced through its lifetime in the event of amortisation or similar. |
| **coupon_rate** | **float** | Required | Simple coupon rate. |
| **identifiers** | **Dict[str, Optional[str]]** | Optional | External market codes and identifiers for the bond, e.g. ISIN. |
| **ex_dividend_days** | **int** | Optional | Optional. Number of calendar days in the ex-dividend period.  If the settlement date falls in the ex-dividend period then the coupon paid is zero and the accrued interest is negative.  If set, this must be a non-negative number.  If not set, or set to 0, then there is no ex-dividend period.                NOTE: This field is deprecated.  If you wish to set the ExDividendDays on a bond, please use the ExDividendConfiguration. |
| **initial_coupon_date** | **datetime** | Optional | Optional and to be DEPRECATED. If set, this is the date at which the bond begins to accrue interest. Instead, this information should be entered in the field StartDate. |
| **first_coupon_pay_date** | **datetime** | Optional | The date that the first coupon of the bond is paid. This is required for bonds that have a long first coupon or short first coupon. The first coupon pay date is used  as an anchor to compare with the start date and determine if this is a long/short coupon period. |
| **calculation_type** | **str** | Optional | The calculation type applied to the bond coupon amount. This is required for bonds that have a particular type of computing the period coupon, such as simple compounding,  irregular coupons etc.  The default CalculationType is &#x60;Standard&#x60;, which returns a coupon amount equal to Principal * Coupon Rate / Coupon Frequency. Coupon Frequency is 12M / Payment Frequency.  Payment Frequency can be 1M, 3M, 6M, 12M etc. So Coupon Frequency can be 12, 4, 2, 1 respectively.    Supported string (enumeration) values are: [Standard, DayCountCoupon, NoCalculationFloater, BrazilFixedCoupon, StandardWithCappedAccruedInterest]. |
| **rounding_conventions** | [List[RoundingConvention]](RoundingConvention.md) | Optional | Rounding conventions for analytics, if any. |
| **ex_dividend_configuration** | [ExDividendConfiguration](ExDividendConfiguration.md) | Optional | *No description available.* |
| **original_issue_price** | **float** | Optional | The price the bond was issued at. This is to be entered as a percentage of par, for example a value of 98.5 would represent 98.5%. |
| **trading_conventions** | [TradingConventions](TradingConventions.md) | Optional | *No description available.* |
| **time_zone_conventions** | [TimeZoneConventions](TimeZoneConventions.md) | Optional | *No description available.* |
| **instrument_type** | **str** | Required | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.Bond import Bond

instance = Bond(
    start_date=datetime.now(),  # required — The Start date of the bond, this is normally when accrual of the first coupon begins.
    maturity_date=datetime.now(),  # required — The Maturity date of the bond, this is when the last coupon accrual period ends.  Note that while most bonds have their last payment on this date there are some cases where the final payment is the next working day.
    dom_ccy="...",  # required — The domestic currency of the instrument. This should be the same as the Currency set on the FlowConventions.
    flow_conventions=FlowConventions(...),  # required
    principal=0.0,  # required — The face-value or principal for the bond at outset.  This might be reduced through its lifetime in the event of amortisation or similar.
    coupon_rate=0.0,  # required — Simple coupon rate.
    identifiers=,  # optional — External market codes and identifiers for the bond, e.g. ISIN.
    ex_dividend_days=0,  # optional — Optional. Number of calendar days in the ex-dividend period.  If the settlement date falls in the ex-dividend period then the coupon paid is zero and the accrued interest is negative.  If set, this must be a non-negative number.  If not set, or set to 0, then there is no ex-dividend period.                NOTE: This field is deprecated.  If you wish to set the ExDividendDays on a bond, please use the ExDividendConfiguration.
    initial_coupon_date=datetime.now(),  # optional — Optional and to be DEPRECATED. If set, this is the date at which the bond begins to accrue interest. Instead, this information should be entered in the field StartDate.
    first_coupon_pay_date=datetime.now(),  # optional — The date that the first coupon of the bond is paid. This is required for bonds that have a long first coupon or short first coupon. The first coupon pay date is used  as an anchor to compare with the start date and determine if this is a long/short coupon period.
    calculation_type="...",  # optional — The calculation type applied to the bond coupon amount. This is required for bonds that have a particular type of computing the period coupon, such as simple compounding,  irregular coupons etc.  The default CalculationType is &#x60;Standard&#x60;, which returns a coupon amount equal to Principal * Coupon Rate / Coupon Frequency. Coupon Frequency is 12M / Payment Frequency.  Payment Frequency can be 1M, 3M, 6M, 12M etc. So Coupon Frequency can be 12, 4, 2, 1 respectively.    Supported string (enumeration) values are: [Standard, DayCountCoupon, NoCalculationFloater, BrazilFixedCoupon, StandardWithCappedAccruedInterest].
    rounding_conventions=[],  # optional — Rounding conventions for analytics, if any.
    ex_dividend_configuration=ExDividendConfiguration(...),  # optional
    original_issue_price=0.0,  # optional — The price the bond was issued at. This is to be entered as a percentage of par, for example a value of 98.5 would represent 98.5%.
    trading_conventions=TradingConventions(...),  # optional
    time_zone_conventions=TimeZoneConventions(...),  # optional
    instrument_type="..."  # required — The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo
)
```

- [FlowConventions](FlowConventions.md)
- [RoundingConvention](RoundingConvention.md) — used in `rounding_conventions`
- [ExDividendConfiguration](ExDividendConfiguration.md)
- [TradingConventions](TradingConventions.md)
- [TimeZoneConventions](TimeZoneConventions.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

