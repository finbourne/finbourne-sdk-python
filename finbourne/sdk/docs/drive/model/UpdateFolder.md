# UpdateFolder

DTO representing the update of the name or path of a file
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **path** | **str** | Required | Path of the updated folder |
| **name** | **str** | Required | Name of the updated folder |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.drive.models.UpdateFolder import UpdateFolder

instance = UpdateFolder(
    path="...",  # required — Path of the updated folder
    name="..."  # required — Name of the updated folder
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

