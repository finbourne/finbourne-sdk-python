# ContiguousActivityWindow

The activity window for a running series of instances: each instance's window starts where the previous  instance's ended, so the series tiles the effective timeline with no gaps and no overlap. Requires the  definition's effectiveAtProgression to be Series.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **initial_activity_since_effective_at** | [RecActivitySinceEffectiveAt](RecActivitySinceEffectiveAt.md) | Required | *No description available.* |
| **window_type** | **str** | Required | Polymorphic discriminator. Supported types: Contiguous. Contiguous requires effectiveAtProgression Series. Available values: Contiguous, FixedLookback, Explicit, ClosedPeriod, ContiguousAsAt. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ContiguousActivityWindow import ContiguousActivityWindow

instance = ContiguousActivityWindow(
    initial_activity_since_effective_at=RecActivitySinceEffectiveAt(...),  # required
    window_type="..."  # required — Polymorphic discriminator. Supported types: Contiguous. Contiguous requires effectiveAtProgression Series. Available values: Contiguous, FixedLookback, Explicit, ClosedPeriod, ContiguousAsAt.
)
```


## Related Models

- [RecActivitySinceEffectiveAt](RecActivitySinceEffectiveAt.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

