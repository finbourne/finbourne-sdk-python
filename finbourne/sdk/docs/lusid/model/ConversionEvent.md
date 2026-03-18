# ConversionEvent

Conversion Event (CONV) - Conversion of securities (generally convertible bonds or preferred shares) into  another form of securities (usually common shares) at a pre-stated price/ratio.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **record_date** | **datetime** | Optional | Required.  Date at which positions are struck at the end of the day to  note which parties will receive the relevant amount of  entitlement, due to be distributed on the PaymentDate. |
| **payment_date** | **datetime** | Optional | Required. Date on which the movement is due to take place (cash and/or securities). |
| **new_instrument** | [NewInstrument](NewInstrument.md) | Required | *No description available.* |
| **response_deadline_date** | **datetime** | Optional | Date/time that the account servicer has set as the deadline to respond,  with instructions, to an outstanding event. Not required. |
| **market_deadline_date** | **datetime** | Optional | Date/time which the issuer or issuer&#39;s agent has set as the deadline to respond,  with an instruction, to an outstanding offer or privilege. Not required. |
| **period_of_action** | [EventDateRange](EventDateRange.md) | Optional | *No description available.* |
| **fractional_units_cash_price** | **float** | Optional | The cash price paid in lieu of fractionalUnits. Not required.  If provided, must have FractionalUnitsCashCurrency too. |
| **fractional_units_cash_currency** | **str** | Optional | Optional. Used in calculating cash-in-lieu of fractional shares. Not required.  If provided, must have FractionalUnitsCashPrice too. |
| **security_offer_elections** | [List[SecurityOfferElection]](SecurityOfferElection.md) | Optional | List of possible security offers for this conversion event. There must be at most one election of this type.    If the ParticipationType is Mandatory:     This list must have exactly one election that is chosen and default.  CashAndSecurityOfferElections and CashOfferElections &lt;b&gt; must be null or empty&lt;/b&gt;.     If the ParticipationType is Voluntary:     This list can be empty,  so long as CashAndSecurityOfferElections or CashOfferElections  has at least one election. None of these elections have to be chosen or default. |
| **cash_and_security_offer_elections** | [List[CashAndSecurityOfferElection]](CashAndSecurityOfferElection.md) | Optional | List of possible cash and security offers for this conversion event. There must be at most one election of this type.    If the ParticipationType is Mandatory:    This list &lt;b&gt; must be null or empty&lt;/b&gt;.    If the ParticipationType is Voluntary:    This list can be empty,  so long as SecurityOfferElections or CashOfferElections  has at least one election. None of these elections have to be chosen or default. |
| **cash_offer_elections** | [List[CashOfferElection]](CashOfferElection.md) | Optional | List of possible cash offers for this conversion event. There must be at most one election of this type.    If the ParticipationType is Mandatory:    This list &lt;b&gt; must be null or empty&lt;/b&gt;.    If the ParticipationType is Voluntary:    This list can be empty,  so long as SecurityOfferElections or CashAndSecurityOfferElections  has at least one election. None of these elections have to be chosen or default. |
| **instrument_event_type** | **str** | Required | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ConversionEvent import ConversionEvent

instance = ConversionEvent(
    record_date=datetime.now(),  # optional — Required.  Date at which positions are struck at the end of the day to  note which parties will receive the relevant amount of  entitlement, due to be distributed on the PaymentDate.
    payment_date=datetime.now(),  # optional — Required. Date on which the movement is due to take place (cash and/or securities).
    new_instrument=NewInstrument(...),  # required
    response_deadline_date=datetime.now(),  # optional — Date/time that the account servicer has set as the deadline to respond,  with instructions, to an outstanding event. Not required.
    market_deadline_date=datetime.now(),  # optional — Date/time which the issuer or issuer&#39;s agent has set as the deadline to respond,  with an instruction, to an outstanding offer or privilege. Not required.
    period_of_action=EventDateRange(...),  # optional
    fractional_units_cash_price=0.0,  # optional — The cash price paid in lieu of fractionalUnits. Not required.  If provided, must have FractionalUnitsCashCurrency too.
    fractional_units_cash_currency="...",  # optional — Optional. Used in calculating cash-in-lieu of fractional shares. Not required.  If provided, must have FractionalUnitsCashPrice too.
    security_offer_elections=[],  # optional — List of possible security offers for this conversion event. There must be at most one election of this type.    If the ParticipationType is Mandatory:     This list must have exactly one election that is chosen and default.  CashAndSecurityOfferElections and CashOfferElections &lt;b&gt; must be null or empty&lt;/b&gt;.     If the ParticipationType is Voluntary:     This list can be empty,  so long as CashAndSecurityOfferElections or CashOfferElections  has at least one election. None of these elections have to be chosen or default.
    cash_and_security_offer_elections=[],  # optional — List of possible cash and security offers for this conversion event. There must be at most one election of this type.    If the ParticipationType is Mandatory:    This list &lt;b&gt; must be null or empty&lt;/b&gt;.    If the ParticipationType is Voluntary:    This list can be empty,  so long as SecurityOfferElections or CashOfferElections  has at least one election. None of these elections have to be chosen or default.
    cash_offer_elections=[],  # optional — List of possible cash offers for this conversion event. There must be at most one election of this type.    If the ParticipationType is Mandatory:    This list &lt;b&gt; must be null or empty&lt;/b&gt;.    If the ParticipationType is Voluntary:    This list can be empty,  so long as SecurityOfferElections or CashAndSecurityOfferElections  has at least one election. None of these elections have to be chosen or default.
    instrument_event_type="..."  # required — The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent
)
```

- [NewInstrument](NewInstrument.md)
- [EventDateRange](EventDateRange.md)
- [SecurityOfferElection](SecurityOfferElection.md) — used in `security_offer_elections`
- [CashAndSecurityOfferElection](CashAndSecurityOfferElection.md) — used in `cash_and_security_offer_elections`
- [CashOfferElection](CashOfferElection.md) — used in `cash_offer_elections`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

