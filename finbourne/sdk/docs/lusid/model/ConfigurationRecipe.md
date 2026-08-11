# ConfigurationRecipe

The Configuration or Calculation Recipe controls how LUSID processes a given request.  This can be used to change where market data used in pricing is loaded from and in what order, or which model is used to  price a given instrument as well as how aggregation will process the produced results.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **scope** | **str** | Required | The scope used when updating or inserting the Configuration Recipe. |
| **code** | **str** | Required | User given string name (code) to identify the recipe. |
| **market** | [MarketContext](MarketContext.md) | Optional | *No description available.* |
| **pricing** | [PricingContext](PricingContext.md) | Optional | *No description available.* |
| **aggregation** | [AggregationContext](AggregationContext.md) | Optional | *No description available.* |
| **description** | **str** | Optional | User can assign a description to understand more humanly the recipe. |
| **holding** | [HoldingContext](HoldingContext.md) | Optional | *No description available.* |
| **translation** | [TranslationContext](TranslationContext.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ConfigurationRecipe import ConfigurationRecipe

instance = ConfigurationRecipe(
    scope="...",  # required — The scope used when updating or inserting the Configuration Recipe.
    code="...",  # required — User given string name (code) to identify the recipe.
    market=MarketContext(...),  # optional
    pricing=PricingContext(...),  # optional
    aggregation=AggregationContext(...),  # optional
    description="...",  # optional — User can assign a description to understand more humanly the recipe.
    holding=HoldingContext(...),  # optional
    translation=TranslationContext(...)  # optional
)
```

- [MarketContext](MarketContext.md)
- [PricingContext](PricingContext.md)
- [AggregationContext](AggregationContext.md)
- [HoldingContext](HoldingContext.md)
- [TranslationContext](TranslationContext.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

