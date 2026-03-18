# SetTransactionConfigurationAlias

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **type** | **str** | Required | *No description available.* |
| **description** | **str** | Required | *No description available.* |
| **transaction_class** | **str** | Required | *No description available.* |
| **transaction_role** | **str** | Required | *No description available.* |
| **is_default** | **bool** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.SetTransactionConfigurationAlias import SetTransactionConfigurationAlias

instance = SetTransactionConfigurationAlias(
    type="...",  # required
    description="...",  # required
    transaction_class="...",  # required
    transaction_role="...",  # required
    is_default=True  # optional
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

