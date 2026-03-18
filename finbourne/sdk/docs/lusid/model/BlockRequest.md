# BlockRequest

A request to create or update a Block.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **order_ids** | [List[ResourceId]](ResourceId.md) | Optional | The related order ids. |
| **properties** | [Dict[str, PerpetualProperty]](PerpetualProperty.md) | Optional | Client-defined properties associated with this block. |
| **instrument_identifiers** | **Dict[str, Optional[str]]** | Required | The instrument ordered. |
| **quantity** | **float** | Required | The total quantity of given instrument ordered. |
| **side** | **str** | Required | The client&#39;s representation of the block&#39;s side (buy, sell, short, etc) |
| **type** | **str** | Required | The block order&#39;s type (examples: Limit, Market, ...) |
| **time_in_force** | **str** | Required | The block orders&#39; time in force (examples: Day, GoodTilCancel, ...) |
| **created_date** | **datetime** | Required | The date on which the block was made |
| **limit_price** | [CurrencyAndAmount](CurrencyAndAmount.md) | Optional | *No description available.* |
| **stop_price** | [CurrencyAndAmount](CurrencyAndAmount.md) | Optional | *No description available.* |
| **is_swept** | **bool** | Optional | Swept blocks are considered no longer of active interest, and no longer take part in various order management processes |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.BlockRequest import BlockRequest

instance = BlockRequest(
    id=ResourceId(...),  # required
    order_ids=[],  # optional — The related order ids.
    properties=PerpetualProperty(...),  # optional — Client-defined properties associated with this block.
    instrument_identifiers=,  # required — The instrument ordered.
    quantity=0.0,  # required — The total quantity of given instrument ordered.
    side="...",  # required — The client&#39;s representation of the block&#39;s side (buy, sell, short, etc)
    type="...",  # required — The block order&#39;s type (examples: Limit, Market, ...)
    time_in_force="...",  # required — The block orders&#39; time in force (examples: Day, GoodTilCancel, ...)
    created_date=datetime.now(),  # required — The date on which the block was made
    limit_price=CurrencyAndAmount(...),  # optional
    stop_price=CurrencyAndAmount(...),  # optional
    is_swept=True  # optional — Swept blocks are considered no longer of active interest, and no longer take part in various order management processes
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md) — used in `order_ids`
- [PerpetualProperty](PerpetualProperty.md) — used in `properties`
- [CurrencyAndAmount](CurrencyAndAmount.md)
- [CurrencyAndAmount](CurrencyAndAmount.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

