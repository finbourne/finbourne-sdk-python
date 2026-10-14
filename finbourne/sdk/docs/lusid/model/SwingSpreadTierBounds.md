# SwingSpreadTierBounds

The bounds of the spread tier a net cashflow fell in.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **lower_bound_exclusive** | **float** | Required | The tier&#39;s lower bound, which the net cashflow was above. |
| **upper_bound_inclusive** | **float** | Optional | The tier&#39;s upper bound, which the net cashflow was at or below. Absent for the unbounded last tier. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.SwingSpreadTierBounds import SwingSpreadTierBounds

instance = SwingSpreadTierBounds(
    lower_bound_exclusive=0.0,  # required — The tier&#39;s lower bound, which the net cashflow was above.
    upper_bound_inclusive=0.0  # optional — The tier&#39;s upper bound, which the net cashflow was at or below. Absent for the unbounded last tier.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

