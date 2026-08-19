# ToleranceBase

Base class for the tolerances that relax how strictly a matching rule compares its two sides. Polymorphic  by ToleranceType; each supported type has a corresponding inherited class.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **tolerance_type** | **str** | Required | Polymorphic discriminator. Supported types: CoreStringCross, CoreAttributeOptionality, CoreDateTolerance, Numeric. Available values: CoreStringCross, CoreAttributeOptionality, CoreDateTolerance, Numeric. |
| **rule_name** | **str** | Required | The reference name of the rule that this tolerance relaxes. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ToleranceBase import ToleranceBase

instance = ToleranceBase(
    tolerance_type="...",  # required — Polymorphic discriminator. Supported types: CoreStringCross, CoreAttributeOptionality, CoreDateTolerance, Numeric. Available values: CoreStringCross, CoreAttributeOptionality, CoreDateTolerance, Numeric.
    rule_name="..."  # required — The reference name of the rule that this tolerance relaxes.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

