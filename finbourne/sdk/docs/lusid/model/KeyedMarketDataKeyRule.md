# KeyedMarketDataKeyRule

One keyed rule of an MdkrGroup shift: the key names the result column (scenario:key) and the rule  is a standard market data key rule resolved for that column.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **key** | **str** | Required | The key naming this rule&#39;s result column, e.g. \&quot;bid\&quot;. |
| **rule** | [MarketDataKeyRule](MarketDataKeyRule.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.KeyedMarketDataKeyRule import KeyedMarketDataKeyRule

instance = KeyedMarketDataKeyRule(
    key="...",  # required — The key naming this rule&#39;s result column, e.g. \&quot;bid\&quot;.
    rule=MarketDataKeyRule(...)  # required
)
```

- [MarketDataKeyRule](MarketDataKeyRule.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

