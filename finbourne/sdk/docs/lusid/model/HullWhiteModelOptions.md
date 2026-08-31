# HullWhiteModelOptions

Model options for the Hull-White one-factor lattice pricer.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **mean_reversion** | **float** | Optional | The mean reversion speed of the short rate. Must be strictly positive. Defaults to 0.03. |
| **volatility** | **float** | Optional | The normal (absolute) volatility of the short rate, e.g. 0.008 for 80bp per year. Defaults to 0.008. |
| **lattice_steps** | **int** | Optional | The number of uniform time steps in the lattice. More steps give a finer discretisation  of the short-rate process at greater computational cost. Defaults to 200. |
| **mean_reversion_by_currency** | **Dict[str, float]** | Optional | Per-currency mean-reversion overrides, keyed by ISO currency code.  A currency absent from this map uses MeanReversion. |
| **volatility_by_currency** | **Dict[str, float]** | Optional | Per-currency short-rate volatility overrides, keyed by ISO currency code.  A currency absent from this map uses Volatility. Short-rate volatility is a per-currency  quantity in practice, so a book spanning several currencies can calibrate each currency  separately instead of sharing a single global figure. |
| **model_options_type** | **str** | Required | Available values: Invalid, OpaqueModelOptions, EmptyModelOptions, IndexModelOptions, FxForwardModelOptions, FundingLegModelOptions, EquityModelOptions, CdsModelOptions, FlexibleLoanPricerOptions, HullWhiteModelOptions, BondLookupModelOptions. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.HullWhiteModelOptions import HullWhiteModelOptions

instance = HullWhiteModelOptions(
    mean_reversion=0.0,  # optional — The mean reversion speed of the short rate. Must be strictly positive. Defaults to 0.03.
    volatility=0.0,  # optional — The normal (absolute) volatility of the short rate, e.g. 0.008 for 80bp per year. Defaults to 0.008.
    lattice_steps=0,  # optional — The number of uniform time steps in the lattice. More steps give a finer discretisation  of the short-rate process at greater computational cost. Defaults to 200.
    mean_reversion_by_currency=,  # optional — Per-currency mean-reversion overrides, keyed by ISO currency code.  A currency absent from this map uses MeanReversion.
    volatility_by_currency=,  # optional — Per-currency short-rate volatility overrides, keyed by ISO currency code.  A currency absent from this map uses Volatility. Short-rate volatility is a per-currency  quantity in practice, so a book spanning several currencies can calibrate each currency  separately instead of sharing a single global figure.
    model_options_type="..."  # required — Available values: Invalid, OpaqueModelOptions, EmptyModelOptions, IndexModelOptions, FxForwardModelOptions, FundingLegModelOptions, EquityModelOptions, CdsModelOptions, FlexibleLoanPricerOptions, HullWhiteModelOptions, BondLookupModelOptions.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

