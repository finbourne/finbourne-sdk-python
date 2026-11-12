# LuminesceMultiQuery

Configuration for a Worker that runs a Luminesce custom multi-query saved in Workspaces, saving its results to Drive as one file. Its parameters are the multi-query's scalar parameters, and the export settings below, which a task may override through the worker's `export-*` parameters.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **type** | **str** | Required | The type of worker |
| **workspace_key** | **str** | Required | The Workspaces key of the multi-query, e.g. &#x60;shared/SomeWorkspace/items/sets/SomeSet&#x60;, read as each run starts. An item of a personal workspace can only be read by the user who saved it, so only runs as that user can use it. |
| **drive_location_and_file_name** | **str** | Required | Where in Drive to save the results. May contain the placeholders &#x60;{executionId}&#x60;, &#x60;{date:format}&#x60; (when the queries started, UTC) and &#x60;{param:name}&#x60; (a scalar parameter&#39;s value); the extension comes from the format. |
| **format** | **str** | Optional | The format to save in: csv (the default), pipe, excel, json, jsonProper, jsonProperWithLineage, jsonProperByTable, xml, parquet, sqlite or pdf. Several results are one worksheet each for excel, one table each for sqlite, one key each for jsonProperByTable, and otherwise one file each within a zip. |
| **may_overwrite** | **bool** | Optional | Whether an existing file of the same name may be overwritten, rather than the run failing. False by default. |
| **drive_template_location** | **str** | Optional | The Drive path and file name of a template to save with. Only excel and pdf support templates. |
| **date_time_format** | **str** | Optional | The format to write DateTime values in, Luminesce&#39;s default (&#x60;yyyy-MM-dd HH:mm:ss.fff&#x60;) when not given. |
| **when_some_fail** | **bool** | Optional | Whether the results of the queries that succeeded are still saved when others did not, the worker then completing with the status PartiallyCompleted. False by default, the worker then failing with nothing saved. |
| **keep_for_seconds** | **int** | Optional | How long Luminesce keeps the results once done, e.g. to look into a run or save them again: 2 hours by default, at most 31 days. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.LuminesceMultiQuery import LuminesceMultiQuery

instance = LuminesceMultiQuery(
    type="...",  # required — The type of worker
    workspace_key="...",  # required — The Workspaces key of the multi-query, e.g. &#x60;shared/SomeWorkspace/items/sets/SomeSet&#x60;, read as each run starts. An item of a personal workspace can only be read by the user who saved it, so only runs as that user can use it.
    drive_location_and_file_name="...",  # required — Where in Drive to save the results. May contain the placeholders &#x60;{executionId}&#x60;, &#x60;{date:format}&#x60; (when the queries started, UTC) and &#x60;{param:name}&#x60; (a scalar parameter&#39;s value); the extension comes from the format.
    format="...",  # optional — The format to save in: csv (the default), pipe, excel, json, jsonProper, jsonProperWithLineage, jsonProperByTable, xml, parquet, sqlite or pdf. Several results are one worksheet each for excel, one table each for sqlite, one key each for jsonProperByTable, and otherwise one file each within a zip.
    may_overwrite=True,  # optional — Whether an existing file of the same name may be overwritten, rather than the run failing. False by default.
    drive_template_location="...",  # optional — The Drive path and file name of a template to save with. Only excel and pdf support templates.
    date_time_format="...",  # optional — The format to write DateTime values in, Luminesce&#39;s default (&#x60;yyyy-MM-dd HH:mm:ss.fff&#x60;) when not given.
    when_some_fail=True,  # optional — Whether the results of the queries that succeeded are still saved when others did not, the worker then completing with the status PartiallyCompleted. False by default, the worker then failing with nothing saved.
    keep_for_seconds=0  # optional — How long Luminesce keeps the results once done, e.g. to look into a run or save them again: 2 hours by default, at most 31 days.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

