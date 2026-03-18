# TranslateEntitiesResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **values** | [Dict[str, TranslationResult]](TranslationResult.md) | Optional | The entities that were successfully translated. |
| **failed** | [Dict[str, ErrorDetail]](ErrorDetail.md) | Optional | The error details corresponding to entities that failed to be translated. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TranslateEntitiesResponse import TranslateEntitiesResponse

instance = TranslateEntitiesResponse(
    values=TranslationResult(...),  # optional — The entities that were successfully translated.
    failed=ErrorDetail(...),  # optional — The error details corresponding to entities that failed to be translated.
    links=[]  # optional
)
```


## Related Models

- [TranslationResult](TranslationResult.md) — used in `values`
- [ErrorDetail](ErrorDetail.md) — used in `failed`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

