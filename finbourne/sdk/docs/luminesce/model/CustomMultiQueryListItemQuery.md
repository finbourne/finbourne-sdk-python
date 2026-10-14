# CustomMultiQueryListItemQuery

One of the queries of a Finbourne.Honeycomb.WebApi.BackgroundQueries.MultiQuery.CustomMultiQueryListItem
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **name** | **str** | Optional | The Name given to the query in the original request |
| **state** | [BackgroundQueryState](BackgroundQueryState.md) | Optional | *No description available.* |
| **has_result** | **bool** | Optional | Whether its results may be fetched |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.luminesce.models.CustomMultiQueryListItemQuery import CustomMultiQueryListItemQuery

instance = CustomMultiQueryListItemQuery(
    name="...",  # optional — The Name given to the query in the original request
    state=BackgroundQueryState(...),  # optional
    has_result=True  # optional — Whether its results may be fetched
)
```

- [BackgroundQueryState](BackgroundQueryState.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

