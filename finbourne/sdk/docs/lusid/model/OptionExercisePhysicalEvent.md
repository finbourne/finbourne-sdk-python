# OptionExercisePhysicalEvent

Event for physical option exercises.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **exercise_date** | **datetime** | Optional | The exercise date of the option. |
| **delivery_date** | **datetime** | Optional | The delivery date of the option. |
| **exercise_type** | **str** | Required | The optionality type of the underlying option e.g. American, European.    Supported string (enumeration) values are: [European, Bermudan, American]. |
| **maturity_date** | **datetime** | Optional | The maturity date of the option. |
| **moneyness** | **str** | Optional | The moneyness of the option e.g. InTheMoney, OutOfTheMoney.    Supported string (enumeration) values are: [InTheMoney, OutOfTheMoney, AtTheMoney]. |
| **new_instrument** | [NewInstrument](NewInstrument.md) | Required | *No description available.* |
| **option_exercise_elections** | [List[OptionExerciseElection]](OptionExerciseElection.md) | Optional | Option exercise election for this OptionExercisePhysicalEvent. |
| **option_type** | **str** | Required | Type of optionality that is present e.g. call, put.    Supported string (enumeration) values are: [Call, Put]. |
| **start_date** | **datetime** | Optional | The trade date of the option. |
| **strike_currency** | **str** | Required | The strike currency of the equity option. |
| **strike_per_unit** | **float** | Required | The strike of the equity option times the number of shares to exchange if exercised. |
| **underlying_value_per_unit** | **float** | Optional | The underlying price times the number of shares to exchange if exercised. |
| **units_ratio** | [UnitsRatio](UnitsRatio.md) | Required | *No description available.* |
| **instrument_event_type** | **str** | Required | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.OptionExercisePhysicalEvent import OptionExercisePhysicalEvent

instance = OptionExercisePhysicalEvent(
    exercise_date=datetime.now(),  # optional — The exercise date of the option.
    delivery_date=datetime.now(),  # optional — The delivery date of the option.
    exercise_type="...",  # required — The optionality type of the underlying option e.g. American, European.    Supported string (enumeration) values are: [European, Bermudan, American].
    maturity_date=datetime.now(),  # optional — The maturity date of the option.
    moneyness="...",  # optional — The moneyness of the option e.g. InTheMoney, OutOfTheMoney.    Supported string (enumeration) values are: [InTheMoney, OutOfTheMoney, AtTheMoney].
    new_instrument=NewInstrument(...),  # required
    option_exercise_elections=[],  # optional — Option exercise election for this OptionExercisePhysicalEvent.
    option_type="...",  # required — Type of optionality that is present e.g. call, put.    Supported string (enumeration) values are: [Call, Put].
    start_date=datetime.now(),  # optional — The trade date of the option.
    strike_currency="...",  # required — The strike currency of the equity option.
    strike_per_unit=0.0,  # required — The strike of the equity option times the number of shares to exchange if exercised.
    underlying_value_per_unit=0.0,  # optional — The underlying price times the number of shares to exchange if exercised.
    units_ratio=UnitsRatio(...),  # required
    instrument_event_type="..."  # required — The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent
)
```

- [NewInstrument](NewInstrument.md)
- [OptionExerciseElection](OptionExerciseElection.md) — used in `option_exercise_elections`
- [UnitsRatio](UnitsRatio.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

