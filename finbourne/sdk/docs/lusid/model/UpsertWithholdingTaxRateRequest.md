# UpsertWithholdingTaxRateRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **series_identifiers** | **Dict[str, Optional[object]]** | Optional | The identifiers that uniquely define this DataSeries, if any, structured according to the FieldSchema of the parent RelationalDatasetDefinition. |
| **effective_at** | **str** | Required | The effectiveAt or cut-label datetime of the DataPoint. |
| **value_fields** | **Dict[str, Optional[object]]** | Required | The values associated with the DataPoint, structured according to the FieldSchema of the parent RelationalDatasetDefinition. |
| **meta_data_fields** | **Dict[str, Optional[object]]** | Optional | The metadata associated with the DataPoint, structured according to the FieldSchema of the parent RelationalDatasetDefinition. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpsertWithholdingTaxRateRequest import UpsertWithholdingTaxRateRequest

instance = UpsertWithholdingTaxRateRequest(
    series_identifiers=,  # optional — The identifiers that uniquely define this DataSeries, if any, structured according to the FieldSchema of the parent RelationalDatasetDefinition.
    effective_at="...",  # required — The effectiveAt or cut-label datetime of the DataPoint.
    value_fields=,  # required — The values associated with the DataPoint, structured according to the FieldSchema of the parent RelationalDatasetDefinition.
    meta_data_fields=  # optional — The metadata associated with the DataPoint, structured according to the FieldSchema of the parent RelationalDatasetDefinition.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

