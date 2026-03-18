# ResourceId

Identifiers of an entity
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **scope** | **str** | Required | The scope used to identify an entity |
| **code** | **str** | Required | The code used to identify an entity |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.notifications.models.ResourceId import ResourceId

instance = ResourceId(
    scope="...",  # required — The scope used to identify an entity
    code="..."  # required — The code used to identify an entity
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

