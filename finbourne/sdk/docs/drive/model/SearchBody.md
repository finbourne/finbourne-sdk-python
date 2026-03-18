# SearchBody

DTO representing the search query
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **with_path** | **str** | Optional | Optional path field to limit the search to result with a matching (case insensitive) path |
| **name** | **str** | Required | Name of the file or folder to be searched |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.drive.models.SearchBody import SearchBody

instance = SearchBody(
    with_path="...",  # optional — Optional path field to limit the search to result with a matching (case insensitive) path
    name="..."  # required — Name of the file or folder to be searched
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

