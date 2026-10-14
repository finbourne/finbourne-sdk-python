# AllocationEventDealFunding

The details of a DealFunding Allocation Event: the deal the vehicle funds, where the money came from and which  investor records are excused from it.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **deal_id** | **str** | Required | The deal the vehicle funds. A later capital call names it in an Investment row of its use of proceeds. |
| **facility_id** | **str** | Optional | The subscription facility the funding was drawn from. Absent means the deal was paid from cash. |
| **excluded_investor_record_ids** | **List[str]** | Optional | The investor records excused from the deal. They pay nothing towards it when it is called and the others take up their share. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AllocationEventDealFunding import AllocationEventDealFunding

instance = AllocationEventDealFunding(
    deal_id="...",  # required — The deal the vehicle funds. A later capital call names it in an Investment row of its use of proceeds.
    facility_id="...",  # optional — The subscription facility the funding was drawn from. Absent means the deal was paid from cash.
    excluded_investor_record_ids=  # optional — The investor records excused from the deal. They pay nothing towards it when it is called and the others take up their share.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

