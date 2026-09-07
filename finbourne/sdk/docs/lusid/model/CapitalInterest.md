# CapitalInterest

LUSID representation of a CapitalInterest.  A CapitalInterest represents an investor's interest in a single commitment line to a  private-markets fund: one instrument per (fund, investor, commitment line). Units act as  a liveness flag (1 while the line is open, 0 once closed) and the economics are carried  by cost, fair value and the running capital balances rather than by quantity.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **quantity_basis** | **str** | Required | How the quantity of the holding is interpreted. Under the &#39;Anchored&#39; basis, units act as a  liveness flag: 1 while the commitment line is open and 0 once it is closed. Only &#39;Anchored&#39;  is currently supported.                Supported string (enumeration) values are: [Anchored, Unitless]. Available values: Anchored, Unitless. |
| **commitment_currency** | **str** | Required | The currency the commitment is denominated in. May differ from both the fund currency  and the portfolio base currency. |
| **fund_entity_id** | **str** | Required | The identifier of the fund entity the commitment is made to. |
| **investor_entity_id** | **str** | Required | The identifier of the investor entity holding the commitment. |
| **commitment_line_id** | **str** | Required | The identifier of the commitment line, unique for a given fund and investor. |
| **original_commitment** | **float** | Required | The committed amount at inception, in the commitment currency. May be zero for evergreen  funds. This is the original value only; subsequent amendments are carried by the running  capital balances, not by the instrument. |
| **commitment_date** | **datetime** | Required | The date the commitment closed. |
| **vintage** | **int** | Optional | The vintage year of the commitment. Defaults to the year of the commitment date. |
| **capital_interest_asset_class** | **str** | Optional | The private-markets asset class of the fund the commitment is made to,  for example private equity, venture capital or infrastructure.                Supported string (enumeration) values are: [PrivateEquity, VentureCapital, PrivateCredit, RealAssets, Infrastructure, FundOfFunds, Secondary, CoInvestment, DirectEquity, ShareholderLoan, Other]. Available values: PrivateEquity, VentureCapital, PrivateCredit, RealAssets, Infrastructure, FundOfFunds, Secondary, CoInvestment, DirectEquity, ShareholderLoan, Other. |
| **relief_policy** | **str** | Optional | How distributions from the commitment line are relieved against the cost of the holding.  Defaults to &#39;InstructedCharacter&#39;.                Supported string (enumeration) values are: [InstructedCharacter, CostRecovery, ProportionalToFairValue, ProportionalToPercentageInterest, NoRelief]. Available values: InstructedCharacter, CostRecovery, ProportionalToFairValue, ProportionalToPercentageInterest, NoRelief. |
| **relief_revision_mode** | **str** | Optional | How revisions to previously applied distribution relief are handled.  Defaults to &#39;ProspectiveTrueUp&#39;.                Supported string (enumeration) values are: [ProspectiveTrueUp, Restate, Final]. Available values: ProspectiveTrueUp, Restate, Final. |
| **fair_value_source_precedence** | **List[str]** | Optional | The order of precedence of the sources a fair value for the interest can be taken from.  Defaults to the reported NAV rolled forward for subsequent capital activity, then cost.                Supported string (enumeration) values for each entry are: [ReportedNav, RollForward, Independent, Cost]. |
| **termination_date** | **datetime** | Optional | The expected end of the fund&#39;s life, if known. This is expected rather than contractual  and does not act as a maturity date for the instrument. |
| **instrument_type** | **str** | Required | Available values: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo, ToBeAnnounced, VolatilitySwap, ToBeAnnouncedOption, CommodityForward, BondOption, CdsOption, CommodityCalendarSwap, BondForward, PreferredShare, CapitalInterest. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CapitalInterest import CapitalInterest

instance = CapitalInterest(
    quantity_basis="...",  # required — How the quantity of the holding is interpreted. Under the &#39;Anchored&#39; basis, units act as a  liveness flag: 1 while the commitment line is open and 0 once it is closed. Only &#39;Anchored&#39;  is currently supported.                Supported string (enumeration) values are: [Anchored, Unitless]. Available values: Anchored, Unitless.
    commitment_currency="...",  # required — The currency the commitment is denominated in. May differ from both the fund currency  and the portfolio base currency.
    fund_entity_id="...",  # required — The identifier of the fund entity the commitment is made to.
    investor_entity_id="...",  # required — The identifier of the investor entity holding the commitment.
    commitment_line_id="...",  # required — The identifier of the commitment line, unique for a given fund and investor.
    original_commitment=0.0,  # required — The committed amount at inception, in the commitment currency. May be zero for evergreen  funds. This is the original value only; subsequent amendments are carried by the running  capital balances, not by the instrument.
    commitment_date=datetime.now(),  # required — The date the commitment closed.
    vintage=0,  # optional — The vintage year of the commitment. Defaults to the year of the commitment date.
    capital_interest_asset_class="...",  # optional — The private-markets asset class of the fund the commitment is made to,  for example private equity, venture capital or infrastructure.                Supported string (enumeration) values are: [PrivateEquity, VentureCapital, PrivateCredit, RealAssets, Infrastructure, FundOfFunds, Secondary, CoInvestment, DirectEquity, ShareholderLoan, Other]. Available values: PrivateEquity, VentureCapital, PrivateCredit, RealAssets, Infrastructure, FundOfFunds, Secondary, CoInvestment, DirectEquity, ShareholderLoan, Other.
    relief_policy="...",  # optional — How distributions from the commitment line are relieved against the cost of the holding.  Defaults to &#39;InstructedCharacter&#39;.                Supported string (enumeration) values are: [InstructedCharacter, CostRecovery, ProportionalToFairValue, ProportionalToPercentageInterest, NoRelief]. Available values: InstructedCharacter, CostRecovery, ProportionalToFairValue, ProportionalToPercentageInterest, NoRelief.
    relief_revision_mode="...",  # optional — How revisions to previously applied distribution relief are handled.  Defaults to &#39;ProspectiveTrueUp&#39;.                Supported string (enumeration) values are: [ProspectiveTrueUp, Restate, Final]. Available values: ProspectiveTrueUp, Restate, Final.
    fair_value_source_precedence=,  # optional — The order of precedence of the sources a fair value for the interest can be taken from.  Defaults to the reported NAV rolled forward for subsequent capital activity, then cost.                Supported string (enumeration) values for each entry are: [ReportedNav, RollForward, Independent, Cost].
    termination_date=datetime.now(),  # optional — The expected end of the fund&#39;s life, if known. This is expected rather than contractual  and does not act as a maturity date for the instrument.
    instrument_type="..."  # required — Available values: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo, ToBeAnnounced, VolatilitySwap, ToBeAnnouncedOption, CommodityForward, BondOption, CdsOption, CommodityCalendarSwap, BondForward, PreferredShare, CapitalInterest.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

