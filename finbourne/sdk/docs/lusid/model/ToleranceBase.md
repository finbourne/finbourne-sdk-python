# ToleranceBase

Base class for the tolerances that relax how strictly a matching rule compares its two sides. Polymorphic  by ToleranceType; each supported type has a corresponding inherited class.

## oneOf Type

`ToleranceBase` can be one of the following types:

* [AggregateNumericTolerance](./AggregateNumericTolerance.md)
* [CoreAttributeOptionalityTolerance](./CoreAttributeOptionalityTolerance.md)
* [CoreDateTolerance](./CoreDateTolerance.md)
* [CoreStringCrossTolerance](./CoreStringCrossTolerance.md)

## Usage

### Creating from a compatible type

```python
from finbourne.sdk.services.lusid.models.ToleranceBase import ToleranceBase

# Construct using any of the compatible types above
aggregate_numeric_tolerance_instance = lusid.models.aggregate_numeric_tolerance.AggregateNumericTolerance(
                        reference_side = '', 
                        absolute_threshold = 1.337, 
                        relative_threshold = 1.337, 
                        threshold_priority = '', 
                        offset = '', 
                        tolerance_type = '', 
                        rule_name = '', )

instance = ToleranceBase(aggregate_numeric_tolerance_instance)
```

## Related Models

- [AggregateNumericTolerance](./AggregateNumericTolerance.md)
- [CoreAttributeOptionalityTolerance](./CoreAttributeOptionalityTolerance.md)
- [CoreDateTolerance](./CoreDateTolerance.md)
- [CoreStringCrossTolerance](./CoreStringCrossTolerance.md)

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

