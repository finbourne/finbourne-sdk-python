# DiaryEntryRequest

The request to add a diary entry
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **diary_entry_code** | **str** | Required | The code of the diary entry. |
| **name** | **str** | Optional | The name of the diary entry. |
| **status** | **str** | Optional | The status of a Diary Entry of Type &#39;Other&#39;. Defaults to &#39;Undefined&#39; and supports &#39;Undefined&#39;, &#39;Estimate&#39;, &#39;Candidate&#39;, and &#39;Final&#39;. |
| **effective_at** | **datetime** | Required | The effective time of the diary entry. |
| **query_as_at** | **datetime** | Optional | The query time of the diary entry. Defaults to latest. |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | A set of properties for the diary entry. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.DiaryEntryRequest import DiaryEntryRequest

instance = DiaryEntryRequest(
    diary_entry_code="...",  # required — The code of the diary entry.
    name="...",  # optional — The name of the diary entry.
    status="...",  # optional — The status of a Diary Entry of Type &#39;Other&#39;. Defaults to &#39;Undefined&#39; and supports &#39;Undefined&#39;, &#39;Estimate&#39;, &#39;Candidate&#39;, and &#39;Final&#39;.
    effective_at=datetime.now(),  # required — The effective time of the diary entry.
    query_as_at=datetime.now(),  # optional — The query time of the diary entry. Defaults to latest.
    properties=ModelProperty(...)  # optional — A set of properties for the diary entry.
)
```

- [ModelProperty](ModelProperty.md) — used in `properties`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

