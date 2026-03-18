# UpdatePasswordPolicyRequestComplexity

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **min_length** | **int** | Required | The minimum length for a password |
| **exclude_first_name** | **bool** | Required | Rule determining whether a user&#39;s first name should be permitted in their password |
| **exclude_last_name** | **bool** | Required | Rule determining whether a user&#39;s last name should be permitted in their password |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.identity.models.UpdatePasswordPolicyRequestComplexity import UpdatePasswordPolicyRequestComplexity

instance = UpdatePasswordPolicyRequestComplexity(
    min_length=0,  # required — The minimum length for a password
    exclude_first_name=True,  # required — Rule determining whether a user&#39;s first name should be permitted in their password
    exclude_last_name=True  # required — Rule determining whether a user&#39;s last name should be permitted in their password
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

