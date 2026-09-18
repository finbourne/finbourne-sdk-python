# PortfolioTransactionDataset

Contains the run-time parameters that are appropriate for check definitions  with datasetSchema.type = \"PortfolioContents\" and datasetSchema.entityType = \"Transaction\"
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **as_at** | **datetime** | Optional | The asAt date to fetch the data. Nullable. Defaults to latest. |
| **from_effective_date** | **datetime** | Optional | The earliest transaction date to check, inclusive. Nullable. Unbounded if not provided. |
| **to_effective_date** | **datetime** | Optional | The latest transaction date to check, inclusive. Nullable — the window is unbounded above if not  provided. This value also resolves as the run&#39;s effectiveAt, so portfolios are resolved and transactions  decorated as of it; when not provided, that defaults to latest. Must be on or after fromEffectiveDate  when both are provided. |
| **portfolio_scope** | **str** | Optional | The scope of the portfolios whose transactions to check. Nullable. Every scope is checked if not provided. |
| **portfolio_selector_attribute** | **str** | Optional | An attribute (field name or propertyKey) to use to narrow down the portfolios whose transactions are  checked. Cannot be provided without portfolioSelectorValue, and vice versa. |
| **portfolio_selector_value** | **str** | Optional | The value of the above attribute used to narrow down the portfolios. Cannot be provided without  portfolioSelectorAttribute, and vice versa. |
| **transaction_selector_attribute** | **str** | Optional | An attribute (field name or propertyKey) to use to narrow down the transactions checked within those  portfolios. Cannot be provided without transactionSelectorValue, and vice versa. |
| **transaction_selector_value** | **str** | Optional | The value of the above attribute used to narrow down the transactions. Cannot be provided without  transactionSelectorAttribute, and vice versa. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PortfolioTransactionDataset import PortfolioTransactionDataset

instance = PortfolioTransactionDataset(
    as_at=datetime.now(),  # optional — The asAt date to fetch the data. Nullable. Defaults to latest.
    from_effective_date=datetime.now(),  # optional — The earliest transaction date to check, inclusive. Nullable. Unbounded if not provided.
    to_effective_date=datetime.now(),  # optional — The latest transaction date to check, inclusive. Nullable — the window is unbounded above if not  provided. This value also resolves as the run&#39;s effectiveAt, so portfolios are resolved and transactions  decorated as of it; when not provided, that defaults to latest. Must be on or after fromEffectiveDate  when both are provided.
    portfolio_scope="...",  # optional — The scope of the portfolios whose transactions to check. Nullable. Every scope is checked if not provided.
    portfolio_selector_attribute="...",  # optional — An attribute (field name or propertyKey) to use to narrow down the portfolios whose transactions are  checked. Cannot be provided without portfolioSelectorValue, and vice versa.
    portfolio_selector_value="...",  # optional — The value of the above attribute used to narrow down the portfolios. Cannot be provided without  portfolioSelectorAttribute, and vice versa.
    transaction_selector_attribute="...",  # optional — An attribute (field name or propertyKey) to use to narrow down the transactions checked within those  portfolios. Cannot be provided without transactionSelectorValue, and vice versa.
    transaction_selector_value="..."  # optional — The value of the above attribute used to narrow down the transactions. Cannot be provided without  transactionSelectorAttribute, and vice versa.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

