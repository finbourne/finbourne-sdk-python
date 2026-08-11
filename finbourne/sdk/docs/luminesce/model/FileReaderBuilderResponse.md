# FileReaderBuilderResponse

Information on how to construct a file-read sql query
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **query** | **str** | Optional | The generated SQL |
| **error** | **str** | Optional | The error from running generated SQL Query, if any |
| **columns** | [List[ColumnInfo]](ColumnInfo.md) | Optional | Column information for the results |
| **data** | **object** | Optional | The resulting data from running the Query |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.luminesce.models.FileReaderBuilderResponse import FileReaderBuilderResponse

instance = FileReaderBuilderResponse(
    query="...",  # optional — The generated SQL
    error="...",  # optional — The error from running generated SQL Query, if any
    columns=[],  # optional — Column information for the results
    data=  # optional — The resulting data from running the Query
)
```

- [ColumnInfo](ColumnInfo.md) — used in `columns`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

