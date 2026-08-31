# CommodityCalendarSwap

LUSID representation of an OTC bilateral commodity calendar swap.  The swap is a strip of periodic commodity forwards struck at a single strike, cash-settled at each  period end against a calendar-average commodity price, with the position amortising as each period  settles. Its present value is Quantity x Price, where the price is supplied externally pre-netted  (the calendar average minus strike) via the quote store. LUSID calculates no analytics for this  instrument, and it can only be priced by lookup pricing. The periodic settlement schedule is  currently stored and validated only; only the maturity lifecycle event is generated.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **dom_ccy** | **str** | Required | The domestic currency of the instrument. |
| **strike** | **float** | Optional | Agreed price per unit at trade inception. Reference only - not used in the market value  calculation, which consumes the pre-netted price from the quote store. |
| **commodity_calendar_schedule** | [CommodityCalendarSchedule](CommodityCalendarSchedule.md) | Required | *No description available.* |
| **delivery_type** | **str** | Required | Whether the swap settles in cash or through physical delivery of the underlying.  Only cash settlement is supported.                Supported string (enumeration) values are: [Cash, Physical]. Available values: Cash, Physical. |
| **quantity_per_period** | **float** | Required | The notional commodity quantity referenced by each settlement period. The initial holding is  this quantity multiplied by the number of periods, stepping down by this quantity as each  period settles. |
| **underlying** | [LusidInstrument](LusidInstrument.md) | Optional | *No description available.* |
| **instrument_type** | **str** | Required | Available values: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo, ToBeAnnounced, VolatilitySwap, ToBeAnnouncedOption, CommodityForward, BondOption, CdsOption, CommodityCalendarSwap, BondForward. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CommodityCalendarSwap import CommodityCalendarSwap

instance = CommodityCalendarSwap(
    dom_ccy="...",  # required — The domestic currency of the instrument.
    strike=0.0,  # optional — Agreed price per unit at trade inception. Reference only - not used in the market value  calculation, which consumes the pre-netted price from the quote store.
    commodity_calendar_schedule=CommodityCalendarSchedule(...),  # required
    delivery_type="...",  # required — Whether the swap settles in cash or through physical delivery of the underlying.  Only cash settlement is supported.                Supported string (enumeration) values are: [Cash, Physical]. Available values: Cash, Physical.
    quantity_per_period=0.0,  # required — The notional commodity quantity referenced by each settlement period. The initial holding is  this quantity multiplied by the number of periods, stepping down by this quantity as each  period settles.
    underlying=LusidInstrument(...),  # optional
    instrument_type="..."  # required — Available values: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo, ToBeAnnounced, VolatilitySwap, ToBeAnnouncedOption, CommodityForward, BondOption, CdsOption, CommodityCalendarSwap, BondForward.
)
```

- [CommodityCalendarSchedule](CommodityCalendarSchedule.md)
- [LusidInstrument](LusidInstrument.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

