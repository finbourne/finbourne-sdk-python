# CreatePortfolioDetails

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **corporate_action_source_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **tax_lot_selection_cost_basis** | **str** | Optional | The cost figure that cost-referencing accounting methods evaluate when selecting tax lots for a disposal. This can be: Cost or AmortisedCost. If not supplied, the portfolio&#39;s current value is left unchanged; supply Default to reset it. A reset or never-configured basis reads back as absent. Available values: Default, Cost, AmortisedCost. |
| **fractional_units_true_up_configuration** | [FractionalUnitsTrueUpConfiguration](FractionalUnitsTrueUpConfiguration.md) | Optional | *No description available.* |
| **holdings_fungibility** | **str** | Optional | Whether the portfolio&#39;s holdings are fungible across the currencies of a currency group. This can be: Default or Enabled. If not supplied, the portfolio&#39;s current value is left unchanged; supply Default to reset it. A reset or never-configured flag reads back as absent. Available values: Default, Enabled. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CreatePortfolioDetails import CreatePortfolioDetails

instance = CreatePortfolioDetails(
    corporate_action_source_id=ResourceId(...),  # optional
    tax_lot_selection_cost_basis="...",  # optional — The cost figure that cost-referencing accounting methods evaluate when selecting tax lots for a disposal. This can be: Cost or AmortisedCost. If not supplied, the portfolio&#39;s current value is left unchanged; supply Default to reset it. A reset or never-configured basis reads back as absent. Available values: Default, Cost, AmortisedCost.
    fractional_units_true_up_configuration=FractionalUnitsTrueUpConfiguration(...),  # optional
    holdings_fungibility="..."  # optional — Whether the portfolio&#39;s holdings are fungible across the currencies of a currency group. This can be: Default or Enabled. If not supplied, the portfolio&#39;s current value is left unchanged; supply Default to reset it. A reset or never-configured flag reads back as absent. Available values: Default, Enabled.
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [FractionalUnitsTrueUpConfiguration](FractionalUnitsTrueUpConfiguration.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

