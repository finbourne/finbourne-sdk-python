# AccountedTransaction

The Valuation Point Data Response for the Fund and specified date.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **accounting_date** | **datetime** | Optional | The transaction&#39;s accounting date. |
| **journal_entry_action** | **str** | Optional | The journal entry line action associated with this transaction. |
| **transaction** | [OutputTransaction](OutputTransaction.md) | Optional | *No description available.* |
| **portfolio_id** | [PortfolioId](PortfolioId.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AccountedTransaction import AccountedTransaction

instance = AccountedTransaction(
    accounting_date=datetime.now(),  # optional — The transaction&#39;s accounting date.
    journal_entry_action="...",  # optional — The journal entry line action associated with this transaction.
    transaction=OutputTransaction(...),  # optional
    portfolio_id=PortfolioId(...)  # optional
)
```

- [OutputTransaction](OutputTransaction.md)
- [PortfolioId](PortfolioId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

