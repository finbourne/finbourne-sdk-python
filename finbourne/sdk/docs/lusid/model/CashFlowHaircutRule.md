# CashFlowHaircutRule

A rule describing how projected cashflow inflows are reduced by a haircut representing expected  default loss or cost of downgrade, for matching-adjustment and liquidity (Solvency II) analyses.  Rules are matched in request order against each cashflow's instrument and the first matching rule  wins; a rule with no criteria acts as a catch-all. Only inflows are haircut; outflows always pass  through untouched.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **rule_id** | **str** | Optional | Optional identifier reported back against cashflows this rule haircut. Defaults to the rule&#39;s position in the list, e.g. &#39;HaircutRules[0]&#39;. |
| **property_key** | **str** | Optional | The instrument property key the rule matches on, e.g. &#39;Instrument/default/CreditRating&#39;. When omitted the rule does not match on a property. |
| **property_value** | **str** | Optional | The instrument property value the rule matches. Required when PropertyKey is supplied. |
| **instrument_type** | **str** | Optional | Optional instrument type filter, e.g. &#39;Bond&#39;. When supplied the rule only matches cashflows from instruments of that type. |
| **haircut_type** | **str** | Required | The mathematical form of the haircut. One of &#39;CumulativeAnnualised&#39; (net &#x3D; gross x (1 - rate)^t, where t is the ACT/365.25 year fraction from the valuation date to the payment date) or &#39;Flat&#39; (net &#x3D; gross x (1 - h(t)), where h(t) is the flat rate or the term structure rate at t). Available values: CumulativeAnnualised, Flat. |
| **rate** | **float** | Optional | The haircut rate as a fraction in the range [0, 1]. Exactly one of Rate and TermStructure must be supplied. |
| **term_structure** | [List[CashFlowHaircutTermPoint]](CashFlowHaircutTermPoint.md) | Optional | The haircut rate term structure, linearly interpolated on time-to-payment with flat extrapolation beyond either end. Exactly one of Rate and TermStructure must be supplied. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CashFlowHaircutRule import CashFlowHaircutRule

instance = CashFlowHaircutRule(
    rule_id="...",  # optional — Optional identifier reported back against cashflows this rule haircut. Defaults to the rule&#39;s position in the list, e.g. &#39;HaircutRules[0]&#39;.
    property_key="...",  # optional — The instrument property key the rule matches on, e.g. &#39;Instrument/default/CreditRating&#39;. When omitted the rule does not match on a property.
    property_value="...",  # optional — The instrument property value the rule matches. Required when PropertyKey is supplied.
    instrument_type="...",  # optional — Optional instrument type filter, e.g. &#39;Bond&#39;. When supplied the rule only matches cashflows from instruments of that type.
    haircut_type="...",  # required — The mathematical form of the haircut. One of &#39;CumulativeAnnualised&#39; (net &#x3D; gross x (1 - rate)^t, where t is the ACT/365.25 year fraction from the valuation date to the payment date) or &#39;Flat&#39; (net &#x3D; gross x (1 - h(t)), where h(t) is the flat rate or the term structure rate at t). Available values: CumulativeAnnualised, Flat.
    rate=0.0,  # optional — The haircut rate as a fraction in the range [0, 1]. Exactly one of Rate and TermStructure must be supplied.
    term_structure=[]  # optional — The haircut rate term structure, linearly interpolated on time-to-payment with flat extrapolation beyond either end. Exactly one of Rate and TermStructure must be supplied.
)
```

- [CashFlowHaircutTermPoint](CashFlowHaircutTermPoint.md) — used in `term_structure`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

