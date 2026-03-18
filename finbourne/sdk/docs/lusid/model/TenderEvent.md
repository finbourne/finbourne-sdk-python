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
| **instrument_event_type** | **str** | Required | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent |


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
    instrument_event_type="..."  # required — The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent
)
```

- [NewInstrument](NewInstrument.md)
- [SecurityOfferElection](SecurityOfferElection.md) — used in `security_offer_elections`
- [CashAndSecurityOfferElection](CashAndSecurityOfferElection.md) — used in `cash_and_security_offer_elections`
- [CashOfferElection](CashOfferElection.md) — used in `cash_offer_elections`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

