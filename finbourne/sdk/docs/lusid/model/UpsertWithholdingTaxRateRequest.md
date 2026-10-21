# UpsertWithholdingTaxRateRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **series_identifiers** | **Dict[str, Optional[object]]** | Optional | The series identifiers that, with effectiveAt, identify the rate row: taxCountry, profileType and the dataset&#39;s own matching dimensions, structured according to its field schema. ruleSource is not accepted here: pass it as the ruleSource query parameter, which applies it to every row in the batch, and omit it for rows that apply at every source. |
| **effective_at** | **str** | Required | The effectiveAt or cut-label datetime of the DataPoint. |
| **value_fields** | **Dict[str, Optional[object]]** | Required | The values associated with the DataPoint, structured according to the FieldSchema of the parent RelationalDatasetDefinition. |
| **meta_data_fields** | **Dict[str, Optional[object]]** | Optional | The metadata associated with the DataPoint, structured according to the FieldSchema of the parent RelationalDatasetDefinition. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpsertWithholdingTaxRateRequest import UpsertWithholdingTaxRateRequest

instance = UpsertWithholdingTaxRateRequest(
    series_identifiers=,  # optional — The series identifiers that, with effectiveAt, identify the rate row: taxCountry, profileType and the dataset&#39;s own matching dimensions, structured according to its field schema. ruleSource is not accepted here: pass it as the ruleSource query parameter, which applies it to every row in the batch, and omit it for rows that apply at every source.
    effective_at="...",  # required — The effectiveAt or cut-label datetime of the DataPoint.
    value_fields=,  # required — The values associated with the DataPoint, structured according to the FieldSchema of the parent RelationalDatasetDefinition.
    meta_data_fields=  # optional — The metadata associated with the DataPoint, structured according to the FieldSchema of the parent RelationalDatasetDefinition.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

