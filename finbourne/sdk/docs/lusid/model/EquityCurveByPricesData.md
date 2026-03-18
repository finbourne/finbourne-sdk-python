# EquityCurveByPricesData

Contains data (i.e. dates and prices + metadata) for building Equity curves
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **base_date** | **datetime** | Required | EffectiveAt date of the provided prices |
| **dates** | **List[datetime]** | Required | Dates provided for the forward price of the Equity at the corresponding price in Prices.  These dates should be in the future with respect to the BaseDate. |
| **lineage** | **str** | Optional | Description of the complex market data&#39;s lineage e.g. &#39;FundAccountant_GreenQuality&#39;. |
| **prices** | **List[float]** | Required | Prices provided for the forward price of the Equity at the corresponding date in Dates. |
| **market_data_options** | [MarketDataOptions](MarketDataOptions.md) | Optional | *No description available.* |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **market_data_type** | **str** | Required | The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData, EquityCurveByPricesData, ConstantVolatilitySurface |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.EquityCurveByPricesData import EquityCurveByPricesData

instance = EquityCurveByPricesData(
    base_date=datetime.now(),  # required — EffectiveAt date of the provided prices
    dates=,  # required — Dates provided for the forward price of the Equity at the corresponding price in Prices.  These dates should be in the future with respect to the BaseDate.
    lineage="...",  # optional — Description of the complex market data&#39;s lineage e.g. &#39;FundAccountant_GreenQuality&#39;.
    prices=,  # required — Prices provided for the forward price of the Equity at the corresponding date in Dates.
    market_data_options=MarketDataOptions(...),  # optional
    version=Version(...),  # optional
    market_data_type="..."  # required — The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData, EquityCurveByPricesData, ConstantVolatilitySurface
)
```

- [MarketDataOptions](MarketDataOptions.md)
- [Version](Version.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

