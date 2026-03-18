# PortfolioReturnBreakdown

A list of Composite Breakdowns.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **portfolio_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **rate_of_return** | **float** | Optional | The return number. |
| **opening_market_value** | **float** | Optional | The opening market value. |
| **closing_market_value** | **float** | Optional | The closing market value. |
| **weight** | **float** | Optional | The weight of the constituent into the composite. |
| **constituents_in_the_composite** | **int** | Optional | The number of members in the Composite on the given day. |
| **constituents_missing** | **int** | Optional | The number of the constituents which have a missing return on that day. |
| **currency** | **str** | Optional | The currency of the portfolio. |
| **open_fx_rate** | **float** | Optional | The opening fxRate which is used in calculation. |
| **close_fx_rate** | **float** | Optional | The closing fxRate which is used in calculation. |
| **local_rate_of_return** | **float** | Optional | The rate of return in the local currency. |
| **local_opening_market_value** | **float** | Optional | The opening market value in the local currency. |
| **local_closing_market_value** | **float** | Optional | The closing market value in the local currency. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PortfolioReturnBreakdown import PortfolioReturnBreakdown

instance = PortfolioReturnBreakdown(
    portfolio_id=ResourceId(...),  # required
    rate_of_return=0.0,  # optional — The return number.
    opening_market_value=0.0,  # optional — The opening market value.
    closing_market_value=0.0,  # optional — The closing market value.
    weight=0.0,  # optional — The weight of the constituent into the composite.
    constituents_in_the_composite=0,  # optional — The number of members in the Composite on the given day.
    constituents_missing=0,  # optional — The number of the constituents which have a missing return on that day.
    currency="...",  # optional — The currency of the portfolio.
    open_fx_rate=0.0,  # optional — The opening fxRate which is used in calculation.
    close_fx_rate=0.0,  # optional — The closing fxRate which is used in calculation.
    local_rate_of_return=0.0,  # optional — The rate of return in the local currency.
    local_opening_market_value=0.0,  # optional — The opening market value in the local currency.
    local_closing_market_value=0.0  # optional — The closing market value in the local currency.
)
```


## Related Models

- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

