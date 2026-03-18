# TransactionConfigurationTypeAlias

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **type** | **str** | Required | The transaction type |
| **description** | **str** | Required | Brief description of the transaction |
| **transaction_class** | **str** | Required | Relates types of a similar class. E.g. Buy/Sell, StockIn/StockOut |
| **transaction_group** | **str** | Optional | Group is a set of codes related to a source, or sync. DEPRECATED: This field will be removed, use &#x60;Source&#x60; instead |
| **source** | **str** | Optional | Used to group a set of transaction types |
| **transaction_roles** | **str** | Required | . The available values are: None, LongLonger, LongShorter, ShortShorter, Shorter, ShortLonger, Longer, AllRoles |
| **is_default** | **bool** | Optional | IsDefault is a flag that denotes the default alias for a source. There can only be, at most, one per source. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TransactionConfigurationTypeAlias import TransactionConfigurationTypeAlias

instance = TransactionConfigurationTypeAlias(
    type="...",  # required — The transaction type
    description="...",  # required — Brief description of the transaction
    transaction_class="...",  # required — Relates types of a similar class. E.g. Buy/Sell, StockIn/StockOut
    transaction_group="...",  # optional — Group is a set of codes related to a source, or sync. DEPRECATED: This field will be removed, use &#x60;Source&#x60; instead
    source="...",  # optional — Used to group a set of transaction types
    transaction_roles="...",  # required — . The available values are: None, LongLonger, LongShorter, ShortShorter, Shorter, ShortLonger, Longer, AllRoles
    is_default=True  # optional — IsDefault is a flag that denotes the default alias for a source. There can only be, at most, one per source.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

