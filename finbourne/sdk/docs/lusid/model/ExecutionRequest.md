# ExecutionRequest

A request to create or update a Execution.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **placement_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **properties** | [Dict[str, PerpetualProperty]](PerpetualProperty.md) | Optional | Client-defined properties associated with this execution. |
| **instrument_identifiers** | **Dict[str, Optional[str]]** | Required | The instrument ordered. |
| **quantity** | **float** | Required | The quantity of given instrument ordered. |
| **state** | **str** | Required | The state of this execution (typically a FIX state; Open, Filled, etc). |
| **side** | **str** | Required | The side (Buy, Sell, ...) of this execution. |
| **type** | **str** | Required | The type of this execution (Market, Limit, etc). |
| **created_date** | **datetime** | Required | The active date of this execution. |
| **settlement_date** | **datetime** | Optional | The (optional) settlement date for this execution |
| **price** | [CurrencyAndAmount](CurrencyAndAmount.md) | Required | *No description available.* |
| **settlement_currency** | **str** | Required | The execution&#39;s settlement currency. |
| **settlement_currency_fx_rate** | **float** | Required | The exectuion&#39;s settlement currency rate. |
| **counterparty** | **str** | Required | The market entity this placement is placed with. |
| **average_price** | **float** | Optional | The average price of all executions for a given placement at the time of upsert |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ExecutionRequest import ExecutionRequest

instance = ExecutionRequest(
    id=ResourceId(...),  # required
    placement_id=ResourceId(...),  # required
    properties=PerpetualProperty(...),  # optional — Client-defined properties associated with this execution.
    instrument_identifiers=,  # required — The instrument ordered.
    quantity=0.0,  # required — The quantity of given instrument ordered.
    state="...",  # required — The state of this execution (typically a FIX state; Open, Filled, etc).
    side="...",  # required — The side (Buy, Sell, ...) of this execution.
    type="...",  # required — The type of this execution (Market, Limit, etc).
    created_date=datetime.now(),  # required — The active date of this execution.
    settlement_date=datetime.now(),  # optional — The (optional) settlement date for this execution
    price=CurrencyAndAmount(...),  # required
    settlement_currency="...",  # required — The execution&#39;s settlement currency.
    settlement_currency_fx_rate=0.0,  # required — The exectuion&#39;s settlement currency rate.
    counterparty="...",  # required — The market entity this placement is placed with.
    average_price=0.0  # optional — The average price of all executions for a given placement at the time of upsert
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [PerpetualProperty](PerpetualProperty.md) — used in `properties`
- [CurrencyAndAmount](CurrencyAndAmount.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

