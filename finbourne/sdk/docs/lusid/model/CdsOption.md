# CdsOption

LUSID representation of an option on a single-name Credit Default Swap or a CDX/iTraxx index,  discriminated by the MasteredInstrumentType field of the referenced MasteredInstrument, which is derived  from the resolved type of the underlying. Referenced via a MasteredInstrument.  Quote-driven by default: it has no coupon or projected interim cashflow, its only cash movement being  the spot premium.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **start_date** | **datetime** | Required | The start date of the instrument. This is normally synonymous with the trade-date. |
| **dom_ccy** | **str** | Required | The domestic currency of the instrument. |
| **strike** | **float** | Required | The strike of the option. |
| **business_day_convention** | **str** | Optional | Business day convention for the maturity-to-settlement date calculation.  Default value: F.                Supported string (enumeration) values are: [NoAdjustment, Previous, P, Following, F, ModifiedPrevious, MP, ModifiedFollowing, MF, HalfMonthModifiedFollowing, Nearest]. Default value: F. Available values: NoAdjustment, None, Previous, P, Following, F, ModifiedPrevious, MP, ModifiedFollowing, MF, HalfMonthModifiedFollowing, Nearest, Invalid. Default: `'F'` |
| **delivery_days** | **int** | Optional | Number of business days between the option maturity date and settlement, used to compute  OptionSettlementDate when not explicitly overridden. Defaults to 2 if not set. Default: `2` |
| **delivery_type** | **str** | Required | Is the option cash settled or physical delivery of the underlying.                Supported string (enumeration) values are: [Cash, Physical]. Available values: Cash, Physical. |
| **exercise_type** | **str** | Optional | Type of optionality that is present; European only in this scope.  Default value: European.                Supported string (enumeration) values are: [European, Bermudan, American]. Default value: European. Available values: None, European, Bermudan, American. Default: `'European'` |
| **notional** | **float** | Required | Fixed per-unit reference multiplier. Aggregate exposure &#x3D; Holding/Units x Notional; not a mutable total. |
| **option_maturity_date** | **datetime** | Required | The last exercise date of the option. |
| **option_settlement_date** | **datetime** | Optional | Explicit override of the option&#39;s settlement date. If not supplied, it is computed as a  business-day-adjusted delivery of DeliveryDays after OptionMaturityDate. |
| **option_type** | **str** | Required | The direction of the credit option: Payer or Receiver.                Supported string (enumeration) values are: [Payer, Receiver]. Available values: Payer, Receiver. |
| **premium** | [Premium](Premium.md) | Optional | *No description available.* |
| **settlement_calendars** | **List[str]** | Optional | Holiday calendars for the maturity-to-settlement date calculation. |
| **underlying** | [MasteredInstrument](MasteredInstrument.md) | Optional | *No description available.* |
| **underlying_version** | **datetime** | Required | The AsAt timestamp of the underlying&#39;s definition at the time this option was written, pinning  lookups of the underlying&#39;s composition and terms independently of subsequent index rolls or re-upserts. |
| **instrument_type** | **str** | Required | Available values: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo, ToBeAnnounced, VolatilitySwap, ToBeAnnouncedOption, CommodityForward, BondOption, CdsOption, CommodityCalendarSwap, BondForward. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CdsOption import CdsOption

instance = CdsOption(
    start_date=datetime.now(),  # required — The start date of the instrument. This is normally synonymous with the trade-date.
    dom_ccy="...",  # required — The domestic currency of the instrument.
    strike=0.0,  # required — The strike of the option.
    business_day_convention="...",  # optional — Business day convention for the maturity-to-settlement date calculation.  Default value: F.                Supported string (enumeration) values are: [NoAdjustment, Previous, P, Following, F, ModifiedPrevious, MP, ModifiedFollowing, MF, HalfMonthModifiedFollowing, Nearest]. Default value: F. Available values: NoAdjustment, None, Previous, P, Following, F, ModifiedPrevious, MP, ModifiedFollowing, MF, HalfMonthModifiedFollowing, Nearest, Invalid.
    delivery_days=0,  # optional — Number of business days between the option maturity date and settlement, used to compute  OptionSettlementDate when not explicitly overridden. Defaults to 2 if not set.
    delivery_type="...",  # required — Is the option cash settled or physical delivery of the underlying.                Supported string (enumeration) values are: [Cash, Physical]. Available values: Cash, Physical.
    exercise_type="...",  # optional — Type of optionality that is present; European only in this scope.  Default value: European.                Supported string (enumeration) values are: [European, Bermudan, American]. Default value: European. Available values: None, European, Bermudan, American.
    notional=0.0,  # required — Fixed per-unit reference multiplier. Aggregate exposure &#x3D; Holding/Units x Notional; not a mutable total.
    option_maturity_date=datetime.now(),  # required — The last exercise date of the option.
    option_settlement_date=datetime.now(),  # optional — Explicit override of the option&#39;s settlement date. If not supplied, it is computed as a  business-day-adjusted delivery of DeliveryDays after OptionMaturityDate.
    option_type="...",  # required — The direction of the credit option: Payer or Receiver.                Supported string (enumeration) values are: [Payer, Receiver]. Available values: Payer, Receiver.
    premium=Premium(...),  # optional
    settlement_calendars=,  # optional — Holiday calendars for the maturity-to-settlement date calculation.
    underlying=MasteredInstrument(...),  # optional
    underlying_version=datetime.now(),  # required — The AsAt timestamp of the underlying&#39;s definition at the time this option was written, pinning  lookups of the underlying&#39;s composition and terms independently of subsequent index rolls or re-upserts.
    instrument_type="..."  # required — Available values: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo, ToBeAnnounced, VolatilitySwap, ToBeAnnouncedOption, CommodityForward, BondOption, CdsOption, CommodityCalendarSwap, BondForward.
)
```

- [Premium](Premium.md)
- [MasteredInstrument](MasteredInstrument.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

