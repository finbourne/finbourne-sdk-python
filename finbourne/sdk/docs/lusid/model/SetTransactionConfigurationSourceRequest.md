# SetTransactionConfigurationSourceRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **aliases** | [List[SetTransactionConfigurationAlias]](SetTransactionConfigurationAlias.md) | Required | *No description available.* |
| **movements** | [List[TransactionConfigurationMovementDataRequest]](TransactionConfigurationMovementDataRequest.md) | Required | *No description available.* |
| **properties** | [Dict[str, PerpetualProperty]](PerpetualProperty.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.SetTransactionConfigurationSourceRequest import SetTransactionConfigurationSourceRequest

instance = SetTransactionConfigurationSourceRequest(
    aliases=[],  # required
    movements=[],  # required
    properties=PerpetualProperty(...)  # optional
)
```


## Related Models

- [SetTransactionConfigurationAlias](SetTransactionConfigurationAlias.md)
- [TransactionConfigurationMovementDataRequest](TransactionConfigurationMovementDataRequest.md)
- [PerpetualProperty](PerpetualProperty.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

