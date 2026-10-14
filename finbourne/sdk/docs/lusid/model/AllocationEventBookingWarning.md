# AllocationEventBookingWarning

One validation rule a booking was allowed to proceed through under the map's policy.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **code** | **str** | Optional | The rule that was allowed through, for instance OverCall. |
| **detail** | **str** | Optional | What the rule found. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AllocationEventBookingWarning import AllocationEventBookingWarning

instance = AllocationEventBookingWarning(
    code="...",  # optional — The rule that was allowed through, for instance OverCall.
    detail="..."  # optional — What the rule found.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

