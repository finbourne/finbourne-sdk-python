# PaymentInstructionStatusTransitionRequest

A request to move one Payment Instruction to a new status.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **status** | **str** | Required | The status to move the Payment Instruction to. One of: Created, Staged, Released, Instructed, Sent, Cancelled, Failed. The transition must be permitted from the instruction&#39;s current status. Available values: Created, Staged, Released, Instructed, Sent, Cancelled, Failed. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PaymentInstructionStatusTransitionRequest import PaymentInstructionStatusTransitionRequest

instance = PaymentInstructionStatusTransitionRequest(
    id=ResourceId(...),  # required
    status="..."  # required — The status to move the Payment Instruction to. One of: Created, Staged, Released, Instructed, Sent, Cancelled, Failed. The transition must be permitted from the instruction&#39;s current status. Available values: Created, Staged, Released, Instructed, Sent, Cancelled, Failed.
)
```


## Related Models

- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

