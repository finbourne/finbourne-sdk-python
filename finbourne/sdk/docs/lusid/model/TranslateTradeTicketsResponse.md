# TranslateTradeTicketsResponse

A response from a request to translate a collection of instruments to a given target dialect.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **values** | [Dict[str, TradeTicket]](TradeTicket.md) | Optional | The instruments which have been successfully translated. |
| **failed** | [Dict[str, ErrorDetail]](ErrorDetail.md) | Optional | The instruments that could not be translated along with a reason for their failure. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TranslateTradeTicketsResponse import TranslateTradeTicketsResponse

instance = TranslateTradeTicketsResponse(
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    values=TradeTicket(...),  # optional — The instruments which have been successfully translated.
    failed=ErrorDetail(...),  # optional — The instruments that could not be translated along with a reason for their failure.
    links=[]  # optional
)
```

- [TradeTicket](TradeTicket.md) — used in `values`
- [ErrorDetail](ErrorDetail.md) — used in `failed`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

