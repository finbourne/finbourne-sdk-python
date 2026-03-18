# SweepBlocksResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **values** | [Dict[str, ResourceId]](ResourceId.md) | Optional | The identifiers of blocks which have been successfully swept, indexed by ephemeral request-lived id. |
| **failed** | [Dict[str, ErrorDetail]](ErrorDetail.md) | Optional | The identifiers of blocks that could not be swept, along with a reason for their failure. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.SweepBlocksResponse import SweepBlocksResponse

instance = SweepBlocksResponse(
    values=ResourceId(...),  # optional — The identifiers of blocks which have been successfully swept, indexed by ephemeral request-lived id.
    failed=ErrorDetail(...)  # optional — The identifiers of blocks that could not be swept, along with a reason for their failure.
)
```


## Related Models

- [ResourceId](ResourceId.md) — used in `values`
- [ErrorDetail](ErrorDetail.md) — used in `failed`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

