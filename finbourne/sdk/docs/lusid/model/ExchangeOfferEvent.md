# ExchangeOfferEvent

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **effective_date** | **datetime** | Optional | *No description available.* |
| **settlement_date** | **datetime** | Optional | *No description available.* |
| **event_source** | **str** | Required | *No description available.* |
| **new_instrument** | [NewInstrument](NewInstrument.md) | Optional | *No description available.* |
| **cash_offer_elections** | [List[CashOfferElection]](CashOfferElection.md) | Optional | *No description available.* |
| **security_offer_elections** | [List[SecurityOfferElection]](SecurityOfferElection.md) | Optional | *No description available.* |
| **mixed_lot_constituents_elections** | [List[MixedLotConstituentsElection]](MixedLotConstituentsElection.md) | Optional | *No description available.* |
| **lapse_elections** | [List[LapseElection]](LapseElection.md) | Optional | *No description available.* |
| **min_piece_size** | **float** | Optional | *No description available.* |
| **min_increment** | **float** | Optional | *No description available.* |
| **fractional_units_cash_price** | **float** | Optional | *No description available.* |
| **fractional_units_cash_currency** | **str** | Optional | *No description available.* |
| **instruction_reference** | **str** | Optional | *No description available.* |
| **instrument_event_type** | **str** | Required | The Type of Event. Available values: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent, ConsentEvent, DrawingEvent, CapitalGainsDistributionEvent, ExchangeOfferEvent. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ExchangeOfferEvent import ExchangeOfferEvent

instance = ExchangeOfferEvent(
    effective_date=datetime.now(),  # optional
    settlement_date=datetime.now(),  # optional
    event_source="...",  # required
    new_instrument=NewInstrument(...),  # optional
    cash_offer_elections=[],  # optional
    security_offer_elections=[],  # optional
    mixed_lot_constituents_elections=[],  # optional
    lapse_elections=[],  # optional
    min_piece_size=0.0,  # optional
    min_increment=0.0,  # optional
    fractional_units_cash_price=0.0,  # optional
    fractional_units_cash_currency="...",  # optional
    instruction_reference="...",  # optional
    instrument_event_type="..."  # required — The Type of Event. Available values: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent, ConsentEvent, DrawingEvent, CapitalGainsDistributionEvent, ExchangeOfferEvent.
)
```

- [NewInstrument](NewInstrument.md)
- [CashOfferElection](CashOfferElection.md)
- [SecurityOfferElection](SecurityOfferElection.md)
- [MixedLotConstituentsElection](MixedLotConstituentsElection.md)
- [LapseElection](LapseElection.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

