# TranslateEntitiesRequest

Request to translate financial entities with a specified script stored in LUSID,  specified in the request by its id. The output of the translation is validated against a dialect stored in LUSID,  again specified in the request by its id.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **entity_payloads** | [Dict[str, TranslationInput]](TranslationInput.md) | Required | Entity payloads to be translated, indexed by (ephemeral) unique correlation ids. |
| **script_id** | [TranslationScriptId](TranslationScriptId.md) | Required | *No description available.* |
| **dialect_id** | [DialectId](DialectId.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TranslateEntitiesRequest import TranslateEntitiesRequest

instance = TranslateEntitiesRequest(
    entity_payloads=TranslationInput(...),  # required — Entity payloads to be translated, indexed by (ephemeral) unique correlation ids.
    script_id=TranslationScriptId(...),  # required
    dialect_id=DialectId(...)  # optional
)
```


## Related Models

- [TranslationInput](TranslationInput.md) — used in `entity_payloads`
- [TranslationScriptId](TranslationScriptId.md)
- [DialectId](DialectId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

