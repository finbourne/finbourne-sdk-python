# PriorityIssueEvent

Priority Issue Event (PRIO) — a voluntary corporate action in which an issuer offers existing  security holders preferential rights to subscribe for new securities at a defined subscription  price before the offer is opened to the wider market. Holders may subscribe up to a basic  entitlement (SECU) and, where offered, apply for additional securities beyond the basic  entitlement (OVER, subject to proration). No instruction (NOAC) results in no transaction.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **announcement_date** | **datetime** | Optional | Date on which the priority issue was announced. Optional, informational. |
| **ex_date** | **datetime** | Optional | First business day on which the security trades without the entitlement. Optional.  When not supplied, transaction-template generation falls back to RecordDate |
| **record_date** | **datetime** | Optional | The entitlement determination date — holders of record on this date are eligible to subscribe. |
| **response_deadline** | **datetime** | Optional | The account-servicer instruction deadline. Must be less than or equal to MarketDeadline. |
| **market_deadline** | **datetime** | Optional | The issuer-agent deadline. |
| **payment_date** | **datetime** | Optional | Date on which cash is debited and the new securities are credited. |
| **security_settlement_date** | **datetime** | Optional | Date the security leg settles when it differs from the cash leg. Optional.  When not supplied, transaction-template generation falls back to PaymentDate |
| **subscription_price** | **float** | Optional | The subscription price per new unit. Applies to both SECU and OVER subscriptions.  Must be greater than zero. |
| **subscription_currency** | **str** | Optional | Currency of the SubscriptionPrice. |
| **new_instrument** | [NewInstrument](NewInstrument.md) | Optional | *No description available.* |
| **proration_rate** | **float** | Optional | The proration rate applied to OVER subscriptions when the offer is oversubscribed.  Treated as 1 (full allocation) when not supplied. Must be greater than 0 and less than  or equal to 1. SECU basic entitlement is never prorated. |
| **fractional_units_cash_price** | **float** | Optional | Price per fractional unit used to compute cash-in-lieu for fractional entitlement remainders.  When not supplied, fractional residuals are discarded with no cash-in-lieu.  Forms an optional pair with FractionalUnitsCashCurrency — both must be supplied together. |
| **fractional_units_cash_currency** | **str** | Optional | Currency of FractionalUnitsCashPrice. Required if and only if FractionalUnitsCashPrice is supplied. |
| **security_offer_elections** | [List[SecurityOfferElection]](SecurityOfferElection.md) | Optional | Security offer elections — exactly one entry keyed &#39;SECU&#39; (basic entitlement) and an optional  entry keyed &#39;OVER&#39; (over-subscription) when the issuer offers the over-subscription facility. |
| **lapse_elections** | [List[LapseElection]](LapseElection.md) | Optional | Lapse elections — exactly one entry keyed &#39;NOAC&#39;, recording the holder&#39;s explicit no-action election. |
| **instrument_event_type** | **str** | Required | The Type of Event. Available values: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent, ConsentEvent, DrawingEvent, CapitalGainsDistributionEvent, ExchangeOfferEvent, DutchAuctionEvent, WorthlessEvent, PutRedemptionEvent, LoanFacilityDelayedCompensationPaymentEvent, InterestPaymentEvent, PriorityIssueEvent. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PriorityIssueEvent import PriorityIssueEvent

instance = PriorityIssueEvent(
    announcement_date=datetime.now(),  # optional — Date on which the priority issue was announced. Optional, informational.
    ex_date=datetime.now(),  # optional — First business day on which the security trades without the entitlement. Optional.  When not supplied, transaction-template generation falls back to RecordDate
    record_date=datetime.now(),  # optional — The entitlement determination date — holders of record on this date are eligible to subscribe.
    response_deadline=datetime.now(),  # optional — The account-servicer instruction deadline. Must be less than or equal to MarketDeadline.
    market_deadline=datetime.now(),  # optional — The issuer-agent deadline.
    payment_date=datetime.now(),  # optional — Date on which cash is debited and the new securities are credited.
    security_settlement_date=datetime.now(),  # optional — Date the security leg settles when it differs from the cash leg. Optional.  When not supplied, transaction-template generation falls back to PaymentDate
    subscription_price=0.0,  # optional — The subscription price per new unit. Applies to both SECU and OVER subscriptions.  Must be greater than zero.
    subscription_currency="...",  # optional — Currency of the SubscriptionPrice.
    new_instrument=NewInstrument(...),  # optional
    proration_rate=0.0,  # optional — The proration rate applied to OVER subscriptions when the offer is oversubscribed.  Treated as 1 (full allocation) when not supplied. Must be greater than 0 and less than  or equal to 1. SECU basic entitlement is never prorated.
    fractional_units_cash_price=0.0,  # optional — Price per fractional unit used to compute cash-in-lieu for fractional entitlement remainders.  When not supplied, fractional residuals are discarded with no cash-in-lieu.  Forms an optional pair with FractionalUnitsCashCurrency — both must be supplied together.
    fractional_units_cash_currency="...",  # optional — Currency of FractionalUnitsCashPrice. Required if and only if FractionalUnitsCashPrice is supplied.
    security_offer_elections=[],  # optional — Security offer elections — exactly one entry keyed &#39;SECU&#39; (basic entitlement) and an optional  entry keyed &#39;OVER&#39; (over-subscription) when the issuer offers the over-subscription facility.
    lapse_elections=[],  # optional — Lapse elections — exactly one entry keyed &#39;NOAC&#39;, recording the holder&#39;s explicit no-action election.
    instrument_event_type="..."  # required — The Type of Event. Available values: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent, ConsentEvent, DrawingEvent, CapitalGainsDistributionEvent, ExchangeOfferEvent, DutchAuctionEvent, WorthlessEvent, PutRedemptionEvent, LoanFacilityDelayedCompensationPaymentEvent, InterestPaymentEvent, PriorityIssueEvent.
)
```

- [NewInstrument](NewInstrument.md)
- [SecurityOfferElection](SecurityOfferElection.md) — used in `security_offer_elections`
- [LapseElection](LapseElection.md) — used in `lapse_elections`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

