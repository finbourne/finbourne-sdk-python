# ClassActionEvent

Class Action Event (CLSA) — a voluntary corporate action under which security holders  receive cash compensation from a court-approved settlement fund following litigation  against an issuer.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **payment_date** | **datetime** | Optional | Date on which the settlement distribution is paid to the holder. |
| **filing_deadline** | **datetime** | Optional | Court-set deadline for submitting a proof of claim. |
| **class_period_start** | **datetime** | Optional | Lower bound of the eligibility window (inclusive). |
| **class_period_end** | **datetime** | Optional | Upper bound of the eligibility window (inclusive). |
| **ex_date** | **datetime** | Optional | Date from which the security trades without the settlement right.  Null for most class actions where no ex date is defined. |
| **record_date** | **datetime** | Optional | Date at which positions are struck for notification scope. Informational only. |
| **announcement_date** | **datetime** | Optional | Settlement public-announcement or court-approval date. |
| **case_reference** | **str** | Optional | Lawsuit or settlement-fund identifier (court case number, fund name). Audit-only. |
| **cash_offer_elections** | [List[CashOfferElection]](CashOfferElection.md) | Optional | Cash offer elections for this event. Exactly one entry carrying the per-share  settlement amount as CashOfferPrice and settlement currency as CashOfferCurrency. |
| **lapse_elections** | [List[LapseElection]](LapseElection.md) | Optional | Lapse elections for this event. Exactly one entry (NOAC) with IsDefault &#x3D; true. |
| **instrument_event_type** | **str** | Required | The Type of Event. Available values: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent, ConsentEvent, DrawingEvent, CapitalGainsDistributionEvent, ExchangeOfferEvent, DutchAuctionEvent, WorthlessEvent, PutRedemptionEvent, LoanFacilityDelayedCompensationPaymentEvent, InterestPaymentEvent, PriorityIssueEvent, ClassActionEvent. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ClassActionEvent import ClassActionEvent

instance = ClassActionEvent(
    payment_date=datetime.now(),  # optional — Date on which the settlement distribution is paid to the holder.
    filing_deadline=datetime.now(),  # optional — Court-set deadline for submitting a proof of claim.
    class_period_start=datetime.now(),  # optional — Lower bound of the eligibility window (inclusive).
    class_period_end=datetime.now(),  # optional — Upper bound of the eligibility window (inclusive).
    ex_date=datetime.now(),  # optional — Date from which the security trades without the settlement right.  Null for most class actions where no ex date is defined.
    record_date=datetime.now(),  # optional — Date at which positions are struck for notification scope. Informational only.
    announcement_date=datetime.now(),  # optional — Settlement public-announcement or court-approval date.
    case_reference="...",  # optional — Lawsuit or settlement-fund identifier (court case number, fund name). Audit-only.
    cash_offer_elections=[],  # optional — Cash offer elections for this event. Exactly one entry carrying the per-share  settlement amount as CashOfferPrice and settlement currency as CashOfferCurrency.
    lapse_elections=[],  # optional — Lapse elections for this event. Exactly one entry (NOAC) with IsDefault &#x3D; true.
    instrument_event_type="..."  # required — The Type of Event. Available values: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent, ConsentEvent, DrawingEvent, CapitalGainsDistributionEvent, ExchangeOfferEvent, DutchAuctionEvent, WorthlessEvent, PutRedemptionEvent, LoanFacilityDelayedCompensationPaymentEvent, InterestPaymentEvent, PriorityIssueEvent, ClassActionEvent.
)
```

- [CashOfferElection](CashOfferElection.md) — used in `cash_offer_elections`
- [LapseElection](LapseElection.md) — used in `lapse_elections`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

