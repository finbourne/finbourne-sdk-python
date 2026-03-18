# FxForwardTenorPipsCurveData

Contains data (i.e. tenors and pips + metadata) for building fx forward curves (when combined with a spot rate and a date to build on)
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **base_date** | **datetime** | Required | EffectiveAt date of the quoted pip rates |
| **dom_ccy** | **str** | Required | Domestic currency of the fx forward |
| **fgn_ccy** | **str** | Required | Foreign currency of the fx forward |
| **tenors** | **List[str]** | Required | Tenors for which the forward rates apply.  For more information on tenors, see [knowledge base article KA-02097](https://support.lusid.com/knowledgebase/article/KA-02097) |
| **pip_rates** | **List[float]** | Required | Rates provided for the fx forward (price in FgnCcy per unit of DomCcy), expressed in pips |
| **lineage** | **str** | Optional | Description of the complex market data&#39;s lineage e.g. &#39;FundAccountant_GreenQuality&#39;. |
| **market_data_options** | [MarketDataOptions](MarketDataOptions.md) | Optional | *No description available.* |
| **calendars** | [List[FxTenorConvention]](FxTenorConvention.md) | Optional | The list of conventions that should be used when interpreting tenors as dates. |
| **spot_days_calculation_type** | **str** | Optional | Configures how to calculate the spot date from the build date using the Calendars provided.  Supported string (enumeration) values are: [ SingleCalendar, UnionCalendars ] |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **market_data_type** | **str** | Required | The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData, EquityCurveByPricesData, ConstantVolatilitySurface |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FxForwardTenorPipsCurveData import FxForwardTenorPipsCurveData

instance = FxForwardTenorPipsCurveData(
    base_date=datetime.now(),  # required — EffectiveAt date of the quoted pip rates
    dom_ccy="...",  # required — Domestic currency of the fx forward
    fgn_ccy="...",  # required — Foreign currency of the fx forward
    tenors=,  # required — Tenors for which the forward rates apply.  For more information on tenors, see [knowledge base article KA-02097](https://support.lusid.com/knowledgebase/article/KA-02097)
    pip_rates=,  # required — Rates provided for the fx forward (price in FgnCcy per unit of DomCcy), expressed in pips
    lineage="...",  # optional — Description of the complex market data&#39;s lineage e.g. &#39;FundAccountant_GreenQuality&#39;.
    market_data_options=MarketDataOptions(...),  # optional
    calendars=[],  # optional — The list of conventions that should be used when interpreting tenors as dates.
    spot_days_calculation_type="...",  # optional — Configures how to calculate the spot date from the build date using the Calendars provided.  Supported string (enumeration) values are: [ SingleCalendar, UnionCalendars ]
    version=Version(...),  # optional
    market_data_type="..."  # required — The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData, EquityCurveByPricesData, ConstantVolatilitySurface
)
```

- [MarketDataOptions](MarketDataOptions.md)
- [FxTenorConvention](FxTenorConvention.md) — used in `calendars`
- [Version](Version.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

