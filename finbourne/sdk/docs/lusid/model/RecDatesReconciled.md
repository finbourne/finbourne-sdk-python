# RecDatesReconciled

The left and right effective and asAt dates of the data reconciled in a run.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **left_effective_at** | **datetime** | Required | The effective datetime of the data reconciled on the left side. |
| **left_as_at** | **datetime** | Required | The asAt datetime of the data reconciled on the left side. |
| **right_effective_at** | **datetime** | Required | The effective datetime of the data reconciled on the right side. |
| **right_as_at** | **datetime** | Required | The asAt datetime of the data reconciled on the right side. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RecDatesReconciled import RecDatesReconciled

instance = RecDatesReconciled(
    left_effective_at=datetime.now(),  # required — The effective datetime of the data reconciled on the left side.
    left_as_at=datetime.now(),  # required — The asAt datetime of the data reconciled on the left side.
    right_effective_at=datetime.now(),  # required — The effective datetime of the data reconciled on the right side.
    right_as_at=datetime.now()  # required — The asAt datetime of the data reconciled on the right side.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

