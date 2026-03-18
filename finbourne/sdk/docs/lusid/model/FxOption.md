# FxOption

LUSID representation of an FX Option.  Including Vanilla, American, European, and Digital (Binary) options.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **start_date** | **datetime** | Required | The start date of the instrument. This is normally synonymous with the trade-date. |
| **dom_ccy** | **str** | Required | The domestic currency of the instrument. |
| **dom_amount** | **float** | Optional | The Amount of DomCcy that will be exchanged if the option is exercised.  This amount should be a positive number, with the Call/Put flag used to indicate direction.  The corresponding amount of FgnCcy that will be exchanged is this amount times the strike.  Note there is no rounding performed on this computed value.  This is an optional field, if not set the option ContractSize will default to 1. |
| **fgn_ccy** | **str** | Required | The foreign currency of the FX. |
| **fgn_amount** | **float** | Optional | For a vanilla FxOption contract, FgnAmount cannot be set.  In case of a digital FxOption (IsPayoffDigital&#x3D;&#x3D;true)  a payoff (if the option is in the money) can be either  in domestic or in foreign currency - for the latter  FgnAmount must be set.  Note: It is invalid to have FgnAmount and DomAmount  at the same time. |
| **strike** | **float** | Optional | The strike of the option. |
| **barriers** | [List[Barrier]](Barrier.md) | Optional | For a barrier option the list should not be empty. Up to two barriers are supported.  An option cannot be at the same time barrier- and touch-option.  One (or both) of the lists must be empty. |
| **exercise_type** | **str** | Optional | Type of optionality that is present; European, American.    Supported string (enumeration) values are: [European, American].  Defaults to \&quot;European\&quot; if not set. |
| **is_call_not_put** | **bool** | Required | True if the option is a call, false if the option is a put. |
| **is_delivery_not_cash** | **bool** | Required | True if the option delivers the FX underlying, False if the option is settled in cash. |
| **is_payoff_digital** | **bool** | Optional | By default IsPayoffDigital is false. If IsPayoffDigital&#x3D;true,  the option is &#39;digital&#39;, and the option payoff is 0 or 1 unit of currency,  instead of a vanilla CallPayoff&#x3D;max(spot-strike,0) or PutPayoff&#x3D;max(strike-spot,0). |
| **option_maturity_date** | **datetime** | Required | The maturity date of the option. |
| **option_settlement_date** | **datetime** | Required | The settlement date of the option. |
| **payout_style** | **str** | Optional | PayoutStyle for touch options.                For options without touch optionality, payoutStyle should not be set.  For options with touch optionality (where the touches data has been set), payoutStyle must be defined and cannot be None.    Supported string (enumeration) values are: [Deferred, Immediate].  Defaults to \&quot;None\&quot; if not set. |
| **premium** | [Premium](Premium.md) | Optional | *No description available.* |
| **touches** | [List[Touch]](Touch.md) | Optional | For a touch option the list should not be empty. Up to two touches are supported.  An option cannot be at the same time barrier- and touch-option.  One (or both) of the lists must be empty. |
| **time_zone_conventions** | [TimeZoneConventions](TimeZoneConventions.md) | Optional | *No description available.* |
| **instrument_type** | **str** | Required | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FxOption import FxOption

instance = FxOption(
    start_date=datetime.now(),  # required — The start date of the instrument. This is normally synonymous with the trade-date.
    dom_ccy="...",  # required — The domestic currency of the instrument.
    dom_amount=0.0,  # optional — The Amount of DomCcy that will be exchanged if the option is exercised.  This amount should be a positive number, with the Call/Put flag used to indicate direction.  The corresponding amount of FgnCcy that will be exchanged is this amount times the strike.  Note there is no rounding performed on this computed value.  This is an optional field, if not set the option ContractSize will default to 1.
    fgn_ccy="...",  # required — The foreign currency of the FX.
    fgn_amount=0.0,  # optional — For a vanilla FxOption contract, FgnAmount cannot be set.  In case of a digital FxOption (IsPayoffDigital&#x3D;&#x3D;true)  a payoff (if the option is in the money) can be either  in domestic or in foreign currency - for the latter  FgnAmount must be set.  Note: It is invalid to have FgnAmount and DomAmount  at the same time.
    strike=0.0,  # optional — The strike of the option.
    barriers=[],  # optional — For a barrier option the list should not be empty. Up to two barriers are supported.  An option cannot be at the same time barrier- and touch-option.  One (or both) of the lists must be empty.
    exercise_type="...",  # optional — Type of optionality that is present; European, American.    Supported string (enumeration) values are: [European, American].  Defaults to \&quot;European\&quot; if not set.
    is_call_not_put=True,  # required — True if the option is a call, false if the option is a put.
    is_delivery_not_cash=True,  # required — True if the option delivers the FX underlying, False if the option is settled in cash.
    is_payoff_digital=True,  # optional — By default IsPayoffDigital is false. If IsPayoffDigital&#x3D;true,  the option is &#39;digital&#39;, and the option payoff is 0 or 1 unit of currency,  instead of a vanilla CallPayoff&#x3D;max(spot-strike,0) or PutPayoff&#x3D;max(strike-spot,0).
    option_maturity_date=datetime.now(),  # required — The maturity date of the option.
    option_settlement_date=datetime.now(),  # required — The settlement date of the option.
    payout_style="...",  # optional — PayoutStyle for touch options.                For options without touch optionality, payoutStyle should not be set.  For options with touch optionality (where the touches data has been set), payoutStyle must be defined and cannot be None.    Supported string (enumeration) values are: [Deferred, Immediate].  Defaults to \&quot;None\&quot; if not set.
    premium=Premium(...),  # optional
    touches=[],  # optional — For a touch option the list should not be empty. Up to two touches are supported.  An option cannot be at the same time barrier- and touch-option.  One (or both) of the lists must be empty.
    time_zone_conventions=TimeZoneConventions(...),  # optional
    instrument_type="..."  # required — The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo
)
```

- [Barrier](Barrier.md) — used in `barriers`
- [Premium](Premium.md)
- [Touch](Touch.md) — used in `touches`
- [TimeZoneConventions](TimeZoneConventions.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

