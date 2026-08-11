# AllocationRequest

A request to create or update an Allocation.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **properties** | [Dict[str, PerpetualProperty]](PerpetualProperty.md) | Optional | Client-defined properties associated with this allocation. |
| **instrument_identifiers** | **Dict[str, Optional[str]]** | Required | The instrument allocated. |
| **quantity** | **float** | Required | The quantity of given instrument allocated. |
| **portfolio_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **allocated_order_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **placement_ids** | [List[ResourceId]](ResourceId.md) | Optional | A placement - also known as an order placed in the market - associated with this allocation. |
| **state** | **str** | Optional | The state of this allocation. |
| **side** | **str** | Optional | The side of this allocation (examples: Buy, Sell, ...). |
| **type** | **str** | Optional | The type of order associated with this allocation (examples: Limit, Market, ...). |
| **settlement_date** | **datetime** | Optional | The settlement date for this allocation. |
| **var_date** | **datetime** | Optional | The date of this allocation. |
| **price** | [CurrencyAndAmount](CurrencyAndAmount.md) | Optional | *No description available.* |
| **settlement_currency** | **str** | Optional | The settlement currency of this allocation. |
| **settlement_currency_fx_rate** | **float** | Optional | The settlement currency to allocation currency FX rate. |
| **counterparty** | **str** | Optional | The counterparty for this allocation. |
| **execution_ids** | [List[ResourceId]](ResourceId.md) | Optional | The executions associated with this allocation |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AllocationRequest import AllocationRequest

instance = AllocationRequest(
    properties=PerpetualProperty(...),  # optional — Client-defined properties associated with this allocation.
    instrument_identifiers=,  # required — The instrument allocated.
    quantity=0.0,  # required — The quantity of given instrument allocated.
    portfolio_id=ResourceId(...),  # required
    allocated_order_id=ResourceId(...),  # required
    id=ResourceId(...),  # required
    placement_ids=[],  # optional — A placement - also known as an order placed in the market - associated with this allocation.
    state="...",  # optional — The state of this allocation.
    side="...",  # optional — The side of this allocation (examples: Buy, Sell, ...).
    type="...",  # optional — The type of order associated with this allocation (examples: Limit, Market, ...).
    settlement_date=datetime.now(),  # optional — The settlement date for this allocation.
    var_date=datetime.now(),  # optional — The date of this allocation.
    price=CurrencyAndAmount(...),  # optional
    settlement_currency="...",  # optional — The settlement currency of this allocation.
    settlement_currency_fx_rate=0.0,  # optional — The settlement currency to allocation currency FX rate.
    counterparty="...",  # optional — The counterparty for this allocation.
    execution_ids=[]  # optional — The executions associated with this allocation
)
```


## Related Models

- [PerpetualProperty](PerpetualProperty.md) — used in `properties`
- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md) — used in `placement_ids`
- [CurrencyAndAmount](CurrencyAndAmount.md)
- [ResourceId](ResourceId.md) — used in `execution_ids`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

