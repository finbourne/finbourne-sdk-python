# UpdateConfigurationItem

The information required to update a configuration item
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **value** | **str** | Required | The new value of the configuration item |
| **description** | **str** | Optional | The new description of the configuration item |
| **block_reveal** | **bool** | Optional | The requested new state of BlockReveal |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.configuration.models.UpdateConfigurationItem import UpdateConfigurationItem

instance = UpdateConfigurationItem(
    value="...",  # required — The new value of the configuration item
    description="...",  # optional — The new description of the configuration item
    block_reveal=True  # optional — The requested new state of BlockReveal
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

