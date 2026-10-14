# AllocationEventReversal

How a booked Allocation Event was reversed.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **reference** | **str** | Optional | The reference the mirror postings were written under: the original booking reference with a -REV suffix. |
| **reason** | **str** | Optional | Why the event was reversed. |
| **reversed_at** | **datetime** | Optional | The datetime at which the event was reversed. |
| **effective_at** | **datetime** | Optional | The date the mirror postings were posted at. |
| **backdated** | **bool** | Optional | Whether the mirror postings were posted at the original event date despite the period being closed. |
| **refund_payable** | [List[AllocationEventRefund]](AllocationEventRefund.md) | Optional | Cash owed back to investors who had already paid in when the event was reversed. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AllocationEventReversal import AllocationEventReversal

instance = AllocationEventReversal(
    reference="...",  # optional — The reference the mirror postings were written under: the original booking reference with a -REV suffix.
    reason="...",  # optional — Why the event was reversed.
    reversed_at=datetime.now(),  # optional — The datetime at which the event was reversed.
    effective_at=datetime.now(),  # optional — The date the mirror postings were posted at.
    backdated=True,  # optional — Whether the mirror postings were posted at the original event date despite the period being closed.
    refund_payable=[]  # optional — Cash owed back to investors who had already paid in when the event was reversed.
)
```

- [AllocationEventRefund](AllocationEventRefund.md) — used in `refund_payable`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

