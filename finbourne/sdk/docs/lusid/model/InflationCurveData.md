# InflationCurveData

Market data for an inflation curve, represented by a list of zero-coupon inflation swap  instruments and corresponding market quotes.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **build_date** | **datetime** | Required | Build date of the curve - this is the reference date for resolution of the swap constituents. |
| **instruments** | [List[LusidInstrument]](LusidInstrument.md) | Required | The set of instruments that define the curve.  The only supported instrument type is: [InflationSwap]. |
| **quotes** | [List[MarketQuote]](MarketQuote.md) | Required | The market quotes corresponding to the the instruments used to define the curve |
| **seasonal_factors** | **List[float]** | Optional | Optional multiplicative seasonal adjustment factors, one per calendar month starting from January.  If provided there must be exactly 12 factors. |
| **output_type** | **str** | Optional | What the values of the built curve represent.  Supported string (enumeration) values are: [Level, Ratio].  Defaults to \&quot;Level\&quot; if not provided. |
| **lineage** | **str** | Optional | Description of the complex market data&#39;s lineage e.g. &#39;FundAccountant_GreenQuality&#39;. |
| **market_data_options** | [MarketDataOptions](MarketDataOptions.md) | Optional | *No description available.* |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **market_data_type** | **str** | Required | Available values: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData, EquityCurveByPricesData, ConstantVolatilitySurface, InflationCurveData. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.InflationCurveData import InflationCurveData

instance = InflationCurveData(
    build_date=datetime.now(),  # required — Build date of the curve - this is the reference date for resolution of the swap constituents.
    instruments=[],  # required — The set of instruments that define the curve.  The only supported instrument type is: [InflationSwap].
    quotes=[],  # required — The market quotes corresponding to the the instruments used to define the curve
    seasonal_factors=,  # optional — Optional multiplicative seasonal adjustment factors, one per calendar month starting from January.  If provided there must be exactly 12 factors.
    output_type="...",  # optional — What the values of the built curve represent.  Supported string (enumeration) values are: [Level, Ratio].  Defaults to \&quot;Level\&quot; if not provided.
    lineage="...",  # optional — Description of the complex market data&#39;s lineage e.g. &#39;FundAccountant_GreenQuality&#39;.
    market_data_options=MarketDataOptions(...),  # optional
    version=Version(...),  # optional
    market_data_type="..."  # required — Available values: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData, EquityCurveByPricesData, ConstantVolatilitySurface, InflationCurveData.
)
```

- [LusidInstrument](LusidInstrument.md) — used in `instruments`
- [MarketQuote](MarketQuote.md) — used in `quotes`
- [MarketDataOptions](MarketDataOptions.md)
- [Version](Version.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

