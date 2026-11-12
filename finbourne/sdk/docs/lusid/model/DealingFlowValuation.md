# DealingFlowValuation

The transfer agency's dealing flows with unit-denominated orders valued at one unit price, and the swing outcome that net flow leads the methodology to.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **net_cashflow** | **float** | Required | The inflows less the outflows at this unit price, in the fund currency. |
| **net_cashflow_pct_of_nav** | **float** | Optional | The net cashflow as a percentage of the fund&#39;s NAV at the previous valuation point. Absent when there is no previous NAV. |
| **gross_inflow** | **float** | Required | The sum of the inflows at this unit price, in the fund currency. Zero or more. |
| **gross_outflow** | **float** | Required | The sum of the outflows at this unit price, in the fund currency, as a magnitude. Zero or more. |
| **outcome** | [EstimateValuationOutcome](EstimateValuationOutcome.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.DealingFlowValuation import DealingFlowValuation

instance = DealingFlowValuation(
    net_cashflow=0.0,  # required — The inflows less the outflows at this unit price, in the fund currency.
    net_cashflow_pct_of_nav=0.0,  # optional — The net cashflow as a percentage of the fund&#39;s NAV at the previous valuation point. Absent when there is no previous NAV.
    gross_inflow=0.0,  # required — The sum of the inflows at this unit price, in the fund currency. Zero or more.
    gross_outflow=0.0,  # required — The sum of the outflows at this unit price, in the fund currency, as a magnitude. Zero or more.
    outcome=EstimateValuationOutcome(...)  # optional
)
```

- [EstimateValuationOutcome](EstimateValuationOutcome.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

