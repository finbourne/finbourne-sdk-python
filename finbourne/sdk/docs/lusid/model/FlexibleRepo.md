# FlexibleRepo

Lusid representation of a repurchase agreement, where one party sells some collateral and agrees to re-buy it at a later date for some given price.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **start_date** | **datetime** | Required | The start date of the instrument. This is normally synonymous with the trade-date. |
| **maturity_date** | **datetime** | Optional | The maturity date of the instrument. This is the date at which the repurchase will occur for a TermRepo.  Optional for OpenRepo, but if not provided, defaults to the StartDate plus a long period (e.g. 2099-12-31). |
| **buyer_or_seller** | **str** | Required | Is the user the Buyer or the Seller of this repo?  Every repo agreement has two sides, a buyer and a seller.  The Buyer pays the PurchasePrice to the Seller in exchange for legal ownership of the collateral.  At Maturity, the Buyer then receives the RepurchasePrice in exchange for returning legal ownership of the collateral.  Controls the direction of purchase and repurchase cashflows, as well as the recipient of cashflows from the collateral.    Supported string (enumeration) values are: [Buyer, Seller]. |
| **repo_ccy** | **str** | Required | Currency of the purchase and repurchase prices. May differ from the currencies on any collateral. |
| **repo_type** | **str** | Required | The type of the repurchase agreement, Open or Term.  If Term, the repurchase automatically takes place at Maturity.  If Open, the agreement is rolled by the given tenor, and an interest cashflow is paid out with each roll,  unless manually triggered by a FlexibleRepoFullClosureEvent.    Supported string (enumeration) values are: [OpenRepo, TermRepo]. |
| **accrual_basis** | **str** | Optional | For calculation of interest, the accrual day count to be used.  Required if no RepoRateSchedules are provided.  If both RepoRateSchedules and AccrualBasis are provided,  then AccrualBasis will take precedence.    Supported string (enumeration) values are: [Actual360, Act360, MoneyMarket, Actual365, Act365, Thirty360, ThirtyU360, Bond, ThirtyE360, EuroBond, ActualActual, ActAct, ActActIsda, ActActIsma, ActActIcma, OneOne, Act364, Act365F, Act365L, Act365_25, Act252, Bus252, NL360, NL365, ActActAFB, Act365Cad, ThirtyActIsda, Thirty365Isda, ThirtyEActIsda, ThirtyE360Isda, ThirtyE365Isda, ThirtyU360EOM]. |
| **collateral** | [Collateral](Collateral.md) | Optional | *No description available.* |
| **haircut** | **float** | Optional | Haircut on the value of the collateral, used to calculate PurchasePrice if not provided directly.  Haircut or Margin should be specified if PurchasePrice is not specified. |
| **margin** | **float** | Optional | Initial margin on the value of the collateral, used to calculate PurchasePrice if not provided directly.  Haircut or Margin should be specified if PurchasePrice is not specified. |
| **open_repo_rolling_period** | **str** | Optional | Required if the RepoType is Open.  The tenor representing the mandatory roll period if the FlexibleRepo is not manually matured.  If a user matures the FlexibleRepo via an instrument event, then the repurchase will delay until the end of this rolling period.  Generally this is set to 1D (one day), i.e. the repurchase will occur on the same day as the instrument event,  though any valid tenor is accepted with TenorUnit set to Day, Week, Month, or Year.  Note that TenorUnit T is not accepted here. |
| **purchase_price** | **float** | Optional | The initial purchase price of the collateral.  If provided directly in this field, then Collateral.CollateralValue,  Haircut, and Margin should not be provided. |
| **repo_rate_schedules** | [List[Schedule]](Schedule.md) | Optional | Schedules used to calculate the repurchase price and any interest payments on the FlexibleRepo.  Only one schedule may be provided, and must be of type FixedSchedule or FloatSchedule.  If RepoType is OpenRepo, a FixedSchedule or FloatSchedule must be provided to calculate the expected Repo Rate,  and RepurchasePrice must be omitted.  If RepoType is TermRepo, only one of RepurchasePrice and RepoRateSchedules should be provided.  If a RepoRateSchedule is provided on a TermRepo, the PaymentFrequency in the FlowConventions should be 1T.  StubType must be set to None, and no ExDividend configuration should be provided. |
| **repurchase_price** | **float** | Optional | The repurchase price of the repo, if known.  Only one of RepurchasePrice and RepoRateSchedules should be provided.  In the case of an OpenRepo, RepurchasePrice should not be provided,  and RepoRateSchedules should be provided instead in order to calculate the RepoRate. |
| **time_zone_conventions** | [TimeZoneConventions](TimeZoneConventions.md) | Optional | *No description available.* |
| **trading_conventions** | [TradingConventions](TradingConventions.md) | Optional | *No description available.* |
| **is_collateral_transfer_activated** | **bool** | Optional | Indicates whether the FlexibleRepoCollateralTransfer event is activated.  Determines the behavior of manufactured coupons and related boolean parameters.  Defaults to false.  When true:  - Generates the FlexibleRepoCollateralTransfer event  - Processes collateral transfer transactions into holding changes  - Generates manufactured payments when due to be paid                When false:  - Does not generate the event  - Generates manufactured payments when due to be received |
| **instrument_type** | **str** | Required | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FlexibleRepo import FlexibleRepo

instance = FlexibleRepo(
    start_date=datetime.now(),  # required — The start date of the instrument. This is normally synonymous with the trade-date.
    maturity_date=datetime.now(),  # optional — The maturity date of the instrument. This is the date at which the repurchase will occur for a TermRepo.  Optional for OpenRepo, but if not provided, defaults to the StartDate plus a long period (e.g. 2099-12-31).
    buyer_or_seller="...",  # required — Is the user the Buyer or the Seller of this repo?  Every repo agreement has two sides, a buyer and a seller.  The Buyer pays the PurchasePrice to the Seller in exchange for legal ownership of the collateral.  At Maturity, the Buyer then receives the RepurchasePrice in exchange for returning legal ownership of the collateral.  Controls the direction of purchase and repurchase cashflows, as well as the recipient of cashflows from the collateral.    Supported string (enumeration) values are: [Buyer, Seller].
    repo_ccy="...",  # required — Currency of the purchase and repurchase prices. May differ from the currencies on any collateral.
    repo_type="...",  # required — The type of the repurchase agreement, Open or Term.  If Term, the repurchase automatically takes place at Maturity.  If Open, the agreement is rolled by the given tenor, and an interest cashflow is paid out with each roll,  unless manually triggered by a FlexibleRepoFullClosureEvent.    Supported string (enumeration) values are: [OpenRepo, TermRepo].
    accrual_basis="...",  # optional — For calculation of interest, the accrual day count to be used.  Required if no RepoRateSchedules are provided.  If both RepoRateSchedules and AccrualBasis are provided,  then AccrualBasis will take precedence.    Supported string (enumeration) values are: [Actual360, Act360, MoneyMarket, Actual365, Act365, Thirty360, ThirtyU360, Bond, ThirtyE360, EuroBond, ActualActual, ActAct, ActActIsda, ActActIsma, ActActIcma, OneOne, Act364, Act365F, Act365L, Act365_25, Act252, Bus252, NL360, NL365, ActActAFB, Act365Cad, ThirtyActIsda, Thirty365Isda, ThirtyEActIsda, ThirtyE360Isda, ThirtyE365Isda, ThirtyU360EOM].
    collateral=Collateral(...),  # optional
    haircut=0.0,  # optional — Haircut on the value of the collateral, used to calculate PurchasePrice if not provided directly.  Haircut or Margin should be specified if PurchasePrice is not specified.
    margin=0.0,  # optional — Initial margin on the value of the collateral, used to calculate PurchasePrice if not provided directly.  Haircut or Margin should be specified if PurchasePrice is not specified.
    open_repo_rolling_period="...",  # optional — Required if the RepoType is Open.  The tenor representing the mandatory roll period if the FlexibleRepo is not manually matured.  If a user matures the FlexibleRepo via an instrument event, then the repurchase will delay until the end of this rolling period.  Generally this is set to 1D (one day), i.e. the repurchase will occur on the same day as the instrument event,  though any valid tenor is accepted with TenorUnit set to Day, Week, Month, or Year.  Note that TenorUnit T is not accepted here.
    purchase_price=0.0,  # optional — The initial purchase price of the collateral.  If provided directly in this field, then Collateral.CollateralValue,  Haircut, and Margin should not be provided.
    repo_rate_schedules=[],  # optional — Schedules used to calculate the repurchase price and any interest payments on the FlexibleRepo.  Only one schedule may be provided, and must be of type FixedSchedule or FloatSchedule.  If RepoType is OpenRepo, a FixedSchedule or FloatSchedule must be provided to calculate the expected Repo Rate,  and RepurchasePrice must be omitted.  If RepoType is TermRepo, only one of RepurchasePrice and RepoRateSchedules should be provided.  If a RepoRateSchedule is provided on a TermRepo, the PaymentFrequency in the FlowConventions should be 1T.  StubType must be set to None, and no ExDividend configuration should be provided.
    repurchase_price=0.0,  # optional — The repurchase price of the repo, if known.  Only one of RepurchasePrice and RepoRateSchedules should be provided.  In the case of an OpenRepo, RepurchasePrice should not be provided,  and RepoRateSchedules should be provided instead in order to calculate the RepoRate.
    time_zone_conventions=TimeZoneConventions(...),  # optional
    trading_conventions=TradingConventions(...),  # optional
    is_collateral_transfer_activated=True,  # optional — Indicates whether the FlexibleRepoCollateralTransfer event is activated.  Determines the behavior of manufactured coupons and related boolean parameters.  Defaults to false.  When true:  - Generates the FlexibleRepoCollateralTransfer event  - Processes collateral transfer transactions into holding changes  - Generates manufactured payments when due to be paid                When false:  - Does not generate the event  - Generates manufactured payments when due to be received
    instrument_type="..."  # required — The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo
)
```

- [Collateral](Collateral.md)
- [Schedule](Schedule.md) — used in `repo_rate_schedules`
- [TimeZoneConventions](TimeZoneConventions.md)
- [TradingConventions](TradingConventions.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

