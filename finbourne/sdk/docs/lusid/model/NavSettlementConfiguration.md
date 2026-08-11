# NavSettlementConfiguration

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **cash_settlement** | [NavSettlementConfigurationCategory](NavSettlementConfigurationCategory.md) | Required | *No description available.* |
| **deferred_cash_receipt** | [NavSettlementConfigurationCategory](NavSettlementConfigurationCategory.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.NavSettlementConfiguration import NavSettlementConfiguration

instance = NavSettlementConfiguration(
    cash_settlement=NavSettlementConfigurationCategory(...),  # required
    deferred_cash_receipt=NavSettlementConfigurationCategory(...)  # required
)
```


## Related Models

- [NavSettlementConfigurationCategory](NavSettlementConfigurationCategory.md)
- [NavSettlementConfigurationCategory](NavSettlementConfigurationCategory.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

