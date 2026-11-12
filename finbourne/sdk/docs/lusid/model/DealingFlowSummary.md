# DealingFlowSummary

The transfer agency estimates a swing decision was made on: the orders dealt at the valuation point, what they summed, and how many pending orders were left out and what those were worth.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **count** | **int** | Required | How many orders were summed. |
| **gross_inflow** | **float** | Required | The sum of the inflows, in the fund currency. Zero or more. |
| **gross_outflow** | **float** | Required | The sum of the outflows, in the fund currency, as a magnitude. Zero or more. |
| **pending_not_counted** | **int** | Required | How many pending orders at the valuation point were left out of the sums because the fund&#39;s dealing estimates do not count pending orders. Zero when the fund counts them. |
| **pending_gross_inflow** | **float** | Required | The sum of the inflows among the pending orders left out, in the fund currency, with units at the estimate price. Zero or more; zero when the fund counts pending orders. |
| **pending_gross_outflow** | **float** | Required | The sum of the outflows among the pending orders left out, in the fund currency, as a magnitude, with units at the estimate price. Zero or more; zero when the fund counts pending orders. |
| **pending_unvalued_count** | **int** | Required | How many of the pending orders left out could not be valued, such as a unit order with no price yet. They are in pendingNotCounted but absent from pendingGrossInflow and pendingGrossOutflow. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.DealingFlowSummary import DealingFlowSummary

instance = DealingFlowSummary(
    count=0,  # required — How many orders were summed.
    gross_inflow=0.0,  # required — The sum of the inflows, in the fund currency. Zero or more.
    gross_outflow=0.0,  # required — The sum of the outflows, in the fund currency, as a magnitude. Zero or more.
    pending_not_counted=0,  # required — How many pending orders at the valuation point were left out of the sums because the fund&#39;s dealing estimates do not count pending orders. Zero when the fund counts them.
    pending_gross_inflow=0.0,  # required — The sum of the inflows among the pending orders left out, in the fund currency, with units at the estimate price. Zero or more; zero when the fund counts pending orders.
    pending_gross_outflow=0.0,  # required — The sum of the outflows among the pending orders left out, in the fund currency, as a magnitude, with units at the estimate price. Zero or more; zero when the fund counts pending orders.
    pending_unvalued_count=0  # required — How many of the pending orders left out could not be valued, such as a unit order with no price yet. They are in pendingNotCounted but absent from pendingGrossInflow and pendingGrossOutflow.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

