# ContractForDifference

LUSID representation of a Contract for Difference.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **start_date** | **datetime** | Required | The start date of the CFD. |
| **maturity_date** | **datetime** | Optional | The maturity date for the CFD. If CFDType is Futures, this should be set to be the maturity date of the underlying  future. If CFDType is Cash, this should not be set. |
| **code** | **str** | Optional | The code of the underlying. |
| **contract_size** | **float** | Optional | The size of the CFD contract, this should represent the total number of stocks that the CFD represents.   This field is optional, if not set it will default to 1. |
| **pay_ccy** | **str** | Required | The currency that this CFD pays out, this can be different to the UnderlyingCcy. |
| **reference_rate** | **float** | Optional | The reference rate of the CFD, this can be set to 0 but not negative values.  This field is optional, if not set it will default to 0. |
| **type** | **str** | Required | The type of CFD.    Supported string (enumeration) values are: [Cash, Futures]. |
| **underlying_ccy** | **str** | Optional | The currency of the underlying |
| **underlying_identifier** | **str** | Optional | External market codes and identifiers for the CFD, e.g. RIC.    Supported string (enumeration) values are: [LusidInstrumentId, Isin, Sedol, Cusip, ClientInternal, Figi, RIC, QuotePermId, REDCode, BBGId, ICECode]. |
| **lot_size** | **int** | Optional | CFD LotSize, the minimum number of shares that can be bought or sold at once.  Optional, if set must be non-negative, if not set defaults to 1. |
| **underlying** | [LusidInstrument](LusidInstrument.md) | Optional | *No description available.* |
| **time_zone_conventions** | [TimeZoneConventions](TimeZoneConventions.md) | Optional | *No description available.* |
| **instrument_type** | **str** | Required | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ContractForDifference import ContractForDifference

instance = ContractForDifference(
    start_date=datetime.now(),  # required — The start date of the CFD.
    maturity_date=datetime.now(),  # optional — The maturity date for the CFD. If CFDType is Futures, this should be set to be the maturity date of the underlying  future. If CFDType is Cash, this should not be set.
    code="...",  # optional — The code of the underlying.
    contract_size=0.0,  # optional — The size of the CFD contract, this should represent the total number of stocks that the CFD represents.   This field is optional, if not set it will default to 1.
    pay_ccy="...",  # required — The currency that this CFD pays out, this can be different to the UnderlyingCcy.
    reference_rate=0.0,  # optional — The reference rate of the CFD, this can be set to 0 but not negative values.  This field is optional, if not set it will default to 0.
    type="...",  # required — The type of CFD.    Supported string (enumeration) values are: [Cash, Futures].
    underlying_ccy="...",  # optional — The currency of the underlying
    underlying_identifier="...",  # optional — External market codes and identifiers for the CFD, e.g. RIC.    Supported string (enumeration) values are: [LusidInstrumentId, Isin, Sedol, Cusip, ClientInternal, Figi, RIC, QuotePermId, REDCode, BBGId, ICECode].
    lot_size=0,  # optional — CFD LotSize, the minimum number of shares that can be bought or sold at once.  Optional, if set must be non-negative, if not set defaults to 1.
    underlying=LusidInstrument(...),  # optional
    time_zone_conventions=TimeZoneConventions(...),  # optional
    instrument_type="..."  # required — The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo
)
```

- [LusidInstrument](LusidInstrument.md)
- [TimeZoneConventions](TimeZoneConventions.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

