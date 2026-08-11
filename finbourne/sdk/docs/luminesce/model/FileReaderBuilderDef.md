# FileReaderBuilderDef

Information on how to construct a file-read sql query
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **auto_detect** | [AutoDetectType](AutoDetectType.md) | Optional | *No description available.* |
| **columns** | [List[ColumnInfo]](ColumnInfo.md) | Optional | Column information for the results |
| **limit** | **int** | Optional | What limit be added to the load query?  Less than or equal to zero means none |
| **source** | [Source](Source.md) | Optional | *No description available.* |
| **available_sources** | [List[Source]](Source.md) | Optional | The source locations the user has access to.  The provider in essence. |
| **variable_name** | **str** | Optional | The name of the variable for the &#x60;use&#x60; statement |
| **file_path** | **str** | Optional | The file (or folder) path |
| **folder_filter** | **str** | Optional | The filter to apply to a folder (all matching files then being read) a RegExp |
| **zip_filter** | **str** | Optional | The filter to apply to folder structures with zip archives (all matching files then being read) a RegExp |
| **add_file_name** | **bool** | Optional | Should a file name column be added to the output? |
| **csv** | [OptionsCsv](OptionsCsv.md) | Optional | *No description available.* |
| **excel** | [OptionsExcel](OptionsExcel.md) | Optional | *No description available.* |
| **sq_lite** | [OptionsSqLite](OptionsSqLite.md) | Optional | *No description available.* |
| **xml** | [OptionsXml](OptionsXml.md) | Optional | *No description available.* |
| **parquet** | [OptionsParquet](OptionsParquet.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.luminesce.models.FileReaderBuilderDef import FileReaderBuilderDef

instance = FileReaderBuilderDef(
    auto_detect=AutoDetectType(...),  # optional
    columns=[],  # optional — Column information for the results
    limit=0,  # optional — What limit be added to the load query?  Less than or equal to zero means none
    source=Source(...),  # optional
    available_sources=[],  # optional — The source locations the user has access to.  The provider in essence.
    variable_name="...",  # optional — The name of the variable for the &#x60;use&#x60; statement
    file_path="...",  # optional — The file (or folder) path
    folder_filter="...",  # optional — The filter to apply to a folder (all matching files then being read) a RegExp
    zip_filter="...",  # optional — The filter to apply to folder structures with zip archives (all matching files then being read) a RegExp
    add_file_name=True,  # optional — Should a file name column be added to the output?
    csv=OptionsCsv(...),  # optional
    excel=OptionsExcel(...),  # optional
    sq_lite=OptionsSqLite(...),  # optional
    xml=OptionsXml(...),  # optional
    parquet=OptionsParquet(...)  # optional
)
```


## Related Models

- [AutoDetectType](AutoDetectType.md)
- [ColumnInfo](ColumnInfo.md) — used in `columns`
- [Source](Source.md)
- [Source](Source.md) — used in `available_sources`
- [OptionsCsv](OptionsCsv.md)
- [OptionsExcel](OptionsExcel.md)
- [OptionsSqLite](OptionsSqLite.md)
- [OptionsXml](OptionsXml.md)
- [OptionsParquet](OptionsParquet.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

