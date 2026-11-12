# RecActivityWindow

Base class for the activity windows that give the date range a rec definition's activity-based  reconciliations cover. Polymorphic by windowType; each supported type has a corresponding inherited class.

## oneOf Type

`RecActivityWindow` can be one of the following types:

* [ContiguousActivityWindow](./ContiguousActivityWindow.md)
* [FixedPeriodLookbackActivityWindow](./FixedPeriodLookbackActivityWindow.md)

## Usage

### Creating from a compatible type

```python
from finbourne.sdk.services.lusid.models.RecActivityWindow import RecActivityWindow

# Construct using any of the compatible types above
contiguous_activity_window_instance = lusid.models.contiguous_activity_window.ContiguousActivityWindow(
                        initial_activity_since_effective_at = lusid.models.rec_activity_since_effective_at.RecActivitySinceEffectiveAt(
                            left = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            right = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                        window_type = '', )

instance = RecActivityWindow(contiguous_activity_window_instance)
```

## Related Models

- [ContiguousActivityWindow](./ContiguousActivityWindow.md)
- [FixedPeriodLookbackActivityWindow](./FixedPeriodLookbackActivityWindow.md)

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

