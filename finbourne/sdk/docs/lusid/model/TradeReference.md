# TradeReference

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **portfolio_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **holding_id** | **str** | Required | The holding the trade&#39;s line was valued from. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TradeReference import TradeReference

instance = TradeReference(
    portfolio_id=ResourceId(...),  # required
    holding_id="..."  # required — The holding the trade&#39;s line was valued from.
)
```


## Related Models

- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

