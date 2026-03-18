# DateAttributes

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **irregular** | **bool** | Required | *No description available.* |
| **irregular_session** | **bool** | Required | *No description available.* |
| **new_hours** | **bool** | Required | *No description available.* |
| **activity** | **str** | Optional | *No description available.* |
| **first_open** | **str** | Optional | *No description available.* |
| **last_open** | **str** | Optional | *No description available.* |
| **first_close** | **str** | Optional | *No description available.* |
| **last_close** | **str** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.DateAttributes import DateAttributes

instance = DateAttributes(
    irregular=True,  # required
    irregular_session=True,  # required
    new_hours=True,  # required
    activity="...",  # optional
    first_open="...",  # optional
    last_open="...",  # optional
    first_close="...",  # optional
    last_close="..."  # optional
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

