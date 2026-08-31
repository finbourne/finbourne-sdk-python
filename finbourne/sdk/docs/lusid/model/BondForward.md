# BondForward

LUSID representation of an OTC bilateral forward contract to buy or sell a specified, already-mastered  debt security (Bond or ComplexBond) at an agreed clean price on a settlement date beyond the market's  standard settlement cycle. No cash moves at trade date, there is no premium, and both parties are  unconditionally obliged. Quote-driven valuation; cash settlement only in the current scope (physical  delivery is future work). Direction is the sign of the holding's units and size is the holding's units,  neither is on the definition, so a partial unwind or novation is an ordinary change in units.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **start_date** | **datetime** | Required | The start date of the instrument. This is normally synonymous with the trade-date. |
| **maturity_date** | **datetime** | Required | The contractual settlement date, on which cash settlement takes place. Named MaturityDate because  IDefinition requires it and every other forward uses it. Supplied as an agreed business day on the  settlement currency&#39;s own calendar; LUSID does not adjust it. |
| **dom_ccy** | **str** | Required | The domestic currency of the instrument. |
| **agreed_clean_price** | **float** | Required | The agreed price, percent of par. Named agreedCleanPrice rather than strike because the contract  carries no optionality, and a percent-of-par price would read as an option strike under that name. |
| **contract_size** | **float** | Required | Face amount of the underlying per unit. Together with the per-100 price this converts price into  money: pricePerUnit &#x3D; agreedCleanPrice / 100 * contractSize. Set 1 to make one unit equal one  currency unit of face. |
| **delivery_type** | **str** | Required | How the forward settles. Only Cash is accepted in the current scope: physical delivery of a bond by  a wrapper instrument has no shipped mechanism for opening the delivered position with purchased  accrued. The field is required rather than defaulted so that a physically-settling contract is  refused explicitly rather than silently cash-settled.                Supported string (enumeration) values are: [Cash, Physical]. Available values: Cash, Physical. |
| **price_basis** | **str** | Required | Whether the agreed price is quoted clean or dirty. Only Clean is accepted: a dirty forward price is  an invoice price for value at settlement, and nothing downstream carries the clean-and-accrued split,  so a Dirty value is rejected at upsert with the conversion instruction. The field is required so that  a dirty price supplied as clean is declared rather than silently mispriced.                Supported string (enumeration) values are: [Clean, Dirty]. Available values: Clean, Dirty. |
| **time_zone_conventions** | [TimeZoneConventions](TimeZoneConventions.md) | Optional | *No description available.* |
| **trading_conventions** | [TradingConventions](TradingConventions.md) | Optional | *No description available.* |
| **underlying** | [LusidInstrument](LusidInstrument.md) | Required | *No description available.* |
| **instrument_type** | **str** | Required | Available values: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo, ToBeAnnounced, VolatilitySwap, ToBeAnnouncedOption, CommodityForward, BondOption, CdsOption, CommodityCalendarSwap, BondForward. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.BondForward import BondForward

instance = BondForward(
    start_date=datetime.now(),  # required — The start date of the instrument. This is normally synonymous with the trade-date.
    maturity_date=datetime.now(),  # required — The contractual settlement date, on which cash settlement takes place. Named MaturityDate because  IDefinition requires it and every other forward uses it. Supplied as an agreed business day on the  settlement currency&#39;s own calendar; LUSID does not adjust it.
    dom_ccy="...",  # required — The domestic currency of the instrument.
    agreed_clean_price=0.0,  # required — The agreed price, percent of par. Named agreedCleanPrice rather than strike because the contract  carries no optionality, and a percent-of-par price would read as an option strike under that name.
    contract_size=0.0,  # required — Face amount of the underlying per unit. Together with the per-100 price this converts price into  money: pricePerUnit &#x3D; agreedCleanPrice / 100 * contractSize. Set 1 to make one unit equal one  currency unit of face.
    delivery_type="...",  # required — How the forward settles. Only Cash is accepted in the current scope: physical delivery of a bond by  a wrapper instrument has no shipped mechanism for opening the delivered position with purchased  accrued. The field is required rather than defaulted so that a physically-settling contract is  refused explicitly rather than silently cash-settled.                Supported string (enumeration) values are: [Cash, Physical]. Available values: Cash, Physical.
    price_basis="...",  # required — Whether the agreed price is quoted clean or dirty. Only Clean is accepted: a dirty forward price is  an invoice price for value at settlement, and nothing downstream carries the clean-and-accrued split,  so a Dirty value is rejected at upsert with the conversion instruction. The field is required so that  a dirty price supplied as clean is declared rather than silently mispriced.                Supported string (enumeration) values are: [Clean, Dirty]. Available values: Clean, Dirty.
    time_zone_conventions=TimeZoneConventions(...),  # optional
    trading_conventions=TradingConventions(...),  # optional
    underlying=LusidInstrument(...),  # required
    instrument_type="..."  # required — Available values: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo, ToBeAnnounced, VolatilitySwap, ToBeAnnouncedOption, CommodityForward, BondOption, CdsOption, CommodityCalendarSwap, BondForward.
)
```

- [TimeZoneConventions](TimeZoneConventions.md)
- [TradingConventions](TradingConventions.md)
- [LusidInstrument](LusidInstrument.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

