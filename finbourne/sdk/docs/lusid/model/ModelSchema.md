# ModelSchema

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **entity** | **str** | Optional | *No description available.* |
| **href** | **str** | Optional | *No description available.* |
| **values** | [Dict[str, FieldSchema]](FieldSchema.md) | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ModelSchema import ModelSchema

instance = ModelSchema(
    entity="...",  # optional
    href="...",  # optional
    values=FieldSchema(...),  # optional
    links=[]  # optional
)
```

- [FieldSchema](FieldSchema.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

