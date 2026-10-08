# FundDetails

The details of a Fund.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **currency** | **str** | Optional | The currency of the fund which is the same as the base currency of all the portfolios of the fund&#39;s Abor. |
| **pricing_basis** | **str** | Optional | The side of the quote the NAV type valued the fund on: Mid, Bid or Ask. Absent when the NAV type defers to the valuation recipe&#39;s own pricing basis. When the NAV type has a swing pricing rule this is the basis the rule applied. |
| **swing_pricing** | [SwingPricingDecision](SwingPricingDecision.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FundDetails import FundDetails

instance = FundDetails(
    currency="...",  # optional — The currency of the fund which is the same as the base currency of all the portfolios of the fund&#39;s Abor.
    pricing_basis="...",  # optional — The side of the quote the NAV type valued the fund on: Mid, Bid or Ask. Absent when the NAV type defers to the valuation recipe&#39;s own pricing basis. When the NAV type has a swing pricing rule this is the basis the rule applied.
    swing_pricing=SwingPricingDecision(...)  # optional
)
```

- [SwingPricingDecision](SwingPricingDecision.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

