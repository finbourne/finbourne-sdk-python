# TradingConventions

Common Trading details for exchange traded instruments like Futures and Bonds
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **price_scale_factor** | **float** | Optional | The factor used to scale prices for the instrument. Currently used by LUSID when calculating cost  and notional amounts on transactions, and in Valuation, PV and exposure when the recipe&#39;s  UseInstrumentScaleFactorAsDefault pricing option is set: a lookup-priced instrument whose price  quote declares no scale factor of its own is then scaled by this factor. When that option is not  set, only the scale factor attached to the price quotes in the QuoteStore is used.  Must be positive and defaults to 1 if not set. |
| **minimum_order_size** | **float** | Optional | The Minimum Order Size  Must be non-negative and defaults to 0 if not set. |
| **minimum_order_increment** | **float** | Optional | The Minimum Order Increment  Must be non-negative and defaults to 0 if not set. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TradingConventions import TradingConventions

instance = TradingConventions(
    price_scale_factor=0.0,  # optional — The factor used to scale prices for the instrument. Currently used by LUSID when calculating cost  and notional amounts on transactions, and in Valuation, PV and exposure when the recipe&#39;s  UseInstrumentScaleFactorAsDefault pricing option is set: a lookup-priced instrument whose price  quote declares no scale factor of its own is then scaled by this factor. When that option is not  set, only the scale factor attached to the price quotes in the QuoteStore is used.  Must be positive and defaults to 1 if not set.
    minimum_order_size=0.0,  # optional — The Minimum Order Size  Must be non-negative and defaults to 0 if not set.
    minimum_order_increment=0.0  # optional — The Minimum Order Increment  Must be non-negative and defaults to 0 if not set.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

