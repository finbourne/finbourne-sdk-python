# ListAggregationResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **aggregation_effective_at** | **datetime** | Optional | *No description available.* |
| **aggregation_as_at** | **datetime** | Optional | *No description available.* |
| **href** | **str** | Optional | *No description available.* |
| **data** | **List[Dict[str, object]]** | Optional | *No description available.* |
| **aggregation_currency** | **str** | Optional | *No description available.* |
| **data_schema** | [../model/ResultDataSchema](ResultDataSchema.md) | Optional | *No description available.* |
| **aggregation_failures** | [../model/List[AggregationMeasureFailureDetail]](AggregationMeasureFailureDetail.md) | Optional | *No description available.* |
| **recipe_id** | [../model/ResourceId](ResourceId.md) | Optional | *No description available.* |
| **scenario_diagnostics** | [../model/ScenarioDiagnostics](ScenarioDiagnostics.md) | Optional | *No description available.* |
| **links** | [../model/List[Link]](Link.md) | Optional | *No description available.* |


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
    scenario_diagnostics=ScenarioDiagnostics(...),  # optional
    links=[]  # optional
)
```

- [ResultDataSchema](ResultDataSchema.md)
- [AggregationMeasureFailureDetail](AggregationMeasureFailureDetail.md)
- [ResourceId](ResourceId.md)
- [ScenarioDiagnostics](ScenarioDiagnostics.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

