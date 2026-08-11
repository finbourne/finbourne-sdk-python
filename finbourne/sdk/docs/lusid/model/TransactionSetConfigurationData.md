# TransactionSetConfigurationData

A collection of the data required to configure transaction types..
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **transaction_configs** | [List[TransactionConfigurationData]](TransactionConfigurationData.md) | Required | Collection of transaction type models |
| **side_definitions** | [List[SideConfigurationData]](SideConfigurationData.md) | Optional | Collection of side definitions |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TransactionSetConfigurationData import TransactionSetConfigurationData

instance = TransactionSetConfigurationData(
    transaction_configs=[],  # required — Collection of transaction type models
    side_definitions=[],  # optional — Collection of side definitions
    links=[]  # optional
)
```


## Related Models

- [TransactionConfigurationData](TransactionConfigurationData.md) — used in `transaction_configs`
- [SideConfigurationData](SideConfigurationData.md) — used in `side_definitions`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

