# AlertRule

An alert rule on an integration instance. Finbourne.Horizon.Integrations.Web.Dto.AlertRule.Type selects the rule and decides which of the optional fields apply. A field that does not belong to the selected type is rejected.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **type** | **str** | Required | The rule type (Allowed: MustStartBy, MaxDuration, FailedAfterRetries) |
| **severity** | **str** | Optional | The severity alerts from this rule are raised at (Allowed: Critical, High, Medium, Low, Informational). Critical pages on-call for a client-facing outage. High needs action today. Medium is a missed or late run. Low is an overrun or record-count check. Informational never pages. Defaults per type when omitted: MustStartBy and FailedAfterRetries Medium, MaxDuration Low. |
| **time_of_day** | **str** | Optional | MustStartBy only. The local time of day, as HH:mm, by which a run must have started. |
| **time_zone** | **str** | Optional | MustStartBy only. The IANA or Windows time zone id that TimeOfDay is expressed in. |
| **days_of_week** | **List[str]** | Optional | MustStartBy only. The days the rule applies on, by name (e.g. Monday). Every day when omitted. |
| **grace_minutes** | **int** | Optional | MustStartBy only. Minutes after TimeOfDay before a missing run counts as a breach. 0 when omitted. |
| **max_minutes** | **int** | Optional | MaxDuration only. Alert once a run has been running for longer than this many minutes. Minimum 10. |
| **include_paused** | **bool** | Optional | MaxDuration only. Also measure paused runs. False when omitted. |
| **alert_on_first_failure** | **bool** | Optional | FailedAfterRetries only. Also alert on the first failure of a retry chain, not only when the retries are exhausted. False when omitted. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.AlertRule import AlertRule

instance = AlertRule(
    type="...",  # required — The rule type (Allowed: MustStartBy, MaxDuration, FailedAfterRetries)
    severity="...",  # optional — The severity alerts from this rule are raised at (Allowed: Critical, High, Medium, Low, Informational). Critical pages on-call for a client-facing outage. High needs action today. Medium is a missed or late run. Low is an overrun or record-count check. Informational never pages. Defaults per type when omitted: MustStartBy and FailedAfterRetries Medium, MaxDuration Low.
    time_of_day="...",  # optional — MustStartBy only. The local time of day, as HH:mm, by which a run must have started.
    time_zone="...",  # optional — MustStartBy only. The IANA or Windows time zone id that TimeOfDay is expressed in.
    days_of_week=,  # optional — MustStartBy only. The days the rule applies on, by name (e.g. Monday). Every day when omitted.
    grace_minutes=0,  # optional — MustStartBy only. Minutes after TimeOfDay before a missing run counts as a breach. 0 when omitted.
    max_minutes=0,  # optional — MaxDuration only. Alert once a run has been running for longer than this many minutes. Minimum 10.
    include_paused=True,  # optional — MaxDuration only. Also measure paused runs. False when omitted.
    alert_on_first_failure=True  # optional — FailedAfterRetries only. Also alert on the first failure of a retry chain, not only when the retries are exhausted. False when omitted.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

