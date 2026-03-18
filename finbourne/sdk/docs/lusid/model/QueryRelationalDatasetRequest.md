# QueryRelationalDatasetRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **query_method** | **str** | Optional | The method used to query data points. Can be either &#39;Latest&#39; or &#39;TimeSeries&#39;. |
| **filter** | **str** | Optional | Expression to filter the result set. For more information about filtering LUSID results, see https://support.lusid.com/knowledgebase/article/KA-01914. |
| **custom_sort_by** | [List[CustomSortBy]](CustomSortBy.md) | Optional | A list of fields and values to sort the results by. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.QueryRelationalDatasetRequest import QueryRelationalDatasetRequest

instance = QueryRelationalDatasetRequest(
    query_method="...",  # optional — The method used to query data points. Can be either &#39;Latest&#39; or &#39;TimeSeries&#39;.
    filter="...",  # optional — Expression to filter the result set. For more information about filtering LUSID results, see https://support.lusid.com/knowledgebase/article/KA-01914.
    custom_sort_by=[]  # optional — A list of fields and values to sort the results by.
)
```

- [CustomSortBy](CustomSortBy.md) — used in `custom_sort_by`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

