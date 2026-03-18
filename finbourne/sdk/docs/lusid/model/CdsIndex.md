# CdsIndex

LUSID representation of a Credit Default Swap Index (CDX).                This instrument has multiple legs, to see how legs are used in LUSID see [knowledge base article KA-02252](https://support.lusid.com/knowledgebase/article/KA-02252).                | Leg Index | Leg Identifier | Description |  | --------- | -------------- | ----------- |  | 1 | ProtectionLeg | Payments made by the protection seller in the case of default across all CDS instruments in the index. |  | 2 | PremiumLeg | The premium payments made by the protection buyer across all CDS instruments in the index. |  | 3 | AdditionalPayments | Cash flows relating to any additional payments (optional). |
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **start_date** | **datetime** | Required | The start date of the instrument. This is normally synonymous with the trade-date. |
| **maturity_date** | **datetime** | Required | The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates that may well be observed or set prior to the maturity date, but refer to a termination date beyond it. |
| **flow_conventions** | [CdsFlowConventions](CdsFlowConventions.md) | Optional | *No description available.* |
| **coupon_rate** | **float** | Required | The coupon rate paid on each payment date of the premium leg as a fraction of 100 percent, e.g. \&quot;0.05\&quot; meaning 500 basis points or 5%.  For a standard corporate CDS (North American) this must be either 100bps or 500bps. |
| **identifiers** | **Dict[str, Optional[str]]** | Required | External market codes and identifiers for the cds index, e.g. a RED code, BBG ID or ICE code. |
| **basket** | [Basket](Basket.md) | Optional | *No description available.* |
| **convention_name** | [FlowConventionName](FlowConventionName.md) | Optional | *No description available.* |
| **notional** | **float** | Required | The notional quantity that applies to both the premium and protection legs. |
| **additional_payments** | [List[AdditionalPayment]](AdditionalPayment.md) | Optional | Optional additional payments at a given date e.g. to level off an uneven swap.  The dates must be distinct and either all payments are Pay or all payments are Receive. |
| **time_zone_conventions** | [TimeZoneConventions](TimeZoneConventions.md) | Optional | *No description available.* |
| **instrument_type** | **str** | Required | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CdsIndex import CdsIndex

instance = CdsIndex(
    start_date=datetime.now(),  # required — The start date of the instrument. This is normally synonymous with the trade-date.
    maturity_date=datetime.now(),  # required — The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates that may well be observed or set prior to the maturity date, but refer to a termination date beyond it.
    flow_conventions=CdsFlowConventions(...),  # optional
    coupon_rate=0.0,  # required — The coupon rate paid on each payment date of the premium leg as a fraction of 100 percent, e.g. \&quot;0.05\&quot; meaning 500 basis points or 5%.  For a standard corporate CDS (North American) this must be either 100bps or 500bps.
    identifiers=,  # required — External market codes and identifiers for the cds index, e.g. a RED code, BBG ID or ICE code.
    basket=Basket(...),  # optional
    convention_name=FlowConventionName(...),  # optional
    notional=0.0,  # required — The notional quantity that applies to both the premium and protection legs.
    additional_payments=[],  # optional — Optional additional payments at a given date e.g. to level off an uneven swap.  The dates must be distinct and either all payments are Pay or all payments are Receive.
    time_zone_conventions=TimeZoneConventions(...),  # optional
    instrument_type="..."  # required — The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo
)
```

- [CdsFlowConventions](CdsFlowConventions.md)
- [Basket](Basket.md)
- [FlowConventionName](FlowConventionName.md)
- [AdditionalPayment](AdditionalPayment.md) — used in `additional_payments`
- [TimeZoneConventions](TimeZoneConventions.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

