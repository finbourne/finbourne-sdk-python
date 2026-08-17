# BondOption

LUSID representation of an OTC bilateral option (call or put) on a single mastered cash bond  (Bond, ComplexBond or InflationLinkedBond). Quote-driven valuation with an upfront premium;  European exercise only, cash-settled in the current scope (physical settlement is future work).
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **start_date** | **datetime** | Required | The start date of the instrument. This is normally synonymous with the trade-date. |
| **dom_ccy** | **str** | Required | The domestic currency of the instrument. |
| **strike** | **float** | Required | The strike as a clean price, percent of par (real/unindexed for a linker). |
| **contract_size** | **float** | Required | The face amount per contract (e.g. 1,000,000). Together with the per-100 clean-price strike this  turns the strike and payoff into money: strikePerUnit &#x3D; strike / 100 * contractSize. |
| **delivery_type** | **str** | Required | How does the option settle. Only Cash is supported for a BondOption.                Supported string (enumeration) values are: [Cash, Physical]. |
| **exercise_dates** | **List[datetime]** | Required | The exercise dates; exactly one entry, equal to the expiry date (European only in scope). |
| **exercise_type** | **str** | Optional | Type of optionality that is present. Only European is supported for a BondOption.                Supported string (enumeration) values are: [European, Bermudan, American]. |
| **expiry_date** | **datetime** | Required | This is the date when the option expires, i.e. the LAST exercise date of the option.  The property is internal, we may change it in the future (think about Bermuda options). |
| **option_type** | **str** | Required | Type of optionality for the option.                Supported string (enumeration) values are: [Call, Put]. |
| **premium** | [Premium](Premium.md) | Optional | *No description available.* |
| **time_zone_conventions** | [TimeZoneConventions](TimeZoneConventions.md) | Optional | *No description available.* |
| **trading_conventions** | [TradingConventions](TradingConventions.md) | Optional | *No description available.* |
| **underlying** | [LusidInstrument](LusidInstrument.md) | Required | *No description available.* |
| **instrument_type** | **str** | Required | Available values: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo, ToBeAnnounced, VolatilitySwap, ToBeAnnouncedOption, CommodityForward, BondOption, CdsOption, CommodityCalendarSwap. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.BondOption import BondOption

instance = BondOption(
    start_date=datetime.now(),  # required — The start date of the instrument. This is normally synonymous with the trade-date.
    dom_ccy="...",  # required — The domestic currency of the instrument.
    strike=0.0,  # required — The strike as a clean price, percent of par (real/unindexed for a linker).
    contract_size=0.0,  # required — The face amount per contract (e.g. 1,000,000). Together with the per-100 clean-price strike this  turns the strike and payoff into money: strikePerUnit &#x3D; strike / 100 * contractSize.
    delivery_type="...",  # required — How does the option settle. Only Cash is supported for a BondOption.                Supported string (enumeration) values are: [Cash, Physical].
    exercise_dates=,  # required — The exercise dates; exactly one entry, equal to the expiry date (European only in scope).
    exercise_type="...",  # optional — Type of optionality that is present. Only European is supported for a BondOption.                Supported string (enumeration) values are: [European, Bermudan, American].
    expiry_date=datetime.now(),  # required — This is the date when the option expires, i.e. the LAST exercise date of the option.  The property is internal, we may change it in the future (think about Bermuda options).
    option_type="...",  # required — Type of optionality for the option.                Supported string (enumeration) values are: [Call, Put].
    premium=Premium(...),  # optional
    time_zone_conventions=TimeZoneConventions(...),  # optional
    trading_conventions=TradingConventions(...),  # optional
    underlying=LusidInstrument(...),  # required
    instrument_type="..."  # required — Available values: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo, ToBeAnnounced, VolatilitySwap, ToBeAnnouncedOption, CommodityForward, BondOption, CdsOption, CommodityCalendarSwap.
)
```

- [Premium](Premium.md)
- [TimeZoneConventions](TimeZoneConventions.md)
- [TradingConventions](TradingConventions.md)
- [LusidInstrument](LusidInstrument.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

