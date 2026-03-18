# BookTransactionsRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **allocation_ids** | [List[ResourceId]](ResourceId.md) | Required | A collection of Allocation IDs |
| **transaction_properties** | [Dict[str, PerpetualProperty]](PerpetualProperty.md) | Optional | A collection of properties |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.BookTransactionsRequest import BookTransactionsRequest

instance = BookTransactionsRequest(
    allocation_ids=[],  # required — A collection of Allocation IDs
    transaction_properties=PerpetualProperty(...)  # optional — A collection of properties
)
```


## Related Models

- [ResourceId](ResourceId.md) — used in `allocation_ids`
- [PerpetualProperty](PerpetualProperty.md) — used in `transaction_properties`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

