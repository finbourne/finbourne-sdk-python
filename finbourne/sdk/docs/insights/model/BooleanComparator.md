# BooleanComparator

Filters a boolean field by comparing it to a supplied boolean value.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **operation** | **str** | Required | The comparison to apply between the field and Finbourne.Insights.WebApi.Dtos.Querying.BooleanComparator.Value. One of the Finbourne.Insights.WebApi.Dtos.Querying.BooleanOperation values (EqualTo, NotEqualTo); discoverable via the queryable-fields metadata endpoint. |
| **value** | **bool** | Required | The value to compare the field against. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.insights.models.BooleanComparator import BooleanComparator

instance = BooleanComparator(
    operation="...",  # required — The comparison to apply between the field and Finbourne.Insights.WebApi.Dtos.Querying.BooleanComparator.Value. One of the Finbourne.Insights.WebApi.Dtos.Querying.BooleanOperation values (EqualTo, NotEqualTo); discoverable via the queryable-fields metadata endpoint.
    value=True  # required — The value to compare the field against.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

