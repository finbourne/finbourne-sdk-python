# FieldDefinition

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **key** | **str** | Required | *No description available.* |
| **is_required** | **bool** | Required | *No description available.* |
| **is_unique** | **bool** | Required | *No description available.* |
| **value_type** | **str** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FieldDefinition import FieldDefinition

instance = FieldDefinition(
    key="...",  # required
    is_required=True,  # required
    is_unique=True,  # required
    value_type="..."  # optional
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

