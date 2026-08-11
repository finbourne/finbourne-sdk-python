# TranslateInstrumentDefinitionsRequest

A collection of instruments to translate, along with the target dialect to translate into.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **instruments** | [Dict[str, LusidInstrument]](LusidInstrument.md) | Required | The collection of instruments to translate.                Each instrument definition should be keyed by a unique correlation id. This id is ephemeral  and is not stored by LUSID. It serves only as a way to easily identify each instrument in the response.                Any instrument that is not already in the LUSID dialect should be given as an ExoticInstrument. |
| **dialect** | **str** | Required | The target dialect that the given instruments should be translated to. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TranslateInstrumentDefinitionsRequest import TranslateInstrumentDefinitionsRequest

instance = TranslateInstrumentDefinitionsRequest(
    instruments=LusidInstrument(...),  # required — The collection of instruments to translate.                Each instrument definition should be keyed by a unique correlation id. This id is ephemeral  and is not stored by LUSID. It serves only as a way to easily identify each instrument in the response.                Any instrument that is not already in the LUSID dialect should be given as an ExoticInstrument.
    dialect="..."  # required — The target dialect that the given instruments should be translated to.
)
```


## Related Models

- [LusidInstrument](LusidInstrument.md) — used in `instruments`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

