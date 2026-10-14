# AllocationEventRoundingResidual

The cents left over when one component of an Allocation Event was rounded to the currency's minor unit, and where they went.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **component** | **str** | Optional | The component the residual belongs to. |
| **cents** | **int** | Optional | The number of minor units left over after each share was truncated to the currency. |
| **amount** | **float** | Optional | The same, in the event currency. |
| **method** | **str** | Optional | How the leftover was placed: LargestRemainder spreads it one minor unit at a time over the largest remainders; RoundingPartner gives all of it to the map&#39;s rounding partner line. Available values: LargestRemainder, RoundingPartner. |
| **taken_by** | **List[str]** | Optional | The investor records that each took a minor unit, in the order they took it. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AllocationEventRoundingResidual import AllocationEventRoundingResidual

instance = AllocationEventRoundingResidual(
    component="...",  # optional — The component the residual belongs to.
    cents=0,  # optional — The number of minor units left over after each share was truncated to the currency.
    amount=0.0,  # optional — The same, in the event currency.
    method="...",  # optional — How the leftover was placed: LargestRemainder spreads it one minor unit at a time over the largest remainders; RoundingPartner gives all of it to the map&#39;s rounding partner line. Available values: LargestRemainder, RoundingPartner.
    taken_by=  # optional — The investor records that each took a minor unit, in the order they took it.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

