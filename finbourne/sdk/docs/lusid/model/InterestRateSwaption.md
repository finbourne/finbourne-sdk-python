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
| **business_day_convention** | **str** | Optional | Business day convention for option exercise date to settlement date calculation.  Supported string (enumeration) values are: [NoAdjustment, Previous, P, Following, F, ModifiedPrevious, MP, ModifiedFollowing, MF, HalfMonthModifiedFollowing, Nearest].                Defaults to \&quot;F\&quot;. |
| **settlement_calendars** | **List[str]** | Optional | Holiday calendars for option exercise date to settlement date calculation. |
| **instrument_type** | **str** | Required | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo |


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
    business_day_convention="...",  # optional — Business day convention for option exercise date to settlement date calculation.  Supported string (enumeration) values are: [NoAdjustment, Previous, P, Following, F, ModifiedPrevious, MP, ModifiedFollowing, MF, HalfMonthModifiedFollowing, Nearest].                Defaults to \&quot;F\&quot;.
    settlement_calendars=,  # optional — Holiday calendars for option exercise date to settlement date calculation.
    instrument_type="..."  # required — The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo
)
```

- [Premium](Premium.md)
- [InterestRateSwap](InterestRateSwap.md)
- [TimeZoneConventions](TimeZoneConventions.md)
- [LusidInstrument](LusidInstrument.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

