# OptionsExcel

Additional options applicable to the given SourceType
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **column_names** | **str** | Optional | Column Names either overrides the header row or steps in when there is no header row (comma delimited list) |
| **column_types** | **str** | Optional | Column types (comma delimited list of: &#39;{types}&#39;, some columns may be left blank while others are specified) |
| **infer_type_row_count** | **int** | Optional | If non-zero and &#39;types&#39; is not specified (or not specified for some columns) this will look through N rows to attempt to work out the column types for columns not pre-specified |
| **no_header** | **bool** | Optional | Set this if there is no header row |
| **calculate** | **bool** | Optional | Whether to attempt a calculation of the imported cell range prior to import |
| **password** | **str** | Optional | If specified will be used as the password used for password protected workbooks |
| **worksheet** | **str** | Optional | The worksheet containing the cell range to import (name or index, will default to first) |
| **range_or_table** | **str** | Optional | The cell range to import as either a specified range or a table name |
| **ignore_invalid_cells** | **bool** | Optional | If specified cells which can not be successfully converted to the target type will be ignored |
| **ignore_blank_rows** | **bool** | Optional | If the entire rows has only blank cells it will be ignored will be ignored |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.luminesce.models.OptionsExcel import OptionsExcel

instance = OptionsExcel(
    column_names="...",  # optional — Column Names either overrides the header row or steps in when there is no header row (comma delimited list)
    column_types="...",  # optional — Column types (comma delimited list of: &#39;{types}&#39;, some columns may be left blank while others are specified)
    infer_type_row_count=0,  # optional — If non-zero and &#39;types&#39; is not specified (or not specified for some columns) this will look through N rows to attempt to work out the column types for columns not pre-specified
    no_header=True,  # optional — Set this if there is no header row
    calculate=True,  # optional — Whether to attempt a calculation of the imported cell range prior to import
    password="...",  # optional — If specified will be used as the password used for password protected workbooks
    worksheet="...",  # optional — The worksheet containing the cell range to import (name or index, will default to first)
    range_or_table="...",  # optional — The cell range to import as either a specified range or a table name
    ignore_invalid_cells=True,  # optional — If specified cells which can not be successfully converted to the target type will be ignored
    ignore_blank_rows=True  # optional — If the entire rows has only blank cells it will be ignored will be ignored
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

