# SwingSpreadApplied

The stored spread applied to a share class's baseline price and the tier it came from.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **bps** | **float** | Required | The spread applied, in basis points. |
| **tier_matched** | [SwingSpreadTierBounds](SwingSpreadTierBounds.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.SwingSpreadApplied import SwingSpreadApplied

instance = SwingSpreadApplied(
    bps=0.0,  # required — The spread applied, in basis points.
    tier_matched=SwingSpreadTierBounds(...)  # required
)
```

- [SwingSpreadTierBounds](SwingSpreadTierBounds.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

