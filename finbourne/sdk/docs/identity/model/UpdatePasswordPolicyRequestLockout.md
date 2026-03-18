# UpdatePasswordPolicyRequestLockout

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **max_attempts** | **int** | Required | The maximum number of unsuccessful attempts before the user is locked out of their account. 0 indicates no limit |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.identity.models.UpdatePasswordPolicyRequestLockout import UpdatePasswordPolicyRequestLockout

instance = UpdatePasswordPolicyRequestLockout(
    max_attempts=0  # required — The maximum number of unsuccessful attempts before the user is locked out of their account. 0 indicates no limit
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

