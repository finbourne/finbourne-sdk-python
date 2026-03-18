# ClosePeriodDiaryEntryRequest

A definition for the period you wish to close
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **diary_entry_code** | **str** | Optional | Unique code assigned to a period. When left blank a code will be created by the system in the format &#39;yyyyMMDD&#39;. |
| **name** | **str** | Optional | Identifiable Name assigned to the period. Where left blank, the system will generate a name in the format &#39;yyyyMMDD&#39;. |
| **effective_at** | **datetime** | Optional | The effective time of the diary entry. |
| **query_as_at** | **datetime** | Optional | The query time of the diary entry. Defaults to latest. |
| **status** | **str** | Optional | The status of a Diary Entry of Type &#39;PeriodBoundary&#39;. Defaults to &#39;Estimate&#39; when closing a period, and supports &#39;Estimate&#39; and &#39;Final&#39; for closing periods and &#39;Final&#39; for locking periods. |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | A set of properties for the diary entry. |
| **closing_options** | **List[str]** | Optional | The options which will be executed once a period is closed or locked. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ClosePeriodDiaryEntryRequest import ClosePeriodDiaryEntryRequest

instance = ClosePeriodDiaryEntryRequest(
    diary_entry_code="...",  # optional — Unique code assigned to a period. When left blank a code will be created by the system in the format &#39;yyyyMMDD&#39;.
    name="...",  # optional — Identifiable Name assigned to the period. Where left blank, the system will generate a name in the format &#39;yyyyMMDD&#39;.
    effective_at=datetime.now(),  # optional — The effective time of the diary entry.
    query_as_at=datetime.now(),  # optional — The query time of the diary entry. Defaults to latest.
    status="...",  # optional — The status of a Diary Entry of Type &#39;PeriodBoundary&#39;. Defaults to &#39;Estimate&#39; when closing a period, and supports &#39;Estimate&#39; and &#39;Final&#39; for closing periods and &#39;Final&#39; for locking periods.
    properties=ModelProperty(...),  # optional — A set of properties for the diary entry.
    closing_options=  # optional — The options which will be executed once a period is closed or locked.
)
```

- [ModelProperty](ModelProperty.md) — used in `properties`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

