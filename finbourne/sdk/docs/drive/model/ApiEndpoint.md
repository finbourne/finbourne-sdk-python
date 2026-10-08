# ApiEndpoint

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **operation** | **str** | Optional | *No description available.* |
| **http_method** | **str** | Required | *No description available.* |
| **path** | **str** | Required | *No description available.* |
| **status** | **str** | Optional | *No description available.* |
| **summary** | **str** | Optional | *No description available.* |
| **description** | **str** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.drive.models.ApiEndpoint import ApiEndpoint

instance = ApiEndpoint(
    operation="...",  # optional
    http_method="...",  # required
    path="...",  # required
    status="...",  # optional
    summary="...",  # optional
    description="..."  # optional
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

