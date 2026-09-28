# AggregateNumericTolerance

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **reference_side** | **str** | Required | Reference side (source of truth). One of: Left, Right. Available values: Left, Right. |
| **absolute_threshold** | **float** | Optional | Numeric tolerance absolute value (allowable diff compared to the reference side value). |
| **relative_threshold** | **float** | Optional | Numeric tolerance value as a relative % of the reference value. |
| **threshold_priority** | **str** | Required | Whether to apply the GreaterOf or LesserOf the absoluteThreshold vs relativeThreshold. One of: GreaterOf, LesserOf. Available values: GreaterOf, LesserOf. |
| **offset** | **str** | Optional | How the threshold should be applied to the reference side value. One of: Above, Below, Either. Defaults to Either. Available values: Above, Below, Either. |
| **tolerance_type** | **str** | Required | Polymorphic discriminator. Supported types: CoreStringCross, CoreAttributeOptionality, CoreDateTolerance, Numeric. Available values: CoreStringCross, CoreAttributeOptionality, CoreDateTolerance, Numeric. |
| **rule_name** | **str** | Required | The reference name of the rule that this tolerance relaxes. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AggregateNumericTolerance import AggregateNumericTolerance

instance = AggregateNumericTolerance(
    reference_side="...",  # required — Reference side (source of truth). One of: Left, Right. Available values: Left, Right.
    absolute_threshold=0.0,  # optional — Numeric tolerance absolute value (allowable diff compared to the reference side value).
    relative_threshold=0.0,  # optional — Numeric tolerance value as a relative % of the reference value.
    threshold_priority="...",  # required — Whether to apply the GreaterOf or LesserOf the absoluteThreshold vs relativeThreshold. One of: GreaterOf, LesserOf. Available values: GreaterOf, LesserOf.
    offset="...",  # optional — How the threshold should be applied to the reference side value. One of: Above, Below, Either. Defaults to Either. Available values: Above, Below, Either.
    tolerance_type="...",  # required — Polymorphic discriminator. Supported types: CoreStringCross, CoreAttributeOptionality, CoreDateTolerance, Numeric. Available values: CoreStringCross, CoreAttributeOptionality, CoreDateTolerance, Numeric.
    rule_name="..."  # required — The reference name of the rule that this tolerance relaxes.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

