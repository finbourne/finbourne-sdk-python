# CustomMultiQueryExport

Where (and how) to save the results of a custom multi-query to Drive, as one file, once its queries are done: the same as calling `api/MultiQueryBackground/{executionId}/drive` then, which may still be called as often as wanted.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **drive_location_and_file_name** | **str** | Optional | Location and file name within Drive to save to. Missing paths will be created, and extension (if given) will be ignored and inferred from the format (zip where several results are zipped). May contain the placeholders &#x60;{executionId}&#x60;, &#x60;{date:format}&#x60; (when the queries started, UTC, e.g. &#x60;{date:yyyyMMdd}&#x60;) and &#x60;{param:name}&#x60; (the value of a scalar parameter). |
| **format** | [ExportType](ExportType.md) | Optional | *No description available.* |
| **may_overwrite** | **bool** | Optional | If there is an existing file at the location with the same name should it be overwritten (rather than the export failing)?  False by default. |
| **drive_template_location** | **str** | Optional | Drive path and full file name including extension of a template to export with.  Only Excel and Pdf exports support templates. |
| **date_time_format** | **str** | Optional | Format to apply for DateTime data, leaving blank gives the Luminesce Exporter default, currently &#x60;yyyy-MM-dd HH:mm:ss.fff&#x60; |
| **when_some_fail** | **bool** | Optional | Should the results of the queries that succeeded still be saved when others did not?  False by default, meaning nothing is saved then. Either way the multi-query as a whole is reported as failed. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.luminesce.models.CustomMultiQueryExport import CustomMultiQueryExport

instance = CustomMultiQueryExport(
    drive_location_and_file_name="...",  # optional — Location and file name within Drive to save to. Missing paths will be created, and extension (if given) will be ignored and inferred from the format (zip where several results are zipped). May contain the placeholders &#x60;{executionId}&#x60;, &#x60;{date:format}&#x60; (when the queries started, UTC, e.g. &#x60;{date:yyyyMMdd}&#x60;) and &#x60;{param:name}&#x60; (the value of a scalar parameter).
    format=ExportType(...),  # optional
    may_overwrite=True,  # optional — If there is an existing file at the location with the same name should it be overwritten (rather than the export failing)?  False by default.
    drive_template_location="...",  # optional — Drive path and full file name including extension of a template to export with.  Only Excel and Pdf exports support templates.
    date_time_format="...",  # optional — Format to apply for DateTime data, leaving blank gives the Luminesce Exporter default, currently &#x60;yyyy-MM-dd HH:mm:ss.fff&#x60;
    when_some_fail=True  # optional — Should the results of the queries that succeeded still be saved when others did not?  False by default, meaning nothing is saved then. Either way the multi-query as a whole is reported as failed.
)
```

- [ExportType](ExportType.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

