# SetPersonIdentifiersRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **identifiers** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | Identifiers to set for a Person. Identifiers not included in the request will not be amended. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.SetPersonIdentifiersRequest import SetPersonIdentifiersRequest

instance = SetPersonIdentifiersRequest(
    identifiers=ModelProperty(...)  # optional — Identifiers to set for a Person. Identifiers not included in the request will not be amended.
)
```


## Related Models

- [ModelProperty](ModelProperty.md) — used in `identifiers`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

