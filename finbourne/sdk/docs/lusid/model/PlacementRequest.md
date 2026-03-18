# PlacementRequest

A request to create or update a Placement.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **parent_placement_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **block_ids** | [List[ResourceId]](ResourceId.md) | Required | The IDs of the Blocks associated with this placement. |
| **properties** | [Dict[str, PerpetualProperty]](PerpetualProperty.md) | Optional | Client-defined properties associated with this order. |
| **instrument_identifiers** | **Dict[str, Optional[str]]** | Required | The instrument ordered. |
| **quantity** | **float** | Required | The quantity of given instrument ordered. |
| **state** | **str** | Optional | The state of this placement (typically a FIX state; Open, Filled, etc). |
| **side** | **str** | Required | The side (Buy, Sell, ...) of this placement. |
| **time_in_force** | **str** | Required | The time in force applicable to this placement (GTC, FOK, Day, etc) |
| **type** | **str** | Required | The type of this placement (Market, Limit, etc). |
| **created_date** | **datetime** | Required | The active date of this placement. |
| **limit_price** | [CurrencyAndAmount](CurrencyAndAmount.md) | Optional | *No description available.* |
| **stop_price** | [CurrencyAndAmount](CurrencyAndAmount.md) | Optional | *No description available.* |
| **counterparty** | **str** | Optional | Optionally specifies the market entity this placement is placed with. |
| **execution_system** | **str** | Optional | Optionally specifies the execution system in use. |
| **entry_type** | **str** | Optional | Optionally specifies the entry type of this placement. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PlacementRequest import PlacementRequest

instance = PlacementRequest(
    id=ResourceId(...),  # required
    parent_placement_id=ResourceId(...),  # optional
    block_ids=[],  # required — The IDs of the Blocks associated with this placement.
    properties=PerpetualProperty(...),  # optional — Client-defined properties associated with this order.
    instrument_identifiers=,  # required — The instrument ordered.
    quantity=0.0,  # required — The quantity of given instrument ordered.
    state="...",  # optional — The state of this placement (typically a FIX state; Open, Filled, etc).
    side="...",  # required — The side (Buy, Sell, ...) of this placement.
    time_in_force="...",  # required — The time in force applicable to this placement (GTC, FOK, Day, etc)
    type="...",  # required — The type of this placement (Market, Limit, etc).
    created_date=datetime.now(),  # required — The active date of this placement.
    limit_price=CurrencyAndAmount(...),  # optional
    stop_price=CurrencyAndAmount(...),  # optional
    counterparty="...",  # optional — Optionally specifies the market entity this placement is placed with.
    execution_system="...",  # optional — Optionally specifies the execution system in use.
    entry_type="..."  # optional — Optionally specifies the entry type of this placement.
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md) — used in `block_ids`
- [PerpetualProperty](PerpetualProperty.md) — used in `properties`
- [CurrencyAndAmount](CurrencyAndAmount.md)
- [CurrencyAndAmount](CurrencyAndAmount.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

