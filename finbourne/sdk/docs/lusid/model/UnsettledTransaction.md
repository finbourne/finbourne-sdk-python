# UnsettledTransaction

A transaction that remains unsettled as at the valuation point, with per-bucket settlement status.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **transaction** | [OutputTransaction](OutputTransaction.md) | Optional | *No description available.* |
| **portfolio_id** | [PortfolioId](PortfolioId.md) | Optional | *No description available.* |
| **overall_settlement_status** | **str** | Optional | The overall settlement status of the transaction (Unsettled, PartSettled, Settled, None). |
| **overall_is_overdue** | **bool** | Optional | Whether the transaction is overdue for settlement. |
| **cash_settlement_status** | **str** | Optional | The settlement status of the cash component. |
| **cash_is_overdue** | **bool** | Optional | Whether the cash component is overdue for settlement. |
| **stock_settlement_status** | **str** | Optional | The settlement status of the stock component. |
| **stock_is_overdue** | **bool** | Optional | Whether the stock component is overdue for settlement. |
| **deferred_cash_settlement_status** | **str** | Optional | The settlement status of the deferred cash component. |
| **deferred_cash_is_overdue** | **bool** | Optional | Whether the deferred cash component is overdue for settlement. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UnsettledTransaction import UnsettledTransaction

instance = UnsettledTransaction(
    transaction=OutputTransaction(...),  # optional
    portfolio_id=PortfolioId(...),  # optional
    overall_settlement_status="...",  # optional — The overall settlement status of the transaction (Unsettled, PartSettled, Settled, None).
    overall_is_overdue=True,  # optional — Whether the transaction is overdue for settlement.
    cash_settlement_status="...",  # optional — The settlement status of the cash component.
    cash_is_overdue=True,  # optional — Whether the cash component is overdue for settlement.
    stock_settlement_status="...",  # optional — The settlement status of the stock component.
    stock_is_overdue=True,  # optional — Whether the stock component is overdue for settlement.
    deferred_cash_settlement_status="...",  # optional — The settlement status of the deferred cash component.
    deferred_cash_is_overdue=True  # optional — Whether the deferred cash component is overdue for settlement.
)
```


## Related Models

- [OutputTransaction](OutputTransaction.md)
- [PortfolioId](PortfolioId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

