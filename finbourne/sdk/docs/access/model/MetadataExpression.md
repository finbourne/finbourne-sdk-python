# MetadataExpression

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **metadata_key** | **str** | Required | *No description available.* |
| **operator** | [Operator](Operator.md) | Required | *No description available.* |
| **text_value** | **str** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.access.models.MetadataExpression import MetadataExpression

instance = MetadataExpression(
    metadata_key="...",  # required
    operator=Operator(...),  # required
    text_value="..."  # optional
)
```

- [Operator](Operator.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

