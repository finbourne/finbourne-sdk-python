# OrderUpdateRequest

A request to create or update a Order.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **quantity** | **float** | Optional | The quantity of the given instrument ordered. |
| **portfolio_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **properties** | [Dict[str, PerpetualProperty]](PerpetualProperty.md) | Optional | Client-defined properties associated with this order. |
| **price** | [CurrencyAndAmount](CurrencyAndAmount.md) | Optional | *No description available.* |
| **limit_price** | [CurrencyAndAmount](CurrencyAndAmount.md) | Optional | *No description available.* |
| **stop_price** | [CurrencyAndAmount](CurrencyAndAmount.md) | Optional | *No description available.* |
| **var_date** | **datetime** | Optional | The date on which the order was made |
| **side** | **str** | Optional | The client&#39;s representation of the order&#39;s side (buy, sell, short, etc) |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.OrderUpdateRequest import OrderUpdateRequest

instance = OrderUpdateRequest(
    id=ResourceId(...),  # required
    quantity=0.0,  # optional — The quantity of the given instrument ordered.
    portfolio_id=ResourceId(...),  # optional
    properties=PerpetualProperty(...),  # optional — Client-defined properties associated with this order.
    price=CurrencyAndAmount(...),  # optional
    limit_price=CurrencyAndAmount(...),  # optional
    stop_price=CurrencyAndAmount(...),  # optional
    var_date=datetime.now(),  # optional — The date on which the order was made
    side="..."  # optional — The client&#39;s representation of the order&#39;s side (buy, sell, short, etc)
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [PerpetualProperty](PerpetualProperty.md) — used in `properties`
- [CurrencyAndAmount](CurrencyAndAmount.md)
- [CurrencyAndAmount](CurrencyAndAmount.md)
- [CurrencyAndAmount](CurrencyAndAmount.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

