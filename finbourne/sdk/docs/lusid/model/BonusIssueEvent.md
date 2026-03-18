# BonusIssueEvent

Representation of a Bonus Issue corporate action.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **announcement_date** | **datetime** | Optional | The date the Bonus Issue is announced. |
| **ex_date** | **datetime** | Optional | The ex-date of the Bonus Issue. |
| **record_date** | **datetime** | Optional | The record date of the Bonus Issue. |
| **payment_date** | **datetime** | Optional | The date the Bonus Issue is executed. |
| **fractional_units_cash_price** | **float** | Optional | Optional. Used in calculating cash-in-lieu of fractional shares. |
| **fractional_units_cash_currency** | **str** | Optional | Optional. Used in calculating cash-in-lieu of fractional shares. |
| **security_offer_elections** | [List[SecurityOfferElection]](SecurityOfferElection.md) | Optional | Possible SecurityElections for this Bonus Issue event, if any. |
| **cash_offer_elections** | [List[CashOfferElection]](CashOfferElection.md) | Optional | Possible CashOfferElections for this Bonus Issue event, if any. |
| **lapse_elections** | [List[LapseElection]](LapseElection.md) | Optional | Possible LapseElections for this Bonus Issue event, if any. |
| **instrument_event_type** | **str** | Required | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.BonusIssueEvent import BonusIssueEvent

instance = BonusIssueEvent(
    announcement_date=datetime.now(),  # optional — The date the Bonus Issue is announced.
    ex_date=datetime.now(),  # optional — The ex-date of the Bonus Issue.
    record_date=datetime.now(),  # optional — The record date of the Bonus Issue.
    payment_date=datetime.now(),  # optional — The date the Bonus Issue is executed.
    fractional_units_cash_price=0.0,  # optional — Optional. Used in calculating cash-in-lieu of fractional shares.
    fractional_units_cash_currency="...",  # optional — Optional. Used in calculating cash-in-lieu of fractional shares.
    security_offer_elections=[],  # optional — Possible SecurityElections for this Bonus Issue event, if any.
    cash_offer_elections=[],  # optional — Possible CashOfferElections for this Bonus Issue event, if any.
    lapse_elections=[],  # optional — Possible LapseElections for this Bonus Issue event, if any.
    instrument_event_type="..."  # required — The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent
)
```

- [SecurityOfferElection](SecurityOfferElection.md) — used in `security_offer_elections`
- [CashOfferElection](CashOfferElection.md) — used in `cash_offer_elections`
- [LapseElection](LapseElection.md) — used in `lapse_elections`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

