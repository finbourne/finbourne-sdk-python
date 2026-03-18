# ExpressionWithAlias

Contract for an expression of data we \"have\" that we may \"want to map to a table-parameter's column\"
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **expression** | **str** | Required | Expression (column name, constant, complex expression, etc.) |
| **alias** | **str** | Optional | Column Alias for the expression |
| **flags** | [MappingFlags](MappingFlags.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.luminesce.models.ExpressionWithAlias import ExpressionWithAlias

instance = ExpressionWithAlias(
    expression="...",  # required — Expression (column name, constant, complex expression, etc.)
    alias="...",  # optional — Column Alias for the expression
    flags=MappingFlags(...)  # optional
)
```

- [MappingFlags](MappingFlags.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

