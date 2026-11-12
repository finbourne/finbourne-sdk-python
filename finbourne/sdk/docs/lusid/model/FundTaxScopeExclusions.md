# FundTaxScopeExclusions

What the UK chargeable-gains figures leave out of the pooled computation.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **instrument_types** | **List[str]** | Required | Instrument types that stay on the portfolio&#39;s ordinary accounting method rather than being pooled, by name. |
| **leaf_outcomes** | **List[str]** | Required | Disposal-leg outcomes the configured regime options disapply. Empty under the standard options. |
| **applied_in_figures** | **bool** | Required | Whether the engine enforces these exclusions when building the pooled lots and gains. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FundTaxScopeExclusions import FundTaxScopeExclusions

instance = FundTaxScopeExclusions(
    instrument_types=,  # required — Instrument types that stay on the portfolio&#39;s ordinary accounting method rather than being pooled, by name.
    leaf_outcomes=,  # required — Disposal-leg outcomes the configured regime options disapply. Empty under the standard options.
    applied_in_figures=True  # required — Whether the engine enforces these exclusions when building the pooled lots and gains.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

