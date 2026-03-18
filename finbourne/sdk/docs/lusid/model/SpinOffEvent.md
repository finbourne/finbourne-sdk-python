# SpinOffEvent

Spin-off event (SOFF), representing the distribution of securities issued by another company.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **announcement_date** | **datetime** | Optional | Optional.  The date the spin-off is announced. |
| **ex_date** | **datetime** | Optional | The first date on which the holder of record has entitled ownership of the new shares. |
| **record_date** | **datetime** | Optional | Optional.  Date you have to be the holder of record in order to receive the additional shares. |
| **payment_date** | **datetime** | Optional | Date on which the distribution of shares takes place. |
| **new_instrument** | [NewInstrument](NewInstrument.md) | Required | *No description available.* |
| **units_ratio** | [UnitsRatio](UnitsRatio.md) | Required | *No description available.* |
| **cost_factor** | **float** | Optional | Optional. The fraction of cost that is transferred from the existing shares to the new shares. |
| **fractional_units_cash_price** | **float** | Optional | Optional. Used in calculating cash-in-lieu of fractional shares. |
| **fractional_units_cash_currency** | **str** | Optional | Optional. Used in calculating cash-in-lieu of fractional shares. |
| **instrument_event_type** | **str** | Required | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.SpinOffEvent import SpinOffEvent

instance = SpinOffEvent(
    announcement_date=datetime.now(),  # optional — Optional.  The date the spin-off is announced.
    ex_date=datetime.now(),  # optional — The first date on which the holder of record has entitled ownership of the new shares.
    record_date=datetime.now(),  # optional — Optional.  Date you have to be the holder of record in order to receive the additional shares.
    payment_date=datetime.now(),  # optional — Date on which the distribution of shares takes place.
    new_instrument=NewInstrument(...),  # required
    units_ratio=UnitsRatio(...),  # required
    cost_factor=0.0,  # optional — Optional. The fraction of cost that is transferred from the existing shares to the new shares.
    fractional_units_cash_price=0.0,  # optional — Optional. Used in calculating cash-in-lieu of fractional shares.
    fractional_units_cash_currency="...",  # optional — Optional. Used in calculating cash-in-lieu of fractional shares.
    instrument_event_type="..."  # required — The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent
)
```

- [NewInstrument](NewInstrument.md)
- [UnitsRatio](UnitsRatio.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

