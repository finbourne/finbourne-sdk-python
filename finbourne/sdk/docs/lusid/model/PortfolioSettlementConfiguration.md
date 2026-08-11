# PortfolioSettlementConfiguration

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **stock_settlement** | [SettlementConfigurationCategory](SettlementConfigurationCategory.md) | Optional | *No description available.* |
| **cash_settlement** | [SettlementConfigurationCategory](SettlementConfigurationCategory.md) | Optional | *No description available.* |
| **deferred_cash_receipt** | [SettlementConfigurationCategory](SettlementConfigurationCategory.md) | Optional | *No description available.* |
| **transaction_matching_alternative_id** | [TransactionMatchingAlternativeId](TransactionMatchingAlternativeId.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PortfolioSettlementConfiguration import PortfolioSettlementConfiguration

instance = PortfolioSettlementConfiguration(
    stock_settlement=SettlementConfigurationCategory(...),  # optional
    cash_settlement=SettlementConfigurationCategory(...),  # optional
    deferred_cash_receipt=SettlementConfigurationCategory(...),  # optional
    transaction_matching_alternative_id=TransactionMatchingAlternativeId(...)  # optional
)
```


## Related Models

- [SettlementConfigurationCategory](SettlementConfigurationCategory.md)
- [SettlementConfigurationCategory](SettlementConfigurationCategory.md)
- [SettlementConfigurationCategory](SettlementConfigurationCategory.md)
- [TransactionMatchingAlternativeId](TransactionMatchingAlternativeId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

