# FileDestinationResponse

The destination a file delivery row describes. A Failed row carries the per-transaction FailureReason when one was recorded, falling back to the raw Error text.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **type** | **str** | Required | *No description available.* |
| **path** | **str** | Required | *No description available.* |
| **status** | **str** | Required | *No description available.* |
| **error** | **str** | Optional | *No description available.* |
| **failure_reason** | **str** | Optional | *No description available.* |
| **name** | **str** | Optional | The configured destination name, such as the SFTP host, when one was recorded. |
| **delivered_at** | **datetime** | Optional | When the file reached the destination; null for a Failed or Pending row. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.FileDestinationResponse import FileDestinationResponse

instance = FileDestinationResponse(
    type="...",  # required
    path="...",  # required
    status="...",  # required
    error="...",  # optional
    failure_reason="...",  # optional
    name="...",  # optional — The configured destination name, such as the SFTP host, when one was recorded.
    delivered_at=datetime.now()  # optional — When the file reached the destination; null for a Failed or Pending row.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

