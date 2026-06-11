# BookTransactionsRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **allocation_ids** | [List[ResourceId]](ResourceId.md) | Required | A collection of Allocation IDs |
| **transaction_properties** | [Dict[str, PerpetualProperty]](PerpetualProperty.md) | Optional | A collection of properties |
| **fx_instrument_type** | **str** | Optional | The type of FX instrument to create when settlement currency differs from portfolio base currency. Use None to suppress FX instrument and order creation. Defaults to None. Available values: None, FxForward, FxSpot. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.BookTransactionsRequest import BookTransactionsRequest

instance = BookTransactionsRequest(
    allocation_ids=[],  # required — A collection of Allocation IDs
    transaction_properties=PerpetualProperty(...),  # optional — A collection of properties
    fx_instrument_type="..."  # optional — The type of FX instrument to create when settlement currency differs from portfolio base currency. Use None to suppress FX instrument and order creation. Defaults to None. Available values: None, FxForward, FxSpot.
)
```


## Related Models

- [ResourceId](ResourceId.md) — used in `allocation_ids`
- [PerpetualProperty](PerpetualProperty.md) — used in `transaction_properties`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

