# DateOrDiaryEntry

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **var_date** | **str** | Optional | A date. If specified, DiaryEntry must not be specified. |
| **diary_entry** | **str** | Optional | The code of a diary entry. If specified, Date must not be specified. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.DateOrDiaryEntry import DateOrDiaryEntry

instance = DateOrDiaryEntry(
    var_date="...",  # optional — A date. If specified, DiaryEntry must not be specified.
    diary_entry="..."  # optional — The code of a diary entry. If specified, Date must not be specified.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

