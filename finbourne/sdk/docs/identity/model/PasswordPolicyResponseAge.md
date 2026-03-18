# PasswordPolicyResponseAge

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **max_age_days** | **int** | Required | The maximum age (in days) a password can be before expiring and needing to be changed |
| **history_count** | **int** | Required | The number of unique passwords that need to be used before a previous password is permitted again |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.identity.models.PasswordPolicyResponseAge import PasswordPolicyResponseAge

instance = PasswordPolicyResponseAge(
    max_age_days=0,  # required — The maximum age (in days) a password can be before expiring and needing to be changed
    history_count=0  # required — The number of unique passwords that need to be used before a previous password is permitted again
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

