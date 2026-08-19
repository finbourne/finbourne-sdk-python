# RecDatasetSchema

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **type** | **str** | Required | The kind of dataset this side draws on. One of: PortfolioContents, LusidEntity, RelationalData. At most one side may be RelationalData. Available values: PortfolioContents, LusidEntity, RelationalData. |
| **entity_type** | **str** | Optional | The entity within the dataset. Required when type is PortfolioContents, in which case it is one of: Holding, Valuation, Transaction, OutputTransaction, SettlementActivity. Must be omitted when type is RelationalData. Available values: Holding, Valuation, Transaction, OutputTransaction, SettlementActivity. |
| **relational_dataset_definition_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RecDatasetSchema import RecDatasetSchema

instance = RecDatasetSchema(
    type="...",  # required — The kind of dataset this side draws on. One of: PortfolioContents, LusidEntity, RelationalData. At most one side may be RelationalData. Available values: PortfolioContents, LusidEntity, RelationalData.
    entity_type="...",  # optional — The entity within the dataset. Required when type is PortfolioContents, in which case it is one of: Holding, Valuation, Transaction, OutputTransaction, SettlementActivity. Must be omitted when type is RelationalData. Available values: Holding, Valuation, Transaction, OutputTransaction, SettlementActivity.
    relational_dataset_definition_id=ResourceId(...)  # optional
)
```

- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

