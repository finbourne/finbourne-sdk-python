# DeleteRelationalDataPointRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **data_series** | [DataSeries](DataSeries.md) | Required | *No description available.* |
| **effective_at** | **str** | Required | The effectiveAt or cut-label datetime of the DataPoint. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.DeleteRelationalDataPointRequest import DeleteRelationalDataPointRequest

instance = DeleteRelationalDataPointRequest(
    data_series=DataSeries(...),  # required
    effective_at="..."  # required — The effectiveAt or cut-label datetime of the DataPoint.
)
```


## Related Models

- [DataSeries](DataSeries.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

