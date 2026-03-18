# TranslationInput

The input to a translation script.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **entity** | **str** | Required | The serialised entity to be passed to the translation script. This could represent e.g. an instrument in any  dialect. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TranslationInput import TranslationInput

instance = TranslationInput(
    entity="..."  # required — The serialised entity to be passed to the translation script. This could represent e.g. an instrument in any  dialect.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

