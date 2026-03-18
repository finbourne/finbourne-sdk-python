# LoanPrincipalRepaymentEvent

Event to signify the repayment of some or all of the principal balance of a loan contract.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **payment_date** | **datetime** | Optional | Date that the Principal is due to be paid. |
| **currency** | **str** | Required | Currency of the repayment. |
| **lapse_elections** | [List[LapseElection]](LapseElection.md) | Optional | Election for controlling whether the Principal is paid automatically or not.  Exactly one election must be provided. |
| **fraction** | **float** | Optional | Fraction of the outstanding settled principal balance to be repaid. Must be between 0 and 1, inclusive.  Defaults to 1 if not set. Ignored if the field Amount is set to a value different than zero. |
| **amount** | **float** | Optional | Amount to be repaid (independent of the fraction).  This field is not used at all if not set or set to 0, in this case the fraction field will be used instead.  Otherwise, the fraction field is ignored. |
| **with_interest** | **bool** | Optional | If set to true, then active contracts whose balance is reduced by the repayment will have  their accrued interest repaid proportionally to the balance reduction. |
| **instrument_event_type** | **str** | Required | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.LoanPrincipalRepaymentEvent import LoanPrincipalRepaymentEvent

instance = LoanPrincipalRepaymentEvent(
    payment_date=datetime.now(),  # optional — Date that the Principal is due to be paid.
    currency="...",  # required — Currency of the repayment.
    lapse_elections=[],  # optional — Election for controlling whether the Principal is paid automatically or not.  Exactly one election must be provided.
    fraction=0.0,  # optional — Fraction of the outstanding settled principal balance to be repaid. Must be between 0 and 1, inclusive.  Defaults to 1 if not set. Ignored if the field Amount is set to a value different than zero.
    amount=0.0,  # optional — Amount to be repaid (independent of the fraction).  This field is not used at all if not set or set to 0, in this case the fraction field will be used instead.  Otherwise, the fraction field is ignored.
    with_interest=True,  # optional — If set to true, then active contracts whose balance is reduced by the repayment will have  their accrued interest repaid proportionally to the balance reduction.
    instrument_event_type="..."  # required — The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent
)
```

- [LapseElection](LapseElection.md) — used in `lapse_elections`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

