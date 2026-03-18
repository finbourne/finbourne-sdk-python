# FilterModel

Representation of the data used in a filter for the where clause
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **filter_type** | [FilterType](FilterType.md) | Required | *No description available.* |
| **type** | [Type](Type.md) | Optional | *No description available.* |
| **filter** | **str** | Optional | The filter value |
| **filter_to** | **float** | Optional | The upper bound filter value for the number filter type |
| **values** | **List[str]** | Optional | An array of possible values for the set filter type |
| **date_from** | **str** | Optional | A lower bound date for the date filter type |
| **date_to** | **str** | Optional | An upper bound date for the date filter type |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.luminesce.models.FilterModel import FilterModel

instance = FilterModel(
    filter_type=FilterType(...),  # required
    type=Type(...),  # optional
    filter="...",  # optional — The filter value
    filter_to=0.0,  # optional — The upper bound filter value for the number filter type
    values=,  # optional — An array of possible values for the set filter type
    date_from="...",  # optional — A lower bound date for the date filter type
    date_to="..."  # optional — An upper bound date for the date filter type
)
```


## Related Models

- [FilterType](FilterType.md)
- [Type](Type.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

