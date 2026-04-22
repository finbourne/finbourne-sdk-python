# ClientConfigurationResponse

Represents a versioned client configuration record.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **name** | **str** | Required | The logical name of the configuration. |
| **config_type** | **str** | Required | The category of configuration. |
| **major_version** | **int** | Required | The major version number. |
| **minor_version** | **int** | Required | The minor version number. |
| **value** | **str** | Required | The JSON configuration value. |
| **is_draft** | **bool** | Required | Whether this version is still in draft state. Draft versions can be edited; locked versions cannot. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.ClientConfigurationResponse import ClientConfigurationResponse

instance = ClientConfigurationResponse(
    name="...",  # required — The logical name of the configuration.
    config_type="...",  # required — The category of configuration.
    major_version=0,  # required — The major version number.
    minor_version=0,  # required — The minor version number.
    value="...",  # required — The JSON configuration value.
    is_draft=True  # required — Whether this version is still in draft state. Draft versions can be edited; locked versions cannot.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

