# PasswordPolicyResponseConditions

Password policy conditions for a password policy
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **complexity** | [PasswordPolicyResponseComplexity](PasswordPolicyResponseComplexity.md) | Required | *No description available.* |
| **age** | [PasswordPolicyResponseAge](PasswordPolicyResponseAge.md) | Required | *No description available.* |
| **lockout** | [PasswordPolicyResponseLockout](PasswordPolicyResponseLockout.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.identity.models.PasswordPolicyResponseConditions import PasswordPolicyResponseConditions

instance = PasswordPolicyResponseConditions(
    complexity=PasswordPolicyResponseComplexity(...),  # required
    age=PasswordPolicyResponseAge(...),  # required
    lockout=PasswordPolicyResponseLockout(...)  # required
)
```


## Related Models

- [PasswordPolicyResponseComplexity](PasswordPolicyResponseComplexity.md)
- [PasswordPolicyResponseAge](PasswordPolicyResponseAge.md)
- [PasswordPolicyResponseLockout](PasswordPolicyResponseLockout.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

