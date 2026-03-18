# UpdatePasswordPolicyRequestAge

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **max_age_days** | **int** | Required | The maximum age (in days) a password can be before expiring and needing to be changed. 0 indicates no limit |
| **history_count** | **int** | Required | The number of unique passwords that need to be used before a previous password is permitted again. 0 indicates none |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.identity.models.UpdatePasswordPolicyRequestAge import UpdatePasswordPolicyRequestAge

instance = UpdatePasswordPolicyRequestAge(
    max_age_days=0,  # required — The maximum age (in days) a password can be before expiring and needing to be changed. 0 indicates no limit
    history_count=0  # required — The number of unique passwords that need to be used before a previous password is permitted again. 0 indicates none
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

