# OrderByTermDesign

A single clause within an Order BY
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **var_field** | **str** | Required | Name of the field to order by |
| **direction** | [OrderByDirection](OrderByDirection.md) | Optional | *No description available.* |
| **table_alias** | **str** | Optional | Table Alias of the field to order by |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.luminesce.models.OrderByTermDesign import OrderByTermDesign

instance = OrderByTermDesign(
    var_field="...",  # required — Name of the field to order by
    direction=OrderByDirection(...),  # optional
    table_alias="..."  # optional — Table Alias of the field to order by
)
```

- [OrderByDirection](OrderByDirection.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

