# DiscountFactorCurveData

A curve containing discount factors and dates to which they apply
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **base_date** | **datetime** | Required | BaseDate for the Curve |
| **dates** | **List[datetime]** | Required | Dates for which the discount factors apply |
| **discount_factors** | **List[float]** | Required | Discount factors to be applied to cashflow on the specified dates |
| **lineage** | **str** | Optional | Description of the complex market data&#39;s lineage e.g. &#39;FundAccountant_GreenQuality&#39;. |
| **market_data_options** | [MarketDataOptions](MarketDataOptions.md) | Optional | *No description available.* |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **market_data_type** | **str** | Required | The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData, EquityCurveByPricesData, ConstantVolatilitySurface |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.DiscountFactorCurveData import DiscountFactorCurveData

instance = DiscountFactorCurveData(
    base_date=datetime.now(),  # required — BaseDate for the Curve
    dates=,  # required — Dates for which the discount factors apply
    discount_factors=,  # required — Discount factors to be applied to cashflow on the specified dates
    lineage="...",  # optional — Description of the complex market data&#39;s lineage e.g. &#39;FundAccountant_GreenQuality&#39;.
    market_data_options=MarketDataOptions(...),  # optional
    version=Version(...),  # optional
    market_data_type="..."  # required — The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData, EquityCurveByPricesData, ConstantVolatilitySurface
)
```

- [MarketDataOptions](MarketDataOptions.md)
- [Version](Version.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

