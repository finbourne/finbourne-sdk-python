# SwingSpreadTier

One tier of spread: the band of net cashflow it covers and the spread applied when the flow falls in it.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **lower_bound_exclusive** | **float** | Required | The size of net cashflow, as a magnitude, above which the tier applies. Zero or more; zero on the first tier swings on any net flow. |
| **upper_bound_inclusive** | **float** | Optional | The size of net cashflow, as a magnitude, up to and including which the tier applies. Omit it on the last tier, which covers every larger flow. |
| **bps** | **float** | Required | The spread, in basis points of the baseline price, applied when the net cashflow falls in the tier. Zero or more. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.SwingSpreadTier import SwingSpreadTier

instance = SwingSpreadTier(
    lower_bound_exclusive=0.0,  # required — The size of net cashflow, as a magnitude, above which the tier applies. Zero or more; zero on the first tier swings on any net flow.
    upper_bound_inclusive=0.0,  # optional — The size of net cashflow, as a magnitude, up to and including which the tier applies. Omit it on the last tier, which covers every larger flow.
    bps=0.0  # required — The spread, in basis points of the baseline price, applied when the net cashflow falls in the tier. Zero or more.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

