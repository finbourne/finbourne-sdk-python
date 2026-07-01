# PartialDefeasanceEvent

Partial Defeasance event (PDEF). A mandatory notification that a bond issuer has escrow-funded  (defeased) a portion of an outstanding issue. No cash flows to holders at this event; the position  is marked pre-refunded and its effective maturity is updated to the future call date carried in  ActualPayDate. The actual cash and position retirement arrive later via a separate  mandatory call event. Supports a Partial Pre-Refunding variant (PPRE).
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **refunded_fraction** | **float** | Required | The issue-level fraction allocated to the refunded (pre-refunded / escrowed) portion. Strictly  in the half-open interval (0, 1]; the non-refunded fraction is the derived complement. This is a  required field. |
| **effective_date** | **datetime** | Optional | The date the defeasance status takes effect on the position. This is a required field. |
| **actual_pay_date** | **datetime** | Optional | The future call date when the bond will actually be retired, used to update the position&#39;s  effective maturity in analytics. Must be on or after EffectiveDate. This is a  required field. |
| **refunded_instrument** | [NewInstrument](NewInstrument.md) | Optional | *No description available.* |
| **new_securities_indicator** | **str** | Optional | Optional audit field preserving the wire-side codeword used for the refunded portion.  Supported string (enumeration) values are: [REFU, DEFE]. Both encodings carry identical semantics. Available values: REFU, DEFE. |
| **additional_business_process** | **str** | Optional | Optional variant indicator. Supported string (enumeration) values are: [PPRE]. Absence (null)  encodes the default Partial Defeasance variant. Available values: PPRE. |
| **lottery_date** | **datetime** | Optional | Optional. The wire&#39;s lottery date; null when the wire carried a sentinel value. |
| **publication_date** | **datetime** | Optional | Optional informational date identifying when the defeasance was publicly noticed. |
| **record_date** | **datetime** | Optional | Optional. The wire&#39;s record date; typically null for a notification event with no distribution. |
| **announcement_date** | **datetime** | Optional | Optional informational announcement date; null when not provided. |
| **instrument_event_type** | **str** | Required | The Type of Event. Available values: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent, ConsentEvent, DrawingEvent, CapitalGainsDistributionEvent, ExchangeOfferEvent, DutchAuctionEvent, WorthlessEvent, PutRedemptionEvent, LoanFacilityDelayedCompensationPaymentEvent, InterestPaymentEvent, PriorityIssueEvent, ClassActionEvent, BankruptcyEvent, LiquidationPaymentEvent, PartialDefeasanceEvent. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PartialDefeasanceEvent import PartialDefeasanceEvent

instance = PartialDefeasanceEvent(
    refunded_fraction=0.0,  # required — The issue-level fraction allocated to the refunded (pre-refunded / escrowed) portion. Strictly  in the half-open interval (0, 1]; the non-refunded fraction is the derived complement. This is a  required field.
    effective_date=datetime.now(),  # optional — The date the defeasance status takes effect on the position. This is a required field.
    actual_pay_date=datetime.now(),  # optional — The future call date when the bond will actually be retired, used to update the position&#39;s  effective maturity in analytics. Must be on or after EffectiveDate. This is a  required field.
    refunded_instrument=NewInstrument(...),  # optional
    new_securities_indicator="...",  # optional — Optional audit field preserving the wire-side codeword used for the refunded portion.  Supported string (enumeration) values are: [REFU, DEFE]. Both encodings carry identical semantics. Available values: REFU, DEFE.
    additional_business_process="...",  # optional — Optional variant indicator. Supported string (enumeration) values are: [PPRE]. Absence (null)  encodes the default Partial Defeasance variant. Available values: PPRE.
    lottery_date=datetime.now(),  # optional — Optional. The wire&#39;s lottery date; null when the wire carried a sentinel value.
    publication_date=datetime.now(),  # optional — Optional informational date identifying when the defeasance was publicly noticed.
    record_date=datetime.now(),  # optional — Optional. The wire&#39;s record date; typically null for a notification event with no distribution.
    announcement_date=datetime.now(),  # optional — Optional informational announcement date; null when not provided.
    instrument_event_type="..."  # required — The Type of Event. Available values: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent, ConsentEvent, DrawingEvent, CapitalGainsDistributionEvent, ExchangeOfferEvent, DutchAuctionEvent, WorthlessEvent, PutRedemptionEvent, LoanFacilityDelayedCompensationPaymentEvent, InterestPaymentEvent, PriorityIssueEvent, ClassActionEvent, BankruptcyEvent, LiquidationPaymentEvent, PartialDefeasanceEvent.
)
```

- [NewInstrument](NewInstrument.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

