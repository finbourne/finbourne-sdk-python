# LockPeriodDiaryEntryRequest

A definition for the period you wish to lock
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **diary_entry_code** | **str** | Optional | Unique code assigned to a period. When left blank last closed period will be located. |
| **closing_options** | **List[str]** | Optional | The options which will be executed once a period is closed or locked. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.LockPeriodDiaryEntryRequest import LockPeriodDiaryEntryRequest

instance = LockPeriodDiaryEntryRequest(
    diary_entry_code="...",  # optional — Unique code assigned to a period. When left blank last closed period will be located.
    closing_options=  # optional — The options which will be executed once a period is closed or locked.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

