# TransactionSettlementSummary

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **overall_status** | [CategorySettlementStatus](CategorySettlementStatus.md) | Required | *No description available.* |
| **stock_status** | [CategorySettlementStatus](CategorySettlementStatus.md) | Required | *No description available.* |
| **cash_status** | [CategorySettlementStatus](CategorySettlementStatus.md) | Required | *No description available.* |
| **deferred_cash_receipt_status** | [CategorySettlementStatus](CategorySettlementStatus.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TransactionSettlementSummary import TransactionSettlementSummary

instance = TransactionSettlementSummary(
    overall_status=CategorySettlementStatus(...),  # required
    stock_status=CategorySettlementStatus(...),  # required
    cash_status=CategorySettlementStatus(...),  # required
    deferred_cash_receipt_status=CategorySettlementStatus(...)  # required
)
```


## Related Models

- [CategorySettlementStatus](CategorySettlementStatus.md)
- [CategorySettlementStatus](CategorySettlementStatus.md)
- [CategorySettlementStatus](CategorySettlementStatus.md)
- [CategorySettlementStatus](CategorySettlementStatus.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

