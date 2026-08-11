# OrderInstructionRequest

A request to create or update a Order Instruction.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **created_date** | **datetime** | Required | The active date of this order instruction. |
| **portfolio_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **instrument_identifiers** | **Dict[str, Optional[str]]** | Optional | The instrument ordered. |
| **quantity** | **float** | Optional | The quantity of given instrument ordered. |
| **weight** | **float** | Optional | The proportion of the total portfolio value ordered for the given instrument ordered. |
| **price** | [CurrencyAndAmount](CurrencyAndAmount.md) | Optional | *No description available.* |
| **properties** | [Dict[str, PerpetualProperty]](PerpetualProperty.md) | Optional | Client-defined properties associated with this execution. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.OrderInstructionRequest import OrderInstructionRequest

instance = OrderInstructionRequest(
    id=ResourceId(...),  # required
    created_date=datetime.now(),  # required — The active date of this order instruction.
    portfolio_id=ResourceId(...),  # optional
    instrument_identifiers=,  # optional — The instrument ordered.
    quantity=0.0,  # optional — The quantity of given instrument ordered.
    weight=0.0,  # optional — The proportion of the total portfolio value ordered for the given instrument ordered.
    price=CurrencyAndAmount(...),  # optional
    properties=PerpetualProperty(...)  # optional — Client-defined properties associated with this execution.
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [CurrencyAndAmount](CurrencyAndAmount.md)
- [PerpetualProperty](PerpetualProperty.md) — used in `properties`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

