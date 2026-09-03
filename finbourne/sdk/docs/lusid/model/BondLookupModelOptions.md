# BondLookupModelOptions

Model options for the quote-anchored bond lookup pricer.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **spread_anchored_risk** | **bool** | Required | Price the bond by discounting its own cashflows over its discounting curve at a constant  spread, instead of marking it to its quoted price. Marking to a quote declares no curve  dependency, so a lookup-priced bond reports no curve delta at all. In this mode the pricer  declares both the discounting curve and a ZSpread quote for the instrument and prices off  them, so holding the spread fixed while the curve is perturbed produces the curve&#39;s delta.  Off by default, as the mode changes both the declared dependencies and where the price  comes from. |
| **cs01_bump_width** | **float** | Optional | The TOTAL width of the central-difference stencil behind the CS01/Central measure: the  instrument&#39;s own z-spread is repriced at spread ± width/2, so a width of 0.0001 means  ±0.5bp reprice points. The width is the whole distance between the two reprice points,  NOT the half-shift. The reported measure is always per one basis point of widening  whatever width is configured. Must be strictly positive.  Defaults to 0.0001 (1bp, repriced at ±0.5bp) when not supplied. |
| **model_options_type** | **str** | Required | Available values: Invalid, OpaqueModelOptions, EmptyModelOptions, IndexModelOptions, FxForwardModelOptions, FundingLegModelOptions, EquityModelOptions, CdsModelOptions, FlexibleLoanPricerOptions, HullWhiteModelOptions, BondLookupModelOptions. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.BondLookupModelOptions import BondLookupModelOptions

instance = BondLookupModelOptions(
    spread_anchored_risk=True,  # required — Price the bond by discounting its own cashflows over its discounting curve at a constant  spread, instead of marking it to its quoted price. Marking to a quote declares no curve  dependency, so a lookup-priced bond reports no curve delta at all. In this mode the pricer  declares both the discounting curve and a ZSpread quote for the instrument and prices off  them, so holding the spread fixed while the curve is perturbed produces the curve&#39;s delta.  Off by default, as the mode changes both the declared dependencies and where the price  comes from.
    cs01_bump_width=0.0,  # optional — The TOTAL width of the central-difference stencil behind the CS01/Central measure: the  instrument&#39;s own z-spread is repriced at spread ± width/2, so a width of 0.0001 means  ±0.5bp reprice points. The width is the whole distance between the two reprice points,  NOT the half-shift. The reported measure is always per one basis point of widening  whatever width is configured. Must be strictly positive.  Defaults to 0.0001 (1bp, repriced at ±0.5bp) when not supplied.
    model_options_type="..."  # required — Available values: Invalid, OpaqueModelOptions, EmptyModelOptions, IndexModelOptions, FxForwardModelOptions, FundingLegModelOptions, EquityModelOptions, CdsModelOptions, FlexibleLoanPricerOptions, HullWhiteModelOptions, BondLookupModelOptions.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

