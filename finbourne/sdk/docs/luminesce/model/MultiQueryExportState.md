# MultiQueryExportState

What became of the export of a custom multi-query once its queries were done (persisted in its shared state, so known to every pod).
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **drive_location_and_file_name** | **str** | Optional | Where it was to be saved, its placeholders filled in |
| **saved_to** | **str** | Optional | The Drive path (and file name, with its extension) it was saved to, once it has been |
| **error** | **str** | Optional | Why it was not saved, if it was not |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.luminesce.models.MultiQueryExportState import MultiQueryExportState

instance = MultiQueryExportState(
    drive_location_and_file_name="...",  # optional — Where it was to be saved, its placeholders filled in
    saved_to="...",  # optional — The Drive path (and file name, with its extension) it was saved to, once it has been
    error="..."  # optional — Why it was not saved, if it was not
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

