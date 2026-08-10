# UpdateRelationalDatasetFieldSchema

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **add** | [../model/RelationalDatasetFieldsToAdd](RelationalDatasetFieldsToAdd.md) | Optional | *No description available.* |
| **update** | [../model/RelationalDatasetFieldsToUpdate](RelationalDatasetFieldsToUpdate.md) | Optional | *No description available.* |
| **remove** | [../model/RelationalDatasetFieldsToRemove](RelationalDatasetFieldsToRemove.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpdateRelationalDatasetFieldSchema import UpdateRelationalDatasetFieldSchema

instance = UpdateRelationalDatasetFieldSchema(
    add=RelationalDatasetFieldsToAdd(...),  # optional
    update=RelationalDatasetFieldsToUpdate(...),  # optional
    remove=RelationalDatasetFieldsToRemove(...)  # optional
)
```


## Related Models

- [RelationalDatasetFieldsToAdd](RelationalDatasetFieldsToAdd.md)
- [RelationalDatasetFieldsToUpdate](RelationalDatasetFieldsToUpdate.md)
- [RelationalDatasetFieldsToRemove](RelationalDatasetFieldsToRemove.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

