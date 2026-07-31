# TextComparator

Filters a text field. Single-value operations (EqualTo, NotEqualTo, StartsWith, EndsWith) compare the field to Finbourne.Insights.WebApi.Dtos.Querying.TextComparator.Value; set operations (In, NotIn) compare it to Finbourne.Insights.WebApi.Dtos.Querying.TextComparator.Values. Exactly one of Finbourne.Insights.WebApi.Dtos.Querying.TextComparator.Value or Finbourne.Insights.WebApi.Dtos.Querying.TextComparator.Values is supplied, matching the chosen Finbourne.Insights.WebApi.Dtos.Querying.TextComparator.Operation.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **operation** | **str** | Required | The comparison to apply between the field and the supplied value(s). One of the Finbourne.Insights.WebApi.Dtos.Querying.TextOperation values (e.g. EqualTo, StartsWith, In); discoverable via the queryable-fields metadata endpoint. |
| **value** | **str** | Optional | The value to compare the field against, for the single-value operations (EqualTo, NotEqualTo, StartsWith, EndsWith). |
| **values** | **List[str]** | Optional | The set of values to compare the field against, for the set operations (In, NotIn). |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.insights.models.TextComparator import TextComparator

instance = TextComparator(
    operation="...",  # required — The comparison to apply between the field and the supplied value(s). One of the Finbourne.Insights.WebApi.Dtos.Querying.TextOperation values (e.g. EqualTo, StartsWith, In); discoverable via the queryable-fields metadata endpoint.
    value="...",  # optional — The value to compare the field against, for the single-value operations (EqualTo, NotEqualTo, StartsWith, EndsWith).
    values=  # optional — The set of values to compare the field against, for the set operations (In, NotIn).
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

