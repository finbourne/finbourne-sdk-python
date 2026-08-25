# IdentityMetricsDataSet

Identity population and activity counts for the domain, pivoted from the latest tranche the identity metrics provider collected.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **name** | **str** | Required | The name of this data set. Always &#x60;IdentityMetrics&#x60;, matching the corresponding Finbourne.Insights.WebApi.Dtos.Metrics.MetricDataSet value and Finbourne.Insights.WebApi.Dtos.Metrics.MetricsResponse property. |
| **collected_at** | **datetime** | Optional | The timestamp of the tranche these values were collected in, in UTC, or null if no tranche was returned. |
| **personal_users** | **int** | Optional | The number of personal (human) users in the domain, or null if not reported. |
| **service_users** | **int** | Optional | The number of service users in the domain, or null if not reported. |
| **never_logged_in** | **int** | Optional | The number of users that have never logged in, or null if not reported. |
| **ignored** | **int** | Optional | The number of users excluded from the other counts, or null if not reported. |
| **account_locked** | **int** | Optional | The number of users whose account is locked, or null if not reported. |
| **suspended_pw_reset** | **int** | Optional | The number of users suspended pending a password reset, or null if not reported. |
| **created_last24_hours** | **int** | Optional | The number of users created in the last 24 hours, or null if not reported. |
| **created_last7_days** | **int** | Optional | The number of users created in the last 7 days, or null if not reported. |
| **created_last30_days** | **int** | Optional | The number of users created in the last 30 days, or null if not reported. |
| **active_last24_hours** | **int** | Optional | The number of users active in the last 24 hours, or null if not reported. |
| **active_last7_days** | **int** | Optional | The number of users active in the last 7 days, or null if not reported. |
| **active_last30_days** | **int** | Optional | The number of users active in the last 30 days, or null if not reported. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.insights.models.IdentityMetricsDataSet import IdentityMetricsDataSet

instance = IdentityMetricsDataSet(
    name="...",  # required — The name of this data set. Always &#x60;IdentityMetrics&#x60;, matching the corresponding Finbourne.Insights.WebApi.Dtos.Metrics.MetricDataSet value and Finbourne.Insights.WebApi.Dtos.Metrics.MetricsResponse property.
    collected_at=datetime.now(),  # optional — The timestamp of the tranche these values were collected in, in UTC, or null if no tranche was returned.
    personal_users=0,  # optional — The number of personal (human) users in the domain, or null if not reported.
    service_users=0,  # optional — The number of service users in the domain, or null if not reported.
    never_logged_in=0,  # optional — The number of users that have never logged in, or null if not reported.
    ignored=0,  # optional — The number of users excluded from the other counts, or null if not reported.
    account_locked=0,  # optional — The number of users whose account is locked, or null if not reported.
    suspended_pw_reset=0,  # optional — The number of users suspended pending a password reset, or null if not reported.
    created_last24_hours=0,  # optional — The number of users created in the last 24 hours, or null if not reported.
    created_last7_days=0,  # optional — The number of users created in the last 7 days, or null if not reported.
    created_last30_days=0,  # optional — The number of users created in the last 30 days, or null if not reported.
    active_last24_hours=0,  # optional — The number of users active in the last 24 hours, or null if not reported.
    active_last7_days=0,  # optional — The number of users active in the last 7 days, or null if not reported.
    active_last30_days=0  # optional — The number of users active in the last 30 days, or null if not reported.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

