# CoreDateTolerance

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **reference_side** | **str** | Required | Reference side (source of truth). Available values: Left, Right. |
| **interval** | **str** | Required | The allowed tolerance for date time core rule values, defined as an ISO Period. |
| **offset** | **str** | Optional | How the interval should be applied to the reference side value. Defaults to Either. Available values: Earlier, Later, Either. |
| **tolerance_type** | **str** | Required | Polymorphic discriminator. Supported types: CoreStringCross, CoreAttributeOptionality, CoreDateTolerance, Numeric. Available values: CoreStringCross, CoreAttributeOptionality, CoreDateTolerance, Numeric. |
| **rule_name** | **str** | Required | The reference name of the rule that this tolerance relaxes. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CoreDateTolerance import CoreDateTolerance

instance = CoreDateTolerance(
    reference_side="...",  # required — Reference side (source of truth). Available values: Left, Right.
    interval="...",  # required — The allowed tolerance for date time core rule values, defined as an ISO Period.
    offset="...",  # optional — How the interval should be applied to the reference side value. Defaults to Either. Available values: Earlier, Later, Either.
    tolerance_type="...",  # required — Polymorphic discriminator. Supported types: CoreStringCross, CoreAttributeOptionality, CoreDateTolerance, Numeric. Available values: CoreStringCross, CoreAttributeOptionality, CoreDateTolerance, Numeric.
    rule_name="..."  # required — The reference name of the rule that this tolerance relaxes.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

