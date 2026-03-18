# RequestedActionKey

A fully qualified action identifier
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **entity_code** | **str** | Required | The type of the resource on which the activity would be performed |
| **scope** | **str** | Required | The scope/provider/vendor of the activity |
| **activity** | **str** | Required | The identifier of the action to be performed on the resource |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.access.models.RequestedActionKey import RequestedActionKey

instance = RequestedActionKey(
    entity_code="...",  # required — The type of the resource on which the activity would be performed
    scope="...",  # required — The scope/provider/vendor of the activity
    activity="..."  # required — The identifier of the action to be performed on the resource
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

