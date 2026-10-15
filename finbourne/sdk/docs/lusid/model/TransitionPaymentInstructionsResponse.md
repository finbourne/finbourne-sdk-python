# TransitionPaymentInstructionsResponse

The response from transitioning the status of a set of Payment Instructions. Each request key from the  incoming map appears in exactly one of Values or Failed.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **values** | [Dict[str, PaymentInstruction]](PaymentInstruction.md) | Optional | The Payment Instructions that were transitioned successfully, at their new status, keyed by the ephemeral request key supplied by the caller. |
| **failed** | [Dict[str, ErrorDetail]](ErrorDetail.md) | Optional | Details of the requested transitions that failed, keyed by the ephemeral request key supplied by the caller. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TransitionPaymentInstructionsResponse import TransitionPaymentInstructionsResponse

instance = TransitionPaymentInstructionsResponse(
    values=PaymentInstruction(...),  # optional — The Payment Instructions that were transitioned successfully, at their new status, keyed by the ephemeral request key supplied by the caller.
    failed=ErrorDetail(...),  # optional — Details of the requested transitions that failed, keyed by the ephemeral request key supplied by the caller.
    links=[]  # optional
)
```


## Related Models

- [PaymentInstruction](PaymentInstruction.md) — used in `values`
- [ErrorDetail](ErrorDetail.md) — used in `failed`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

