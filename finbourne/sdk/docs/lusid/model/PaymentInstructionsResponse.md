# PaymentInstructionsResponse

The response from upserting a set of Payment Instructions. Each request key from the  incoming map appears in exactly one of Successes or Failed.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **successes** | [Dict[str, PaymentInstruction]](PaymentInstruction.md) | Optional | The Payment Instructions that were created or updated successfully, keyed by the ephemeral request key supplied by the caller. |
| **failed** | [Dict[str, ErrorDetail]](ErrorDetail.md) | Optional | Details of the requests that failed, keyed by the ephemeral request key supplied by the caller. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PaymentInstructionsResponse import PaymentInstructionsResponse

instance = PaymentInstructionsResponse(
    successes=PaymentInstruction(...),  # optional — The Payment Instructions that were created or updated successfully, keyed by the ephemeral request key supplied by the caller.
    failed=ErrorDetail(...),  # optional — Details of the requests that failed, keyed by the ephemeral request key supplied by the caller.
    links=[]  # optional
)
```


## Related Models

- [PaymentInstruction](PaymentInstruction.md) — used in `successes`
- [ErrorDetail](ErrorDetail.md) — used in `failed`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

