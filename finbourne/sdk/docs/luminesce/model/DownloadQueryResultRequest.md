# DownloadQueryResultRequest

How to download the results of a background query: in what format, which of them, and (so far for csv only) formatted as the grid shows them.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **format** | [ExportType](ExportType.md) | Optional | *No description available.* |
| **sort_by** | **str** | Optional | Order the results by these fields. Use the &#x60;-&#x60; sign to denote descending order, e.g. &#x60;-MyFieldName&#x60;.  Numeric indexes may be used also, e.g. &#x60;2,-3&#x60;. Multiple fields can be denoted by a comma e.g. &#x60;-MyFieldName,AnotherFieldName,-AFurtherFieldName&#x60;. Default is null, the sort order specified in the query itself. |
| **filter** | **str** | Optional | Further limits the fetched results beyond that of the original query. - An ODATA filter per Finbourne.Filtering syntax, e.g. &#x60;SomeField eq &#39;Hello&#39;&#x60; - may be combined with &#x60;sqlFilter&#x60;. |
| **sql_filter** | **str** | Optional | Further limits the fetched results beyond that of the original query. - Raw SQL for filtering, e.g. &#x60;strftime(&#39;%Y-%m&#39;, SomeDateField) &#x3D; &#39;2026-06&#39;&#x60; - may be combined with &#x60;filter&#x60; while supporting additional syntax that cannot. |
| **select** | **str** | Optional | Default is null (meaning return all columns in the original query itself). The values are in terms of the result column name from the original data set and are comma delimited, and may aggregate the data, e.g. &#x60;some_field, count(*) as a, max(x) as b&#x60; (where &#x60;groupBy&#x60; would likely be &#x60;1&#x60;). The columns of &#x60;formatting&#x60; are in terms of the columns selected. |
| **group_by** | **str** | Optional | Groups by the specified fields: a comma delimited list of 1 based numeric indexes into &#x60;select&#x60;, or repeats of its expressions. Default is null (meaning no grouping will be performed on the selected columns). |
| **date_time_format** | **str** | Optional | Format to apply for DateTime data not otherwise formatted, leaving blank gives the Luminesce Exporter default, currently &#x60;yyyy-MM-dd HH:mm:ss.fff&#x60; |
| **load_wait_milliseconds** | **int** | Optional | Optional maximum additional wait period for post execution platform processing. |
| **formatting** | [ExportFormatting](ExportFormatting.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.luminesce.models.DownloadQueryResultRequest import DownloadQueryResultRequest

instance = DownloadQueryResultRequest(
    format=ExportType(...),  # optional
    sort_by="...",  # optional — Order the results by these fields. Use the &#x60;-&#x60; sign to denote descending order, e.g. &#x60;-MyFieldName&#x60;.  Numeric indexes may be used also, e.g. &#x60;2,-3&#x60;. Multiple fields can be denoted by a comma e.g. &#x60;-MyFieldName,AnotherFieldName,-AFurtherFieldName&#x60;. Default is null, the sort order specified in the query itself.
    filter="...",  # optional — Further limits the fetched results beyond that of the original query. - An ODATA filter per Finbourne.Filtering syntax, e.g. &#x60;SomeField eq &#39;Hello&#39;&#x60; - may be combined with &#x60;sqlFilter&#x60;.
    sql_filter="...",  # optional — Further limits the fetched results beyond that of the original query. - Raw SQL for filtering, e.g. &#x60;strftime(&#39;%Y-%m&#39;, SomeDateField) &#x3D; &#39;2026-06&#39;&#x60; - may be combined with &#x60;filter&#x60; while supporting additional syntax that cannot.
    select="...",  # optional — Default is null (meaning return all columns in the original query itself). The values are in terms of the result column name from the original data set and are comma delimited, and may aggregate the data, e.g. &#x60;some_field, count(*) as a, max(x) as b&#x60; (where &#x60;groupBy&#x60; would likely be &#x60;1&#x60;). The columns of &#x60;formatting&#x60; are in terms of the columns selected.
    group_by="...",  # optional — Groups by the specified fields: a comma delimited list of 1 based numeric indexes into &#x60;select&#x60;, or repeats of its expressions. Default is null (meaning no grouping will be performed on the selected columns).
    date_time_format="...",  # optional — Format to apply for DateTime data not otherwise formatted, leaving blank gives the Luminesce Exporter default, currently &#x60;yyyy-MM-dd HH:mm:ss.fff&#x60;
    load_wait_milliseconds=0,  # optional — Optional maximum additional wait period for post execution platform processing.
    formatting=ExportFormatting(...)  # optional
)
```


## Related Models

- [ExportType](ExportType.md)
- [ExportFormatting](ExportFormatting.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

