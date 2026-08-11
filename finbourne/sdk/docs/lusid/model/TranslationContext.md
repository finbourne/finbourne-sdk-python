# TranslationContext

Options for overriding default scripted translation configuration.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **disable_scripted_translation** | **bool** | Optional | *No description available.* |
| **script_map** | [ScriptMapReference](ScriptMapReference.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TranslationContext import TranslationContext

instance = TranslationContext(
    disable_scripted_translation=True,  # optional
    script_map=ScriptMapReference(...)  # optional
)
```

- [ScriptMapReference](ScriptMapReference.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

