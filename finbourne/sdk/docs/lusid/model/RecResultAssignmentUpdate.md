# RecResultAssignmentUpdate

An assignment update (assigned user or role) within a batch review item. Omitting the object leaves  the existing value untouched; a null value nullifies it.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **value** | **str** | Optional | The value to set, or null to nullify. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RecResultAssignmentUpdate import RecResultAssignmentUpdate

instance = RecResultAssignmentUpdate(
    value="..."  # optional — The value to set, or null to nullify.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

