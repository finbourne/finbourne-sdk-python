# MarketDataOptions

Base class for representing market data options in LUSID.  Abstractly, these are any options that one should be able to specify for ComplexMarketData entities.  For example, CurveOptions allows one to decide how the data provided in a discountFactorCurve is interpolated.  This base class should not be directly instantiated;  each supported MarketDataOptionsType has a corresponding inherited class.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **market_data_options_type** | **str** | Required | The available values are: CurveOptions |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.MarketDataOptions import MarketDataOptions

instance = MarketDataOptions(
    market_data_options_type="..."  # required — The available values are: CurveOptions
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

