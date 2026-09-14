# InflationConvexityOptions

Parameters of the Jarrow-Yildirim convexity correction applied to projected inflation index  values. Unlike most option blocks there is no defaulting here: nothing in the pricing chain  infers an index volatility, a nominal volatility or a correlation from market data, so an armed  correction is entirely the caller's stated view and every member must be supplied.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **nominal_index_correlation** | **float** | Optional | Correlation between the inflation index and the nominal short rate, in [-1, 1]. A positive  correlation makes the factor greater than one for a projection funded later than the curve&#39;s  own observation basis. |
| **index_volatility** | **float** | Optional | Lognormal volatility of the inflation index, as a decimal (0.0095 is 0.95%). Must be  strictly positive - a zero volatility disarms the correction arithmetically, which is what  omitting the whole block already expresses. |
| **nominal_volatility** | **float** | Optional | Volatility of the nominal short rate in the Hull-White dynamics the correction assumes, as a  decimal (0.008 is 80bp). Must be strictly positive. |
| **nominal_mean_reversion** | **float** | Optional | Mean reversion speed of the nominal short rate, per year. Must be strictly positive: the  closed form divides by it. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.InflationConvexityOptions import InflationConvexityOptions

instance = InflationConvexityOptions(
    nominal_index_correlation=0.0,  # optional — Correlation between the inflation index and the nominal short rate, in [-1, 1]. A positive  correlation makes the factor greater than one for a projection funded later than the curve&#39;s  own observation basis.
    index_volatility=0.0,  # optional — Lognormal volatility of the inflation index, as a decimal (0.0095 is 0.95%). Must be  strictly positive - a zero volatility disarms the correction arithmetically, which is what  omitting the whole block already expresses.
    nominal_volatility=0.0,  # optional — Volatility of the nominal short rate in the Hull-White dynamics the correction assumes, as a  decimal (0.008 is 80bp). Must be strictly positive.
    nominal_mean_reversion=0.0  # optional — Mean reversion speed of the nominal short rate, per year. Must be strictly positive: the  closed form divides by it.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

