# CreateTradeTicketsResponse

Batch trade ticket creation response
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **values** | [List[LusidTradeTicket]](LusidTradeTicket.md) | Required | *No description available.* |
| **failures** | [List[ErrorDetail]](ErrorDetail.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CreateTradeTicketsResponse import CreateTradeTicketsResponse

instance = CreateTradeTicketsResponse(
    values=[],  # required
    failures=[]  # required
)
```


## Related Models

- [LusidTradeTicket](LusidTradeTicket.md)
- [ErrorDetail](ErrorDetail.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

