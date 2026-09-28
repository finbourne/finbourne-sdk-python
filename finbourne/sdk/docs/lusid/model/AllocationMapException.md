# AllocationMapException

A departure from the default participation of an Allocation Map for one investor record.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **investor_record_id** | **str** | Required | The investor record the exception applies to. |
| **treatment** | **str** | Required | What the exception does. Excluded removes the investor record from every allocation; FixedPercentage gives it participationPercent of each event off the top, before the remainder is shared pro rata between the other participants. Available values: Excluded, FixedPercentage. |
| **participation_percent** | **float** | Optional | For a FixedPercentage exception, the fixed share as a fraction in the range (0, 1]. Not allowed on an Excluded exception. The fixed shares of all exceptions may not sum to more than 1. |
| **reason** | **str** | Required | Why the exception exists, for example a side letter or regulatory restriction. Required. |
| **effective_from** | **datetime** | Optional | The datetime from which the exception is in force. Defaults to always if not specified. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AllocationMapException import AllocationMapException

instance = AllocationMapException(
    investor_record_id="...",  # required — The investor record the exception applies to.
    treatment="...",  # required — What the exception does. Excluded removes the investor record from every allocation; FixedPercentage gives it participationPercent of each event off the top, before the remainder is shared pro rata between the other participants. Available values: Excluded, FixedPercentage.
    participation_percent=0.0,  # optional — For a FixedPercentage exception, the fixed share as a fraction in the range (0, 1]. Not allowed on an Excluded exception. The fixed shares of all exceptions may not sum to more than 1.
    reason="...",  # required — Why the exception exists, for example a side letter or regulatory restriction. Required.
    effective_from=datetime.now()  # optional — The datetime from which the exception is in force. Defaults to always if not specified.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

