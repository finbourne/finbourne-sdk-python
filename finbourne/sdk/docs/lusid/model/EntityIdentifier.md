# EntityIdentifier

Dto to expose mapped keys to new standardised format
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **identifier_scope** | **str** | Optional | The scope of the identifier |
| **identifier_type** | **str** | Required | The type of the identifier |
| **identifier_value** | **str** | Required | The value of the identifier |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.EntityIdentifier import EntityIdentifier

instance = EntityIdentifier(
    identifier_scope="...",  # optional — The scope of the identifier
    identifier_type="...",  # required — The type of the identifier
    identifier_value="..."  # required — The value of the identifier
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

