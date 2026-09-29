# CoreStringCrossTolerance

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **reference_value** | **str** | Required | The value for the reference side. |
| **cross_value** | **str** | Required | The value for the side other than the reference one. |
| **reference_side** | **str** | Optional | Reference side (source of truth). Available values: Left, Right, Either. |
| **tolerance_type** | **str** | Required | Polymorphic discriminator. Supported types: CoreStringCross, CoreAttributeOptionality, CoreDateTolerance, Numeric. Available values: CoreStringCross, CoreAttributeOptionality, CoreDateTolerance, Numeric. |
| **rule_name** | **str** | Required | The reference name of the rule that this tolerance relaxes. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CoreStringCrossTolerance import CoreStringCrossTolerance

instance = CoreStringCrossTolerance(
    reference_value="...",  # required — The value for the reference side.
    cross_value="...",  # required — The value for the side other than the reference one.
    reference_side="...",  # optional — Reference side (source of truth). Available values: Left, Right, Either.
    tolerance_type="...",  # required — Polymorphic discriminator. Supported types: CoreStringCross, CoreAttributeOptionality, CoreDateTolerance, Numeric. Available values: CoreStringCross, CoreAttributeOptionality, CoreDateTolerance, Numeric.
    rule_name="..."  # required — The reference name of the rule that this tolerance relaxes.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

