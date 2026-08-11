# ToBeAnnouncedOption

LUSID representation of an OTC option on a ToBeAnnounced (TBA) forward contract.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **start_date** | **datetime** | Required | The start date of the instrument. This is normally synonymous with the trade-date. |
| **expiry_date** | **datetime** | Required | The date on which the option expires, i.e. the last exercise date of the option. |
| **dom_ccy** | **str** | Required | The domestic currency of the instrument. |
| **option_type** | **str** | Required | Type of optionality for the option.                Supported string (enumeration) values are: [Call, Put]. |
| **strike** | **float** | Required | The strike of the option. |
| **delivery_type** | **str** | Required | Is the option cash settled or physical delivery of the underlying TBA.                Supported string (enumeration) values are: [Cash, Physical]. |
| **underlying** | [MasteredInstrument](MasteredInstrument.md) | Required | *No description available.* |
| **exercise_type** | **str** | Required | Type of optionality that is present; European only in this scope.                Supported string (enumeration) values are: [European]. |
| **premium** | [Premium](Premium.md) | Required | *No description available.* |
| **delivery_days** | **int** | Optional | Number of business days between exercise date and settlement of the option payoff or underlying.  Defaults to 0 if not set. |
| **business_day_convention** | **str** | Optional | Business day convention for option exercise date to settlement date calculation.  Default value: F. Available values: NoAdjustment, None, Previous, P, Following, F, ModifiedPrevious, MP, ModifiedFollowing, MF, HalfMonthModifiedFollowing, Nearest, Invalid. |
| **settlement_calendars** | **List[str]** | Optional | Holiday calendar for option exercise date to settlement date calculation. |
| **time_zone_conventions** | [TimeZoneConventions](TimeZoneConventions.md) | Optional | *No description available.* |
| **trading_conventions** | [TradingConventions](TradingConventions.md) | Optional | *No description available.* |
| **instrument_type** | **str** | Required | Available values: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo, ToBeAnnounced, VolatilitySwap, ToBeAnnouncedOption, CommodityForward. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ToBeAnnouncedOption import ToBeAnnouncedOption

instance = ToBeAnnouncedOption(
    start_date=datetime.now(),  # required — The start date of the instrument. This is normally synonymous with the trade-date.
    expiry_date=datetime.now(),  # required — The date on which the option expires, i.e. the last exercise date of the option.
    dom_ccy="...",  # required — The domestic currency of the instrument.
    option_type="...",  # required — Type of optionality for the option.                Supported string (enumeration) values are: [Call, Put].
    strike=0.0,  # required — The strike of the option.
    delivery_type="...",  # required — Is the option cash settled or physical delivery of the underlying TBA.                Supported string (enumeration) values are: [Cash, Physical].
    underlying=MasteredInstrument(...),  # required
    exercise_type="...",  # required — Type of optionality that is present; European only in this scope.                Supported string (enumeration) values are: [European].
    premium=Premium(...),  # required
    delivery_days=0,  # optional — Number of business days between exercise date and settlement of the option payoff or underlying.  Defaults to 0 if not set.
    business_day_convention="...",  # optional — Business day convention for option exercise date to settlement date calculation.  Default value: F. Available values: NoAdjustment, None, Previous, P, Following, F, ModifiedPrevious, MP, ModifiedFollowing, MF, HalfMonthModifiedFollowing, Nearest, Invalid.
    settlement_calendars=,  # optional — Holiday calendar for option exercise date to settlement date calculation.
    time_zone_conventions=TimeZoneConventions(...),  # optional
    trading_conventions=TradingConventions(...),  # optional
    instrument_type="..."  # required — Available values: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo, ToBeAnnounced, VolatilitySwap, ToBeAnnouncedOption, CommodityForward.
)
```

- [MasteredInstrument](MasteredInstrument.md)
- [Premium](Premium.md)
- [TimeZoneConventions](TimeZoneConventions.md)
- [TradingConventions](TradingConventions.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

