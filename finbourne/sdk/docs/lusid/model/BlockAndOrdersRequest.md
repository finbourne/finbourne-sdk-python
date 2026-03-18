# BlockAndOrdersRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **block_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **orders** | [List[BlockedOrderRequest]](BlockedOrderRequest.md) | Required | An order which belongs to a block. Fields common to both entities (such as instrument) should be derived from the block. |
| **block_properties** | [Dict[str, PerpetualProperty]](PerpetualProperty.md) | Optional | Client-defined properties associated with this block. |
| **instrument_identifiers** | **Dict[str, Optional[str]]** | Required | The instrument ordered. |
| **side** | **str** | Optional | The client&#39;s representation of the block&#39;s side (buy, sell, short, etc). BlockedOrders in the request which do not specify a side will have their side populated with this value. |
| **type** | **str** | Optional | The block order&#39;s type (examples: Limit, Market, ...) |
| **time_in_force** | **str** | Optional | The block orders&#39; time in force (examples: Day, GoodTilCancel, ...) |
| **var_date** | **datetime** | Optional | The date on which the block was made |
| **limit_price** | [CurrencyAndAmount](CurrencyAndAmount.md) | Optional | *No description available.* |
| **stop_price** | [CurrencyAndAmount](CurrencyAndAmount.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.BlockAndOrdersRequest import BlockAndOrdersRequest

instance = BlockAndOrdersRequest(
    block_id=ResourceId(...),  # required
    orders=[],  # required — An order which belongs to a block. Fields common to both entities (such as instrument) should be derived from the block.
    block_properties=PerpetualProperty(...),  # optional — Client-defined properties associated with this block.
    instrument_identifiers=,  # required — The instrument ordered.
    side="...",  # optional — The client&#39;s representation of the block&#39;s side (buy, sell, short, etc). BlockedOrders in the request which do not specify a side will have their side populated with this value.
    type="...",  # optional — The block order&#39;s type (examples: Limit, Market, ...)
    time_in_force="...",  # optional — The block orders&#39; time in force (examples: Day, GoodTilCancel, ...)
    var_date=datetime.now(),  # optional — The date on which the block was made
    limit_price=CurrencyAndAmount(...),  # optional
    stop_price=CurrencyAndAmount(...)  # optional
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [BlockedOrderRequest](BlockedOrderRequest.md) — used in `orders`
- [PerpetualProperty](PerpetualProperty.md) — used in `block_properties`
- [CurrencyAndAmount](CurrencyAndAmount.md)
- [CurrencyAndAmount](CurrencyAndAmount.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

