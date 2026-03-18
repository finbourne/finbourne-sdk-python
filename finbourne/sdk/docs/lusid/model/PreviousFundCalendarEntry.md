# PreviousFundCalendarEntry

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **code** | **str** | Required | The unique Code of the Calendar Entry. The Calendar Entry, together with the Fund Scope and Code, uniquely identifies a Fund Calendar Entry. |
| **display_name** | **str** | Required | The name of the Fund Calendar entry. |
| **description** | **str** | Optional | A description for the Fund Calendar entry. |
| **effective_at** | **datetime** | Optional | The effective at of the Calendar Entry. |
| **as_at** | **datetime** | Required | The asAt datetime for the Calendar Entry. |
| **holdings_as_at_override** | **datetime** | Optional | The optional AsAt Override to use for building holdings in the Valuation Point. Defaults to Latest. |
| **valuations_as_at_override** | **datetime** | Optional | The optional AsAt Override to use for performing valuations in the Valuation Point. Defaults to Latest. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PreviousFundCalendarEntry import PreviousFundCalendarEntry

instance = PreviousFundCalendarEntry(
    code="...",  # required — The unique Code of the Calendar Entry. The Calendar Entry, together with the Fund Scope and Code, uniquely identifies a Fund Calendar Entry.
    display_name="...",  # required — The name of the Fund Calendar entry.
    description="...",  # optional — A description for the Fund Calendar entry.
    effective_at=datetime.now(),  # optional — The effective at of the Calendar Entry.
    as_at=datetime.now(),  # required — The asAt datetime for the Calendar Entry.
    holdings_as_at_override=datetime.now(),  # optional — The optional AsAt Override to use for building holdings in the Valuation Point. Defaults to Latest.
    valuations_as_at_override=datetime.now()  # optional — The optional AsAt Override to use for performing valuations in the Valuation Point. Defaults to Latest.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

