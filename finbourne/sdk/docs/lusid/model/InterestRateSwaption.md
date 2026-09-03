# InterestRateSwaption

LUSID representation of an Interest Rate Swaption.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **start_date** | **datetime** | Required | The start date of the instrument. This is normally synonymous with the trade-date. |
| **pay_or_receive_fixed** | **str** | Required | Pay or Receive the fixed leg of the underlying swap.    Supported string (enumeration) values are: [Pay, Receive]. |
| **premium** | [Premium](Premium.md) | Optional | *No description available.* |
| **delivery_method** | **str** | Required | How does the option settle    Supported string (enumeration) values are: [Cash, Physical]. |
| **swap** | [InterestRateSwap](InterestRateSwap.md) | Optional | *No description available.* |
| **time_zone_conventions** | [TimeZoneConventions](TimeZoneConventions.md) | Optional | *No description available.* |
| **underlying** | [LusidInstrument](LusidInstrument.md) | Optional | *No description available.* |
| **delivery_days** | **int** | Optional | Number of business days between exercise date and settlement of the option payoff or underlying.                Defaults to 0. |
| **business_day_convention** | **str** | Optional | Business day convention for option exercise date to settlement date calculation.  Default value: F. Available values: NoAdjustment, None, Previous, P, Following, F, ModifiedPrevious, MP, ModifiedFollowing, MF, HalfMonthModifiedFollowing, Nearest, Invalid. |
| **settlement_calendars** | **List[str]** | Optional | Holiday calendars for option exercise date to settlement date calculation. |
| **dom_ccy** | **str** | Optional | The currency the option settles in.                Optional, and in almost all cases it should be left to default. If not specified, the currency of  the underlying swap is used, which for a cross-currency swap is the currency of its first leg.                A specified currency is taken as given and is not validated against the underlying swap, since  settling in another currency is rare but legitimate. Note that valuation of such a swaption is not  supported, as converting from the currency the swap is valued in needs an fx rate the instrument  does not define. |
| **exercise_date** | **datetime** | Optional | The date the option expires, and for European exercise the date it is exercised. For American  exercise it is the end of the window the option may be exercised in, so it should be set on the  instrument for the option to be exercisable up to the intended date.                If not specified, the start date of the underlying swap is used. |
| **exercise_type** | **str** | Optional | Type of optionality that is present; European, American.                Supported string (enumeration) values are: [European, American].  Defaults to \&quot;European\&quot; if not set.                A European option is exercised on its exercise date, so its exercise event is generated with  that date already set. An American option may be exercised at any point up to that date, so the  date it is actually exercised on is supplied on the exercise event; set exerciseDate on the  instrument to open the window the event may fall in.                The swap delivered on exercise keeps the start date it was defined with, so exercising early  or late leaves it aged or forward-starting relative to the exercise. Keeping that swap  correct for the intended exercise is the responsibility of whoever defines it. In particular,  for an American physically settled swaption on a cross-currency underlying, neither the swap&#39;s  start date nor its fx notionals are determined at trade time, so amending the delivered swap  position after exercise is an operational step the client must carry out. |
| **strike** | **float** | Optional | The rate the option strikes against.                May only be specified when the underlying swap has no single fixed leg, as otherwise that leg&#39;s  fixed rate is the strike. It must be specified when the underlying swap has two fixed legs, as  there is then no single rate to strike against. |
| **trading_conventions** | [TradingConventions](TradingConventions.md) | Optional | *No description available.* |
| **instrument_type** | **str** | Required | Available values: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo, ToBeAnnounced, VolatilitySwap, ToBeAnnouncedOption, CommodityForward, BondOption, CdsOption, CommodityCalendarSwap, BondForward, PreferredShare. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.InterestRateSwaption import InterestRateSwaption

instance = InterestRateSwaption(
    start_date=datetime.now(),  # required — The start date of the instrument. This is normally synonymous with the trade-date.
    pay_or_receive_fixed="...",  # required — Pay or Receive the fixed leg of the underlying swap.    Supported string (enumeration) values are: [Pay, Receive].
    premium=Premium(...),  # optional
    delivery_method="...",  # required — How does the option settle    Supported string (enumeration) values are: [Cash, Physical].
    swap=InterestRateSwap(...),  # optional
    time_zone_conventions=TimeZoneConventions(...),  # optional
    underlying=LusidInstrument(...),  # optional
    delivery_days=0,  # optional — Number of business days between exercise date and settlement of the option payoff or underlying.                Defaults to 0.
    business_day_convention="...",  # optional — Business day convention for option exercise date to settlement date calculation.  Default value: F. Available values: NoAdjustment, None, Previous, P, Following, F, ModifiedPrevious, MP, ModifiedFollowing, MF, HalfMonthModifiedFollowing, Nearest, Invalid.
    settlement_calendars=,  # optional — Holiday calendars for option exercise date to settlement date calculation.
    dom_ccy="...",  # optional — The currency the option settles in.                Optional, and in almost all cases it should be left to default. If not specified, the currency of  the underlying swap is used, which for a cross-currency swap is the currency of its first leg.                A specified currency is taken as given and is not validated against the underlying swap, since  settling in another currency is rare but legitimate. Note that valuation of such a swaption is not  supported, as converting from the currency the swap is valued in needs an fx rate the instrument  does not define.
    exercise_date=datetime.now(),  # optional — The date the option expires, and for European exercise the date it is exercised. For American  exercise it is the end of the window the option may be exercised in, so it should be set on the  instrument for the option to be exercisable up to the intended date.                If not specified, the start date of the underlying swap is used.
    exercise_type="...",  # optional — Type of optionality that is present; European, American.                Supported string (enumeration) values are: [European, American].  Defaults to \&quot;European\&quot; if not set.                A European option is exercised on its exercise date, so its exercise event is generated with  that date already set. An American option may be exercised at any point up to that date, so the  date it is actually exercised on is supplied on the exercise event; set exerciseDate on the  instrument to open the window the event may fall in.                The swap delivered on exercise keeps the start date it was defined with, so exercising early  or late leaves it aged or forward-starting relative to the exercise. Keeping that swap  correct for the intended exercise is the responsibility of whoever defines it. In particular,  for an American physically settled swaption on a cross-currency underlying, neither the swap&#39;s  start date nor its fx notionals are determined at trade time, so amending the delivered swap  position after exercise is an operational step the client must carry out.
    strike=0.0,  # optional — The rate the option strikes against.                May only be specified when the underlying swap has no single fixed leg, as otherwise that leg&#39;s  fixed rate is the strike. It must be specified when the underlying swap has two fixed legs, as  there is then no single rate to strike against.
    trading_conventions=TradingConventions(...),  # optional
    instrument_type="..."  # required — Available values: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo, ToBeAnnounced, VolatilitySwap, ToBeAnnouncedOption, CommodityForward, BondOption, CdsOption, CommodityCalendarSwap, BondForward, PreferredShare.
)
```

- [Premium](Premium.md)
- [InterestRateSwap](InterestRateSwap.md)
- [TimeZoneConventions](TimeZoneConventions.md)
- [LusidInstrument](LusidInstrument.md)
- [TradingConventions](TradingConventions.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

