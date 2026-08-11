# BatchDeleteRelationalDataResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **values** | **Dict[str, Optional[str]]** | Required | A list of data points that were successfully upserted. |
| **failed** | [Dict[str, ErrorDetail]](ErrorDetail.md) | Optional | A list of data points that failed to be upserted, along with the associated error message. |
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.BatchDeleteRelationalDataResponse import BatchDeleteRelationalDataResponse

instance = BatchDeleteRelationalDataResponse(
    values=,  # required — A list of data points that were successfully upserted.
    failed=ErrorDetail(...),  # optional — A list of data points that failed to be upserted, along with the associated error message.
    href="..."  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
)
```

- [ErrorDetail](ErrorDetail.md) — used in `failed`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

