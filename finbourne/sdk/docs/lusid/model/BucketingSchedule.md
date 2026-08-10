# BucketingSchedule

A schedule for dates
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **tenor** | **str** | Optional | Rolling tenor |
| **roll_direction** | **str** | Optional | Optional direction in which the bucketing dates are rolled out from the schedule tenor.  Supported string (enumeration) values are: [ForwardFromStart, BackwardFromEnd].  If absent (and StubType is also absent), the pre-existing date generation behaviour is used. Available values: ForwardFromStart, BackwardFromEnd. |
| **stub_type** | **str** | Optional | Optional treatment of the irregular (stub) period when the window length is not an exact multiple of the tenor.  Supported string (enumeration) values are: [ShortStub, LongStub].  If absent (and RollDirection is also absent), the pre-existing date generation behaviour is used. Available values: ShortStub, LongStub. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.BucketingSchedule import BucketingSchedule

instance = BucketingSchedule(
    tenor="...",  # optional — Rolling tenor
    roll_direction="...",  # optional — Optional direction in which the bucketing dates are rolled out from the schedule tenor.  Supported string (enumeration) values are: [ForwardFromStart, BackwardFromEnd].  If absent (and StubType is also absent), the pre-existing date generation behaviour is used. Available values: ForwardFromStart, BackwardFromEnd.
    stub_type="..."  # optional — Optional treatment of the irregular (stub) period when the window length is not an exact multiple of the tenor.  Supported string (enumeration) values are: [ShortStub, LongStub].  If absent (and RollDirection is also absent), the pre-existing date generation behaviour is used. Available values: ShortStub, LongStub.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

