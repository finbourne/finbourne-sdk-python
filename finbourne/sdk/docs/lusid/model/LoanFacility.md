# LoanFacility

Loan Facility. This is a very lightweight instrument which acts as a placeholder for the state that is built  from the instrument events. The facility acts as an agreement between a single borrower and many lenders (investors).  Several contracts may be drawn up to enable the lending of funds to the borrower. These contracts are modelled via  FlexibleLoan instruments in LUSID. The instrument events on the facility may relate to the facility as a whole  (for example to define a global commitment amount), or they may relate to a single contract (such as a paydown  transaction on a particular contract).
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **start_date** | **datetime** | Required | The start date of the instrument. This is normally synonymous with the trade-date. |
| **maturity_date** | **datetime** | Required | The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates that may well be observed or set prior to the maturity date, but refer to a termination date beyond it. |
| **dom_ccy** | **str** | Required | The domestic currency of the instrument. |
| **initial_commitment** | **float** | Required | The initial commitment for the loan facility. |
| **loan_type** | **str** | Required | LoanType for this facility. The facility can either be a revolving or a  term loan.    Supported string (enumeration) values are: [Revolver, TermLoan]. |
| **schedules** | [List[Schedule]](Schedule.md) | Required | Repayment schedules for the loan. |
| **time_zone_conventions** | [TimeZoneConventions](TimeZoneConventions.md) | Optional | *No description available.* |
| **instrument_type** | **str** | Required | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.LoanFacility import LoanFacility

instance = LoanFacility(
    start_date=datetime.now(),  # required — The start date of the instrument. This is normally synonymous with the trade-date.
    maturity_date=datetime.now(),  # required — The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates that may well be observed or set prior to the maturity date, but refer to a termination date beyond it.
    dom_ccy="...",  # required — The domestic currency of the instrument.
    initial_commitment=0.0,  # required — The initial commitment for the loan facility.
    loan_type="...",  # required — LoanType for this facility. The facility can either be a revolving or a  term loan.    Supported string (enumeration) values are: [Revolver, TermLoan].
    schedules=[],  # required — Repayment schedules for the loan.
    time_zone_conventions=TimeZoneConventions(...),  # optional
    instrument_type="..."  # required — The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo
)
```

- [Schedule](Schedule.md) — used in `schedules`
- [TimeZoneConventions](TimeZoneConventions.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

