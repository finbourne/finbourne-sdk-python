# AllocationEventTransferConsideration

The consideration paid for a transferred capital interest.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **amount** | **float** | Required | The consideration amount. |
| **currency** | **str** | Required | The ISO 4217 code of the currency of the consideration. |
| **record_only** | **bool** | Optional | Whether the consideration is recorded for reference only, with no cash movement booked. Defaults to false. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AllocationEventTransferConsideration import AllocationEventTransferConsideration

instance = AllocationEventTransferConsideration(
    amount=0.0,  # required — The consideration amount.
    currency="...",  # required — The ISO 4217 code of the currency of the consideration.
    record_only=True  # optional — Whether the consideration is recorded for reference only, with no cash movement booked. Defaults to false.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

