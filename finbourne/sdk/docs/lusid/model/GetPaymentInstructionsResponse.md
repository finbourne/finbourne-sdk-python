# GetPaymentInstructionsResponse

The response from getting Payment Instructions by payment record id. Each requested payment record id  appears in exactly one of Values or Failed.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **values** | [Dict[str, PaymentInstruction]](PaymentInstruction.md) | Optional | The Payment Instructions that were found, keyed by the payment record id used to retrieve them. Only Payment Instructions that were found will be contained in this collection. |
| **failed** | [Dict[str, ErrorDetail]](ErrorDetail.md) | Optional | The payment record ids that did not resolve to a Payment Instruction, along with the nature of the failure. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.GetPaymentInstructionsResponse import GetPaymentInstructionsResponse

instance = GetPaymentInstructionsResponse(
    values=PaymentInstruction(...),  # optional — The Payment Instructions that were found, keyed by the payment record id used to retrieve them. Only Payment Instructions that were found will be contained in this collection.
    failed=ErrorDetail(...),  # optional — The payment record ids that did not resolve to a Payment Instruction, along with the nature of the failure.
    links=[]  # optional
)
```


## Related Models

- [PaymentInstruction](PaymentInstruction.md) — used in `values`
- [ErrorDetail](ErrorDetail.md) — used in `failed`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

