# TradeTicket

The base class for representing a Trade Ticket in LUSID.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **trade_ticket_type** | **str** | Required | The available values are: LusidTradeTicket, ExternalTradeTicket |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TradeTicket import TradeTicket

instance = TradeTicket(
    trade_ticket_type="..."  # required — The available values are: LusidTradeTicket, ExternalTradeTicket
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

