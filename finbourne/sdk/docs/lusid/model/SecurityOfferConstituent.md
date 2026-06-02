# SecurityOfferConstituent

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **new_instrument** | [NewInstrument](NewInstrument.md) | Required | *No description available.* |
| **units_ratio** | [UnitsRatio](UnitsRatio.md) | Required | *No description available.* |
| **settlement_date** | **datetime** | Required | *No description available.* |
| **min_piece_size** | **float** | Optional | *No description available.* |
| **min_increment** | **float** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.SecurityOfferConstituent import SecurityOfferConstituent

instance = SecurityOfferConstituent(
    new_instrument=NewInstrument(...),  # required
    units_ratio=UnitsRatio(...),  # required
    settlement_date=datetime.now(),  # required
    min_piece_size=0.0,  # optional
    min_increment=0.0  # optional
)
```


## Related Models

- [NewInstrument](NewInstrument.md)
- [UnitsRatio](UnitsRatio.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

