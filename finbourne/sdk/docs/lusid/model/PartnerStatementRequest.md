# PartnerStatementRequest

The request to produce a partner statement over a period.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **period_start** | **datetime** | Required | The start of the statement period, exclusive. |
| **period_end** | **datetime** | Required | The end of the statement period, inclusive. |
| **nav_type_code** | **str** | Optional | The NAV type to produce the statement under. Defaults to the fund&#39;s primary NAV type. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PartnerStatementRequest import PartnerStatementRequest

instance = PartnerStatementRequest(
    period_start=datetime.now(),  # required — The start of the statement period, exclusive.
    period_end=datetime.now(),  # required — The end of the statement period, inclusive.
    nav_type_code="..."  # optional — The NAV type to produce the statement under. Defaults to the fund&#39;s primary NAV type.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

