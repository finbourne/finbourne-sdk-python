# CollateralInstrument

Wrapper for one instrument in a larger collateral basket, as part of a repurchase agreement modelled as a FlexibleRepo.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **units** | **float** | Required | The amount of the instrument in the basket for this repurchase agreement. |
| **instrument** | [MasteredInstrument](MasteredInstrument.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CollateralInstrument import CollateralInstrument

instance = CollateralInstrument(
    units=0.0,  # required — The amount of the instrument in the basket for this repurchase agreement.
    instrument=MasteredInstrument(...)  # required
)
```

- [MasteredInstrument](MasteredInstrument.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

