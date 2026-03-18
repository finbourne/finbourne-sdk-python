# ApiKey

The metadata of an API key
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | **str** | Required | The unique Id of the API key |
| **display_name** | **str** | Required | The display name of the API key |
| **created_date** | **datetime** | Required | The creation date of the API key |
| **deactivation_date** | **datetime** | Optional | The deactivation date of the API key |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.identity.models.ApiKey import ApiKey

instance = ApiKey(
    id="...",  # required — The unique Id of the API key
    display_name="...",  # required — The display name of the API key
    created_date=datetime.now(),  # required — The creation date of the API key
    deactivation_date=datetime.now()  # optional — The deactivation date of the API key
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

