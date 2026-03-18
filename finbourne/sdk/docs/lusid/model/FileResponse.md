# FileResponse

Allows a file (represented as a stream) to be returned from an Api call
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **file_stream** | **bytes** | Optional | *No description available.* |
| **content_type** | **str** | Optional | *No description available.* |
| **downloaded_filename** | **str** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FileResponse import FileResponse

instance = FileResponse(
    file_stream=,  # optional
    content_type="...",  # optional
    downloaded_filename="..."  # optional
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

