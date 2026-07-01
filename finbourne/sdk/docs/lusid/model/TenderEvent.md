# TenderEvent

Tender Event (TEND).
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **announcement_date** | **datetime** | Optional | The date the tender is announced. |
| **ex_date** | **datetime** | Optional | The ex date (entitlement date) of the event. |
| **record_date** | **datetime** | Optional | Date you have to be the holder of record in order to participate in the tender. |
| **payment_date** | **datetime** | Optional | The payment date of the event. |
| **new_instrument** | [NewInstrument](NewInstrument.md) | Required | *No description available.* |
| **fractional_units_cash_price** | **float** | Optional | The cash price paid in lieu of fractionalUnits. |
| **fractional_units_cash_currency** | **str** | Optional | The currency of the cash paid in lieu of fractionalUnits. |
| **security_offer_elections** | [List[SecurityOfferElection]](SecurityOfferElection.md) | Optional | List of possible SecurityOfferElections for this event. |
| **cash_and_security_offer_elections** | [List[CashAndSecurityOfferElection]](CashAndSecurityOfferElection.md) | Optional | List of possible CashAndSecurityOfferElections for this event. |
| **cash_offer_elections** | [List[CashOfferElection]](CashOfferElection.md) | Optional | List of possible CashOfferElections for this event. |
| **offer_type** | **str** | Optional | Informational ISO 20022 OfferTp indicator (e.g. \&quot;ACPR\&quot;). Optional. No calculation impact. |
| **accrued_interest_per_unit** | **float** | Optional | Optional per-unit accrued interest on the tendered face, from the last coupon date up to  (but excluding) PaymentDate. Bond instrument types only. If left empty, analytics-core  resolves it at event time from the bond&#39;s coupon schedule and market data. |
| **min_piece_size** | **float** | Optional | Bond-specific minimum instructable face amount. Optional. Must be strictly positive when set. |
| **min_increment** | **float** | Optional | Bond-specific increment above MinPieceSize. Optional. When set, MinPieceSize must also be set.  Must be strictly positive. |
| **proration_rate** | **float** | Optional | Proration applied when the offer is oversubscribed. Defaults to 1 if not set.  Must be greater than 0 and less than or equal to 1. Default: `1` |
| **response_deadline_date** | **datetime** | Optional | Account-servicer SLA deadline for holder instruction. Optional at the DTO layer;  required under Voluntary participation on bond instrument types. |
| **market_deadline_date** | **datetime** | Optional | Offeror&#39;s-agent deadline for holder instruction. Optional at the DTO layer;  required under Voluntary participation on bond instrument types. |
| **early_response_deadline** | **datetime** | Optional | Optional early-tender deadline. When set, must be on or before ResponseDeadlineDate. |
| **instrument_event_type** | **str** | Required | The Type of Event. Available values: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent, ConsentEvent, DrawingEvent, CapitalGainsDistributionEvent, ExchangeOfferEvent, DutchAuctionEvent, WorthlessEvent, PutRedemptionEvent, LoanFacilityDelayedCompensationPaymentEvent, InterestPaymentEvent, PriorityIssueEvent, ClassActionEvent, BankruptcyEvent, LiquidationPaymentEvent, PartialDefeasanceEvent. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TenderEvent import TenderEvent

instance = TenderEvent(
    announcement_date=datetime.now(),  # optional — The date the tender is announced.
    ex_date=datetime.now(),  # optional — The ex date (entitlement date) of the event.
    record_date=datetime.now(),  # optional — Date you have to be the holder of record in order to participate in the tender.
    payment_date=datetime.now(),  # optional — The payment date of the event.
    new_instrument=NewInstrument(...),  # required
    fractional_units_cash_price=0.0,  # optional — The cash price paid in lieu of fractionalUnits.
    fractional_units_cash_currency="...",  # optional — The currency of the cash paid in lieu of fractionalUnits.
    security_offer_elections=[],  # optional — List of possible SecurityOfferElections for this event.
    cash_and_security_offer_elections=[],  # optional — List of possible CashAndSecurityOfferElections for this event.
    cash_offer_elections=[],  # optional — List of possible CashOfferElections for this event.
    offer_type="...",  # optional — Informational ISO 20022 OfferTp indicator (e.g. \&quot;ACPR\&quot;). Optional. No calculation impact.
    accrued_interest_per_unit=0.0,  # optional — Optional per-unit accrued interest on the tendered face, from the last coupon date up to  (but excluding) PaymentDate. Bond instrument types only. If left empty, analytics-core  resolves it at event time from the bond&#39;s coupon schedule and market data.
    min_piece_size=0.0,  # optional — Bond-specific minimum instructable face amount. Optional. Must be strictly positive when set.
    min_increment=0.0,  # optional — Bond-specific increment above MinPieceSize. Optional. When set, MinPieceSize must also be set.  Must be strictly positive.
    proration_rate=0.0,  # optional — Proration applied when the offer is oversubscribed. Defaults to 1 if not set.  Must be greater than 0 and less than or equal to 1.
    response_deadline_date=datetime.now(),  # optional — Account-servicer SLA deadline for holder instruction. Optional at the DTO layer;  required under Voluntary participation on bond instrument types.
    market_deadline_date=datetime.now(),  # optional — Offeror&#39;s-agent deadline for holder instruction. Optional at the DTO layer;  required under Voluntary participation on bond instrument types.
    early_response_deadline=datetime.now(),  # optional — Optional early-tender deadline. When set, must be on or before ResponseDeadlineDate.
    instrument_event_type="..."  # required — The Type of Event. Available values: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent, ConsentEvent, DrawingEvent, CapitalGainsDistributionEvent, ExchangeOfferEvent, DutchAuctionEvent, WorthlessEvent, PutRedemptionEvent, LoanFacilityDelayedCompensationPaymentEvent, InterestPaymentEvent, PriorityIssueEvent, ClassActionEvent, BankruptcyEvent, LiquidationPaymentEvent, PartialDefeasanceEvent.
)
```

- [NewInstrument](NewInstrument.md)
- [SecurityOfferElection](SecurityOfferElection.md) — used in `security_offer_elections`
- [CashAndSecurityOfferElection](CashAndSecurityOfferElection.md) — used in `cash_and_security_offer_elections`
- [CashOfferElection](CashOfferElection.md) — used in `cash_offer_elections`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

