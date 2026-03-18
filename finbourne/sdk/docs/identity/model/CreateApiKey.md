# CreateApiKey

Create an API key
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **display_name** | **str** | Required | The display name for the API key |
| **deactivation_date** | **datetime** | Optional | The optional date at which the key should deactivate |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.identity.models.CreateApiKey import CreateApiKey

instance = CreateApiKey(
    display_name="...",  # required — The display name for the API key
    deactivation_date=datetime.now()  # optional — The optional date at which the key should deactivate
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

