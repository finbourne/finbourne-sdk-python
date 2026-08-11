# TransactionFieldMap

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **transaction_id** | **str** | Required | *No description available.* |
| **type** | **str** | Required | *No description available.* |
| **source** | **str** | Required | *No description available.* |
| **instrument** | **str** | Required | *No description available.* |
| **transaction_date** | **str** | Required | *No description available.* |
| **settlement_date** | **str** | Required | *No description available.* |
| **units** | **str** | Required | *No description available.* |
| **transaction_price** | [TransactionPriceAndType](TransactionPriceAndType.md) | Optional | *No description available.* |
| **transaction_currency** | **str** | Required | *No description available.* |
| **exchange_rate** | **str** | Optional | *No description available.* |
| **total_consideration** | [TransactionCurrencyAndAmount](TransactionCurrencyAndAmount.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TransactionFieldMap import TransactionFieldMap

instance = TransactionFieldMap(
    transaction_id="...",  # required
    type="...",  # required
    source="...",  # required
    instrument="...",  # required
    transaction_date="...",  # required
    settlement_date="...",  # required
    units="...",  # required
    transaction_price=TransactionPriceAndType(...),  # optional
    transaction_currency="...",  # required
    exchange_rate="...",  # optional
    total_consideration=TransactionCurrencyAndAmount(...)  # required
)
```

- [TransactionPriceAndType](TransactionPriceAndType.md)
- [TransactionCurrencyAndAmount](TransactionCurrencyAndAmount.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

