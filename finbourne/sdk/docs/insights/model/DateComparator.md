# DateComparator

Filters a date/time field by comparing it to a supplied date/time value.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **operation** | **str** | Required | The comparison to apply between the field and Finbourne.Insights.WebApi.Dtos.Querying.DateComparator.Value. One of the Finbourne.Insights.WebApi.Dtos.Querying.DateOperation values (e.g. Before, OnOrAfter); discoverable via the queryable-fields metadata endpoint. |
| **value** | **datetime** | Required | The value to compare the field against. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.insights.models.DateComparator import DateComparator

instance = DateComparator(
    operation="...",  # required — The comparison to apply between the field and Finbourne.Insights.WebApi.Dtos.Querying.DateComparator.Value. One of the Finbourne.Insights.WebApi.Dtos.Querying.DateOperation values (e.g. Before, OnOrAfter); discoverable via the queryable-fields metadata endpoint.
    value=datetime.now()  # required — The value to compare the field against.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

