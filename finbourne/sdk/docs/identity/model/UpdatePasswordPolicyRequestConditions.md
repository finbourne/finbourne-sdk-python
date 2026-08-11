# UpdatePasswordPolicyRequestConditions

Password policy conditions for a password policy
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **complexity** | [UpdatePasswordPolicyRequestComplexity](UpdatePasswordPolicyRequestComplexity.md) | Required | *No description available.* |
| **age** | [UpdatePasswordPolicyRequestAge](UpdatePasswordPolicyRequestAge.md) | Required | *No description available.* |
| **lockout** | [UpdatePasswordPolicyRequestLockout](UpdatePasswordPolicyRequestLockout.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.identity.models.UpdatePasswordPolicyRequestConditions import UpdatePasswordPolicyRequestConditions

instance = UpdatePasswordPolicyRequestConditions(
    complexity=UpdatePasswordPolicyRequestComplexity(...),  # required
    age=UpdatePasswordPolicyRequestAge(...),  # required
    lockout=UpdatePasswordPolicyRequestLockout(...)  # required
)
```


## Related Models

- [UpdatePasswordPolicyRequestComplexity](UpdatePasswordPolicyRequestComplexity.md)
- [UpdatePasswordPolicyRequestAge](UpdatePasswordPolicyRequestAge.md)
- [UpdatePasswordPolicyRequestLockout](UpdatePasswordPolicyRequestLockout.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

