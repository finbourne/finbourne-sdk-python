# UpdateMarketDataFieldConfigurationRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **add** | [../model/MetadataFieldsToAdd](MetadataFieldsToAdd.md) | Optional | *No description available.* |
| **update** | [../model/MetadataFieldsToUpdate](MetadataFieldsToUpdate.md) | Optional | *No description available.* |
| **remove** | [../model/MetadataFieldsToRemove](MetadataFieldsToRemove.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpdateMarketDataFieldConfigurationRequest import UpdateMarketDataFieldConfigurationRequest

instance = UpdateMarketDataFieldConfigurationRequest(
    add=MetadataFieldsToAdd(...),  # optional
    update=MetadataFieldsToUpdate(...),  # optional
    remove=MetadataFieldsToRemove(...)  # optional
)
```


## Related Models

- [MetadataFieldsToAdd](MetadataFieldsToAdd.md)
- [MetadataFieldsToUpdate](MetadataFieldsToUpdate.md)
- [MetadataFieldsToRemove](MetadataFieldsToRemove.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

