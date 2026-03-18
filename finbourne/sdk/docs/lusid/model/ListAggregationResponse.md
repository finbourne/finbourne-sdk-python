# ListAggregationResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **aggregation_effective_at** | **datetime** | Optional | *No description available.* |
| **aggregation_as_at** | **datetime** | Optional | *No description available.* |
| **href** | **str** | Optional | *No description available.* |
| **data** | **List[Dict[str, object]]** | Optional | *No description available.* |
| **aggregation_currency** | **str** | Optional | *No description available.* |
| **data_schema** | [ResultDataSchema](ResultDataSchema.md) | Optional | *No description available.* |
| **aggregation_failures** | [List[AggregationMeasureFailureDetail]](AggregationMeasureFailureDetail.md) | Optional | *No description available.* |
| **recipe_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ListAggregationResponse import ListAggregationResponse

instance = ListAggregationResponse(
    aggregation_effective_at=datetime.now(),  # optional
    aggregation_as_at=datetime.now(),  # optional
    href="...",  # optional
    data=,  # optional
    aggregation_currency="...",  # optional
    data_schema=ResultDataSchema(...),  # optional
    aggregation_failures=[],  # optional
    recipe_id=ResourceId(...),  # optional
    links=[]  # optional
)
```

- [ResultDataSchema](ResultDataSchema.md)
- [AggregationMeasureFailureDetail](AggregationMeasureFailureDetail.md)
- [ResourceId](ResourceId.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

