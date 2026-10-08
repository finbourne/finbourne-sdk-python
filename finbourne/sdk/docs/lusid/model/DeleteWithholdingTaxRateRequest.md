# DeleteWithholdingTaxRateRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **series_identifiers** | **Dict[str, Optional[object]]** | Optional | The identifiers that uniquely define this DataSeries, if any, structured according to the FieldSchema of the parent RelationalDatasetDefinition. |
| **effective_at** | **str** | Required | The effectiveAt or cut-label datetime of the DataPoint. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.DeleteWithholdingTaxRateRequest import DeleteWithholdingTaxRateRequest

instance = DeleteWithholdingTaxRateRequest(
    series_identifiers=,  # optional — The identifiers that uniquely define this DataSeries, if any, structured according to the FieldSchema of the parent RelationalDatasetDefinition.
    effective_at="..."  # required — The effectiveAt or cut-label datetime of the DataPoint.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

