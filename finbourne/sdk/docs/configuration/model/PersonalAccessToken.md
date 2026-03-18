# PersonalAccessToken

Representation of a Personal Access Token under a Configuration Item format.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **value** | **str** | Required | Value of the Personal Access Token. *(read-only)* |
| **type** | **str** | Required | The type of the Personal Access Token. *(read-only)* |
| **description** | **str** | Required | The description of the Personal Access Token. *(read-only)* |
| **ref** | **str** | Required | The reference to the Personal Access Token *(read-only)* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.configuration.models.PersonalAccessToken import PersonalAccessToken

instance = PersonalAccessToken(
    value="...",  # required — Value of the Personal Access Token.
    type="...",  # required — The type of the Personal Access Token.
    description="...",  # required — The description of the Personal Access Token.
    ref="...",  # required — The reference to the Personal Access Token
    links=[]  # optional
)
```

- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

