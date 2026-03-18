# FxForwardCurveData

Contains data (i.e. dates and rates + metadata) for building fx forward curves
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **base_date** | **datetime** | Required | EffectiveAt date of the quoted rates |
| **dom_ccy** | **str** | Required | Domestic currency of the fx forward |
| **fgn_ccy** | **str** | Required | Foreign currency of the fx forward |
| **dates** | **List[datetime]** | Required | Dates for which the forward rates apply |
| **rates** | **List[float]** | Required | Rates provided for the fx forward (price in FgnCcy per unit of DomCcy) |
| **lineage** | **str** | Optional | Description of the complex market data&#39;s lineage e.g. &#39;FundAccountant_GreenQuality&#39;. |
| **market_data_options** | [MarketDataOptions](MarketDataOptions.md) | Optional | *No description available.* |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **market_data_type** | **str** | Required | The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData, EquityCurveByPricesData, ConstantVolatilitySurface |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FxForwardCurveData import FxForwardCurveData

instance = FxForwardCurveData(
    base_date=datetime.now(),  # required — EffectiveAt date of the quoted rates
    dom_ccy="...",  # required — Domestic currency of the fx forward
    fgn_ccy="...",  # required — Foreign currency of the fx forward
    dates=,  # required — Dates for which the forward rates apply
    rates=,  # required — Rates provided for the fx forward (price in FgnCcy per unit of DomCcy)
    lineage="...",  # optional — Description of the complex market data&#39;s lineage e.g. &#39;FundAccountant_GreenQuality&#39;.
    market_data_options=MarketDataOptions(...),  # optional
    version=Version(...),  # optional
    market_data_type="..."  # required — The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData, EquityCurveByPricesData, ConstantVolatilitySurface
)
```

- [MarketDataOptions](MarketDataOptions.md)
- [Version](Version.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

