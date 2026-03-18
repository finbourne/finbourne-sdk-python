# RelationalDataPointResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **relational_dataset_definition_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **data_series** | [RelationalDataSeriesResponse](RelationalDataSeriesResponse.md) | Required | *No description available.* |
| **effective_at** | **datetime** | Required | The effectiveAt or cut-label datetime of the DataPoint. |
| **value_fields** | [Dict[str, RelationalDataPointFieldValueResponse]](RelationalDataPointFieldValueResponse.md) | Required | The values associated with the DataPoint, structured according to the FieldSchema of the parent RelationalDatasetDefinition. |
| **meta_data_fields** | [Dict[str, RelationalDataPointFieldValueResponse]](RelationalDataPointFieldValueResponse.md) | Required | The metadata associated with the DataPoint, structured according to the FieldSchema of the parent RelationalDatasetDefinition. |
| **effective_at_entered** | **str** | Required | The effectiveAt datetime as entered when the DataPoint was created. |
| **data_point_version** | [DataPointVersion](DataPointVersion.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RelationalDataPointResponse import RelationalDataPointResponse

instance = RelationalDataPointResponse(
    relational_dataset_definition_id=ResourceId(...),  # required
    data_series=RelationalDataSeriesResponse(...),  # required
    effective_at=datetime.now(),  # required — The effectiveAt or cut-label datetime of the DataPoint.
    value_fields=RelationalDataPointFieldValueResponse(...),  # required — The values associated with the DataPoint, structured according to the FieldSchema of the parent RelationalDatasetDefinition.
    meta_data_fields=RelationalDataPointFieldValueResponse(...),  # required — The metadata associated with the DataPoint, structured according to the FieldSchema of the parent RelationalDatasetDefinition.
    effective_at_entered="...",  # required — The effectiveAt datetime as entered when the DataPoint was created.
    data_point_version=DataPointVersion(...)  # optional
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [RelationalDataSeriesResponse](RelationalDataSeriesResponse.md)
- [RelationalDataPointFieldValueResponse](RelationalDataPointFieldValueResponse.md) — used in `value_fields`
- [RelationalDataPointFieldValueResponse](RelationalDataPointFieldValueResponse.md) — used in `meta_data_fields`
- [DataPointVersion](DataPointVersion.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

