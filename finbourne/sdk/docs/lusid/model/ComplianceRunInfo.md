# ComplianceRunInfo

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **run_id** | **str** | Required | The unique identifier of a compliance run |
| **instigated_at** | **datetime** | Required | The time the compliance run was launched (e.g. button pressed). Currently it is also both the as at and effective at time in whichthe rule set and portfolio data (including any pending trades if the run is pretrade) is taken for the caluation, although it may be possible to run compliance for historical effective at and as at dates in the future. |
| **completed_at** | **datetime** | Required | The time the compliance run calculation was completed |
| **schedule** | **str** | Required | Whether the compliance run was pre or post trade |
| **all_rules_passed** | **bool** | Required | True if all rules passed, for all the portfolios they were assigned to |
| **has_results** | **bool** | Required | False when no results have been returned eg. when no rules exist |
| **as_at** | **datetime** | Required | Legacy AsAt time for backwards compatibility |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ComplianceRunInfo import ComplianceRunInfo

instance = ComplianceRunInfo(
    run_id="...",  # required — The unique identifier of a compliance run
    instigated_at=datetime.now(),  # required — The time the compliance run was launched (e.g. button pressed). Currently it is also both the as at and effective at time in whichthe rule set and portfolio data (including any pending trades if the run is pretrade) is taken for the caluation, although it may be possible to run compliance for historical effective at and as at dates in the future.
    completed_at=datetime.now(),  # required — The time the compliance run calculation was completed
    schedule="...",  # required — Whether the compliance run was pre or post trade
    all_rules_passed=True,  # required — True if all rules passed, for all the portfolios they were assigned to
    has_results=True,  # required — False when no results have been returned eg. when no rules exist
    as_at=datetime.now()  # required — Legacy AsAt time for backwards compatibility
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

