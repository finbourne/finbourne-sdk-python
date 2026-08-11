# BackgroundMultiQueryResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **execution_id** | **UUID** | Optional | *No description available.* *(read-only)* |
| **progress** | [Link](Link.md) | Optional | *No description available.* |
| **cancel** | [Link](Link.md) | Optional | *No description available.* |
| **fetch_json** | [List[Link]](Link.md) | Optional | Json (as a string) data request links for all of the child queries *(read-only)* |
| **fetch_json_proper** | [List[Link]](Link.md) | Optional | Json-proper data request links for all of the child queries *(read-only)* |
| **fetch_json_proper_with_lineage** | [List[Link]](Link.md) | Optional | Json-proper-with-lineage data request links for all of the child queries *(read-only)* |
| **fetch_xml** | [List[Link]](Link.md) | Optional | Xml data request links for all of the child queries *(read-only)* |
| **fetch_parquet** | [List[Link]](Link.md) | Optional | Parquet data request links for all of the child queries *(read-only)* |
| **fetch_csv** | [List[Link]](Link.md) | Optional | CSV data request links for all of the child queries *(read-only)* |
| **fetch_pipe** | [List[Link]](Link.md) | Optional | Pipe delimited data request links for all of the child queries *(read-only)* |
| **fetch_excel** | [List[Link]](Link.md) | Optional | Excel workbook data request links for all of the child queries *(read-only)* |
| **fetch_sqlite** | [List[Link]](Link.md) | Optional | SqLite DB data request links for all of the child queries *(read-only)* |
| **histogram** | [List[Link]](Link.md) | Optional | Histogram links for all of the child queries *(read-only)* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.luminesce.models.BackgroundMultiQueryResponse import BackgroundMultiQueryResponse

instance = BackgroundMultiQueryResponse(
    execution_id="...",  # optional
    progress=Link(...),  # optional
    cancel=Link(...),  # optional
    fetch_json=[],  # optional — Json (as a string) data request links for all of the child queries
    fetch_json_proper=[],  # optional — Json-proper data request links for all of the child queries
    fetch_json_proper_with_lineage=[],  # optional — Json-proper-with-lineage data request links for all of the child queries
    fetch_xml=[],  # optional — Xml data request links for all of the child queries
    fetch_parquet=[],  # optional — Parquet data request links for all of the child queries
    fetch_csv=[],  # optional — CSV data request links for all of the child queries
    fetch_pipe=[],  # optional — Pipe delimited data request links for all of the child queries
    fetch_excel=[],  # optional — Excel workbook data request links for all of the child queries
    fetch_sqlite=[],  # optional — SqLite DB data request links for all of the child queries
    histogram=[]  # optional — Histogram links for all of the child queries
)
```

- [Link](Link.md)
- [Link](Link.md)
- [Link](Link.md) — used in `fetch_json`
- [Link](Link.md) — used in `fetch_json_proper`
- [Link](Link.md) — used in `fetch_json_proper_with_lineage`
- [Link](Link.md) — used in `fetch_xml`
- [Link](Link.md) — used in `fetch_parquet`
- [Link](Link.md) — used in `fetch_csv`
- [Link](Link.md) — used in `fetch_pipe`
- [Link](Link.md) — used in `fetch_excel`
- [Link](Link.md) — used in `fetch_sqlite`
- [Link](Link.md) — used in `histogram`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

