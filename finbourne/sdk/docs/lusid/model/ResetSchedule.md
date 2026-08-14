# ResetSchedule

The schedule on which the price return of the asset leg of a total return swap is observed and exchanged.  Each reset period pays the change in the asset's price over the period, sourced from quoted market data.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **conventions** | [FlowConventions](FlowConventions.md) | Optional | *No description available.* |
| **first_reset_date** | **datetime** | Optional | The date of the first price reset. Optional; when absent the reset dates are rolled forward from the swap start date. |
| **frequency** | **str** | Required | The frequency at which the asset price is reset and the price return is exchanged, e.g. 3M. |
| **last_reset_date** | **datetime** | Optional | The date of the last price reset. Optional; when absent the reset dates are rolled forward until the swap maturity date. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ResetSchedule import ResetSchedule

instance = ResetSchedule(
    conventions=FlowConventions(...),  # optional
    first_reset_date=datetime.now(),  # optional — The date of the first price reset. Optional; when absent the reset dates are rolled forward from the swap start date.
    frequency="...",  # required — The frequency at which the asset price is reset and the price return is exchanged, e.g. 3M.
    last_reset_date=datetime.now()  # optional — The date of the last price reset. Optional; when absent the reset dates are rolled forward until the swap maturity date.
)
```


## Related Models

- [FlowConventions](FlowConventions.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

