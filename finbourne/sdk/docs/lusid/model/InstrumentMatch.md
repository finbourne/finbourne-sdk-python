# InstrumentMatch

A collection of instrument search results
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **mastered_instruments** | [List[InstrumentDefinition]](InstrumentDefinition.md) | Optional | The collection of instruments found by the search which have been mastered within LUSID. |
| **external_instruments** | [List[InstrumentDefinition]](InstrumentDefinition.md) | Optional | The collection of instruments found by the search which have not been mastered within LUSID and instead found via OpenFIGI. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.InstrumentMatch import InstrumentMatch

instance = InstrumentMatch(
    mastered_instruments=[],  # optional — The collection of instruments found by the search which have been mastered within LUSID.
    external_instruments=[]  # optional — The collection of instruments found by the search which have not been mastered within LUSID and instead found via OpenFIGI.
)
```


## Related Models

- [InstrumentDefinition](InstrumentDefinition.md) — used in `mastered_instruments`
- [InstrumentDefinition](InstrumentDefinition.md) — used in `external_instruments`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

