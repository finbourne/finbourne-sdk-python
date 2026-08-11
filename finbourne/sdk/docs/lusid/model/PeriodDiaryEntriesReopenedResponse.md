# PeriodDiaryEntriesReopenedResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **effective_from** | **datetime** | Optional | The effective datetime at which the deletion became valid. May be null in the case where multiple date times are applicable. |
| **as_at** | **datetime** | Required | The asAt datetime at which the deletion was committed to LUSID. |
| **period_diary_entries_removed** | **int** | Required | Number of Diary Entries removed as a result of reopening periods |
| **period_diary_entries_from** | **datetime** | Required | The start point where periods were removed from |
| **period_diary_entries_to** | **datetime** | Required | The end point where periods were removed to |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PeriodDiaryEntriesReopenedResponse import PeriodDiaryEntriesReopenedResponse

instance = PeriodDiaryEntriesReopenedResponse(
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    effective_from=datetime.now(),  # optional — The effective datetime at which the deletion became valid. May be null in the case where multiple date times are applicable.
    as_at=datetime.now(),  # required — The asAt datetime at which the deletion was committed to LUSID.
    period_diary_entries_removed=0,  # required — Number of Diary Entries removed as a result of reopening periods
    period_diary_entries_from=datetime.now(),  # required — The start point where periods were removed from
    period_diary_entries_to=datetime.now(),  # required — The end point where periods were removed to
    links=[]  # optional
)
```

- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

