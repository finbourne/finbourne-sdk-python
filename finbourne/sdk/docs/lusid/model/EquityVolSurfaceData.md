# EquityVolSurfaceData

Market Data for an equity vol surface, represented by a list of instruments and corresponding market quotes
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **base_date** | **datetime** | Required | Base date of the surface |
| **instruments** | [List[LusidInstrument]](LusidInstrument.md) | Required | The set of instruments that define the surface. |
| **quotes** | [List[MarketQuote]](MarketQuote.md) | Required | The set of market quotes that define the surface, in NormalVol or LogNormalVol terms. |
| **lineage** | **str** | Optional | Description of the complex market data&#39;s lineage e.g. &#39;FundAccountant_GreenQuality&#39;. |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **market_data_type** | **str** | Required | The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData, EquityCurveByPricesData, ConstantVolatilitySurface |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.EquityVolSurfaceData import EquityVolSurfaceData

instance = EquityVolSurfaceData(
    base_date=datetime.now(),  # required — Base date of the surface
    instruments=[],  # required — The set of instruments that define the surface.
    quotes=[],  # required — The set of market quotes that define the surface, in NormalVol or LogNormalVol terms.
    lineage="...",  # optional — Description of the complex market data&#39;s lineage e.g. &#39;FundAccountant_GreenQuality&#39;.
    version=Version(...),  # optional
    market_data_type="..."  # required — The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData, EquityCurveByPricesData, ConstantVolatilitySurface
)
```

- [LusidInstrument](LusidInstrument.md) — used in `instruments`
- [MarketQuote](MarketQuote.md) — used in `quotes`
- [Version](Version.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

