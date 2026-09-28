# RecActivitySinceEffectiveAt

A per-side exclusive lower bound on an activity window's effective range.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **left** | **datetime** | Required | The exclusive lower bound for the left side. Activity effective at exactly this datetime falls outside the window. |
| **right** | **datetime** | Required | The exclusive lower bound for the right side. Activity effective at exactly this datetime falls outside the window. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RecActivitySinceEffectiveAt import RecActivitySinceEffectiveAt

instance = RecActivitySinceEffectiveAt(
    left=datetime.now(),  # required — The exclusive lower bound for the left side. Activity effective at exactly this datetime falls outside the window.
    right=datetime.now()  # required — The exclusive lower bound for the right side. Activity effective at exactly this datetime falls outside the window.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

