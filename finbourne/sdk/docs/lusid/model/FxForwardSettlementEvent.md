# FxForwardSettlementEvent

Settlement for FX Forward, including NDF and deliverable.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **maturity_date** | **datetime** | Optional | Maturity date of the forward |
| **dom_amount_per_unit** | **float** | Required | Amount per unit in the DomCcy (domestic currency) |
| **dom_ccy** | **str** | Required | The domestic currency of the forward |
| **fgn_amount_per_unit** | **float** | Required | Amount per unit in the FgnCcy (foreign currency) |
| **fgn_ccy** | **str** | Required | The foreign currency of the forward. |
| **is_ndf** | **bool** | Required | Is this settlement corresponding to a deliverable forward, or an NDF |
| **fixing_date** | **datetime** | Optional | Optional.  Required if the event is an NDF (i.e. if IsNdf &#x3D; true).  Date of the FxRate fixings. |
| **settlement_ccy** | **str** | Optional | Optional.  Required if the event is an NDF (i.e. if IsNdf &#x3D; true).  May be set to either DomCcy or FgnCcy, or a third currency. |
| **cash_flow_per_unit** | **float** | Optional | Optional.  Required if the event is an NDF (i.e. if IsNdf &#x3D; true).  CashFlow per unit.  Paid in the SettlementCcy. |
| **domestic_to_foreign_rate** | **float** | Optional | Domestic currency to foreign currency FX rate.  Not required, only used to override quotes. |
| **domestic_to_settlement_rate** | **float** | Optional | Domestic currency to settlement currency FX rate  Not required, only used to override quotes. |
| **foreign_to_settlement_rate** | **float** | Optional | Foreign currency to settlement currency FX rate  Not required, only used to override quotes. *(read-only)* |
| **instrument_event_type** | **str** | Required | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FxForwardSettlementEvent import FxForwardSettlementEvent

instance = FxForwardSettlementEvent(
    maturity_date=datetime.now(),  # optional — Maturity date of the forward
    dom_amount_per_unit=0.0,  # required — Amount per unit in the DomCcy (domestic currency)
    dom_ccy="...",  # required — The domestic currency of the forward
    fgn_amount_per_unit=0.0,  # required — Amount per unit in the FgnCcy (foreign currency)
    fgn_ccy="...",  # required — The foreign currency of the forward.
    is_ndf=True,  # required — Is this settlement corresponding to a deliverable forward, or an NDF
    fixing_date=datetime.now(),  # optional — Optional.  Required if the event is an NDF (i.e. if IsNdf &#x3D; true).  Date of the FxRate fixings.
    settlement_ccy="...",  # optional — Optional.  Required if the event is an NDF (i.e. if IsNdf &#x3D; true).  May be set to either DomCcy or FgnCcy, or a third currency.
    cash_flow_per_unit=0.0,  # optional — Optional.  Required if the event is an NDF (i.e. if IsNdf &#x3D; true).  CashFlow per unit.  Paid in the SettlementCcy.
    domestic_to_foreign_rate=0.0,  # optional — Domestic currency to foreign currency FX rate.  Not required, only used to override quotes.
    domestic_to_settlement_rate=0.0,  # optional — Domestic currency to settlement currency FX rate  Not required, only used to override quotes.
    foreign_to_settlement_rate=0.0,  # optional — Foreign currency to settlement currency FX rate  Not required, only used to override quotes.
    instrument_event_type="..."  # required — The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

