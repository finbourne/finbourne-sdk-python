# CoreAttributeOptionalityTolerance

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **optional_side** | **str** | Optional | Which side is allowed to have no value while still attempting to match. Defaults to Either. Available values: Left, Right, Either. |
| **tolerance_type** | **str** | Required | Polymorphic discriminator. Supported types: CoreStringCross, CoreAttributeOptionality, CoreDateTolerance, Numeric. Available values: CoreStringCross, CoreAttributeOptionality, CoreDateTolerance, Numeric. |
| **rule_name** | **str** | Required | The reference name of the rule that this tolerance relaxes. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CoreAttributeOptionalityTolerance import CoreAttributeOptionalityTolerance

instance = CoreAttributeOptionalityTolerance(
    optional_side="...",  # optional — Which side is allowed to have no value while still attempting to match. Defaults to Either. Available values: Left, Right, Either.
    tolerance_type="...",  # required — Polymorphic discriminator. Supported types: CoreStringCross, CoreAttributeOptionality, CoreDateTolerance, Numeric. Available values: CoreStringCross, CoreAttributeOptionality, CoreDateTolerance, Numeric.
    rule_name="..."  # required — The reference name of the rule that this tolerance relaxes.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

