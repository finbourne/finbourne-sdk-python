# BatchAcceptMarginCallsResponse

The outcome of accepting several margin calls: those accepted, and those refused with the reason.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **values** | [List[MarginCall]](MarginCall.md) | Required | The calls that were accepted. |
| **failed** | [Dict[str, ErrorDetail]](ErrorDetail.md) | Required | The calls that could not be accepted, keyed by call id, with the reason. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.BatchAcceptMarginCallsResponse import BatchAcceptMarginCallsResponse

instance = BatchAcceptMarginCallsResponse(
    values=[],  # required — The calls that were accepted.
    failed=ErrorDetail(...)  # required — The calls that could not be accepted, keyed by call id, with the reason.
)
```


## Related Models

- [MarginCall](MarginCall.md) — used in `values`
- [ErrorDetail](ErrorDetail.md) — used in `failed`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

