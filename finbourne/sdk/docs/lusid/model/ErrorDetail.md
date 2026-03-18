# ErrorDetail

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | **str** | Optional | The id of the failed item that this error relates to. |
| **type** | **str** | Optional | The type of failure that occurred. |
| **detail** | **str** | Optional | Description of the failure that occurred. |
| **error_details** | **List[Dict[str, str]]** | Optional | Information about the particular instance of the failure (supplied information depends on the type of failure). |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ErrorDetail import ErrorDetail

instance = ErrorDetail(
    id="...",  # optional — The id of the failed item that this error relates to.
    type="...",  # optional — The type of failure that occurred.
    detail="...",  # optional — Description of the failure that occurred.
    error_details=  # optional — Information about the particular instance of the failure (supplied information depends on the type of failure).
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

