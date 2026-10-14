# SwingSpreads

The stored spreads a Single fund swings by, one set for each direction of net cashflow.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **inflow** | [DirectionSpreads](DirectionSpreads.md) | Optional | *No description available.* |
| **outflow** | [DirectionSpreads](DirectionSpreads.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.SwingSpreads import SwingSpreads

instance = SwingSpreads(
    inflow=DirectionSpreads(...),  # optional
    outflow=DirectionSpreads(...)  # optional
)
```


## Related Models

- [DirectionSpreads](DirectionSpreads.md)
- [DirectionSpreads](DirectionSpreads.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

