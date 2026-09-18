# RunCheckRequest

Exactly one dataset must be provided, matching the check definition's datasetSchema.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **lusid_entity_dataset** | [LusidEntityDataset](LusidEntityDataset.md) | Optional | *No description available.* |
| **limit_individual_breaches_per_rule** | **int** | Optional | The maximum number of individual breaches to return per rule. Defaults to 100 if not specified. |
| **portfolio_holding_dataset** | [PortfolioHoldingDataset](PortfolioHoldingDataset.md) | Optional | *No description available.* |
| **portfolio_transaction_dataset** | [PortfolioTransactionDataset](PortfolioTransactionDataset.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RunCheckRequest import RunCheckRequest

instance = RunCheckRequest(
    lusid_entity_dataset=LusidEntityDataset(...),  # optional
    limit_individual_breaches_per_rule=0,  # optional — The maximum number of individual breaches to return per rule. Defaults to 100 if not specified.
    portfolio_holding_dataset=PortfolioHoldingDataset(...),  # optional
    portfolio_transaction_dataset=PortfolioTransactionDataset(...)  # optional
)
```


## Related Models

- [LusidEntityDataset](LusidEntityDataset.md)
- [PortfolioHoldingDataset](PortfolioHoldingDataset.md)
- [PortfolioTransactionDataset](PortfolioTransactionDataset.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

