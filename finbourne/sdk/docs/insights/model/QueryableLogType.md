# QueryableLogType

The queryable fields of a single log type, returned by the queryable-fields metadata endpoint.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **log_type** | **str** | Required | The log type, e.g. Requests, Vendor, Access, Trace or TraceEvent. |
| **fields** | [List[QueryableLogField]](QueryableLogField.md) | Required | The fields of this log type that can be selected and/or filtered. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.insights.models.QueryableLogType import QueryableLogType

instance = QueryableLogType(
    log_type="...",  # required — The log type, e.g. Requests, Vendor, Access, Trace or TraceEvent.
    fields=[]  # required — The fields of this log type that can be selected and/or filtered.
)
```

- [QueryableLogField](QueryableLogField.md) — used in `fields`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

