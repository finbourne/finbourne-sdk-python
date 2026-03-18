# UpdateFile

DTO representing the update of the name or path of a file
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **path** | **str** | Required | Path of the updated file |
| **name** | **str** | Required | Name of the updated file |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.drive.models.UpdateFile import UpdateFile

instance = UpdateFile(
    path="...",  # required — Path of the updated file
    name="..."  # required — Name of the updated file
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

