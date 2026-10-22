# MarginRun

A margin run: the valuation of the collateral agreements for a business date, planned as shards that report  their progress, and the margin calls and lines it has published so far.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The URI of this margin run. |
| **id** | **str** | Required | The identifier of the run: the effective date and the asAt it was valued at. Filterable. |
| **effective_at** | **datetime** | Required | The business date the run values collateral agreements for. Filterable. |
| **as_at** | **datetime** | Required | The asAt datetime the run reads agreements, portfolios and market data at. Filterable. |
| **status** | **str** | Required | The status of the run. One of Pending, Running, Completed or CompletedWithIssues. Filterable. |
| **agreements** | [List[ResourceId]](ResourceId.md) | Required | The collateral agreements the run covers. |
| **call_count** | **int** | Required | The number of margin calls the run has published so far. |
| **line_count** | **int** | Required | The number of margin lines the run has published so far. |
| **shard_count** | **int** | Required | The number of valuation shards the run was planned as. |
| **completed_shards** | **int** | Required | The number of shards that have completed. |
| **failed_shards** | **int** | Required | The number of shards that failed to value. |
| **issues** | [List[MarginRunIssue]](MarginRunIssue.md) | Required | Agreements the run could not value or roll up into a call, or the caller may not calculate margin for, with the reason. |
| **shards** | [List[MarginRunShard]](MarginRunShard.md) | Required | The valuation shards the run is planned as, with their progress. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.MarginRun import MarginRun

instance = MarginRun(
    href="...",  # optional — The URI of this margin run.
    id="...",  # required — The identifier of the run: the effective date and the asAt it was valued at. Filterable.
    effective_at=datetime.now(),  # required — The business date the run values collateral agreements for. Filterable.
    as_at=datetime.now(),  # required — The asAt datetime the run reads agreements, portfolios and market data at. Filterable.
    status="...",  # required — The status of the run. One of Pending, Running, Completed or CompletedWithIssues. Filterable.
    agreements=[],  # required — The collateral agreements the run covers.
    call_count=0,  # required — The number of margin calls the run has published so far.
    line_count=0,  # required — The number of margin lines the run has published so far.
    shard_count=0,  # required — The number of valuation shards the run was planned as.
    completed_shards=0,  # required — The number of shards that have completed.
    failed_shards=0,  # required — The number of shards that failed to value.
    issues=[],  # required — Agreements the run could not value or roll up into a call, or the caller may not calculate margin for, with the reason.
    shards=[]  # required — The valuation shards the run is planned as, with their progress.
)
```

- [ResourceId](ResourceId.md) — used in `agreements`
- [MarginRunIssue](MarginRunIssue.md) — used in `issues`
- [MarginRunShard](MarginRunShard.md) — used in `shards`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

