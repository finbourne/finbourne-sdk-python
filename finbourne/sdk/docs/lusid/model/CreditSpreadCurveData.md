# CreditSpreadCurveData

A credit spread curve matching tenors against par spread quotes
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **base_date** | **datetime** | Required | EffectiveAt date of the quoted rates |
| **dom_ccy** | **str** | Required | Domestic currency of the curve |
| **tenors** | **List[str]** | Required | The tenors for which the rates apply  For more information on tenors, see [knowledge base article KA-02097](https://support.lusid.com/knowledgebase/article/KA-02097) |
| **spreads** | **List[float]** | Required | Par spread quotes corresponding to the tenors. |
| **recovery_rate** | **float** | Required | The recovery rate in default. |
| **reference_date** | **datetime** | Optional | If tenors are provided, this is the date against which the tenors will be resolved.  This is of importance to CDX spread quotes, which are usually quoted in tenors relative to the CDX start date.  In this case, the ReferenceDate would be equal to the CDX start date, and the BaseDate would be the date for which the spreads are valid.  If not provided, this defaults to the BaseDate of the curve. |
| **maturities** | **List[datetime]** | Optional | The maturity dates for which the rates apply.  Either tenors or maturities should be provided, not both. |
| **lineage** | **str** | Optional | Description of the complex market data&#39;s lineage e.g. &#39;FundAccountant_GreenQuality&#39;. |
| **market_data_options** | [MarketDataOptions](MarketDataOptions.md) | Optional | *No description available.* |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **market_data_type** | **str** | Required | The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData, EquityCurveByPricesData, ConstantVolatilitySurface |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CreditSpreadCurveData import CreditSpreadCurveData

instance = CreditSpreadCurveData(
    base_date=datetime.now(),  # required — EffectiveAt date of the quoted rates
    dom_ccy="...",  # required — Domestic currency of the curve
    tenors=,  # required — The tenors for which the rates apply  For more information on tenors, see [knowledge base article KA-02097](https://support.lusid.com/knowledgebase/article/KA-02097)
    spreads=,  # required — Par spread quotes corresponding to the tenors.
    recovery_rate=0.0,  # required — The recovery rate in default.
    reference_date=datetime.now(),  # optional — If tenors are provided, this is the date against which the tenors will be resolved.  This is of importance to CDX spread quotes, which are usually quoted in tenors relative to the CDX start date.  In this case, the ReferenceDate would be equal to the CDX start date, and the BaseDate would be the date for which the spreads are valid.  If not provided, this defaults to the BaseDate of the curve.
    maturities=,  # optional — The maturity dates for which the rates apply.  Either tenors or maturities should be provided, not both.
    lineage="...",  # optional — Description of the complex market data&#39;s lineage e.g. &#39;FundAccountant_GreenQuality&#39;.
    market_data_options=MarketDataOptions(...),  # optional
    version=Version(...),  # optional
    market_data_type="..."  # required — The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData, EquityCurveByPricesData, ConstantVolatilitySurface
)
```

- [MarketDataOptions](MarketDataOptions.md)
- [Version](Version.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

