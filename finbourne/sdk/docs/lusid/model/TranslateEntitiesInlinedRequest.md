# TranslateEntitiesInlinedRequest

Request to translate financial entities with a given script body.  The output of the translation is validated against a schema specified in the request.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **entity_payloads** | [Dict[str, TranslationInput]](TranslationInput.md) | Required | Entity payloads to be translated indexed by (ephemeral) unique correlation ids. |
| **script_body** | **str** | Required | The body of the translation script to use for translating the entities. |
| **var_schema** | [DialectSchema](DialectSchema.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TranslateEntitiesInlinedRequest import TranslateEntitiesInlinedRequest

instance = TranslateEntitiesInlinedRequest(
    entity_payloads=TranslationInput(...),  # required — Entity payloads to be translated indexed by (ephemeral) unique correlation ids.
    script_body="...",  # required — The body of the translation script to use for translating the entities.
    var_schema=DialectSchema(...)  # optional
)
```


## Related Models

- [TranslationInput](TranslationInput.md) — used in `entity_payloads`
- [DialectSchema](DialectSchema.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

