# IdentifierPartSchema

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **index** | **int** | Required | *No description available.* |
| **name** | **str** | Required | *No description available.* |
| **display_name** | **str** | Required | *No description available.* |
| **description** | **str** | Required | *No description available.* |
| **required** | **bool** | Required | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.insights.models.IdentifierPartSchema import IdentifierPartSchema

instance = IdentifierPartSchema(
    index=0,  # required
    name="...",  # required
    display_name="...",  # required
    description="...",  # required
    required=True,  # required
    links=[]  # optional
)
```

- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

