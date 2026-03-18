# SetPasswordResponse

The result of setting a password
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **updated_at** | **datetime** | Required | The date and time at which the password was successfully updated |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.identity.models.SetPasswordResponse import SetPasswordResponse

instance = SetPasswordResponse(
    updated_at=datetime.now(),  # required — The date and time at which the password was successfully updated
    links=[]  # optional
)
```

- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

