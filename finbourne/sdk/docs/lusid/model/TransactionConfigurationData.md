# TransactionConfigurationData

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **aliases** | [List[TransactionConfigurationTypeAlias]](TransactionConfigurationTypeAlias.md) | Required | List of transaction types that map to this specific transaction configuration |
| **movements** | [List[TransactionConfigurationMovementData]](TransactionConfigurationMovementData.md) | Required | Movement data for the transaction type |
| **properties** | [Dict[str, PerpetualProperty]](PerpetualProperty.md) | Optional | Properties attached to the transaction type |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TransactionConfigurationData import TransactionConfigurationData

instance = TransactionConfigurationData(
    aliases=[],  # required — List of transaction types that map to this specific transaction configuration
    movements=[],  # required — Movement data for the transaction type
    properties=PerpetualProperty(...)  # optional — Properties attached to the transaction type
)
```


## Related Models

- [TransactionConfigurationTypeAlias](TransactionConfigurationTypeAlias.md) — used in `aliases`
- [TransactionConfigurationMovementData](TransactionConfigurationMovementData.md) — used in `movements`
- [PerpetualProperty](PerpetualProperty.md) — used in `properties`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

