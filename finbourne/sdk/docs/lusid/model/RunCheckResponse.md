# RunCheckResponse

Response containing the results of running data quality checks
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **data_quality_check_results** | [List[DataQualityCheckResult]](DataQualityCheckResult.md) | Optional | Collection of data quality check results |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RunCheckResponse import RunCheckResponse

instance = RunCheckResponse(
    data_quality_check_results=[]  # optional — Collection of data quality check results
)
```


## Related Models

- [DataQualityCheckResult](DataQualityCheckResult.md) — used in `data_quality_check_results`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

