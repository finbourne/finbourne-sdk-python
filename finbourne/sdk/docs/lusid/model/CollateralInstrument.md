# CollateralInstrument

Wrapper for one instrument in a larger collateral basket, as part of a repurchase agreement modelled as a FlexibleRepo.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **units** | **float** | Required | The amount of the instrument in the basket for this repurchase agreement. |
| **instrument** | [MasteredInstrument](MasteredInstrument.md) | Required | *No description available.* |
| **collateral_start_date** | **datetime** | Optional | The date from which the instrument is held as collateral for this repurchase agreement.  Read only: an instrument upsert cannot set or change it. An existing value must be sent back unchanged.  When not set, the instrument is held from the StartDate of the FlexibleRepo. |
| **collateral_end_date** | **datetime** | Optional | The date on which the instrument stops being held as collateral for this repurchase agreement.  Read only: an instrument upsert cannot set or change it. An existing value must be sent back unchanged.  When not set, the instrument is held until the MaturityDate of the FlexibleRepo. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CollateralInstrument import CollateralInstrument

instance = CollateralInstrument(
    units=0.0,  # required — The amount of the instrument in the basket for this repurchase agreement.
    instrument=MasteredInstrument(...),  # required
    collateral_start_date=datetime.now(),  # optional — The date from which the instrument is held as collateral for this repurchase agreement.  Read only: an instrument upsert cannot set or change it. An existing value must be sent back unchanged.  When not set, the instrument is held from the StartDate of the FlexibleRepo.
    collateral_end_date=datetime.now()  # optional — The date on which the instrument stops being held as collateral for this repurchase agreement.  Read only: an instrument upsert cannot set or change it. An existing value must be sent back unchanged.  When not set, the instrument is held until the MaturityDate of the FlexibleRepo.
)
```

- [MasteredInstrument](MasteredInstrument.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

