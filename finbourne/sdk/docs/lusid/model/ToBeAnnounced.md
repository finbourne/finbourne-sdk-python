# ToBeAnnounced

LUSID representation of a TBA (To Be Announced) forward contract for generic agency mortgage-backed securities.  Valued as Quantity x Price via EOD quote lookup; carries no coupon cashflows, accrual or factor.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **start_date** | **datetime** | Required | The trade inception date of the TBA. |
| **maturity_date** | **datetime** | Required | The contractual settlement date of the TBA (e.g. the agency&#39;s announced settlement date for the month). |
| **dom_ccy** | **str** | Required | The domestic currency of the TBA. |
| **agency** | **str** | Optional | The issuing agency of the underlying generic collateral, e.g. \&quot;FNMA\&quot;, \&quot;FHLMC\&quot;, \&quot;GNMA\&quot;.  Note this property does not impact valuation. From a LUSID analytics perspective, it is purely informational. |
| **coupon** | **float** | Optional | The stated coupon rate of the underlying generic collateral, e.g. 3.0, 4.5.  Note this property does not impact valuation - there are no coupon cash flows on the TBA itself.  From a LUSID analytics perspective, it is purely informational. |
| **tenor** | **str** | Optional | The tenor of the underlying generic collateral, e.g. \&quot;30Y\&quot;, \&quot;15Y\&quot;.  Note this property does not impact valuation. From a LUSID analytics perspective, it is purely informational. |
| **time_zone_conventions** | [TimeZoneConventions](TimeZoneConventions.md) | Optional | *No description available.* |
| **trading_conventions** | [TradingConventions](TradingConventions.md) | Optional | *No description available.* |
| **instrument_type** | **str** | Required | Available values: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo, ToBeAnnounced, VolatilitySwap, ToBeAnnouncedOption, CommodityForward, BondOption. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ToBeAnnounced import ToBeAnnounced

instance = ToBeAnnounced(
    start_date=datetime.now(),  # required — The trade inception date of the TBA.
    maturity_date=datetime.now(),  # required — The contractual settlement date of the TBA (e.g. the agency&#39;s announced settlement date for the month).
    dom_ccy="...",  # required — The domestic currency of the TBA.
    agency="...",  # optional — The issuing agency of the underlying generic collateral, e.g. \&quot;FNMA\&quot;, \&quot;FHLMC\&quot;, \&quot;GNMA\&quot;.  Note this property does not impact valuation. From a LUSID analytics perspective, it is purely informational.
    coupon=0.0,  # optional — The stated coupon rate of the underlying generic collateral, e.g. 3.0, 4.5.  Note this property does not impact valuation - there are no coupon cash flows on the TBA itself.  From a LUSID analytics perspective, it is purely informational.
    tenor="...",  # optional — The tenor of the underlying generic collateral, e.g. \&quot;30Y\&quot;, \&quot;15Y\&quot;.  Note this property does not impact valuation. From a LUSID analytics perspective, it is purely informational.
    time_zone_conventions=TimeZoneConventions(...),  # optional
    trading_conventions=TradingConventions(...),  # optional
    instrument_type="..."  # required — Available values: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo, ToBeAnnounced, VolatilitySwap, ToBeAnnouncedOption, CommodityForward, BondOption.
)
```

- [TimeZoneConventions](TimeZoneConventions.md)
- [TradingConventions](TradingConventions.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

