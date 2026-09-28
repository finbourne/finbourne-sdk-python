# RecDatesReconciled

The left and right effective and asAt dates of the data reconciled in a run, plus the exclusive lower bound of each side's activity window on activity-based rec types.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **left_effective_at** | **datetime** | Required | The effective datetime of the data reconciled on the left side. |
| **left_as_at** | **datetime** | Required | The asAt datetime of the data reconciled on the left side. |
| **right_effective_at** | **datetime** | Required | The effective datetime of the data reconciled on the right side. |
| **right_as_at** | **datetime** | Required | The asAt datetime of the data reconciled on the right side. |
| **left_activity_since_effective_at** | **datetime** | Optional | The exclusive lower bound of the left side&#39;s activity window, so the window is (leftActivitySinceEffectiveAt, leftEffectiveAt]. Populated only on activity-based rec types; null on point-in-time rec types and when the definition has no activity window. |
| **right_activity_since_effective_at** | **datetime** | Optional | The exclusive lower bound of the right side&#39;s activity window, so the window is (rightActivitySinceEffectiveAt, rightEffectiveAt]. Populated only on activity-based rec types; null on point-in-time rec types and when the definition has no activity window. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RecDatesReconciled import RecDatesReconciled

instance = RecDatesReconciled(
    left_effective_at=datetime.now(),  # required — The effective datetime of the data reconciled on the left side.
    left_as_at=datetime.now(),  # required — The asAt datetime of the data reconciled on the left side.
    right_effective_at=datetime.now(),  # required — The effective datetime of the data reconciled on the right side.
    right_as_at=datetime.now(),  # required — The asAt datetime of the data reconciled on the right side.
    left_activity_since_effective_at=datetime.now(),  # optional — The exclusive lower bound of the left side&#39;s activity window, so the window is (leftActivitySinceEffectiveAt, leftEffectiveAt]. Populated only on activity-based rec types; null on point-in-time rec types and when the definition has no activity window.
    right_activity_since_effective_at=datetime.now()  # optional — The exclusive lower bound of the right side&#39;s activity window, so the window is (rightActivitySinceEffectiveAt, rightEffectiveAt]. Populated only on activity-based rec types; null on point-in-time rec types and when the definition has no activity window.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

