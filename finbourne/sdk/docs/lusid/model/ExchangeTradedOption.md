# ExchangeTradedOption

LUSID representation of an Exchange Traded Option.  Including, but not limited to, Equity Options, Bond Options, Index Options, Future Options, and Interest Rate Options.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **start_date** | **datetime** | Required | The start date of the instrument. This is normally synonymous with the trade-date. |
| **contract_details** | [ExchangeTradedOptionContractDetails](ExchangeTradedOptionContractDetails.md) | Required | *No description available.* |
| **contracts** | **float** | Required | The number of contracts held. |
| **ref_spot_price** | **float** | Optional | The reference price at which the contract was entered into. Optional.  If omitted, the option has no reference price of its own.  Under ConstantTimeValueOfMoney, a holding with a notional cost (for example from Transaction/default/NotionalAmount) is then valued like a future, against its notional cost plus the variation margin settled to date.  A holding without a notional cost is then valued at its full market price.  If 0, the reference is taken from the holding&#39;s cost.  Any other value is used as given.  Writes through Luminesce that do not supply RefSpotPrice store 0. |
| **trading_conventions** | [TradingConventions](TradingConventions.md) | Optional | *No description available.* |
| **time_zone_conventions** | [TimeZoneConventions](TimeZoneConventions.md) | Optional | *No description available.* |
| **instrument_type** | **str** | Required | Available values: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo, ToBeAnnounced, VolatilitySwap, ToBeAnnouncedOption, CommodityForward, BondOption, CdsOption, CommodityCalendarSwap, BondForward, PreferredShare, CapitalInterest, WholeLoanFacility, StripBond. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ExchangeTradedOption import ExchangeTradedOption

instance = ExchangeTradedOption(
    start_date=datetime.now(),  # required — The start date of the instrument. This is normally synonymous with the trade-date.
    contract_details=ExchangeTradedOptionContractDetails(...),  # required
    contracts=0.0,  # required — The number of contracts held.
    ref_spot_price=0.0,  # optional — The reference price at which the contract was entered into. Optional.  If omitted, the option has no reference price of its own.  Under ConstantTimeValueOfMoney, a holding with a notional cost (for example from Transaction/default/NotionalAmount) is then valued like a future, against its notional cost plus the variation margin settled to date.  A holding without a notional cost is then valued at its full market price.  If 0, the reference is taken from the holding&#39;s cost.  Any other value is used as given.  Writes through Luminesce that do not supply RefSpotPrice store 0.
    trading_conventions=TradingConventions(...),  # optional
    time_zone_conventions=TimeZoneConventions(...),  # optional
    instrument_type="..."  # required — Available values: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo, ToBeAnnounced, VolatilitySwap, ToBeAnnouncedOption, CommodityForward, BondOption, CdsOption, CommodityCalendarSwap, BondForward, PreferredShare, CapitalInterest, WholeLoanFacility, StripBond.
)
```

- [ExchangeTradedOptionContractDetails](ExchangeTradedOptionContractDetails.md)
- [TradingConventions](TradingConventions.md)
- [TimeZoneConventions](TimeZoneConventions.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

