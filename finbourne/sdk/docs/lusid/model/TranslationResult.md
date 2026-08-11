# TranslationResult

The result of invoking a translation script.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **entity** | **str** | Required | The serialised entity the translation script produced. |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Required | Any properties the translation script produced. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TranslationResult import TranslationResult

instance = TranslationResult(
    entity="...",  # required — The serialised entity the translation script produced.
    properties=ModelProperty(...)  # required — Any properties the translation script produced.
)
```

- [ModelProperty](ModelProperty.md) — used in `properties`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

