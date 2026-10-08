# SwingPricingDecision

What the NAV type's swing pricing rule decided for a valuation point: the net dealing flow it measured, how  it compared with the threshold, and the pricing basis the point was valued on as a result.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **net_dealing_flow** | **float** | Optional | The net dealing flow the rule measured for the valuation point, in the fund currency. Subscriptions are positive and redemptions negative. |
| **net_dealing_flow_percentage_of_nav** | **float** | Optional | The net dealing flow as a percentage of the previous valuation point&#39;s NAV. Zero when there is no previous NAV to measure against. |
| **threshold_percentage_of_nav** | **float** | Optional | The threshold the rule compared the flow with. |
| **direction** | **str** | Optional | Whether the fund swung and which way: None, Inflow or Outflow. |
| **pricing_basis_applied** | **str** | Optional | The pricing basis the valuation point was valued on after the rule was applied. Absent when the fund did not swing and the NAV type defers to the recipe. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.SwingPricingDecision import SwingPricingDecision

instance = SwingPricingDecision(
    net_dealing_flow=0.0,  # optional — The net dealing flow the rule measured for the valuation point, in the fund currency. Subscriptions are positive and redemptions negative.
    net_dealing_flow_percentage_of_nav=0.0,  # optional — The net dealing flow as a percentage of the previous valuation point&#39;s NAV. Zero when there is no previous NAV to measure against.
    threshold_percentage_of_nav=0.0,  # optional — The threshold the rule compared the flow with.
    direction="...",  # optional — Whether the fund swung and which way: None, Inflow or Outflow.
    pricing_basis_applied="..."  # optional — The pricing basis the valuation point was valued on after the rule was applied. Absent when the fund did not swing and the NAV type defers to the recipe.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

