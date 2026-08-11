# IfRequestHeaderExpression

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **header_name** | **str** | Required | *No description available.* |
| **operator** | [TextOperator](TextOperator.md) | Required | *No description available.* |
| **value** | **str** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.access.models.IfRequestHeaderExpression import IfRequestHeaderExpression

instance = IfRequestHeaderExpression(
    header_name="...",  # required
    operator=TextOperator(...),  # required
    value="..."  # optional
)
```

- [TextOperator](TextOperator.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

