# RecommendedSortBy

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **attribute_name** | **str** | Required | The property key, identifier type, or field to be sorted by. |
| **sort_order** | **str** | Optional | The sorting direction. Either ascending (ASC) or descending (DESC). |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RecommendedSortBy import RecommendedSortBy

instance = RecommendedSortBy(
    attribute_name="...",  # required — The property key, identifier type, or field to be sorted by.
    sort_order="..."  # optional — The sorting direction. Either ascending (ASC) or descending (DESC).
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

