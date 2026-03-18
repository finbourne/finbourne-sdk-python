# SetShareClassInstrumentsRequest

The request used to create a Fund.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **share_class_instrument_scopes** | **List[str]** | Required | The scopes in which the instruments lie, currently limited to one. |
| **share_class_instruments** | [List[InstrumentResolutionDetail]](InstrumentResolutionDetail.md) | Required | Details the user-provided instrument identifiers and the instrument resolved from them. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.SetShareClassInstrumentsRequest import SetShareClassInstrumentsRequest

instance = SetShareClassInstrumentsRequest(
    share_class_instrument_scopes=,  # required — The scopes in which the instruments lie, currently limited to one.
    share_class_instruments=[]  # required — Details the user-provided instrument identifiers and the instrument resolved from them.
)
```

- [InstrumentResolutionDetail](InstrumentResolutionDetail.md) — used in `share_class_instruments`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

