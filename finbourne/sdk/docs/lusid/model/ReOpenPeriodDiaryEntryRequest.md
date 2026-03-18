# ReOpenPeriodDiaryEntryRequest

A definition for the period you wish to re open
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **diary_entry_code** | **str** | Optional | Unique code assigned to a period. When left blank last period will be used. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ReOpenPeriodDiaryEntryRequest import ReOpenPeriodDiaryEntryRequest

instance = ReOpenPeriodDiaryEntryRequest(
    diary_entry_code="..."  # optional — Unique code assigned to a period. When left blank last period will be used.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

