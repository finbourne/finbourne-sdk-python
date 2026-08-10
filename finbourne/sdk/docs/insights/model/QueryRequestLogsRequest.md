# QueryRequestLogsRequest

Body of the QueryRequestLogs endpoint. A query is bounded by a time range (Finbourne.Insights.WebApi.Dtos.QueryRequestLogsRequest.StartAt/Finbourne.Insights.WebApi.Dtos.QueryRequestLogsRequest.EndAt) and refined by an optional set of Finbourne.Insights.WebApi.Dtos.QueryRequestLogsRequest.Filters that are combined with logical AND. The discoverable set of filterable fields, their data types and the operations available for each is returned by the queryable-fields metadata endpoint.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **start_at** | **datetime** | Optional | The inclusive start of the time range to query. Required unless Finbourne.Insights.WebApi.Dtos.QueryRequestLogsRequest.Page is supplied. Used to bound the underlying partition scan, so a tighter range is cheaper and faster. |
| **end_at** | **datetime** | Optional | The end of the time range to query. Required unless Finbourne.Insights.WebApi.Dtos.QueryRequestLogsRequest.Page or Finbourne.Insights.WebApi.Dtos.QueryRequestLogsRequest.TimeRange is supplied. |
| **time_range** | [../model/TimeRange](TimeRange.md) | Optional | *No description available.* |
| **filters** | [../model/List[InsightsFilter]](InsightsFilter.md) | Optional | Optional filters to apply, combined with logical AND. Each filter targets a filterable field and supplies exactly one comparator matching that field&#39;s data type. |
| **sort_by** | **str** | Optional | Order the results by these fields. Use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName. Multiple fields can be denoted by a comma e.g. -MyFieldName,AnotherFieldName,-AFurtherFieldName. |
| **max_results** | **int** | Optional | The maximum total number of records to capture in the result set; applied as the Luminesce query limit and so bounding the work the query performs. The minimum value is 1 and the maximum is 10000; defaults to 500 when not supplied. The per-page limit then controls how many of these captured records are returned per page. |
| **limit** | **int** | Optional | When paginating, only return this number of records per page. The minimum value is 0 (return all captured records in a single page) and the maximum is 10000. |
| **page** | **str** | Optional | Encoded page string returned from a previous search result that will retrieve the next page of data. When this field is supplied, the query-defining fields should not be supplied. |
| **fields** | **List[str]** | Optional | Optional list of additional field names to include in the response. The fields Timestamp, Id, Application and Operation are always returned. Values are matched case-insensitively against the queryable fields of the request logs. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.insights.models.QueryRequestLogsRequest import QueryRequestLogsRequest

instance = QueryRequestLogsRequest(
    start_at=datetime.now(),  # optional — The inclusive start of the time range to query. Required unless Finbourne.Insights.WebApi.Dtos.QueryRequestLogsRequest.Page is supplied. Used to bound the underlying partition scan, so a tighter range is cheaper and faster.
    end_at=datetime.now(),  # optional — The end of the time range to query. Required unless Finbourne.Insights.WebApi.Dtos.QueryRequestLogsRequest.Page or Finbourne.Insights.WebApi.Dtos.QueryRequestLogsRequest.TimeRange is supplied.
    time_range=TimeRange(...),  # optional
    filters=[],  # optional — Optional filters to apply, combined with logical AND. Each filter targets a filterable field and supplies exactly one comparator matching that field&#39;s data type.
    sort_by="...",  # optional — Order the results by these fields. Use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName. Multiple fields can be denoted by a comma e.g. -MyFieldName,AnotherFieldName,-AFurtherFieldName.
    max_results=0,  # optional — The maximum total number of records to capture in the result set; applied as the Luminesce query limit and so bounding the work the query performs. The minimum value is 1 and the maximum is 10000; defaults to 500 when not supplied. The per-page limit then controls how many of these captured records are returned per page.
    limit=0,  # optional — When paginating, only return this number of records per page. The minimum value is 0 (return all captured records in a single page) and the maximum is 10000.
    page="...",  # optional — Encoded page string returned from a previous search result that will retrieve the next page of data. When this field is supplied, the query-defining fields should not be supplied.
    fields=  # optional — Optional list of additional field names to include in the response. The fields Timestamp, Id, Application and Operation are always returned. Values are matched case-insensitively against the queryable fields of the request logs.
)
```

- [TimeRange](TimeRange.md)
- [InsightsFilter](InsightsFilter.md) — used in `filters`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

