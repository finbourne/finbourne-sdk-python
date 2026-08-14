# NoticeConvention

Defines the notice period by which a cancellation election must be made ahead of the  cancel effective date, else the option lapses.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **calendars** | **List[str]** | Optional | Holiday calendar code(s) used to resolve business days, required when the day type is Business. |
| **day_type** | **str** | Required | Indicates whether the notice days are counted using business days or calendar days.                Supported string (enumeration) values are: [Business, Calendar]. Available values: Business, Calendar. |
| **notice_days** | **int** | Optional | The number of days prior to the cancel effective date by which the election must be made.                Defaults to 2 if not set. Default: `2` |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.NoticeConvention import NoticeConvention

instance = NoticeConvention(
    calendars=,  # optional — Holiday calendar code(s) used to resolve business days, required when the day type is Business.
    day_type="...",  # required — Indicates whether the notice days are counted using business days or calendar days.                Supported string (enumeration) values are: [Business, Calendar]. Available values: Business, Calendar.
    notice_days=0  # optional — The number of days prior to the cancel effective date by which the election must be made.                Defaults to 2 if not set.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

