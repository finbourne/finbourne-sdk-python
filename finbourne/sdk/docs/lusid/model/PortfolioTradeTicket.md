# PortfolioTradeTicket

Response for querying trade tickets
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **source_portfolio_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **trade_ticket** | [LusidTradeTicket](LusidTradeTicket.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PortfolioTradeTicket import PortfolioTradeTicket

instance = PortfolioTradeTicket(
    source_portfolio_id=ResourceId(...),  # optional
    trade_ticket=LusidTradeTicket(...)  # optional
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [LusidTradeTicket](LusidTradeTicket.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

