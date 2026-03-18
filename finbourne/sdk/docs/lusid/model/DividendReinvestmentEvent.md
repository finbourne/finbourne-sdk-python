# DividendReinvestmentEvent

Event for dividend reinvestments.  Elections for cash or the associated security.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **announcement_date** | **datetime** | Optional | Date on which the dividend was announced / declared. |
| **cash_elections** | [List[CashElection]](CashElection.md) | Required | CashElection for this DividendReinvestmentEvent |
| **ex_date** | **datetime** | Optional | The first business day on which the dividend is not owed to the buying party.  Typically this is T-1 from the RecordDate. |
| **payment_date** | **datetime** | Optional | The date the company pays out dividends to shareholders. |
| **record_date** | **datetime** | Optional | Date you have to be the holder of record in order to participate in the tender. |
| **security_elections** | [List[SecurityElection]](SecurityElection.md) | Required | SecurityElection for this DividendReinvestmentEvent |
| **security_settlement_date** | **datetime** | Optional | The settlement date of the additional units.  Equal to the PaymentDate if not provided. |
| **instrument_event_type** | **str** | Required | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.DividendReinvestmentEvent import DividendReinvestmentEvent

instance = DividendReinvestmentEvent(
    announcement_date=datetime.now(),  # optional — Date on which the dividend was announced / declared.
    cash_elections=[],  # required — CashElection for this DividendReinvestmentEvent
    ex_date=datetime.now(),  # optional — The first business day on which the dividend is not owed to the buying party.  Typically this is T-1 from the RecordDate.
    payment_date=datetime.now(),  # optional — The date the company pays out dividends to shareholders.
    record_date=datetime.now(),  # optional — Date you have to be the holder of record in order to participate in the tender.
    security_elections=[],  # required — SecurityElection for this DividendReinvestmentEvent
    security_settlement_date=datetime.now(),  # optional — The settlement date of the additional units.  Equal to the PaymentDate if not provided.
    instrument_event_type="..."  # required — The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent
)
```

- [CashElection](CashElection.md) — used in `cash_elections`
- [SecurityElection](SecurityElection.md) — used in `security_elections`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

