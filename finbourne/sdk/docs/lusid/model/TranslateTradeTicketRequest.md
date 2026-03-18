# TranslateTradeTicketRequest

A collection of instruments to translate, along with the target dialect to translate into.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **tickets** | [Dict[str, TradeTicket]](TradeTicket.md) | Required | The collection of trade tickets to translate.                Each trade ticket should be keyed by a unique correlation id. This id is ephemeral  and is not stored by LUSID. It serves only as a way to easily identify each instrument in the response. |
| **dialect** | **str** | Required | The target dialect that the given instruments should be translated to. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TranslateTradeTicketRequest import TranslateTradeTicketRequest

instance = TranslateTradeTicketRequest(
    tickets=TradeTicket(...),  # required — The collection of trade tickets to translate.                Each trade ticket should be keyed by a unique correlation id. This id is ephemeral  and is not stored by LUSID. It serves only as a way to easily identify each instrument in the response.
    dialect="..."  # required — The target dialect that the given instruments should be translated to.
)
```


## Related Models

- [TradeTicket](TradeTicket.md) — used in `tickets`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

