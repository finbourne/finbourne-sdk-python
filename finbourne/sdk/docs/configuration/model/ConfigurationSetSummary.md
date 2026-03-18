# ConfigurationSetSummary

A group of configuration items
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **type** | **str** | Required | The type (personal or shared) of the configuration set |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.configuration.models.ConfigurationSetSummary import ConfigurationSetSummary

instance = ConfigurationSetSummary(
    id=ResourceId(...),  # required
    type="...",  # required — The type (personal or shared) of the configuration set
    links=[]  # optional
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

