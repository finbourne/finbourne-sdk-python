# RecDatePolicy

The date policy of a rec definition: how the effective dates of successive instances may progress, whether each  side reconciles at the latest knowledge or at a pinned asAt, and — for activity-based rec types — how the  activity window is bounded.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **effective_at_progression** | **str** | Optional | How the effective dates of successive instances may progress. Series (the default): each instance&#39;s leftEffectiveAt and rightEffectiveAt must be strictly after the previous instance&#39;s. Unconstrained: no relationship between instances. Immutable once the definition has instances. Available values: Series, Unconstrained. |
| **as_at_policy** | [RecAsAtPolicy](RecAsAtPolicy.md) | Optional | *No description available.* |
| **activity_window** | [RecActivityWindow](RecActivityWindow.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RecDatePolicy import RecDatePolicy

instance = RecDatePolicy(
    effective_at_progression="...",  # optional — How the effective dates of successive instances may progress. Series (the default): each instance&#39;s leftEffectiveAt and rightEffectiveAt must be strictly after the previous instance&#39;s. Unconstrained: no relationship between instances. Immutable once the definition has instances. Available values: Series, Unconstrained.
    as_at_policy=RecAsAtPolicy(...),  # optional
    activity_window=RecActivityWindow(...)  # optional
)
```

- [RecAsAtPolicy](RecAsAtPolicy.md)
- [RecActivityWindow](RecActivityWindow.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

