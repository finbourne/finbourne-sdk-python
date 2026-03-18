# TransactionTypeAlias

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **type** | **str** | Required | The transaction type |
| **description** | **str** | Required | Brief description of the transaction |
| **transaction_class** | **str** | Required | Relates types of a similar class. E.g. Buy/Sell, StockIn/StockOut |
| **transaction_roles** | **str** | Required | Transactions role within a class. E.g. Increase a long position |
| **is_default** | **bool** | Optional | IsDefault is a flag that denotes the default alias for a source. There can only be, at most, one per source. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TransactionTypeAlias import TransactionTypeAlias

instance = TransactionTypeAlias(
    type="...",  # required — The transaction type
    description="...",  # required — Brief description of the transaction
    transaction_class="...",  # required — Relates types of a similar class. E.g. Buy/Sell, StockIn/StockOut
    transaction_roles="...",  # required — Transactions role within a class. E.g. Increase a long position
    is_default=True  # optional — IsDefault is a flag that denotes the default alias for a source. There can only be, at most, one per source.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

