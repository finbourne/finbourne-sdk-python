# MergerEvent

Merger Event (MRGR).
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **announcement_date** | **datetime** | Optional | The date the merger is announced. |
| **cash_and_security_offer_elections** | [List[CashAndSecurityOfferElection]](CashAndSecurityOfferElection.md) | Optional | List of possible CashAndSecurityOfferElections for this merger event |
| **cash_offer_elections** | [List[CashOfferElection]](CashOfferElection.md) | Optional | List of possible CashOfferElections for this merger event |
| **ex_date** | **datetime** | Optional | The first date on which the holder of record of the original shares has entitled ownership of the new shares. |
| **fractional_units_cash_currency** | **str** | Optional | Optional. Used in calculating cash-in-lieu of fractional shares. |
| **fractional_units_cash_price** | **float** | Optional | Optional. Used in calculating cash-in-lieu of fractional shares. |
| **new_instrument** | [NewInstrument](NewInstrument.md) | Required | *No description available.* |
| **payment_date** | **datetime** | Optional | Date on which the merger takes place. |
| **record_date** | **datetime** | Optional | Optional. Date you have to be the holder of record of the original shares in order to receive the new shares. |
| **security_offer_elections** | [List[SecurityOfferElection]](SecurityOfferElection.md) | Optional | List of possible SecurityOfferElections for this merger event |
| **instrument_event_type** | **str** | Required | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.MergerEvent import MergerEvent

instance = MergerEvent(
    announcement_date=datetime.now(),  # optional — The date the merger is announced.
    cash_and_security_offer_elections=[],  # optional — List of possible CashAndSecurityOfferElections for this merger event
    cash_offer_elections=[],  # optional — List of possible CashOfferElections for this merger event
    ex_date=datetime.now(),  # optional — The first date on which the holder of record of the original shares has entitled ownership of the new shares.
    fractional_units_cash_currency="...",  # optional — Optional. Used in calculating cash-in-lieu of fractional shares.
    fractional_units_cash_price=0.0,  # optional — Optional. Used in calculating cash-in-lieu of fractional shares.
    new_instrument=NewInstrument(...),  # required
    payment_date=datetime.now(),  # optional — Date on which the merger takes place.
    record_date=datetime.now(),  # optional — Optional. Date you have to be the holder of record of the original shares in order to receive the new shares.
    security_offer_elections=[],  # optional — List of possible SecurityOfferElections for this merger event
    instrument_event_type="..."  # required — The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent
)
```

- [CashAndSecurityOfferElection](CashAndSecurityOfferElection.md) — used in `cash_and_security_offer_elections`
- [CashOfferElection](CashOfferElection.md) — used in `cash_offer_elections`
- [NewInstrument](NewInstrument.md)
- [SecurityOfferElection](SecurityOfferElection.md) — used in `security_offer_elections`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

