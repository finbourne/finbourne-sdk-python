# WarrantsExerciseEvent

Warrants Exercise (EXWA) — the holder's election to exercise an outstanding warrant, paying the  strike and receiving the underlying security, or to let it lapse at zero proceeds. Elective  (Voluntary / MandatoryWithChoices) on EquityOption (EquityOptionType = Warrant) and SimpleInstrument.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **payment_date** | **datetime** | Optional | The DvP settlement date on which the strike is paid and the underlying is delivered.  Must be on or after PeriodOfActionEnd. |
| **period_of_action_start** | **datetime** | Optional | Start of the exercise window. |
| **period_of_action_end** | **datetime** | Optional | End of the exercise window. |
| **response_deadline_date** | **datetime** | Optional | Holder response deadline. Required when participation is MandatoryWithChoices. |
| **market_deadline_date** | **datetime** | Optional | Market deadline. Required when participation is MandatoryWithChoices. |
| **early_response_deadline** | **datetime** | Optional | Early response deadline. Optional; populated by some vendor wires. |
| **strike_per_unit** | **float** | Optional | Cash payable per warrant on exercise. Null-allowed on upsert if the warrant instrument resolves  a non-null EquityOption.Strike (instrument-level fallback applied later). If supplied, must be  strictly positive and accompanied by a StrikeCurrency. |
| **strike_currency** | **str** | Optional | Currency of the strike (ISO 4217 3-letter code). Required if StrikePerUnit is non-null. |
| **units_ratio** | [UnitsRatio](UnitsRatio.md) | Optional | *No description available.* |
| **new_instrument** | [NewInstrument](NewInstrument.md) | Optional | *No description available.* |
| **fraction_disposition** | **str** | Optional | Handling of fractional underlying units. Defaults to round-down (RDDN) in the holdings engine when null.                Supported string (enumeration) values are: [RDDN, CINL]. Available values: RDDN, CINL. |
| **option_exercise_elections** | [List[OptionExerciseElection]](OptionExerciseElection.md) | Optional | Option exercise elections for this event. At least one entry. |
| **lapse_elections** | [List[LapseElection]](LapseElection.md) | Optional | Lapse elections for this event. Required when participation is MandatoryWithChoices or when the  issuer publishes a no-action default. |
| **instrument_event_type** | **str** | Required | The Type of Event. Available values: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent, ConsentEvent, DrawingEvent, CapitalGainsDistributionEvent, ExchangeOfferEvent, DutchAuctionEvent, WorthlessEvent, PutRedemptionEvent, LoanFacilityDelayedCompensationPaymentEvent, InterestPaymentEvent, PriorityIssueEvent, ClassActionEvent, BankruptcyEvent, LiquidationPaymentEvent, PartialDefeasanceEvent, SecurityWriteOffEvent, WarrantsExerciseEvent, PariPassuEvent. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.WarrantsExerciseEvent import WarrantsExerciseEvent

instance = WarrantsExerciseEvent(
    payment_date=datetime.now(),  # optional — The DvP settlement date on which the strike is paid and the underlying is delivered.  Must be on or after PeriodOfActionEnd.
    period_of_action_start=datetime.now(),  # optional — Start of the exercise window.
    period_of_action_end=datetime.now(),  # optional — End of the exercise window.
    response_deadline_date=datetime.now(),  # optional — Holder response deadline. Required when participation is MandatoryWithChoices.
    market_deadline_date=datetime.now(),  # optional — Market deadline. Required when participation is MandatoryWithChoices.
    early_response_deadline=datetime.now(),  # optional — Early response deadline. Optional; populated by some vendor wires.
    strike_per_unit=0.0,  # optional — Cash payable per warrant on exercise. Null-allowed on upsert if the warrant instrument resolves  a non-null EquityOption.Strike (instrument-level fallback applied later). If supplied, must be  strictly positive and accompanied by a StrikeCurrency.
    strike_currency="...",  # optional — Currency of the strike (ISO 4217 3-letter code). Required if StrikePerUnit is non-null.
    units_ratio=UnitsRatio(...),  # optional
    new_instrument=NewInstrument(...),  # optional
    fraction_disposition="...",  # optional — Handling of fractional underlying units. Defaults to round-down (RDDN) in the holdings engine when null.                Supported string (enumeration) values are: [RDDN, CINL]. Available values: RDDN, CINL.
    option_exercise_elections=[],  # optional — Option exercise elections for this event. At least one entry.
    lapse_elections=[],  # optional — Lapse elections for this event. Required when participation is MandatoryWithChoices or when the  issuer publishes a no-action default.
    instrument_event_type="..."  # required — The Type of Event. Available values: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent, ConsentEvent, DrawingEvent, CapitalGainsDistributionEvent, ExchangeOfferEvent, DutchAuctionEvent, WorthlessEvent, PutRedemptionEvent, LoanFacilityDelayedCompensationPaymentEvent, InterestPaymentEvent, PriorityIssueEvent, ClassActionEvent, BankruptcyEvent, LiquidationPaymentEvent, PartialDefeasanceEvent, SecurityWriteOffEvent, WarrantsExerciseEvent, PariPassuEvent.
)
```

- [UnitsRatio](UnitsRatio.md)
- [NewInstrument](NewInstrument.md)
- [OptionExerciseElection](OptionExerciseElection.md) — used in `option_exercise_elections`
- [LapseElection](LapseElection.md) — used in `lapse_elections`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

