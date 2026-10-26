# LusidEntityRecDefinitionDetails

A definition that reconciles one type of LUSID entity. A filter selects the population of each side, and a single  matching ruleset of that entity type drives the definition.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **entity_type** | **str** | Required | The type of LUSID entity to reconcile, which is also the rec type of the results. Supported types: Instrument. Must equal the reconciliationType of the matching ruleset. Available values: Holding, CashHolding, Valuation, InputTransaction, OutputTransaction, SettlementActivity, External, Instrument. |
| **matching_ruleset_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **left_filter** | **str** | Optional | Optional filter that selects the population of the left side, e.g. \&quot;scope eq &#39;default&#39;\&quot;. It resolves against the left side entity fields. Null reads the whole population of the side. |
| **right_filter** | **str** | Optional | Optional filter that selects the population of the right side. It resolves against the right side entity fields. Null reads the whole population of the side. |
| **definition_type** | **str** | Required | What this definition reconciles, and so which shape of details it carries. Available values: PortfolioContents, LusidEntity, External. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.LusidEntityRecDefinitionDetails import LusidEntityRecDefinitionDetails

instance = LusidEntityRecDefinitionDetails(
    entity_type="...",  # required — The type of LUSID entity to reconcile, which is also the rec type of the results. Supported types: Instrument. Must equal the reconciliationType of the matching ruleset. Available values: Holding, CashHolding, Valuation, InputTransaction, OutputTransaction, SettlementActivity, External, Instrument.
    matching_ruleset_id=ResourceId(...),  # required
    left_filter="...",  # optional — Optional filter that selects the population of the left side, e.g. \&quot;scope eq &#39;default&#39;\&quot;. It resolves against the left side entity fields. Null reads the whole population of the side.
    right_filter="...",  # optional — Optional filter that selects the population of the right side. It resolves against the right side entity fields. Null reads the whole population of the side.
    definition_type="..."  # required — What this definition reconciles, and so which shape of details it carries. Available values: PortfolioContents, LusidEntity, External.
)
```

- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

