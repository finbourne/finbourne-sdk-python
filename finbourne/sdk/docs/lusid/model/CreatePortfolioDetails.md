# CreatePortfolioDetails

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **corporate_action_source_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **tax_lot_selection_cost_basis** | **str** | Optional | The cost figure that cost-referencing accounting methods evaluate when selecting tax lots for a disposal. This can be: Cost or AmortisedCost. If not supplied, the portfolio&#39;s current value is left unchanged; supply Default to reset it. Available values: Cost, AmortisedCost. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CreatePortfolioDetails import CreatePortfolioDetails

instance = CreatePortfolioDetails(
    corporate_action_source_id=ResourceId(...),  # optional
    tax_lot_selection_cost_basis="..."  # optional — The cost figure that cost-referencing accounting methods evaluate when selecting tax lots for a disposal. This can be: Cost or AmortisedCost. If not supplied, the portfolio&#39;s current value is left unchanged; supply Default to reset it. Available values: Cost, AmortisedCost.
)
```


## Related Models

- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

