# GroupOfMarketDataKeyRules

Represents a collection of MarketDataKeyRules that should be resolved together when resolving market data.  That is, market data resolution will always attempt to resolve with all rules in the group  before deciding what market data to return.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **market_data_key_rule_group_operation** | **str** | Required | The operation that will be used to process the collection of market data items and failures found on resolution  into a single market data item or failure to be used.  Supported values: [FirstLatest, AverageOfQuotesFound, AverageOfAllQuotes, FirstMinimum, FirstMaximum] |
| **market_rules** | [List[MarketDataKeyRule]](MarketDataKeyRule.md) | Required | The rules that should be grouped together in market data resolution. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.GroupOfMarketDataKeyRules import GroupOfMarketDataKeyRules

instance = GroupOfMarketDataKeyRules(
    market_data_key_rule_group_operation="...",  # required — The operation that will be used to process the collection of market data items and failures found on resolution  into a single market data item or failure to be used.  Supported values: [FirstLatest, AverageOfQuotesFound, AverageOfAllQuotes, FirstMinimum, FirstMaximum]
    market_rules=[]  # required — The rules that should be grouped together in market data resolution.
)
```

- [MarketDataKeyRule](MarketDataKeyRule.md) — used in `market_rules`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

