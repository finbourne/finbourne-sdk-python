# EquityOption

LUSID representation of a plain vanilla OTC Equity Option.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **start_date** | **datetime** | Required | The start date of the instrument. This is normally synonymous with the trade-date. |
| **option_maturity_date** | **datetime** | Required | The maturity date of the option. |
| **option_settlement_date** | **datetime** | Optional | The settlement date of the option. |
| **delivery_type** | **str** | Required | Is the option cash settled or physical delivery of option    Supported string (enumeration) values are: [Cash, Physical]. |
| **option_type** | **str** | Required | Type of optionality for the option    Supported string (enumeration) values are: [Call, Put]. |
| **strike** | **float** | Required | The strike of the option. |
| **dom_ccy** | **str** | Required | The domestic currency of the instrument. |
| **underlying_identifier** | **str** | Optional | The market identifier type of the underlying code, e.g RIC.    Supported string (enumeration) values are: [LusidInstrumentId, Isin, Sedol, Cusip, ClientInternal, Figi, RIC, QuotePermId, REDCode, BBGId, ICECode].  Optional field, should be used in combination with the Code field.  Not compatible with the Underlying field. |
| **code** | **str** | Optional | The identifying code for the equity underlying, e.g. &#39;IBM.N&#39;.  Optional field, should be used in combination with the UnderlyingIdentifier field.  Not compatible with the Underlying field. |
| **equity_option_type** | **str** | Optional | Equity option types. E.g. Vanilla (default), RightsIssue, Warrant.    Supported string (enumeration) values are: [Vanilla, RightsIssue, Warrant]. |
| **number_of_shares** | **float** | Optional | The amount of shares to exchange if the option is exercised. |
| **premium** | [Premium](Premium.md) | Optional | *No description available.* |
| **exercise_type** | **str** | Optional | Type of optionality that is present; European, American.    Supported string (enumeration) values are: [European, American].  Defaults to \&quot;European\&quot; if not set. |
| **underlying** | [LusidInstrument](LusidInstrument.md) | Optional | *No description available.* |
| **delivery_days** | **int** | Optional | Number of business days between exercise date and settlement of the option payoff or underlying.  Defaults to 0 if not set. |
| **business_day_convention** | **str** | Optional | Business day convention for option exercise date to settlement date calculation.  Supported string (enumeration) values are: [NoAdjustment, Previous, P, Following, F, ModifiedPrevious, MP, ModifiedFollowing, MF, HalfMonthModifiedFollowing, Nearest].  Defaults to \&quot;F\&quot; if not set. |
| **settlement_calendars** | **List[str]** | Optional | Holiday calendars for option exercise date to settlement date calculation. |
| **time_zone_conventions** | [TimeZoneConventions](TimeZoneConventions.md) | Optional | *No description available.* |
| **trading_conventions** | [TradingConventions](TradingConventions.md) | Optional | *No description available.* |
| **instrument_type** | **str** | Required | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.EquityOption import EquityOption

instance = EquityOption(
    start_date=datetime.now(),  # required — The start date of the instrument. This is normally synonymous with the trade-date.
    option_maturity_date=datetime.now(),  # required — The maturity date of the option.
    option_settlement_date=datetime.now(),  # optional — The settlement date of the option.
    delivery_type="...",  # required — Is the option cash settled or physical delivery of option    Supported string (enumeration) values are: [Cash, Physical].
    option_type="...",  # required — Type of optionality for the option    Supported string (enumeration) values are: [Call, Put].
    strike=0.0,  # required — The strike of the option.
    dom_ccy="...",  # required — The domestic currency of the instrument.
    underlying_identifier="...",  # optional — The market identifier type of the underlying code, e.g RIC.    Supported string (enumeration) values are: [LusidInstrumentId, Isin, Sedol, Cusip, ClientInternal, Figi, RIC, QuotePermId, REDCode, BBGId, ICECode].  Optional field, should be used in combination with the Code field.  Not compatible with the Underlying field.
    code="...",  # optional — The identifying code for the equity underlying, e.g. &#39;IBM.N&#39;.  Optional field, should be used in combination with the UnderlyingIdentifier field.  Not compatible with the Underlying field.
    equity_option_type="...",  # optional — Equity option types. E.g. Vanilla (default), RightsIssue, Warrant.    Supported string (enumeration) values are: [Vanilla, RightsIssue, Warrant].
    number_of_shares=0.0,  # optional — The amount of shares to exchange if the option is exercised.
    premium=Premium(...),  # optional
    exercise_type="...",  # optional — Type of optionality that is present; European, American.    Supported string (enumeration) values are: [European, American].  Defaults to \&quot;European\&quot; if not set.
    underlying=LusidInstrument(...),  # optional
    delivery_days=0,  # optional — Number of business days between exercise date and settlement of the option payoff or underlying.  Defaults to 0 if not set.
    business_day_convention="...",  # optional — Business day convention for option exercise date to settlement date calculation.  Supported string (enumeration) values are: [NoAdjustment, Previous, P, Following, F, ModifiedPrevious, MP, ModifiedFollowing, MF, HalfMonthModifiedFollowing, Nearest].  Defaults to \&quot;F\&quot; if not set.
    settlement_calendars=,  # optional — Holiday calendars for option exercise date to settlement date calculation.
    time_zone_conventions=TimeZoneConventions(...),  # optional
    trading_conventions=TradingConventions(...),  # optional
    instrument_type="..."  # required — The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo
)
```

- [Premium](Premium.md)
- [LusidInstrument](LusidInstrument.md)
- [TimeZoneConventions](TimeZoneConventions.md)
- [TradingConventions](TradingConventions.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

