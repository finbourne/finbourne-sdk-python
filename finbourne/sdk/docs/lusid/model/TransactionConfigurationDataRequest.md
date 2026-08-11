# TransactionConfigurationDataRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **aliases** | [List[TransactionConfigurationTypeAlias]](TransactionConfigurationTypeAlias.md) | Required | List of transaction codes that map to this specific transaction model |
| **movements** | [List[TransactionConfigurationMovementDataRequest]](TransactionConfigurationMovementDataRequest.md) | Required | Movement data for the transaction code |
| **properties** | [Dict[str, PerpetualProperty]](PerpetualProperty.md) | Optional | Properties attached to the underlying holding. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TransactionConfigurationDataRequest import TransactionConfigurationDataRequest

instance = TransactionConfigurationDataRequest(
    aliases=[],  # required — List of transaction codes that map to this specific transaction model
    movements=[],  # required — Movement data for the transaction code
    properties=PerpetualProperty(...)  # optional — Properties attached to the underlying holding.
)
```


## Related Models

- [TransactionConfigurationTypeAlias](TransactionConfigurationTypeAlias.md) — used in `aliases`
- [TransactionConfigurationMovementDataRequest](TransactionConfigurationMovementDataRequest.md) — used in `movements`
- [PerpetualProperty](PerpetualProperty.md) — used in `properties`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

