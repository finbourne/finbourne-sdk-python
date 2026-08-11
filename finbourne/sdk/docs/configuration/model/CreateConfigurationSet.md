# CreateConfigurationSet

The information required to create a new configuration set
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **type** | **str** | Required | The type (personal or shared) of the new configuration set |
| **description** | **str** | Optional | The description of the new configuration set |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.configuration.models.CreateConfigurationSet import CreateConfigurationSet

instance = CreateConfigurationSet(
    id=ResourceId(...),  # required
    type="...",  # required — The type (personal or shared) of the new configuration set
    description="..."  # optional — The description of the new configuration set
)
```


## Related Models

- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

