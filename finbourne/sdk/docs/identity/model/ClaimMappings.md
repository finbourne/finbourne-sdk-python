# ClaimMappings

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **user_id** | **str** | Required | *No description available.* |
| **login** | **str** | Required | *No description available.* |
| **email** | **str** | Required | *No description available.* |
| **first_name** | **str** | Required | *No description available.* |
| **last_name** | **str** | Required | *No description available.* |
| **user_type** | **str** | Required | *No description available.* |
| **groups** | **str** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.identity.models.ClaimMappings import ClaimMappings

instance = ClaimMappings(
    user_id="...",  # required
    login="...",  # required
    email="...",  # required
    first_name="...",  # required
    last_name="...",  # required
    user_type="...",  # required
    groups="..."  # optional
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

