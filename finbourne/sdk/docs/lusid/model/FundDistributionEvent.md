# FundDistributionEvent

A distribution from the fund to the holder of a CapitalInterest. A recallable distribution restores  unfunded capital (the fund may call it again); a non-recallable distribution permanently returns capital.                The total amount may optionally be broken down into slots by character (returnOfCapital, realisedGain,  dividend, interest, otherIncome, carryPaid, withholding, returnOfExcess). When any slot amount is supplied  the slot amounts must sum to the total, one transaction is booked per populated slot, and the recallable  portion of each of the five capital/income characters is given by its matching Recallable amount.  Without slots a single legacy distribution transaction is booked for the total, recallable according  to isRecallable.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **var_date** | **datetime** | Optional | The date the distribution takes effect. |
| **amount** | **float** | Required | The total amount distributed. Must be positive. When slot amounts are supplied they must sum to this total. |
| **is_recallable** | **bool** | Optional | Legacy flag, used only when no slot amount is supplied: true when the fund may recall the whole  distributed amount, so the distribution restores unfunded capital rather than permanently returning  it. Defaults to false. Must not be combined with slot amounts. |
| **return_of_capital_amount** | **float** | Optional | The part of the distribution that returns capital. Optional slot; must not be negative. |
| **realised_gain_amount** | **float** | Optional | The part of the distribution that is realised gain. Optional slot; must not be negative. |
| **dividend_amount** | **float** | Optional | The part of the distribution that is dividend income. Optional slot; must not be negative. |
| **interest_amount** | **float** | Optional | The part of the distribution that is interest income. Optional slot; must not be negative. |
| **other_income_amount** | **float** | Optional | The part of the distribution that is other income. Optional slot; must not be negative. |
| **return_of_capital_recallable_amount** | **float** | Optional | The recallable portion of returnOfCapitalAmount. Optional; must not exceed returnOfCapitalAmount. |
| **realised_gain_recallable_amount** | **float** | Optional | The recallable portion of realisedGainAmount. Optional; must not exceed realisedGainAmount. |
| **dividend_recallable_amount** | **float** | Optional | The recallable portion of dividendAmount. Optional; must not exceed dividendAmount. |
| **interest_recallable_amount** | **float** | Optional | The recallable portion of interestAmount. Optional; must not exceed interestAmount. |
| **other_income_recallable_amount** | **float** | Optional | The recallable portion of otherIncomeAmount. Optional; must not exceed otherIncomeAmount. |
| **carry_paid_amount** | **float** | Optional | The part of the distribution that is carried interest paid to the general partner. Optional slot; must not be negative. |
| **withholding_amount** | **float** | Optional | The part of the distribution withheld for tax (a deemed distribution). Optional slot; must not be negative. |
| **return_of_excess_amount** | **float** | Optional | The part of the distribution that returns capital called in excess. Optional slot; must not be negative. |
| **recallable_until** | **datetime** | Optional | The date until which the recallable portions may be recalled, if limited. Must not precede the distribution date. |
| **deal_id** | **str** | Optional | The identifier of the deal the distribution relates to, if any. |
| **allocation_event_id** | **str** | Optional | The identifier of the allocation event the distribution relates to, if any. |
| **waterfall_tier** | **str** | Optional | The waterfall tier the distribution was paid under, if any. |
| **instrument_event_type** | **str** | Required | The Type of Event. Available values: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent, ConsentEvent, DrawingEvent, CapitalGainsDistributionEvent, ExchangeOfferEvent, DutchAuctionEvent, WorthlessEvent, PutRedemptionEvent, LoanFacilityDelayedCompensationPaymentEvent, InterestPaymentEvent, PriorityIssueEvent, ClassActionEvent, BankruptcyEvent, LiquidationPaymentEvent, PartialDefeasanceEvent, SecurityWriteOffEvent, WarrantsExerciseEvent, PariPassuEvent, ChangeEvent, PikBondCouponEvent, PikBondCashCouponEvent, PikBondInterestCapitalisationEvent, PikBondPrincipalEvent, DelistingEvent, PikBondInterestEvent, CommodityForwardCashSettlementEvent, PaymentInKindEvent, CommodityForwardPhysicalSettlementEvent, CancelSwapEvent, BondOptionTerminationEvent, TerminationEvent, CommodityCalendarSwapCashFlowEvent, DepositSweepEvent, BondForwardCashSettlementEvent, BondForwardTerminationEvent, AmendCommitmentEvent, CapitalCallEvent, FundDistributionEvent, NavReportEvent, DividendSuspensionEvent, LoanInterestCapitalisationEvent, TotalReturnSwapCashFlowEvent, GlobalLoanFacilityReinitialisationEvent, InvestorLoanFacilityReinitialisationEvent, CapitalCallReceiptEvent, RecallableCapitalExpiryEvent, CapitalInterestTransferEvent, FacilityDrawEvent, FacilityRepaymentEvent, FacilityInterestEvent, FacilityCommitmentFeeEvent, InstalmentCallEvent, DepositInterestCapitalisationEvent. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FundDistributionEvent import FundDistributionEvent

instance = FundDistributionEvent(
    var_date=datetime.now(),  # optional — The date the distribution takes effect.
    amount=0.0,  # required — The total amount distributed. Must be positive. When slot amounts are supplied they must sum to this total.
    is_recallable=True,  # optional — Legacy flag, used only when no slot amount is supplied: true when the fund may recall the whole  distributed amount, so the distribution restores unfunded capital rather than permanently returning  it. Defaults to false. Must not be combined with slot amounts.
    return_of_capital_amount=0.0,  # optional — The part of the distribution that returns capital. Optional slot; must not be negative.
    realised_gain_amount=0.0,  # optional — The part of the distribution that is realised gain. Optional slot; must not be negative.
    dividend_amount=0.0,  # optional — The part of the distribution that is dividend income. Optional slot; must not be negative.
    interest_amount=0.0,  # optional — The part of the distribution that is interest income. Optional slot; must not be negative.
    other_income_amount=0.0,  # optional — The part of the distribution that is other income. Optional slot; must not be negative.
    return_of_capital_recallable_amount=0.0,  # optional — The recallable portion of returnOfCapitalAmount. Optional; must not exceed returnOfCapitalAmount.
    realised_gain_recallable_amount=0.0,  # optional — The recallable portion of realisedGainAmount. Optional; must not exceed realisedGainAmount.
    dividend_recallable_amount=0.0,  # optional — The recallable portion of dividendAmount. Optional; must not exceed dividendAmount.
    interest_recallable_amount=0.0,  # optional — The recallable portion of interestAmount. Optional; must not exceed interestAmount.
    other_income_recallable_amount=0.0,  # optional — The recallable portion of otherIncomeAmount. Optional; must not exceed otherIncomeAmount.
    carry_paid_amount=0.0,  # optional — The part of the distribution that is carried interest paid to the general partner. Optional slot; must not be negative.
    withholding_amount=0.0,  # optional — The part of the distribution withheld for tax (a deemed distribution). Optional slot; must not be negative.
    return_of_excess_amount=0.0,  # optional — The part of the distribution that returns capital called in excess. Optional slot; must not be negative.
    recallable_until=datetime.now(),  # optional — The date until which the recallable portions may be recalled, if limited. Must not precede the distribution date.
    deal_id="...",  # optional — The identifier of the deal the distribution relates to, if any.
    allocation_event_id="...",  # optional — The identifier of the allocation event the distribution relates to, if any.
    waterfall_tier="...",  # optional — The waterfall tier the distribution was paid under, if any.
    instrument_event_type="..."  # required — The Type of Event. Available values: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent, ConsentEvent, DrawingEvent, CapitalGainsDistributionEvent, ExchangeOfferEvent, DutchAuctionEvent, WorthlessEvent, PutRedemptionEvent, LoanFacilityDelayedCompensationPaymentEvent, InterestPaymentEvent, PriorityIssueEvent, ClassActionEvent, BankruptcyEvent, LiquidationPaymentEvent, PartialDefeasanceEvent, SecurityWriteOffEvent, WarrantsExerciseEvent, PariPassuEvent, ChangeEvent, PikBondCouponEvent, PikBondCashCouponEvent, PikBondInterestCapitalisationEvent, PikBondPrincipalEvent, DelistingEvent, PikBondInterestEvent, CommodityForwardCashSettlementEvent, PaymentInKindEvent, CommodityForwardPhysicalSettlementEvent, CancelSwapEvent, BondOptionTerminationEvent, TerminationEvent, CommodityCalendarSwapCashFlowEvent, DepositSweepEvent, BondForwardCashSettlementEvent, BondForwardTerminationEvent, AmendCommitmentEvent, CapitalCallEvent, FundDistributionEvent, NavReportEvent, DividendSuspensionEvent, LoanInterestCapitalisationEvent, TotalReturnSwapCashFlowEvent, GlobalLoanFacilityReinitialisationEvent, InvestorLoanFacilityReinitialisationEvent, CapitalCallReceiptEvent, RecallableCapitalExpiryEvent, CapitalInterestTransferEvent, FacilityDrawEvent, FacilityRepaymentEvent, FacilityInterestEvent, FacilityCommitmentFeeEvent, InstalmentCallEvent, DepositInterestCapitalisationEvent.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

