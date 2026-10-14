# AllocationReceivable

One investor's position on a booked capital call.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **investor_record_id** | **str** | Optional | The investor record. |
| **called** | **float** | Optional | What the investor record was called for. |
| **received** | **float** | Optional | What has been received and applied so far. |
| **outstanding** | **float** | Optional | What is still owed. Never negative: an overpayment becomes a refund payable instead. |
| **days_past_due** | **int** | Optional | How many days past the due date the outstanding amount is, or zero when not yet due or nothing is owed. |
| **bucket** | **str** | Optional | The ageing bucket: Current, 1-30, 31-60, 61-90 or 90+. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AllocationReceivable import AllocationReceivable

instance = AllocationReceivable(
    investor_record_id="...",  # optional — The investor record.
    called=0.0,  # optional — What the investor record was called for.
    received=0.0,  # optional — What has been received and applied so far.
    outstanding=0.0,  # optional — What is still owed. Never negative: an overpayment becomes a refund payable instead.
    days_past_due=0,  # optional — How many days past the due date the outstanding amount is, or zero when not yet due or nothing is owed.
    bucket="..."  # optional — The ageing bucket: Current, 1-30, 31-60, 61-90 or 90+.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

