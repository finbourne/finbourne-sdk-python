# LuminesceMultiQueryResponse

Readonly configuration for the Luminesce custom multi-query Worker
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **type** | **str** | Optional | The type of worker |
| **workspace_key** | **str** | Optional | The Workspaces key of the multi-query the worker runs |
| **drive_location_and_file_name** | **str** | Optional | Where in Drive the results are saved, which may contain placeholders |
| **format** | **str** | Optional | The format the results are saved in, csv when not given |
| **may_overwrite** | **bool** | Optional | Whether an existing file of the same name may be overwritten |
| **drive_template_location** | **str** | Optional | The Drive path of the template the results are saved with |
| **date_time_format** | **str** | Optional | The format DateTime values are written in |
| **when_some_fail** | **bool** | Optional | Whether the results of the queries that succeeded are still saved when others did not |
| **keep_for_seconds** | **int** | Optional | How long Luminesce keeps the results once done, in seconds |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.LuminesceMultiQueryResponse import LuminesceMultiQueryResponse

instance = LuminesceMultiQueryResponse(
    type="...",  # optional — The type of worker
    workspace_key="...",  # optional — The Workspaces key of the multi-query the worker runs
    drive_location_and_file_name="...",  # optional — Where in Drive the results are saved, which may contain placeholders
    format="...",  # optional — The format the results are saved in, csv when not given
    may_overwrite=True,  # optional — Whether an existing file of the same name may be overwritten
    drive_template_location="...",  # optional — The Drive path of the template the results are saved with
    date_time_format="...",  # optional — The format DateTime values are written in
    when_some_fail=True,  # optional — Whether the results of the queries that succeeded are still saved when others did not
    keep_for_seconds=0  # optional — How long Luminesce keeps the results once done, in seconds
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

