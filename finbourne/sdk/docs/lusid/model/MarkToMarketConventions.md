# MarkToMarketConventions

A set of conventions for mark to market. Mark to market is a method   that values financial instruments based on current market prices,   reflecting their current value, rather than historical cost.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **calendar_code** | **str** | Optional | The calendar to use when generating mark to market cashflows and events. |
| **hour_offset_tenor** | **str** | Optional | The hour tenor component of the time offset against the maturity date.  This is an optional field, if a value is provided it must be a positive value between &#39;0hour&#39; and &#39;23hour&#39;. |
| **minute_offset_tenor** | **str** | Optional | The minute tenor component of the time offset against the maturity date.  This is an optional field, if a value is provided it must be a positive value between &#39;0min&#39; and &#39;59min&#39;. |
| **mtm_settle_days** | **int** | Optional | The number of business days after each mark to market date on which its variation margin is paid.  This is an optional field, defaulting to 0 (paid on the mark to market date); if a value is provided it must be between 0 and 10 inclusive. |
| **mtm_settlement_calendar** | **str** | Optional | The calendar the mark to market settlement days are counted on.  This is an optional field; if no value is provided the mark to market calendar is used, and without that only weekends are non-business days. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.MarkToMarketConventions import MarkToMarketConventions

instance = MarkToMarketConventions(
    calendar_code="...",  # optional — The calendar to use when generating mark to market cashflows and events.
    hour_offset_tenor="...",  # optional — The hour tenor component of the time offset against the maturity date.  This is an optional field, if a value is provided it must be a positive value between &#39;0hour&#39; and &#39;23hour&#39;.
    minute_offset_tenor="...",  # optional — The minute tenor component of the time offset against the maturity date.  This is an optional field, if a value is provided it must be a positive value between &#39;0min&#39; and &#39;59min&#39;.
    mtm_settle_days=0,  # optional — The number of business days after each mark to market date on which its variation margin is paid.  This is an optional field, defaulting to 0 (paid on the mark to market date); if a value is provided it must be between 0 and 10 inclusive.
    mtm_settlement_calendar="..."  # optional — The calendar the mark to market settlement days are counted on.  This is an optional field; if no value is provided the mark to market calendar is used, and without that only weekends are non-business days.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

