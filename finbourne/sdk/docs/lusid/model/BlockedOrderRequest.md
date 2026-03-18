# BlockedOrderRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **properties** | [Dict[str, PerpetualProperty]](PerpetualProperty.md) | Optional | Client-defined properties associated with this order. |
| **quantity** | **float** | Required | The quantity of the given instrument ordered. |
| **order_book_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **portfolio_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **state** | **str** | Optional | The order&#39;s state (examples: New, PartiallyFilled, ...) |
| **var_date** | **datetime** | Optional | The date on which the order was made |
| **price** | [CurrencyAndAmount](CurrencyAndAmount.md) | Optional | *No description available.* |
| **order_instruction** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **package** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **side** | **str** | Optional | The client&#39;s representation of the order&#39;s side (buy, sell, short, etc) |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.BlockedOrderRequest import BlockedOrderRequest

instance = BlockedOrderRequest(
    properties=PerpetualProperty(...),  # optional — Client-defined properties associated with this order.
    quantity=0.0,  # required — The quantity of the given instrument ordered.
    order_book_id=ResourceId(...),  # optional
    portfolio_id=ResourceId(...),  # optional
    id=ResourceId(...),  # required
    state="...",  # optional — The order&#39;s state (examples: New, PartiallyFilled, ...)
    var_date=datetime.now(),  # optional — The date on which the order was made
    price=CurrencyAndAmount(...),  # optional
    order_instruction=ResourceId(...),  # optional
    package=ResourceId(...),  # optional
    side="..."  # optional — The client&#39;s representation of the order&#39;s side (buy, sell, short, etc)
)
```


## Related Models

- [PerpetualProperty](PerpetualProperty.md) — used in `properties`
- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [CurrencyAndAmount](CurrencyAndAmount.md)
- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

