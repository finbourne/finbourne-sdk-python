# ExportAggregation

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **col_id** | **str** | Required | *No description available.* |
| **agg_func** | [ExportAggregationFunction](ExportAggregationFunction.md) | Optional | *No description available.* |
| **placement** | [ExportAggregationPlacement](ExportAggregationPlacement.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.luminesce.models.ExportAggregation import ExportAggregation

instance = ExportAggregation(
    col_id="...",  # required
    agg_func=ExportAggregationFunction(...),  # optional
    placement=ExportAggregationPlacement(...)  # optional
)
```

- [ExportAggregationFunction](ExportAggregationFunction.md)
- [ExportAggregationPlacement](ExportAggregationPlacement.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

