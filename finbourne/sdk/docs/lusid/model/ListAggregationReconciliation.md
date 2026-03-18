# ListAggregationReconciliation

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **left** | [ListAggregationResponse](ListAggregationResponse.md) | Optional | *No description available.* |
| **right** | [ListAggregationResponse](ListAggregationResponse.md) | Optional | *No description available.* |
| **diff** | **List[Dict[str, object]]** | Optional | *No description available.* |
| **data_schema** | [ResultDataSchema](ResultDataSchema.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ListAggregationReconciliation import ListAggregationReconciliation

instance = ListAggregationReconciliation(
    left=ListAggregationResponse(...),  # optional
    right=ListAggregationResponse(...),  # optional
    diff=,  # optional
    data_schema=ResultDataSchema(...)  # optional
)
```


## Related Models

- [ListAggregationResponse](ListAggregationResponse.md)
- [ListAggregationResponse](ListAggregationResponse.md)
- [ResultDataSchema](ResultDataSchema.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

