# MasteredInstrument

LUSID representation of a reference to another instrument that has already been upserted (Mastered)
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **identifiers** | **Dict[str, Optional[str]]** | Required | Dictionary of identifiers of the mastered instrument |
| **mastered_dom_ccy** | **str** | Optional | DomCcy of the Instrument that Mastered Instrument points to - read only field *(read-only)* |
| **mastered_instrument_type** | **str** | Optional | Type of the Instrument that Mastered Instrument points to - read only field *(read-only)* |
| **mastered_lusid_instrument_id** | **str** | Optional | Luid of the Instrument that Mastered Instrument points to - read only field *(read-only)* |
| **mastered_name** | **str** | Optional | Name of the Instrument that Mastered Instrument points to - read only field *(read-only)* |
| **mastered_scope** | **str** | Optional | Scope of the Instrument that Mastered Instrument points to - read only field *(read-only)* |
| **mastered_asset_class** | **str** | Optional | Asset class of the underlying mastered instrument - read only field    Supported string (enumeration) values are: [InterestRates, FX, Inflation, Equities, Credit, Commodities, Money].  Defaults to \&quot;Unknown\&quot; if not set. *(read-only)* |
| **instrument_type** | **str** | Required | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.MasteredInstrument import MasteredInstrument

instance = MasteredInstrument(
    identifiers=,  # required — Dictionary of identifiers of the mastered instrument
    mastered_dom_ccy="...",  # optional — DomCcy of the Instrument that Mastered Instrument points to - read only field
    mastered_instrument_type="...",  # optional — Type of the Instrument that Mastered Instrument points to - read only field
    mastered_lusid_instrument_id="...",  # optional — Luid of the Instrument that Mastered Instrument points to - read only field
    mastered_name="...",  # optional — Name of the Instrument that Mastered Instrument points to - read only field
    mastered_scope="...",  # optional — Scope of the Instrument that Mastered Instrument points to - read only field
    mastered_asset_class="...",  # optional — Asset class of the underlying mastered instrument - read only field    Supported string (enumeration) values are: [InterestRates, FX, Inflation, Equities, Credit, Commodities, Money].  Defaults to \&quot;Unknown\&quot; if not set.
    instrument_type="..."  # required — The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

