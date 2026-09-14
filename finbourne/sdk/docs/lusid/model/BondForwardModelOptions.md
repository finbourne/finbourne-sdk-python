# BondForwardModelOptions

Model options for bond forward pricing.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **bond_forward_projection_type** | **str** | Optional | Determines how the forward price of the deliverable bond is projected to the settlement date.                Supported string (enumeration) values are: [QuotedContractPrice, ForwardProjectedFromFundingCurve,  DeliverableSpreadAnchoredToQuote].  Defaults to QuotedContractPrice - the original quote-driven behaviour - when not supplied, so  options persisted before this property existed keep the behaviour they were saved under.                ForwardProjectedFromFundingCurve carries the deliverable&#39;s quoted dirty spot to settlement on the  discount curve. DeliverableSpreadAnchoredToQuote does the same carry but models that spot as well,  off the spread anchored for the deliverable in the base market, which is what gives the forward  the deliverable&#39;s own curve delta rather than only the carry&#39;s - the larger of the two terms. It  requires the deliverable to be a mastered Bond or ComplexBond settling in the forward&#39;s own  currency, and a credit-spread curve or ZSpread quote to be resolvable for it. |
| **model_options_type** | **str** | Required | Available values: Invalid, OpaqueModelOptions, EmptyModelOptions, IndexModelOptions, FxForwardModelOptions, FundingLegModelOptions, EquityModelOptions, CdsModelOptions, FlexibleLoanPricerOptions, HullWhiteModelOptions, BondLookupModelOptions, BondForwardModelOptions. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.BondForwardModelOptions import BondForwardModelOptions

instance = BondForwardModelOptions(
    bond_forward_projection_type="...",  # optional — Determines how the forward price of the deliverable bond is projected to the settlement date.                Supported string (enumeration) values are: [QuotedContractPrice, ForwardProjectedFromFundingCurve,  DeliverableSpreadAnchoredToQuote].  Defaults to QuotedContractPrice - the original quote-driven behaviour - when not supplied, so  options persisted before this property existed keep the behaviour they were saved under.                ForwardProjectedFromFundingCurve carries the deliverable&#39;s quoted dirty spot to settlement on the  discount curve. DeliverableSpreadAnchoredToQuote does the same carry but models that spot as well,  off the spread anchored for the deliverable in the base market, which is what gives the forward  the deliverable&#39;s own curve delta rather than only the carry&#39;s - the larger of the two terms. It  requires the deliverable to be a mastered Bond or ComplexBond settling in the forward&#39;s own  currency, and a credit-spread curve or ZSpread quote to be resolvable for it.
    model_options_type="..."  # required — Available values: Invalid, OpaqueModelOptions, EmptyModelOptions, IndexModelOptions, FxForwardModelOptions, FundingLegModelOptions, EquityModelOptions, CdsModelOptions, FlexibleLoanPricerOptions, HullWhiteModelOptions, BondLookupModelOptions, BondForwardModelOptions.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

