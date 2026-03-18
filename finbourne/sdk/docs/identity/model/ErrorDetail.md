# ErrorDetail

Provides details about an entity error that occured
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | **str** | Optional | Id of the entity this error relates to |
| **type** | **str** | Optional | Error type |
| **detail** | **str** | Optional | Human readable description of the error |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.identity.models.ErrorDetail import ErrorDetail

instance = ErrorDetail(
    id="...",  # optional — Id of the entity this error relates to
    type="...",  # optional — Error type
    detail="..."  # optional — Human readable description of the error
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

