# RepurchaseOfferEvent

Representation of a repurchase offer corporate action.  Represents an offer by the issuer to repurchase its own shares from a shareholder at a given price.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **payment_date** | **datetime** | Optional | Payment date of the event. |
| **market_deadline_date** | **datetime** | Optional | Date set by the issuer or by an agent of the issuer as the latest date to respond to the offer. Must be before or equal to the PaymentDate. |
| **repurchase_quantity** | **float** | Required | Quantity of the security to be repurchased. |
| **cash_offer_elections** | [List[CashOfferElection]](CashOfferElection.md) | Required | List of possible CashOfferElections for this event. Only 1 should be provided. |
| **lapse_elections** | [List[LapseElection]](LapseElection.md) | Required | List of possible LapseElections for this event. Only 1 should be provided.  Allows the user to opt out of the offer. |
| **tender_offer_elections** | [List[TenderOfferElection]](TenderOfferElection.md) | Required | List of possible TenderOfferElections for this event. Only 1 should be provided. |
| **proration_rate** | **float** | Optional | The fraction used to calculate a proportional adjustment for RepurchaseQuantity when a full period is not used.  Defaults to 1 if not set. Must be greater than 0 and less than or equal to 1. Default: `1` |
| **response_deadline_date** | **datetime** | Optional | Date set by the account servicer as the latest date to respond to the offer.  Optional. If set, must be before or equal to MarketDeadlineDate.  Defaults to MarketDeadlineDate if not set. |
| **early_response_deadline** | **datetime** | Optional | Optional CTEN early-tender deadline. If set, must be on or before ResponseDeadlineDate.  Used for bond tender offers where early tenders attract a premium. |
| **min_piece_size** | **float** | Optional | Bond-specific minimum instructable face amount. Optional.  Must be strictly positive when set. |
| **min_increment** | **float** | Optional | Bond-specific increment above MinPieceSize. Optional.  When set, MinPieceSize must also be set. Must be strictly positive. |
| **accrued_interest_per_unit** | **float** | Optional | Optional per-unit accrued interest on the accepted face amount, from the last coupon date  up to (but excluding) PaymentDate. Bond-like instruments only. If left empty,  resolves it internally at event time from the bond&#39;s coupon schedule and market data. |
| **consent_and_tender_elections** | [List[ConsentAndTenderElection]](ConsentAndTenderElection.md) | Optional | List of possible consent-and-tender elections for this event (CTEN) — tender the holding and grant consent together. |
| **consent_granted_elections** | [List[ConsentGrantedElection]](ConsentGrantedElection.md) | Optional | List of possible consent-granted elections for this event (CONY) — vote in favour, optionally attracting a consent fee. |
| **consent_denied_elections** | [List[ConsentDeniedElection]](ConsentDeniedElection.md) | Optional | List of possible consent-denied elections for this event (CONN) — vote against the proposal. |
| **abstain_elections** | [List[AbstainElection]](AbstainElection.md) | Optional | List of possible abstain elections for this event (ABST) — decline to vote on the consent. |
| **unknown_proceeds_elections** | [List[UnknownProceedsElection]](UnknownProceedsElection.md) | Optional | List of possible unknown-proceeds elections for this event (UNKNOWN) — the outturn is not yet known. |
| **instrument_event_type** | **str** | Required | The Type of Event. Available values: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent, ConsentEvent, DrawingEvent, CapitalGainsDistributionEvent, ExchangeOfferEvent, DutchAuctionEvent, WorthlessEvent, PutRedemptionEvent, LoanFacilityDelayedCompensationPaymentEvent, InterestPaymentEvent, PriorityIssueEvent, ClassActionEvent, BankruptcyEvent, LiquidationPaymentEvent, PartialDefeasanceEvent, SecurityWriteOffEvent, WarrantsExerciseEvent, PariPassuEvent, ChangeEvent, PikBondCouponEvent, PikBondCashCouponEvent, PikBondInterestCapitalisationEvent, PikBondPrincipalEvent, DelistingEvent, PikBondInterestEvent, CommodityForwardCashSettlementEvent, PaymentInKindEvent, CommodityForwardPhysicalSettlementEvent, CancelSwapEvent, BondOptionTerminationEvent, TerminationEvent, CommodityCalendarSwapCashFlowEvent, DepositSweepEvent, BondForwardCashSettlementEvent, BondForwardTerminationEvent, AmendCommitmentEvent, CapitalCallEvent, FundDistributionEvent, NavReportEvent, DividendSuspensionEvent, LoanInterestCapitalisationEvent. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RepurchaseOfferEvent import RepurchaseOfferEvent

instance = RepurchaseOfferEvent(
    payment_date=datetime.now(),  # optional — Payment date of the event.
    market_deadline_date=datetime.now(),  # optional — Date set by the issuer or by an agent of the issuer as the latest date to respond to the offer. Must be before or equal to the PaymentDate.
    repurchase_quantity=0.0,  # required — Quantity of the security to be repurchased.
    cash_offer_elections=[],  # required — List of possible CashOfferElections for this event. Only 1 should be provided.
    lapse_elections=[],  # required — List of possible LapseElections for this event. Only 1 should be provided.  Allows the user to opt out of the offer.
    tender_offer_elections=[],  # required — List of possible TenderOfferElections for this event. Only 1 should be provided.
    proration_rate=0.0,  # optional — The fraction used to calculate a proportional adjustment for RepurchaseQuantity when a full period is not used.  Defaults to 1 if not set. Must be greater than 0 and less than or equal to 1.
    response_deadline_date=datetime.now(),  # optional — Date set by the account servicer as the latest date to respond to the offer.  Optional. If set, must be before or equal to MarketDeadlineDate.  Defaults to MarketDeadlineDate if not set.
    early_response_deadline=datetime.now(),  # optional — Optional CTEN early-tender deadline. If set, must be on or before ResponseDeadlineDate.  Used for bond tender offers where early tenders attract a premium.
    min_piece_size=0.0,  # optional — Bond-specific minimum instructable face amount. Optional.  Must be strictly positive when set.
    min_increment=0.0,  # optional — Bond-specific increment above MinPieceSize. Optional.  When set, MinPieceSize must also be set. Must be strictly positive.
    accrued_interest_per_unit=0.0,  # optional — Optional per-unit accrued interest on the accepted face amount, from the last coupon date  up to (but excluding) PaymentDate. Bond-like instruments only. If left empty,  resolves it internally at event time from the bond&#39;s coupon schedule and market data.
    consent_and_tender_elections=[],  # optional — List of possible consent-and-tender elections for this event (CTEN) — tender the holding and grant consent together.
    consent_granted_elections=[],  # optional — List of possible consent-granted elections for this event (CONY) — vote in favour, optionally attracting a consent fee.
    consent_denied_elections=[],  # optional — List of possible consent-denied elections for this event (CONN) — vote against the proposal.
    abstain_elections=[],  # optional — List of possible abstain elections for this event (ABST) — decline to vote on the consent.
    unknown_proceeds_elections=[],  # optional — List of possible unknown-proceeds elections for this event (UNKNOWN) — the outturn is not yet known.
    instrument_event_type="..."  # required — The Type of Event. Available values: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent, ConsentEvent, DrawingEvent, CapitalGainsDistributionEvent, ExchangeOfferEvent, DutchAuctionEvent, WorthlessEvent, PutRedemptionEvent, LoanFacilityDelayedCompensationPaymentEvent, InterestPaymentEvent, PriorityIssueEvent, ClassActionEvent, BankruptcyEvent, LiquidationPaymentEvent, PartialDefeasanceEvent, SecurityWriteOffEvent, WarrantsExerciseEvent, PariPassuEvent, ChangeEvent, PikBondCouponEvent, PikBondCashCouponEvent, PikBondInterestCapitalisationEvent, PikBondPrincipalEvent, DelistingEvent, PikBondInterestEvent, CommodityForwardCashSettlementEvent, PaymentInKindEvent, CommodityForwardPhysicalSettlementEvent, CancelSwapEvent, BondOptionTerminationEvent, TerminationEvent, CommodityCalendarSwapCashFlowEvent, DepositSweepEvent, BondForwardCashSettlementEvent, BondForwardTerminationEvent, AmendCommitmentEvent, CapitalCallEvent, FundDistributionEvent, NavReportEvent, DividendSuspensionEvent, LoanInterestCapitalisationEvent.
)
```

- [CashOfferElection](CashOfferElection.md) — used in `cash_offer_elections`
- [LapseElection](LapseElection.md) — used in `lapse_elections`
- [TenderOfferElection](TenderOfferElection.md) — used in `tender_offer_elections`
- [ConsentAndTenderElection](ConsentAndTenderElection.md) — used in `consent_and_tender_elections`
- [ConsentGrantedElection](ConsentGrantedElection.md) — used in `consent_granted_elections`
- [ConsentDeniedElection](ConsentDeniedElection.md) — used in `consent_denied_elections`
- [AbstainElection](AbstainElection.md) — used in `abstain_elections`
- [UnknownProceedsElection](UnknownProceedsElection.md) — used in `unknown_proceeds_elections`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

