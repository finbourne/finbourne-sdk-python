# SwingPricingRule

Moves a NAV type's pricing basis with its net dealing flow. When the flow, as a percentage of the previous  valuation point's NAV, exceeds the threshold the fund is valued on the inflow or outflow basis instead of  the NAV type's own basis.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **threshold_percentage_of_nav** | **float** | Required | The net dealing flow, as a percentage of the previous valuation point&#39;s NAV, above which the fund swings. Must be zero or more; zero swings on any non-zero flow. |
| **inflow_basis** | **str** | Optional | The pricing basis the fund is valued on when net subscriptions exceed the threshold: Mid, Bid or Ask. Defaults to Ask. Available values: Mid, Bid, Ask. |
| **outflow_basis** | **str** | Optional | The pricing basis the fund is valued on when net redemptions exceed the threshold: Mid, Bid or Ask. Defaults to Bid. Available values: Mid, Bid, Ask. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.SwingPricingRule import SwingPricingRule

instance = SwingPricingRule(
    threshold_percentage_of_nav=0.0,  # required — The net dealing flow, as a percentage of the previous valuation point&#39;s NAV, above which the fund swings. Must be zero or more; zero swings on any non-zero flow.
    inflow_basis="...",  # optional — The pricing basis the fund is valued on when net subscriptions exceed the threshold: Mid, Bid or Ask. Defaults to Ask. Available values: Mid, Bid, Ask.
    outflow_basis="..."  # optional — The pricing basis the fund is valued on when net redemptions exceed the threshold: Mid, Bid or Ask. Defaults to Bid. Available values: Mid, Bid, Ask.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

