# TransactionSetConfigurationDataRequest

A bundle of requests to configure a set of transaction types.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **transaction_config_requests** | [List[TransactionConfigurationDataRequest]](TransactionConfigurationDataRequest.md) | Required | Collection of transaction type models |
| **side_config_requests** | [List[SideConfigurationDataRequest]](SideConfigurationDataRequest.md) | Optional | Collection of side definition requests. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TransactionSetConfigurationDataRequest import TransactionSetConfigurationDataRequest

instance = TransactionSetConfigurationDataRequest(
    transaction_config_requests=[],  # required — Collection of transaction type models
    side_config_requests=[]  # optional — Collection of side definition requests.
)
```


## Related Models

- [TransactionConfigurationDataRequest](TransactionConfigurationDataRequest.md) — used in `transaction_config_requests`
- [SideConfigurationDataRequest](SideConfigurationDataRequest.md) — used in `side_config_requests`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

