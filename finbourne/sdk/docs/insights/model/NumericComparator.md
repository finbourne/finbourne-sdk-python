# NumericComparator

Filters a numeric field by comparing it to a supplied numeric value.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **operation** | **str** | Required | The comparison to apply between the field and Finbourne.Insights.WebApi.Dtos.Querying.NumericComparator.Value. One of the Finbourne.Insights.WebApi.Dtos.Querying.NumericOperation values (e.g. EqualTo, GreaterThan); discoverable via the queryable-fields metadata endpoint. |
| **value** | **float** | Required | The value to compare the field against. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.insights.models.NumericComparator import NumericComparator

instance = NumericComparator(
    operation="...",  # required — The comparison to apply between the field and Finbourne.Insights.WebApi.Dtos.Querying.NumericComparator.Value. One of the Finbourne.Insights.WebApi.Dtos.Querying.NumericOperation values (e.g. EqualTo, GreaterThan); discoverable via the queryable-fields metadata endpoint.
    value=0.0  # required — The value to compare the field against.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

