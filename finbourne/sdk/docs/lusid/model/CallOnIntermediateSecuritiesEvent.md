# CallOnIntermediateSecuritiesEvent

CallOnIntermediateSecuritiesEvent event (EXRI), representing an exercise on intermediate securities resulting from an intermediate securities distribution.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **expiry_date** | **datetime** | Optional | The date on which the issue ends. |
| **payment_date** | **datetime** | Optional | The payment date of the event. |
| **new_instrument** | [NewInstrument](NewInstrument.md) | Required | *No description available.* |
| **units_ratio** | [UnitsRatio](UnitsRatio.md) | Required | *No description available.* |
| **price** | **float** | Required | The price at which new units are purchased. |
| **exercise_currency** | **str** | Required | The currency of the exercise. |
| **option_exercise_elections** | [List[OptionExerciseElection]](OptionExerciseElection.md) | Optional | Option exercise election for this event. |
| **lapse_elections** | [List[LapseElection]](LapseElection.md) | Optional | Lapse election for this event. |
| **oversubscribe_elections** | [List[OversubscribeElection]](OversubscribeElection.md) | Optional | List of possible oversubscribe elections for this event (OVER) — subscribe for more than the entitled amount. |
| **sell_entitlement_elections** | [List[SellEntitlementElection]](SellEntitlementElection.md) | Optional | List of possible sell-entitlement elections for this event (SLLE) — sell the intermediate securities rather than exercise. |
| **unknown_proceeds_elections** | [List[UnknownProceedsElection]](UnknownProceedsElection.md) | Optional | List of possible unknown-proceeds elections for this event (UNKNOWN) — the outturn is not yet known. |
| **instrument_event_type** | **str** | Required | The Type of Event. Available values: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent, ConsentEvent, DrawingEvent, CapitalGainsDistributionEvent, ExchangeOfferEvent, DutchAuctionEvent, WorthlessEvent, PutRedemptionEvent, LoanFacilityDelayedCompensationPaymentEvent, InterestPaymentEvent, PriorityIssueEvent, ClassActionEvent, BankruptcyEvent, LiquidationPaymentEvent, PartialDefeasanceEvent, SecurityWriteOffEvent, WarrantsExerciseEvent, PariPassuEvent, ChangeEvent, PikBondCouponEvent, PikBondCashCouponEvent, PikBondInterestCapitalisationEvent, PikBondPrincipalEvent, DelistingEvent, PikBondInterestEvent, CommodityForwardCashSettlementEvent, PaymentInKindEvent, CommodityForwardPhysicalSettlementEvent, CancelSwapEvent, BondOptionTerminationEvent, TerminationEvent, CommodityCalendarSwapCashFlowEvent, DepositSweepEvent, BondForwardCashSettlementEvent, BondForwardTerminationEvent, AmendCommitmentEvent, CapitalCallEvent, FundDistributionEvent, NavReportEvent, DividendSuspensionEvent, LoanInterestCapitalisationEvent. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CallOnIntermediateSecuritiesEvent import CallOnIntermediateSecuritiesEvent

instance = CallOnIntermediateSecuritiesEvent(
    expiry_date=datetime.now(),  # optional — The date on which the issue ends.
    payment_date=datetime.now(),  # optional — The payment date of the event.
    new_instrument=NewInstrument(...),  # required
    units_ratio=UnitsRatio(...),  # required
    price=0.0,  # required — The price at which new units are purchased.
    exercise_currency="...",  # required — The currency of the exercise.
    option_exercise_elections=[],  # optional — Option exercise election for this event.
    lapse_elections=[],  # optional — Lapse election for this event.
    oversubscribe_elections=[],  # optional — List of possible oversubscribe elections for this event (OVER) — subscribe for more than the entitled amount.
    sell_entitlement_elections=[],  # optional — List of possible sell-entitlement elections for this event (SLLE) — sell the intermediate securities rather than exercise.
    unknown_proceeds_elections=[],  # optional — List of possible unknown-proceeds elections for this event (UNKNOWN) — the outturn is not yet known.
    instrument_event_type="..."  # required — The Type of Event. Available values: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent, ConsentEvent, DrawingEvent, CapitalGainsDistributionEvent, ExchangeOfferEvent, DutchAuctionEvent, WorthlessEvent, PutRedemptionEvent, LoanFacilityDelayedCompensationPaymentEvent, InterestPaymentEvent, PriorityIssueEvent, ClassActionEvent, BankruptcyEvent, LiquidationPaymentEvent, PartialDefeasanceEvent, SecurityWriteOffEvent, WarrantsExerciseEvent, PariPassuEvent, ChangeEvent, PikBondCouponEvent, PikBondCashCouponEvent, PikBondInterestCapitalisationEvent, PikBondPrincipalEvent, DelistingEvent, PikBondInterestEvent, CommodityForwardCashSettlementEvent, PaymentInKindEvent, CommodityForwardPhysicalSettlementEvent, CancelSwapEvent, BondOptionTerminationEvent, TerminationEvent, CommodityCalendarSwapCashFlowEvent, DepositSweepEvent, BondForwardCashSettlementEvent, BondForwardTerminationEvent, AmendCommitmentEvent, CapitalCallEvent, FundDistributionEvent, NavReportEvent, DividendSuspensionEvent, LoanInterestCapitalisationEvent.
)
```

- [NewInstrument](NewInstrument.md)
- [UnitsRatio](UnitsRatio.md)
- [OptionExerciseElection](OptionExerciseElection.md) — used in `option_exercise_elections`
- [LapseElection](LapseElection.md) — used in `lapse_elections`
- [OversubscribeElection](OversubscribeElection.md) — used in `oversubscribe_elections`
- [SellEntitlementElection](SellEntitlementElection.md) — used in `sell_entitlement_elections`
- [UnknownProceedsElection](UnknownProceedsElection.md) — used in `unknown_proceeds_elections`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

