# TermDeposit

LUSID representation of a Term Deposit.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **start_date** | **datetime** | Required | The start date of the instrument. For term deposits this is the start date of the interest calculation period. |
| **maturity_date** | **datetime** | Required | The maturity date of the instrument. For term deposits this is the last date of the interest calculation period. |
| **contract_size** | **float** | Required | The principal amount of the term deposit. |
| **flow_convention** | [FlowConventions](FlowConventions.md) | Required | *No description available.* |
| **rate** | **float** | Required | The fixed rate for the term deposit. Specified as a decimal, e.g 0.03 is meant to be 3% interest |
| **dom_ccy** | **str** | Optional | The domestic currency of the instrument. This should be the same as the Currency set on the FlowConventions.  You do not need to populate this field for Term Deposits in LUSID as all functionality is driven by the Currency set on the FlowConventions.  LUSID will not store values saved on this field. |
| **trading_conventions** | [TradingConventions](TradingConventions.md) | Optional | *No description available.* |
| **time_zone_conventions** | [TimeZoneConventions](TimeZoneConventions.md) | Optional | *No description available.* |
| **instrument_type** | **str** | Required | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TermDeposit import TermDeposit

instance = TermDeposit(
    start_date=datetime.now(),  # required — The start date of the instrument. For term deposits this is the start date of the interest calculation period.
    maturity_date=datetime.now(),  # required — The maturity date of the instrument. For term deposits this is the last date of the interest calculation period.
    contract_size=0.0,  # required — The principal amount of the term deposit.
    flow_convention=FlowConventions(...),  # required
    rate=0.0,  # required — The fixed rate for the term deposit. Specified as a decimal, e.g 0.03 is meant to be 3% interest
    dom_ccy="...",  # optional — The domestic currency of the instrument. This should be the same as the Currency set on the FlowConventions.  You do not need to populate this field for Term Deposits in LUSID as all functionality is driven by the Currency set on the FlowConventions.  LUSID will not store values saved on this field.
    trading_conventions=TradingConventions(...),  # optional
    time_zone_conventions=TimeZoneConventions(...),  # optional
    instrument_type="..."  # required — The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo
)
```

- [FlowConventions](FlowConventions.md)
- [TradingConventions](TradingConventions.md)
- [TimeZoneConventions](TimeZoneConventions.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

