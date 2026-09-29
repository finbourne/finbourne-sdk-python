# FxForwardPipsCurveData

Contains data (i.e. dates and pips + metadata) for building fx forward curves (when combined with a spot rate to build on)
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **base_date** | **datetime** | Required | EffectiveAt date of the quoted pip rates |
| **dom_ccy** | **str** | Required | Domestic currency of the fx forward |
| **fgn_ccy** | **str** | Required | Foreign currency of the fx forward |
| **dates** | **List[datetime]** | Required | Dates for which the forward rates apply |
| **pip_rates** | **List[float]** | Required | Rates provided for the fx forward (price in FgnCcy per unit of DomCcy), expressed in pips |
| **pip_multiplier** | **float** | Optional | Optional. The scaling factor applied to the pip rates to convert them into a forward rate adjustment,  so that forwardRate &#x3D; spotRate + pipRate * pipMultiplier. Must be strictly positive when supplied.  When omitted, the market convention for the currency pair is used:  0.01 when the foreign (quote) currency is JPY, and 0.0001 (the four-decimal-place convention of the major pairs) otherwise. |
| **lineage** | **str** | Optional | Description of the complex market data&#39;s lineage e.g. &#39;FundAccountant_GreenQuality&#39;. |
| **market_data_options** | [MarketDataOptions](MarketDataOptions.md) | Optional | *No description available.* |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **market_data_type** | **str** | Required | Available values: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData, EquityCurveByPricesData, ConstantVolatilitySurface, InflationCurveData. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FxForwardPipsCurveData import FxForwardPipsCurveData

instance = FxForwardPipsCurveData(
    base_date=datetime.now(),  # required — EffectiveAt date of the quoted pip rates
    dom_ccy="...",  # required — Domestic currency of the fx forward
    fgn_ccy="...",  # required — Foreign currency of the fx forward
    dates=,  # required — Dates for which the forward rates apply
    pip_rates=,  # required — Rates provided for the fx forward (price in FgnCcy per unit of DomCcy), expressed in pips
    pip_multiplier=0.0,  # optional — Optional. The scaling factor applied to the pip rates to convert them into a forward rate adjustment,  so that forwardRate &#x3D; spotRate + pipRate * pipMultiplier. Must be strictly positive when supplied.  When omitted, the market convention for the currency pair is used:  0.01 when the foreign (quote) currency is JPY, and 0.0001 (the four-decimal-place convention of the major pairs) otherwise.
    lineage="...",  # optional — Description of the complex market data&#39;s lineage e.g. &#39;FundAccountant_GreenQuality&#39;.
    market_data_options=MarketDataOptions(...),  # optional
    version=Version(...),  # optional
    market_data_type="..."  # required — Available values: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData, EquityCurveByPricesData, ConstantVolatilitySurface, InflationCurveData.
)
```

- [MarketDataOptions](MarketDataOptions.md)
- [Version](Version.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

