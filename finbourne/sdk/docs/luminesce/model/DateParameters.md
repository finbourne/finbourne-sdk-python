# DateParameters

Collection of date parameters used in dashboards
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **date_from** | **datetime** | Optional | Parameter to determine the lower bound in a date range |
| **date_to** | **datetime** | Optional | Parameter to determine the upper bound in a date range |
| **effective_at** | **datetime** | Optional | EffectiveAt of the dashboard |
| **effective_from** | **datetime** | Optional | EffectiveFrom of the dashboard |
| **as_at** | **datetime** | Required | AsAt of the dashboard |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.luminesce.models.DateParameters import DateParameters

instance = DateParameters(
    date_from=datetime.now(),  # optional — Parameter to determine the lower bound in a date range
    date_to=datetime.now(),  # optional — Parameter to determine the upper bound in a date range
    effective_at=datetime.now(),  # optional — EffectiveAt of the dashboard
    effective_from=datetime.now(),  # optional — EffectiveFrom of the dashboard
    as_at=datetime.now()  # required — AsAt of the dashboard
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

