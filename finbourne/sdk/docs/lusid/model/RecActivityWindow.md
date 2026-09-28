# RecActivityWindow

Base class for the activity windows that give the date range a rec definition's activity-based  reconciliations cover. Polymorphic by windowType; each supported type has a corresponding inherited class.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **initial_activity_since_effective_at** | [RecActivitySinceEffectiveAt](RecActivitySinceEffectiveAt.md) | Required | *No description available.* |
| **window_type** | **str** | Required | Polymorphic discriminator. Supported types: Contiguous. Contiguous requires effectiveAtProgression Series. Available values: Contiguous, FixedLookback, Explicit, ClosedPeriod, ContiguousAsAt. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RecActivityWindow import RecActivityWindow

instance = RecActivityWindow(
    initial_activity_since_effective_at=RecActivitySinceEffectiveAt(...),  # required
    window_type="..."  # required — Polymorphic discriminator. Supported types: Contiguous. Contiguous requires effectiveAtProgression Series. Available values: Contiguous, FixedLookback, Explicit, ClosedPeriod, ContiguousAsAt.
)
```


## Related Models

- [RecActivitySinceEffectiveAt](RecActivitySinceEffectiveAt.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

