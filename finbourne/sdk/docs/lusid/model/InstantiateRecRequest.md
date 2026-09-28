# InstantiateRecRequest

The request to instantiate a new rec instance from a rec definition and start its first run. Each  date accepts a date-time or a LUSID cut label, and defaults to the current date-time when omitted.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **rec_definition_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **left_effective_at** | **str** | Optional | The left effective datetime, as a date-time or a LUSID cut label. Defaults to the current date-time. When the definition&#39;s datePolicy.effectiveAtProgression is Series, must be strictly after the previous instance&#39;s leftEffectiveAt. |
| **left_as_at** | **str** | Optional | The left asAt datetime, as a date-time or a LUSID cut label. Must be omitted when the definition&#39;s datePolicy.asAtPolicy.left is Latest, as the system reconciles at the latest knowledge on every run. When it is Explicit, defaults to the current date-time and is pinned on the instance. |
| **right_effective_at** | **str** | Optional | The right effective datetime, as a date-time or a LUSID cut label. Defaults to the current date-time. When the definition&#39;s datePolicy.effectiveAtProgression is Series, must be strictly after the previous instance&#39;s rightEffectiveAt. |
| **right_as_at** | **str** | Optional | The right asAt datetime, as a date-time or a LUSID cut label. Must be omitted when the definition&#39;s datePolicy.asAtPolicy.right is Latest, as the system reconciles at the latest knowledge on every run. When it is Explicit, defaults to the current date-time and is pinned on the instance. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.InstantiateRecRequest import InstantiateRecRequest

instance = InstantiateRecRequest(
    rec_definition_id=ResourceId(...),  # required
    left_effective_at="...",  # optional — The left effective datetime, as a date-time or a LUSID cut label. Defaults to the current date-time. When the definition&#39;s datePolicy.effectiveAtProgression is Series, must be strictly after the previous instance&#39;s leftEffectiveAt.
    left_as_at="...",  # optional — The left asAt datetime, as a date-time or a LUSID cut label. Must be omitted when the definition&#39;s datePolicy.asAtPolicy.left is Latest, as the system reconciles at the latest knowledge on every run. When it is Explicit, defaults to the current date-time and is pinned on the instance.
    right_effective_at="...",  # optional — The right effective datetime, as a date-time or a LUSID cut label. Defaults to the current date-time. When the definition&#39;s datePolicy.effectiveAtProgression is Series, must be strictly after the previous instance&#39;s rightEffectiveAt.
    right_as_at="..."  # optional — The right asAt datetime, as a date-time or a LUSID cut label. Must be omitted when the definition&#39;s datePolicy.asAtPolicy.right is Latest, as the system reconciles at the latest knowledge on every run. When it is Explicit, defaults to the current date-time and is pinned on the instance.
)
```


## Related Models

- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

