# PaymentInstructionStatus

The current status of a Payment Instruction. Managed exclusively via the dedicated  status transition API — not accepted on upsert.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **current_value** | **str** | Required | The current status value. One of: Created, Staged, Released, Instructed, Sent, Cancelled. |
| **as_at_last_transition** | **datetime** | Required | The as-at timestamp of the most recent status transition. |
| **user_id_last_transition** | **str** | Required | The ID of the user who made the most recent status transition. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PaymentInstructionStatus import PaymentInstructionStatus

instance = PaymentInstructionStatus(
    current_value="...",  # required — The current status value. One of: Created, Staged, Released, Instructed, Sent, Cancelled.
    as_at_last_transition=datetime.now(),  # required — The as-at timestamp of the most recent status transition.
    user_id_last_transition="..."  # required — The ID of the user who made the most recent status transition.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

