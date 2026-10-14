# DealingFlowSummary

The transfer agency estimates a swing decision was made on: how many orders were dealt at the valuation point and what they summed.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **count** | **int** | Required | How many orders were summed. |
| **gross_inflow** | **float** | Required | The sum of the inflows, in the fund currency. Zero or more. |
| **gross_outflow** | **float** | Required | The sum of the outflows, in the fund currency, as a magnitude. Zero or more. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.DealingFlowSummary import DealingFlowSummary

instance = DealingFlowSummary(
    count=0,  # required — How many orders were summed.
    gross_inflow=0.0,  # required — The sum of the inflows, in the fund currency. Zero or more.
    gross_outflow=0.0  # required — The sum of the outflows, in the fund currency, as a magnitude. Zero or more.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

