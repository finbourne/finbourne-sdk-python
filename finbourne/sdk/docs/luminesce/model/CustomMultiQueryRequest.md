# CustomMultiQueryRequest

A caller-supplied set of queries to run in the background, as one multi-query.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **execution_id** | **str** | Optional | An explicit ExecutionId to use.  This must be blank OR assigned to a valid GUID-as-a-string. |
| **scalar_parameters** | **Dict[str, Optional[str]]** | Optional | Scalar parameter values, handed to every query that runs (e.g. filling in &#x60;:someParameter:defaultValue&#x60; style references). At most 100, each named as an identifier of at most 256 characters, with a value of at most 4096. |
| **queries** | [List[CustomMultiQueryItem]](CustomMultiQueryItem.md) | Required | The queries to run.  Those ready are started in the order given here (one still waiting on those it refers to does not hold up a later one), and each may only refer to queries earlier in the list. |
| **queries_from_workspace** | **str** | Optional | A custom multi-query saved in the Workspaces API to take the queries from, rather than giving them in &#x60;Queries&#x60; (exactly one of which must be given), e.g. &#x60;shared/SomeWorkspace/items/sets/SomeSet&#x60;. What this request leaves unspecified of &#x60;maxInParallel&#x60;, &#x60;timeoutSeconds&#x60;, &#x60;keepForSeconds&#x60; and &#x60;queryName&#x60; is taken from it too, and its saved scalar parameter values are used for any this request does not give. It may instead be a Saved Query, e.g. &#x60;shared/SomeWorkspace/items/queries/SomeQuery&#x60;, run as the one query, named &#x60;Result&#x60;. |
| **max_in_parallel** | **int** | Optional | Maximum number of the queries that may run concurrently.  Defaults to 1, meaning they run one after another. Explicitly null means as many as their dependencies allow. |
| **timeout_seconds** | **int** | Optional | Maximum time each query may run for, in seconds, timed from when it starts: &lt;0 → ∞, 0 or null → 1200s (20m). There is no limit on the set as a whole.  Null (or absent) with &#x60;queriesFromWorkspace&#x60; is that saved with it. |
| **keep_for_seconds** | **int** | Optional | Maximum time the results may be kept for, in seconds: &lt;0 → 1200 (20m), 0 or null → 28800 (8h), max &#x3D; 2,678,400 (31d). Null (or absent) with &#x60;queriesFromWorkspace&#x60; is that saved with it. |
| **execution_flags** | [SqlExecutionFlags](SqlExecutionFlags.md) | Optional | *No description available.* |
| **query_name** | **str** | Optional | A name for this set of queries.  This goes into logs and is returned when listing the sets of queries. |
| **export** | [CustomMultiQueryExport](CustomMultiQueryExport.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.luminesce.models.CustomMultiQueryRequest import CustomMultiQueryRequest

instance = CustomMultiQueryRequest(
    execution_id="...",  # optional — An explicit ExecutionId to use.  This must be blank OR assigned to a valid GUID-as-a-string.
    scalar_parameters=,  # optional — Scalar parameter values, handed to every query that runs (e.g. filling in &#x60;:someParameter:defaultValue&#x60; style references). At most 100, each named as an identifier of at most 256 characters, with a value of at most 4096.
    queries=[],  # required — The queries to run.  Those ready are started in the order given here (one still waiting on those it refers to does not hold up a later one), and each may only refer to queries earlier in the list.
    queries_from_workspace="...",  # optional — A custom multi-query saved in the Workspaces API to take the queries from, rather than giving them in &#x60;Queries&#x60; (exactly one of which must be given), e.g. &#x60;shared/SomeWorkspace/items/sets/SomeSet&#x60;. What this request leaves unspecified of &#x60;maxInParallel&#x60;, &#x60;timeoutSeconds&#x60;, &#x60;keepForSeconds&#x60; and &#x60;queryName&#x60; is taken from it too, and its saved scalar parameter values are used for any this request does not give. It may instead be a Saved Query, e.g. &#x60;shared/SomeWorkspace/items/queries/SomeQuery&#x60;, run as the one query, named &#x60;Result&#x60;.
    max_in_parallel=0,  # optional — Maximum number of the queries that may run concurrently.  Defaults to 1, meaning they run one after another. Explicitly null means as many as their dependencies allow.
    timeout_seconds=0,  # optional — Maximum time each query may run for, in seconds, timed from when it starts: &lt;0 → ∞, 0 or null → 1200s (20m). There is no limit on the set as a whole.  Null (or absent) with &#x60;queriesFromWorkspace&#x60; is that saved with it.
    keep_for_seconds=0,  # optional — Maximum time the results may be kept for, in seconds: &lt;0 → 1200 (20m), 0 or null → 28800 (8h), max &#x3D; 2,678,400 (31d). Null (or absent) with &#x60;queriesFromWorkspace&#x60; is that saved with it.
    execution_flags=SqlExecutionFlags(...),  # optional
    query_name="...",  # optional — A name for this set of queries.  This goes into logs and is returned when listing the sets of queries.
    export=CustomMultiQueryExport(...)  # optional
)
```

- [CustomMultiQueryItem](CustomMultiQueryItem.md) — used in `queries`
- [SqlExecutionFlags](SqlExecutionFlags.md)
- [CustomMultiQueryExport](CustomMultiQueryExport.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

