# UpsertTranslationScriptRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [TranslationScriptId](TranslationScriptId.md) | Required | *No description available.* |
| **body** | **str** | Required | Body of the translation script, i.e. the actual translation code. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpsertTranslationScriptRequest import UpsertTranslationScriptRequest

instance = UpsertTranslationScriptRequest(
    id=TranslationScriptId(...),  # required
    body="..."  # required — Body of the translation script, i.e. the actual translation code.
)
```


## Related Models

- [TranslationScriptId](TranslationScriptId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

