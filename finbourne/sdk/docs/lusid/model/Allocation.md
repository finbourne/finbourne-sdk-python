# Allocation

An Allocation of a certain quantity of a specific instrument against an originating  Order.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **allocated_order_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **portfolio_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **quantity** | **float** | Required | The quantity of given instrument allocated. |
| **instrument_identifiers** | **Dict[str, Optional[str]]** | Required | The instrument allocated. |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **properties** | [Dict[str, PerpetualProperty]](PerpetualProperty.md) | Optional | Client-defined properties associated with this allocation. |
| **instrument_scope** | **str** | Optional | The scope in which the instrument lies |
| **lusid_instrument_id** | **str** | Required | The LUSID instrument id for the instrument allocated. |
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
| **data_model_membership** | [DataModelMembership](DataModelMembership.md) | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.Allocation import Allocation

instance = Allocation(
    id=ResourceId(...),  # required
    allocated_order_id=ResourceId(...),  # required
    portfolio_id=ResourceId(...),  # required
    quantity=0.0,  # required — The quantity of given instrument allocated.
    instrument_identifiers=,  # required — The instrument allocated.
    version=Version(...),  # optional
    properties=PerpetualProperty(...),  # optional — Client-defined properties associated with this allocation.
    instrument_scope="...",  # optional — The scope in which the instrument lies
    lusid_instrument_id="...",  # required — The LUSID instrument id for the instrument allocated.
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
    execution_ids=[],  # optional — The executions associated with this allocation
    data_model_membership=DataModelMembership(...),  # optional
    links=[]  # optional
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [Version](Version.md)
- [PerpetualProperty](PerpetualProperty.md) — used in `properties`
- [ResourceId](ResourceId.md) — used in `placement_ids`
- [CurrencyAndAmount](CurrencyAndAmount.md)
- [ResourceId](ResourceId.md) — used in `execution_ids`
- [DataModelMembership](DataModelMembership.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

