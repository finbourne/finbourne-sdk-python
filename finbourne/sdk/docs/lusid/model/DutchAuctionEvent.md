# DutchAuctionEvent

Dutch Auction Event (DTCH) — a voluntary corporate action with price-discovery, proration,  and per-holder bid audit. Tri-modal: CASH (uniform clearing-price cash buyback via  TenderOfferElection), SECU (clean security-for-security exchange via SecurityOfferElection),  or CASE (security exchange with signed per-unit cash settlement via CashAndSecurityOfferElection).
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **payment_date** | **datetime** | Optional | Settlement date for both the security and cash legs of the auction. |
| **market_deadline_date** | **datetime** | Optional | Issuer or acquirer instruction deadline. |
| **currency** | **str** | Required | Event settlement currency (ISO 4217). |
| **tender_offer_elections** | [List[TenderOfferElection]](TenderOfferElection.md) | Optional | List of possible TenderOfferElections for this event. Populated on the CASH path (Count &#x3D;&#x3D; 1);  empty on the SECU and CASE paths. |
| **security_offer_elections** | [List[SecurityOfferElection]](SecurityOfferElection.md) | Optional | List of possible SecurityOfferElections for this event. Populated on the SECU path (Count &#x3D;&#x3D; 1);  empty on the CASH and CASE paths. |
| **cash_and_security_offer_elections** | [List[CashAndSecurityOfferElection]](CashAndSecurityOfferElection.md) | Optional | List of possible CashAndSecurityOfferElections for this event. Populated on the CASE path  (Count &#x3D;&#x3D; 1); empty on the CASH and SECU paths. |
| **lapse_elections** | [List[LapseElection]](LapseElection.md) | Optional | List of possible LapseElections for this event. Required on all three paths (Count &#x3D;&#x3D; 1).  Allows the holder to opt out of the offer (NOAC). |
| **response_deadline_date** | **datetime** | Optional | Account-servicer response deadline. Defaults to MarketDeadlineDate when not supplied.  When provided, must be on or before MarketDeadlineDate. |
| **early_response_deadline** | **datetime** | Optional | Early-participation deadline. When provided, must be on or before ResponseDeadlineDate. |
| **ex_date** | **datetime** | Optional | The ex date of the event. Optional; carried for cross-event consistency. |
| **record_date** | **datetime** | Optional | The record date of the event. Optional and not required by AMI-SeCo for DTCH  (the event is instruction-driven via QINS, not record-date-driven). |
| **announcement_date** | **datetime** | Optional | Public announcement date of the auction. Optional. |
| **target_quantity** | **float** | Optional | Total quantity of securities sought by the issuer or acquirer. Optional. |
| **proration_rate** | **float** | Optional | Proportional adjustment applied to the security and cash legs on all paths.  Must be in (0, 1]. |
| **new_instrument** | [NewInstrument](NewInstrument.md) | Optional | *No description available.* |
| **fractional_units_cash_price** | **float** | Optional | Cash-in-lieu price per fractional unit on the SECU and CASE paths.  Null indicates round-down disposition of fractional remainders.  Distinct from the CASE path&#39;s main cash settlement (which lives on CashAndSecurityOfferElection). |
| **fractional_units_cash_currency** | **str** | Optional | Currency of the cash-in-lieu paid on fractional remainders on the SECU and CASE paths.  Required when FractionalUnitsCashPrice is non-null. |
| **bid_price** | **float** | Optional | Per-holder bid price submitted at instruction time. Audit-only; no calculation impact. |
| **instrument_event_type** | **str** | Required | The Type of Event. Available values: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent, ConsentEvent, DrawingEvent, CapitalGainsDistributionEvent, ExchangeOfferEvent, DutchAuctionEvent, WorthlessEvent, PutRedemptionEvent, LoanFacilityDelayedCompensationPaymentEvent. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.DutchAuctionEvent import DutchAuctionEvent

instance = DutchAuctionEvent(
    payment_date=datetime.now(),  # optional — Settlement date for both the security and cash legs of the auction.
    market_deadline_date=datetime.now(),  # optional — Issuer or acquirer instruction deadline.
    currency="...",  # required — Event settlement currency (ISO 4217).
    tender_offer_elections=[],  # optional — List of possible TenderOfferElections for this event. Populated on the CASH path (Count &#x3D;&#x3D; 1);  empty on the SECU and CASE paths.
    security_offer_elections=[],  # optional — List of possible SecurityOfferElections for this event. Populated on the SECU path (Count &#x3D;&#x3D; 1);  empty on the CASH and CASE paths.
    cash_and_security_offer_elections=[],  # optional — List of possible CashAndSecurityOfferElections for this event. Populated on the CASE path  (Count &#x3D;&#x3D; 1); empty on the CASH and SECU paths.
    lapse_elections=[],  # optional — List of possible LapseElections for this event. Required on all three paths (Count &#x3D;&#x3D; 1).  Allows the holder to opt out of the offer (NOAC).
    response_deadline_date=datetime.now(),  # optional — Account-servicer response deadline. Defaults to MarketDeadlineDate when not supplied.  When provided, must be on or before MarketDeadlineDate.
    early_response_deadline=datetime.now(),  # optional — Early-participation deadline. When provided, must be on or before ResponseDeadlineDate.
    ex_date=datetime.now(),  # optional — The ex date of the event. Optional; carried for cross-event consistency.
    record_date=datetime.now(),  # optional — The record date of the event. Optional and not required by AMI-SeCo for DTCH  (the event is instruction-driven via QINS, not record-date-driven).
    announcement_date=datetime.now(),  # optional — Public announcement date of the auction. Optional.
    target_quantity=0.0,  # optional — Total quantity of securities sought by the issuer or acquirer. Optional.
    proration_rate=0.0,  # optional — Proportional adjustment applied to the security and cash legs on all paths.  Must be in (0, 1].
    new_instrument=NewInstrument(...),  # optional
    fractional_units_cash_price=0.0,  # optional — Cash-in-lieu price per fractional unit on the SECU and CASE paths.  Null indicates round-down disposition of fractional remainders.  Distinct from the CASE path&#39;s main cash settlement (which lives on CashAndSecurityOfferElection).
    fractional_units_cash_currency="...",  # optional — Currency of the cash-in-lieu paid on fractional remainders on the SECU and CASE paths.  Required when FractionalUnitsCashPrice is non-null.
    bid_price=0.0,  # optional — Per-holder bid price submitted at instruction time. Audit-only; no calculation impact.
    instrument_event_type="..."  # required — The Type of Event. Available values: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent, ConsentEvent, DrawingEvent, CapitalGainsDistributionEvent, ExchangeOfferEvent, DutchAuctionEvent, WorthlessEvent, PutRedemptionEvent, LoanFacilityDelayedCompensationPaymentEvent.
)
```

- [TenderOfferElection](TenderOfferElection.md) — used in `tender_offer_elections`
- [SecurityOfferElection](SecurityOfferElection.md) — used in `security_offer_elections`
- [CashAndSecurityOfferElection](CashAndSecurityOfferElection.md) — used in `cash_and_security_offer_elections`
- [LapseElection](LapseElection.md) — used in `lapse_elections`
- [NewInstrument](NewInstrument.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

