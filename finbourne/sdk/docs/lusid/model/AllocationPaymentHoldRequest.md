# AllocationPaymentHoldRequest

The request used to place, move or release a hold on a partner's payment against an allocation event.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **status** | **str** | Required | The hold status to set: Blocked, Escrow or Released. A hold may only be released by a different user from the one who placed it. |
| **reason** | **str** | Optional | The reason for the hold. |
| **reference** | **str** | Optional | An external reference for the hold, such as a compliance case number. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AllocationPaymentHoldRequest import AllocationPaymentHoldRequest

instance = AllocationPaymentHoldRequest(
    status="...",  # required — The hold status to set: Blocked, Escrow or Released. A hold may only be released by a different user from the one who placed it.
    reason="...",  # optional — The reason for the hold.
    reference="..."  # optional — An external reference for the hold, such as a compliance case number.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

