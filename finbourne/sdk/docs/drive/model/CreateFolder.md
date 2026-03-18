# CreateFolder

DTO representing the creation of a folder
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **path** | **str** | Required | Path of the created folder |
| **name** | **str** | Required | Name of the created folder |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.drive.models.CreateFolder import CreateFolder

instance = CreateFolder(
    path="...",  # required — Path of the created folder
    name="..."  # required — Name of the created folder
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

