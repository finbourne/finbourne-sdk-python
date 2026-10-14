# CustomMultiQueryRequest

A caller-supplied set of queries to run in the background, as one multi-query.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **execution_id** | **str** | Optional | An explicit ExecutionId to use.  This must be blank OR assigned to a valid GUID-as-a-string. |
| **scalar_parameters** | **Dict[str, Optional[str]]** | Optional | Scalar parameter values, handed to every query that runs (e.g. filling in &#x60;:someParameter:defaultValue&#x60; style references). At most 100, each named as an identifier of at most 256 characters, with a value of at most 4096. |
| **queries** | [List[CustomMultiQueryItem]](CustomMultiQueryItem.md) | Required | The queries to run.  Those ready are started in the order given here (one still waiting on those it refers to does not hold up a later one), and each may only refer to queries earlier in the list. |
| **max_in_parallel** | **int** | Optional | Maximum number of the queries that may run concurrently.  Defaults to 1, meaning they run one after another. Explicitly null means as many as their dependencies allow. |
| **timeout_seconds** | **int** | Optional | Maximum time each query may run for, in seconds, timed from when it starts: &lt;0 → ∞, 0 → 1200s (20m). There is no limit on the set as a whole. |
| **keep_for_seconds** | **int** | Optional | Maximum time the results may be kept for, in seconds: &lt;0 → 1200 (20m), 0 → 28800 (8h), max &#x3D; 2,678,400 (31d) |
| **query_name** | **str** | Optional | A name for this set of queries.  This goes into logs and is returned when listing the sets of queries. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.luminesce.models.CustomMultiQueryRequest import CustomMultiQueryRequest

instance = CustomMultiQueryRequest(
    execution_id="...",  # optional — An explicit ExecutionId to use.  This must be blank OR assigned to a valid GUID-as-a-string.
    scalar_parameters=,  # optional — Scalar parameter values, handed to every query that runs (e.g. filling in &#x60;:someParameter:defaultValue&#x60; style references). At most 100, each named as an identifier of at most 256 characters, with a value of at most 4096.
    queries=[],  # required — The queries to run.  Those ready are started in the order given here (one still waiting on those it refers to does not hold up a later one), and each may only refer to queries earlier in the list.
    max_in_parallel=0,  # optional — Maximum number of the queries that may run concurrently.  Defaults to 1, meaning they run one after another. Explicitly null means as many as their dependencies allow.
    timeout_seconds=0,  # optional — Maximum time each query may run for, in seconds, timed from when it starts: &lt;0 → ∞, 0 → 1200s (20m). There is no limit on the set as a whole.
    keep_for_seconds=0,  # optional — Maximum time the results may be kept for, in seconds: &lt;0 → 1200 (20m), 0 → 28800 (8h), max &#x3D; 2,678,400 (31d)
    query_name="..."  # optional — A name for this set of queries.  This goes into logs and is returned when listing the sets of queries.
)
```

- [CustomMultiQueryItem](CustomMultiQueryItem.md) — used in `queries`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

