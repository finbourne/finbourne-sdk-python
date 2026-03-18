# ResourceId

Unique identifier for a resource
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **scope** | **str** | Required | The scope used to identify a resource |
| **code** | **str** | Optional | The code used to identify a resource |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.luminesce.models.ResourceId import ResourceId

instance = ResourceId(
    scope="...",  # required — The scope used to identify a resource
    code="..."  # optional — The code used to identify a resource
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

