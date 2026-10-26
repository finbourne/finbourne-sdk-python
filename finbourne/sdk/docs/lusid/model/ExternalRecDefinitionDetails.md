# ExternalRecDefinitionDetails

A definition reconciling relational data on both sides, driven by a single External matching ruleset.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **matching_ruleset_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **left_filter** | **str** | Optional | Optional filter over the left dataset&#39;s rows, in the dataset&#39;s own grammar, e.g. \&quot;Values[custodian] eq &#39;something&#39;\&quot;. |
| **right_filter** | **str** | Optional | Optional filter over the right dataset&#39;s rows, in the dataset&#39;s own grammar. |
| **definition_type** | **str** | Required | What this definition reconciles, and so which shape of details it carries. Available values: PortfolioContents, LusidEntity, External. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ExternalRecDefinitionDetails import ExternalRecDefinitionDetails

instance = ExternalRecDefinitionDetails(
    matching_ruleset_id=ResourceId(...),  # required
    left_filter="...",  # optional — Optional filter over the left dataset&#39;s rows, in the dataset&#39;s own grammar, e.g. \&quot;Values[custodian] eq &#39;something&#39;\&quot;.
    right_filter="...",  # optional — Optional filter over the right dataset&#39;s rows, in the dataset&#39;s own grammar.
    definition_type="..."  # required — What this definition reconciles, and so which shape of details it carries. Available values: PortfolioContents, LusidEntity, External.
)
```


## Related Models

- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

