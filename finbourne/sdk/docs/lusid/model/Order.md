# Order

An Order for a certain quantity of a specific instrument
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **properties** | [Dict[str, PerpetualProperty]](PerpetualProperty.md) | Optional | Client-defined properties associated with this order. |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **instrument_identifiers** | **Dict[str, Optional[str]]** | Required | The instrument ordered. |
| **quantity** | **float** | Optional | The quantity of the given instrument ordered. |
| **side** | **str** | Required | The client&#39;s representation of the order&#39;s side (buy, sell, short, etc) |
| **order_book_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **portfolio_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **instrument_scope** | **str** | Optional | The scope in which the instrument lies |
| **lusid_instrument_id** | **str** | Required | The LUSID instrument id for the instrument ordered. |
| **state** | **str** | Optional | The order&#39;s state (examples: New, PartiallyFilled, ...) |
| **type** | **str** | Optional | The order&#39;s type (examples: Limit, Market, ...) |
| **time_in_force** | **str** | Optional | The order&#39;s time in force (examples: Day, GoodTilCancel, ...) |
| **var_date** | **datetime** | Optional | The date on which the order was made |
| **price** | [CurrencyAndAmount](CurrencyAndAmount.md) | Optional | *No description available.* |
| **limit_price** | [CurrencyAndAmount](CurrencyAndAmount.md) | Optional | *No description available.* |
| **stop_price** | [CurrencyAndAmount](CurrencyAndAmount.md) | Optional | *No description available.* |
| **order_instruction_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **package_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **weight** | **float** | Optional | The proportion of the total portfolio value ordered for the given instrument ordered. |
| **amount** | [CurrencyAndAmount](CurrencyAndAmount.md) | Optional | *No description available.* |
| **data_model_membership** | [DataModelMembership](DataModelMembership.md) | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.Order import Order

instance = Order(
    properties=PerpetualProperty(...),  # optional — Client-defined properties associated with this order.
    version=Version(...),  # optional
    instrument_identifiers=,  # required — The instrument ordered.
    quantity=0.0,  # optional — The quantity of the given instrument ordered.
    side="...",  # required — The client&#39;s representation of the order&#39;s side (buy, sell, short, etc)
    order_book_id=ResourceId(...),  # optional
    portfolio_id=ResourceId(...),  # optional
    id=ResourceId(...),  # required
    instrument_scope="...",  # optional — The scope in which the instrument lies
    lusid_instrument_id="...",  # required — The LUSID instrument id for the instrument ordered.
    state="...",  # optional — The order&#39;s state (examples: New, PartiallyFilled, ...)
    type="...",  # optional — The order&#39;s type (examples: Limit, Market, ...)
    time_in_force="...",  # optional — The order&#39;s time in force (examples: Day, GoodTilCancel, ...)
    var_date=datetime.now(),  # optional — The date on which the order was made
    price=CurrencyAndAmount(...),  # optional
    limit_price=CurrencyAndAmount(...),  # optional
    stop_price=CurrencyAndAmount(...),  # optional
    order_instruction_id=ResourceId(...),  # optional
    package_id=ResourceId(...),  # optional
    weight=0.0,  # optional — The proportion of the total portfolio value ordered for the given instrument ordered.
    amount=CurrencyAndAmount(...),  # optional
    data_model_membership=DataModelMembership(...),  # optional
    links=[]  # optional
)
```


## Related Models

- [PerpetualProperty](PerpetualProperty.md) — used in `properties`
- [Version](Version.md)
- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [CurrencyAndAmount](CurrencyAndAmount.md)
- [CurrencyAndAmount](CurrencyAndAmount.md)
- [CurrencyAndAmount](CurrencyAndAmount.md)
- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [CurrencyAndAmount](CurrencyAndAmount.md)
- [DataModelMembership](DataModelMembership.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

