# UpsertRelationalDataPointRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **data_series** | [DataSeries](DataSeries.md) | Required | *No description available.* |
| **effective_at** | **str** | Required | The effectiveAt or cut-label datetime of the DataPoint. |
| **value_fields** | **Dict[str, Optional[object]]** | Required | The values associated with the DataPoint, structured according to the FieldSchema of the parent RelationalDatasetDefinition. |
| **meta_data_fields** | **Dict[str, Optional[object]]** | Optional | The metadata associated with the DataPoint, structured according to the FieldSchema of the parent RelationalDatasetDefinition. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpsertRelationalDataPointRequest import UpsertRelationalDataPointRequest

instance = UpsertRelationalDataPointRequest(
    data_series=DataSeries(...),  # required
    effective_at="...",  # required — The effectiveAt or cut-label datetime of the DataPoint.
    value_fields=,  # required — The values associated with the DataPoint, structured according to the FieldSchema of the parent RelationalDatasetDefinition.
    meta_data_fields=  # optional — The metadata associated with the DataPoint, structured according to the FieldSchema of the parent RelationalDatasetDefinition.
)
```


## Related Models

- [DataSeries](DataSeries.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

