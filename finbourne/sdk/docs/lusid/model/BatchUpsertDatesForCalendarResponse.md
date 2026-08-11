# BatchUpsertDatesForCalendarResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **values** | [Dict[str, CalendarDate]](CalendarDate.md) | Optional | The dates which have been successfully upserted. |
| **failed** | [Dict[str, ErrorDetail]](ErrorDetail.md) | Optional | The dates that could not be upserted along with a reason for their failure. |
| **metadata** | **Dict[str, Optional[List[ResponseMetaData]]]** | Optional | Contains warnings related to the upserted dates |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.BatchUpsertDatesForCalendarResponse import BatchUpsertDatesForCalendarResponse

instance = BatchUpsertDatesForCalendarResponse(
    values=CalendarDate(...),  # optional — The dates which have been successfully upserted.
    failed=ErrorDetail(...),  # optional — The dates that could not be upserted along with a reason for their failure.
    metadata=,  # optional — Contains warnings related to the upserted dates
    links=[]  # optional
)
```


## Related Models

- [CalendarDate](CalendarDate.md) — used in `values`
- [ErrorDetail](ErrorDetail.md) — used in `failed`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

