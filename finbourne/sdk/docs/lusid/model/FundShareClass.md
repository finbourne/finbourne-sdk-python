# FundShareClass

LUSID representation of a FundShareClass.  A ShareClass represents a pool of shares, held by investors, within a fund.   A ShareClass can represent a differing investment approach by either Fees,   Income, Currency Risk and Investor type.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **short_code** | **str** | Required | A short identifier, unique across a single fund, usually made up of the ShareClass components. Eg \&quot;A Accumulation Euro Hedged Class\&quot; could become \&quot;A Acc H EUR\&quot;. |
| **fund_share_class_type** | **str** | Optional | The type of distribution that the ShareClass will calculate. Can be either &#39;Income&#39; or &#39;Accumulation&#39; - Income classes will pay out and Accumulation classes will retain their ShareClass attributable income. Available values: Income, Accumulation. |
| **distribution_payment_type** | **str** | Optional | The tax treatment applied to any distributions calculated within the ShareClass. Can be either &#39;Net&#39; (Distribution Calculated net of tax) or &#39;Gross&#39; (Distribution calculated gross of tax). Available values: Invalid, Gross, Net. |
| **distribution_type** | **str** | Optional | The type of distribution calculated for the ShareClass. Can be either &#39;Income&#39; or &#39;Accumulation&#39;. Available values: Income, Accumulation. |
| **hedging** | **str** | Optional | A flag to indicate the ShareClass is operating currency hedging as a means to limit currency risk as part of its investment strategy. Available values: Invalid, None, ApplyHedging. |
| **dom_ccy** | **str** | Required | The domestic currency of the instrument. |
| **rounding_conventions** | [List[SimpleRoundingConvention]](SimpleRoundingConvention.md) | Optional | Rounding Convention used for the FundShareClass quotes |
| **rounding_convention_units** | [List[SimpleRoundingConvention]](SimpleRoundingConvention.md) | Optional | Rounding Conventions used for the FundShareClass units |
| **trading_conventions** | [TradingConventions](TradingConventions.md) | Optional | *No description available.* |
| **time_zone_conventions** | [TimeZoneConventions](TimeZoneConventions.md) | Optional | *No description available.* |
| **instrument_type** | **str** | Required | Available values: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo, ToBeAnnounced, VolatilitySwap, ToBeAnnouncedOption, CommodityForward, BondOption, CdsOption, CommodityCalendarSwap, BondForward, PreferredShare. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FundShareClass import FundShareClass

instance = FundShareClass(
    short_code="...",  # required — A short identifier, unique across a single fund, usually made up of the ShareClass components. Eg \&quot;A Accumulation Euro Hedged Class\&quot; could become \&quot;A Acc H EUR\&quot;.
    fund_share_class_type="...",  # optional — The type of distribution that the ShareClass will calculate. Can be either &#39;Income&#39; or &#39;Accumulation&#39; - Income classes will pay out and Accumulation classes will retain their ShareClass attributable income. Available values: Income, Accumulation.
    distribution_payment_type="...",  # optional — The tax treatment applied to any distributions calculated within the ShareClass. Can be either &#39;Net&#39; (Distribution Calculated net of tax) or &#39;Gross&#39; (Distribution calculated gross of tax). Available values: Invalid, Gross, Net.
    distribution_type="...",  # optional — The type of distribution calculated for the ShareClass. Can be either &#39;Income&#39; or &#39;Accumulation&#39;. Available values: Income, Accumulation.
    hedging="...",  # optional — A flag to indicate the ShareClass is operating currency hedging as a means to limit currency risk as part of its investment strategy. Available values: Invalid, None, ApplyHedging.
    dom_ccy="...",  # required — The domestic currency of the instrument.
    rounding_conventions=[],  # optional — Rounding Convention used for the FundShareClass quotes
    rounding_convention_units=[],  # optional — Rounding Conventions used for the FundShareClass units
    trading_conventions=TradingConventions(...),  # optional
    time_zone_conventions=TimeZoneConventions(...),  # optional
    instrument_type="..."  # required — Available values: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo, ToBeAnnounced, VolatilitySwap, ToBeAnnouncedOption, CommodityForward, BondOption, CdsOption, CommodityCalendarSwap, BondForward, PreferredShare.
)
```

- [SimpleRoundingConvention](SimpleRoundingConvention.md) — used in `rounding_conventions`
- [SimpleRoundingConvention](SimpleRoundingConvention.md) — used in `rounding_convention_units`
- [TradingConventions](TradingConventions.md)
- [TimeZoneConventions](TimeZoneConventions.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

