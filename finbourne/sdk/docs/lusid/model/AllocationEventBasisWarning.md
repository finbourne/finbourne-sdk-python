# AllocationEventBasisWarning

One thing the basis source had to work around when it read the register for an Allocation Event.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **code** | **str** | Optional | The warning, for example MissingFeeRate or RoundingPartnerNotParticipant. |
| **investor_record_id** | **str** | Optional | The investor record the warning concerns, or absent when it concerns the event as a whole. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AllocationEventBasisWarning import AllocationEventBasisWarning

instance = AllocationEventBasisWarning(
    code="...",  # optional — The warning, for example MissingFeeRate or RoundingPartnerNotParticipant.
    investor_record_id="..."  # optional — The investor record the warning concerns, or absent when it concerns the event as a whole.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

