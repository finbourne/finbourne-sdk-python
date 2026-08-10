# ResourceListOfSystemLog

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **values** | [../model/List[SystemLog]](SystemLog.md) | Required | *No description available.* |
| **href** | **str** | Optional | *No description available.* |
| **links** | [../model/List[Link]](Link.md) | Optional | *No description available.* |
| **next_page** | **str** | Optional | *No description available.* |
| **previous_page** | **str** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.identity.models.ResourceListOfSystemLog import ResourceListOfSystemLog

instance = ResourceListOfSystemLog(
    values=[],  # required
    href="...",  # optional
    links=[],  # optional
    next_page="...",  # optional
    previous_page="..."  # optional
)
```


## Related Models

- [SystemLog](SystemLog.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

