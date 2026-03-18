# OptionsCsv

Additional options applicable to the given SourceType
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **column_names** | **str** | Optional | Column Names either overrides the header row or steps in when there is no header row (comma delimited list) |
| **column_names_wanted** | **str** | Optional | Column (by Name) that should be returned (comma delimited list) |
| **column_types** | **str** | Optional | Column types (comma delimited list of: &#39;{types}&#39;, some columns may be left blank while others are specified) |
| **infer_type_row_count** | **int** | Optional | If non-zero and &#39;types&#39; is not specified (or not specified for some columns) this will look through N rows to attempt to work out the column types for columns not pre-specified |
| **no_header** | **bool** | Optional | Set this if there is no header row |
| **delimiter** | **str** | Optional | The delimiter between values (\\t for tab) |
| **escape** | **str** | Optional | Character used to escape the &#39;Quote&#39; character when within a value |
| **quote** | **str** | Optional | Character used around any field containing the &#39;delimiter&#39; or a line break. |
| **values_to_make_null** | **str** | Optional | Regex of values to map to &#39;null&#39; in the returned data. |
| **skip_pre_header** | **int** | Optional | Number of rows to ignore before the header row |
| **skip_post_header** | **int** | Optional | Number of rows to ignore after the header row |
| **skip_invalid_rows** | **bool** | Optional | Skip invalid data rows (totally invalid ones),  This also allows for potentially wrong data if it can be handled somewhat e.g. embedded quotes misused (and still returns such rows). In either case a warning will show in the progress feedback. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.luminesce.models.OptionsCsv import OptionsCsv

instance = OptionsCsv(
    column_names="...",  # optional — Column Names either overrides the header row or steps in when there is no header row (comma delimited list)
    column_names_wanted="...",  # optional — Column (by Name) that should be returned (comma delimited list)
    column_types="...",  # optional — Column types (comma delimited list of: &#39;{types}&#39;, some columns may be left blank while others are specified)
    infer_type_row_count=0,  # optional — If non-zero and &#39;types&#39; is not specified (or not specified for some columns) this will look through N rows to attempt to work out the column types for columns not pre-specified
    no_header=True,  # optional — Set this if there is no header row
    delimiter="...",  # optional — The delimiter between values (\\t for tab)
    escape="...",  # optional — Character used to escape the &#39;Quote&#39; character when within a value
    quote="...",  # optional — Character used around any field containing the &#39;delimiter&#39; or a line break.
    values_to_make_null="...",  # optional — Regex of values to map to &#39;null&#39; in the returned data.
    skip_pre_header=0,  # optional — Number of rows to ignore before the header row
    skip_post_header=0,  # optional — Number of rows to ignore after the header row
    skip_invalid_rows=True  # optional — Skip invalid data rows (totally invalid ones),  This also allows for potentially wrong data if it can be handled somewhat e.g. embedded quotes misused (and still returns such rows). In either case a warning will show in the progress feedback.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

