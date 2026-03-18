# IrVolCubeData

Market Data required to build a volatility cube for swaption pricing,  represented by a list of instruments and corresponding market quotes
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **base_date** | **datetime** | Required | Base date of the cube - this is the start date of the swaptions on the cube. |
| **instruments** | [List[LusidInstrument]](LusidInstrument.md) | Required | Retrieve the set of instruments that define the cube. |
| **quotes** | [List[MarketQuote]](MarketQuote.md) | Required | Access the set of quotes that define the cube. |
| **lineage** | **str** | Optional | Description of the complex market data&#39;s lineage e.g. &#39;FundAccountant_GreenQuality&#39;. |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **market_data_type** | **str** | Required | The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData, EquityCurveByPricesData, ConstantVolatilitySurface |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.IrVolCubeData import IrVolCubeData

instance = IrVolCubeData(
    base_date=datetime.now(),  # required — Base date of the cube - this is the start date of the swaptions on the cube.
    instruments=[],  # required — Retrieve the set of instruments that define the cube.
    quotes=[],  # required — Access the set of quotes that define the cube.
    lineage="...",  # optional — Description of the complex market data&#39;s lineage e.g. &#39;FundAccountant_GreenQuality&#39;.
    version=Version(...),  # optional
    market_data_type="..."  # required — The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData, EquityCurveByPricesData, ConstantVolatilitySurface
)
```

- [LusidInstrument](LusidInstrument.md) — used in `instruments`
- [MarketQuote](MarketQuote.md) — used in `quotes`
- [Version](Version.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

