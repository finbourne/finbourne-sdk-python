# PutRedemptionEvent

Put Redemption (BPUT) — early redemption of a bond at the holder's election under an  indenture-defined put option. Supports both Voluntary (the AMI-SeCo canonical shape) and  Mandatory (a deliberate market extension beyond SCoRE) participation on Bond, ComplexBond,  and InflationLinkedBond instruments. Cloned from RepurchaseOfferEvent (BIDS) and narrowed  to debt with a fixed event-level OfferPrice instead of a per-election holder-bid price.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **payment_date** | **datetime** | Optional | Settlement date for the cash + security legs of the put redemption. |
| **offer_price** | **float** | Required | Put price per unit of face value (AMI-SeCo OFFR). Per-100 PRCT semantics —  &#x60;OfferPrice &#x3D; 100.00&#x60; means par; &#x60;97.50&#x60; means 97.5% of par. Must be strictly positive. |
| **currency** | **str** | Required | Settlement currency of the cash leg (ISO 4217 3-letter code). |
| **cash_offer_elections** | [List[CashOfferElection]](CashOfferElection.md) | Required | List of possible CashOfferElections. Exactly one entry per event in both Mandatory and Voluntary paths. |
| **lapse_elections** | [List[LapseElection]](LapseElection.md) | Required | List of possible LapseElections. Exactly one entry for Voluntary (NOAC default). Empty for Mandatory. |
| **market_deadline_date** | **datetime** | Optional | Issuer / agent deadline for holder instructions. Required for Voluntary participation;  optional for Mandatory (no holder-deadline concept). |
| **response_deadline_date** | **datetime** | Optional | Account-servicer deadline. Defaults to MarketDeadlineDate when omitted.  If set, must be on or before MarketDeadlineDate. |
| **early_response_deadline** | **datetime** | Optional | Early-participation deadline. Rare on BPUT; carried for cross-event consistency.  If set, must be on or before ResponseDeadlineDate. |
| **ex_date** | **datetime** | Optional | AMI-SeCo §4.6 does not list this for BPUT; carried for cross-event consistency.  If set, must be on or before MarketDeadlineDate. |
| **announcement_date** | **datetime** | Optional | Public announcement date. If set, must be on or before ExDate. |
| **accrued_interest_per_unit** | **float** | Optional | Per-unit accrued interest. Optional — loader / post-processor derives from the bond&#39;s coupon  schedule and day-count when not supplied. EconomicallyComplete enforces non-null for  accrual-bearing instruments via InstrumentTypeAccruesInterest. |
| **proration_rate** | **float** | Optional | Issuer-side aggregate proration cap (AMI-SeCo PROR). Default 1.0; range (0, 1]. |
| **instrument_event_type** | **str** | Required | The Type of Event. Available values: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent, ConsentEvent, DrawingEvent, CapitalGainsDistributionEvent, ExchangeOfferEvent, DutchAuctionEvent, WorthlessEvent, PutRedemptionEvent, LoanFacilityDelayedCompensationPaymentEvent, InterestPaymentEvent. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PutRedemptionEvent import PutRedemptionEvent

instance = PutRedemptionEvent(
    payment_date=datetime.now(),  # optional — Settlement date for the cash + security legs of the put redemption.
    offer_price=0.0,  # required — Put price per unit of face value (AMI-SeCo OFFR). Per-100 PRCT semantics —  &#x60;OfferPrice &#x3D; 100.00&#x60; means par; &#x60;97.50&#x60; means 97.5% of par. Must be strictly positive.
    currency="...",  # required — Settlement currency of the cash leg (ISO 4217 3-letter code).
    cash_offer_elections=[],  # required — List of possible CashOfferElections. Exactly one entry per event in both Mandatory and Voluntary paths.
    lapse_elections=[],  # required — List of possible LapseElections. Exactly one entry for Voluntary (NOAC default). Empty for Mandatory.
    market_deadline_date=datetime.now(),  # optional — Issuer / agent deadline for holder instructions. Required for Voluntary participation;  optional for Mandatory (no holder-deadline concept).
    response_deadline_date=datetime.now(),  # optional — Account-servicer deadline. Defaults to MarketDeadlineDate when omitted.  If set, must be on or before MarketDeadlineDate.
    early_response_deadline=datetime.now(),  # optional — Early-participation deadline. Rare on BPUT; carried for cross-event consistency.  If set, must be on or before ResponseDeadlineDate.
    ex_date=datetime.now(),  # optional — AMI-SeCo §4.6 does not list this for BPUT; carried for cross-event consistency.  If set, must be on or before MarketDeadlineDate.
    announcement_date=datetime.now(),  # optional — Public announcement date. If set, must be on or before ExDate.
    accrued_interest_per_unit=0.0,  # optional — Per-unit accrued interest. Optional — loader / post-processor derives from the bond&#39;s coupon  schedule and day-count when not supplied. EconomicallyComplete enforces non-null for  accrual-bearing instruments via InstrumentTypeAccruesInterest.
    proration_rate=0.0,  # optional — Issuer-side aggregate proration cap (AMI-SeCo PROR). Default 1.0; range (0, 1].
    instrument_event_type="..."  # required — The Type of Event. Available values: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent, ConsentEvent, DrawingEvent, CapitalGainsDistributionEvent, ExchangeOfferEvent, DutchAuctionEvent, WorthlessEvent, PutRedemptionEvent, LoanFacilityDelayedCompensationPaymentEvent, InterestPaymentEvent.
)
```

- [CashOfferElection](CashOfferElection.md) — used in `cash_offer_elections`
- [LapseElection](LapseElection.md) — used in `lapse_elections`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

