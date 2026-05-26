# FileDestinationResponse

record containing details of a single file destination for a run.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **type** | **str** | Required | *No description available.* |
| **path** | **str** | Required | *No description available.* |
| **status** | **str** | Required | *No description available.* |
| **error** | **str** | Optional | *No description available.* |
| **failure_reason** | **str** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.FileDestinationResponse import FileDestinationResponse

instance = FileDestinationResponse(
    type="...",  # required
    path="...",  # required
    status="...",  # required
    error="...",  # optional
    failure_reason="..."  # optional
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

