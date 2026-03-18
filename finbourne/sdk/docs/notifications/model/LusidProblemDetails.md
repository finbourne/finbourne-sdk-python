# LusidProblemDetails

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **name** | **str** | Required | *No description available.* |
| **error_details** | **List[Dict[str, str]]** | Optional | *No description available.* |
| **code** | **int** | Required | *No description available.* |
| **type** | **str** | Optional | *No description available.* |
| **title** | **str** | Optional | *No description available.* |
| **status** | **int** | Optional | *No description available.* |
| **detail** | **str** | Optional | *No description available.* |
| **instance** | **str** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.notifications.models.LusidProblemDetails import LusidProblemDetails

instance = LusidProblemDetails(
    name="...",  # required
    error_details=,  # optional
    code=0,  # required
    type="...",  # optional
    title="...",  # optional
    status=0,  # optional
    detail="...",  # optional
    instance="..."  # optional
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

