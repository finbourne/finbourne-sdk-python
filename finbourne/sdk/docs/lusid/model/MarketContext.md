# MarketContext

Market context node. This defines how LUSID processes parts of a request that require resolution of market data such as instrument prices or  Fx rates. It controls where the data is loaded from and which sources take precedence.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **market_rules** | [List[MarketDataKeyRule]](MarketDataKeyRule.md) | Optional | The set of rules that define how to resolve particular use cases. These can be relatively general or specific in nature.  Nominally any number are possible and will be processed in order where applicable. However, there is evidently a potential  for increased computational cost where many rules must be applied to resolve data. Ensuring that portfolios are structured in  such a way as to reduce the number of rules required is therefore sensible. |
| **suppliers** | [MarketContextSuppliers](MarketContextSuppliers.md) | Optional | *No description available.* |
| **options** | [MarketOptions](MarketOptions.md) | Optional | *No description available.* |
| **specific_rules** | [List[MarketDataSpecificRule]](MarketDataSpecificRule.md) | Optional | Extends market data key rules to be able to catch dependencies depending on where the dependency comes from, as opposed to what the dependency is asking for.  Using two specific rules, one could instruct rates curves requested by bonds to be retrieved from a different scope than rates curves requested by swaps.  WARNING: The use of specific rules impacts performance. Where possible, one should use MarketDataKeyRules only. |
| **grouped_market_rules** | [List[GroupOfMarketDataKeyRules]](GroupOfMarketDataKeyRules.md) | Optional | The list of groups of rules that will be used in market data resolution.  Rules given within a group will, if the group is being used to resolve data,  all be applied with the results of those individual resolution attempts combined into a single result.  The method for combining results is determined by the operation detailed in the GroupOfMarketDataKeyRules.                Notes:  - When resolving MarketData, MarketRules will be applied first followed by GroupedMarketRules  if data could not be found using only the MarketRules provided.  - GroupedMarketRules can only be used for resolving data from the QuoteStore.                Caution: As every rule in a given group will be applied in resolution if the group is applied,  groups are computationally expensive for market data resolution.  Therefore, heuristically, rule groups should be kept as small as possible. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.MarketContext import MarketContext

instance = MarketContext(
    market_rules=[],  # optional — The set of rules that define how to resolve particular use cases. These can be relatively general or specific in nature.  Nominally any number are possible and will be processed in order where applicable. However, there is evidently a potential  for increased computational cost where many rules must be applied to resolve data. Ensuring that portfolios are structured in  such a way as to reduce the number of rules required is therefore sensible.
    suppliers=MarketContextSuppliers(...),  # optional
    options=MarketOptions(...),  # optional
    specific_rules=[],  # optional — Extends market data key rules to be able to catch dependencies depending on where the dependency comes from, as opposed to what the dependency is asking for.  Using two specific rules, one could instruct rates curves requested by bonds to be retrieved from a different scope than rates curves requested by swaps.  WARNING: The use of specific rules impacts performance. Where possible, one should use MarketDataKeyRules only.
    grouped_market_rules=[]  # optional — The list of groups of rules that will be used in market data resolution.  Rules given within a group will, if the group is being used to resolve data,  all be applied with the results of those individual resolution attempts combined into a single result.  The method for combining results is determined by the operation detailed in the GroupOfMarketDataKeyRules.                Notes:  - When resolving MarketData, MarketRules will be applied first followed by GroupedMarketRules  if data could not be found using only the MarketRules provided.  - GroupedMarketRules can only be used for resolving data from the QuoteStore.                Caution: As every rule in a given group will be applied in resolution if the group is applied,  groups are computationally expensive for market data resolution.  Therefore, heuristically, rule groups should be kept as small as possible.
)
```


## Related Models

- [MarketDataKeyRule](MarketDataKeyRule.md) — used in `market_rules`
- [MarketContextSuppliers](MarketContextSuppliers.md)
- [MarketOptions](MarketOptions.md)
- [MarketDataSpecificRule](MarketDataSpecificRule.md) — used in `specific_rules`
- [GroupOfMarketDataKeyRules](GroupOfMarketDataKeyRules.md) — used in `grouped_market_rules`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

