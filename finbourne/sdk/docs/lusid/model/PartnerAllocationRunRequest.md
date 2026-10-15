# PartnerAllocationRunRequest

The request to allocate a period's income summary to the partners of a partnership fund.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **period_start** | **datetime** | Required | The start of the period to allocate, exclusive. |
| **period_end** | **datetime** | Required | The end of the period to allocate, inclusive. A valuation point must end on this date. |
| **nav_type_code** | **str** | Optional | The NAV type to allocate under. Defaults to the fund&#39;s primary NAV type. |
| **dry_run** | **bool** | Optional | When true, the allocation is computed and returned but nothing is booked. |
| **correction** | **bool** | Optional | When true, a period that has already been allocated may be re-allocated. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PartnerAllocationRunRequest import PartnerAllocationRunRequest

instance = PartnerAllocationRunRequest(
    period_start=datetime.now(),  # required — The start of the period to allocate, exclusive.
    period_end=datetime.now(),  # required — The end of the period to allocate, inclusive. A valuation point must end on this date.
    nav_type_code="...",  # optional — The NAV type to allocate under. Defaults to the fund&#39;s primary NAV type.
    dry_run=True,  # optional — When true, the allocation is computed and returned but nothing is booked.
    correction=True  # optional — When true, a period that has already been allocated may be re-allocated.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

