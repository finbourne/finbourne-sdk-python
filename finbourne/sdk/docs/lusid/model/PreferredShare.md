# PreferredShare

LUSID representation of a preferred (preference) share: an equity-classified security that pays an  intrinsic, schedule-driven dividend of DividendRate x ParValue. The schedule is perpetual unless a  MaturityDate is supplied, in which case the share redeems at par on that date.  It carries Bond's shape rather than Equity's - StartDate, MaturityDate and FlowConventions are real,  settable properties - but its dividend is a flat amount per period rather than a day-count-weighted  coupon, and its schedule can be open ended.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **start_date** | **datetime** | Required | The start date of the instrument. This is the first dividend accrual start date. |
| **maturity_date** | **datetime** | Optional | The redemption date of a dated series. Omit it for a perpetual, which is the default: there is  no sentinel date for the client to supply, and a distant date such as one in the year 9999 is  taken literally and schedules a par redemption on it. |
| **flow_conventions** | [FlowConventions](FlowConventions.md) | Required | *No description available.* |
| **identifiers** | [PreferredShareAllOfIdentifiers](PreferredShareAllOfIdentifiers.md) | Optional | *No description available.* |
| **dom_ccy** | **str** | Required | The domestic currency of the instrument. It is the currency of the dividends and of ParValue. |
| **call_schedule** | [OptionalitySchedule](OptionalitySchedule.md) | Optional | *No description available.* |
| **cfi_code** | **str** | Optional | The ISO 10962 CFI code, if the client stores one. Free text, not validated against the standard. |
| **conversion_schedule** | [BondConversionSchedule](BondConversionSchedule.md) | Optional | *No description available.* |
| **dividend_rate** | **float** | Required | The fixed annualised dividend rate applied to ParValue, so 0.06 is 6%. A scalar for the life of  the share: there is no rate reset, so a fixed-to-floating preferred carries the rate for the  current period and is re-upserted at each reset. |
| **first_dividend_date** | **datetime** | Optional | Anchors a short or long first dividend period. Omitted means no stub. |
| **is_cumulative** | **bool** | Required | Whether a missed dividend accumulates as arrears rather than being forfeited. The client must  state it; there is no default. |
| **lot_size** | **int** | Optional | The minimum number of shares that can be traded at once. Microstructure only: it has no effect  on valuation or on cash flows. Defaults to 1. |
| **par_value** | **float** | Required | The liquidation preference per share. It is the base for the dividend, for the call strike and  for the redemption amount. It is not a price multiplier. |
| **instrument_type** | **str** | Required | Available values: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo, ToBeAnnounced, VolatilitySwap, ToBeAnnouncedOption, CommodityForward, BondOption, CdsOption, CommodityCalendarSwap, BondForward, PreferredShare. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PreferredShare import PreferredShare

instance = PreferredShare(
    start_date=datetime.now(),  # required — The start date of the instrument. This is the first dividend accrual start date.
    maturity_date=datetime.now(),  # optional — The redemption date of a dated series. Omit it for a perpetual, which is the default: there is  no sentinel date for the client to supply, and a distant date such as one in the year 9999 is  taken literally and schedules a par redemption on it.
    flow_conventions=FlowConventions(...),  # required
    identifiers=PreferredShareAllOfIdentifiers(...),  # optional
    dom_ccy="...",  # required — The domestic currency of the instrument. It is the currency of the dividends and of ParValue.
    call_schedule=OptionalitySchedule(...),  # optional
    cfi_code="...",  # optional — The ISO 10962 CFI code, if the client stores one. Free text, not validated against the standard.
    conversion_schedule=BondConversionSchedule(...),  # optional
    dividend_rate=0.0,  # required — The fixed annualised dividend rate applied to ParValue, so 0.06 is 6%. A scalar for the life of  the share: there is no rate reset, so a fixed-to-floating preferred carries the rate for the  current period and is re-upserted at each reset.
    first_dividend_date=datetime.now(),  # optional — Anchors a short or long first dividend period. Omitted means no stub.
    is_cumulative=True,  # required — Whether a missed dividend accumulates as arrears rather than being forfeited. The client must  state it; there is no default.
    lot_size=0,  # optional — The minimum number of shares that can be traded at once. Microstructure only: it has no effect  on valuation or on cash flows. Defaults to 1.
    par_value=0.0,  # required — The liquidation preference per share. It is the base for the dividend, for the call strike and  for the redemption amount. It is not a price multiplier.
    instrument_type="..."  # required — Available values: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo, ToBeAnnounced, VolatilitySwap, ToBeAnnouncedOption, CommodityForward, BondOption, CdsOption, CommodityCalendarSwap, BondForward, PreferredShare.
)
```

- [FlowConventions](FlowConventions.md)
- [PreferredShareAllOfIdentifiers](PreferredShareAllOfIdentifiers.md)
- [OptionalitySchedule](OptionalitySchedule.md)
- [BondConversionSchedule](BondConversionSchedule.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

