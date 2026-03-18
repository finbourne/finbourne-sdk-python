# WeightedInstruments

Class that models a set of instruments of which each has some quantity and can be identified by a unique label.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **instruments** | [List[WeightedInstrument]](WeightedInstrument.md) | Required | The instruments that are held in the set. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.WeightedInstruments import WeightedInstruments

instance = WeightedInstruments(
    instruments=[]  # required — The instruments that are held in the set.
)
```


## Related Models

- [WeightedInstrument](WeightedInstrument.md) — used in `instruments`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

