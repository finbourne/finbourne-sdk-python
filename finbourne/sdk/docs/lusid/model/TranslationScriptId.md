# TranslationScriptId

Id of the Translation Script.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **scope** | **str** | Required | Scope of the translation script. |
| **code** | **str** | Required | Code of the translation script. |
| **version** | **str** | Required | Semantic Version of the translation script of the form MAJOR.MINOR.PATCH. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TranslationScriptId import TranslationScriptId

instance = TranslationScriptId(
    scope="...",  # required — Scope of the translation script.
    code="...",  # required — Code of the translation script.
    version="..."  # required — Semantic Version of the translation script of the form MAJOR.MINOR.PATCH.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

