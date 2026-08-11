# FilterTermDesign

A single filter clause
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **operator** | [QueryDesignerBinaryOperator](QueryDesignerBinaryOperator.md) | Required | *No description available.* |
| **value** | **str** | Required | The value to compare against (always as a string, but will be formatted to the correct type) |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.luminesce.models.FilterTermDesign import FilterTermDesign

instance = FilterTermDesign(
    operator=QueryDesignerBinaryOperator(...),  # required
    value="..."  # required — The value to compare against (always as a string, but will be formatted to the correct type)
)
```


## Related Models

- [QueryDesignerBinaryOperator](QueryDesignerBinaryOperator.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

