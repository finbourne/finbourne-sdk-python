# DataSeries

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **series_scope** | **str** | Required | The scope of the DataSeries. |
| **applicable_entity** | [ApplicableEntity](ApplicableEntity.md) | Required | *No description available.* |
| **series_identifiers** | **Dict[str, Optional[object]]** | Optional | The identifiers that uniquely define this DataSeries, if any, structured according to the FieldSchema of the parent RelationalDatasetDefinition. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.DataSeries import DataSeries

instance = DataSeries(
    series_scope="...",  # required — The scope of the DataSeries.
    applicable_entity=ApplicableEntity(...),  # required
    series_identifiers=  # optional — The identifiers that uniquely define this DataSeries, if any, structured according to the FieldSchema of the parent RelationalDatasetDefinition.
)
```

- [ApplicableEntity](ApplicableEntity.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

