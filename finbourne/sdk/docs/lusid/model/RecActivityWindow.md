# RecActivityWindow

Base class for the activity windows that give the date range a rec definition's activity-based  reconciliations cover. Polymorphic by windowType; each supported type has a corresponding inherited class.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **window_type** | **str** | Required | Polymorphic discriminator. Supported types: Contiguous. Contiguous requires effectiveAtProgression Series. Available values: Contiguous, FixedLookback, Explicit, ClosedPeriod, ContiguousAsAt. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RecActivityWindow import RecActivityWindow

instance = RecActivityWindow(
    window_type="..."  # required — Polymorphic discriminator. Supported types: Contiguous. Contiguous requires effectiveAtProgression Series. Available values: Contiguous, FixedLookback, Explicit, ClosedPeriod, ContiguousAsAt.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

