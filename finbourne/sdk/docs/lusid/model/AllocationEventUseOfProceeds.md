# AllocationEventUseOfProceeds

One row of a CapitalCall Allocation Event's use of proceeds: what part of the call pays for what.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **purpose** | **str** | Required | What the row pays for: Investment, FacilityRepayment, FacilityInterest, ManagementFee or Expenses. Available values: Investment, FacilityRepayment, FacilityInterest, ManagementFee, Expenses. |
| **deal_id** | **str** | Optional | The deal the row funds, or whose facility draw it repays. Required for an Investment row. |
| **amount** | **float** | Required | The part of the call the row takes, in the event currency. Greater than zero. |
| **facility_id** | **str** | Optional | The facility the row repays. Required for a FacilityRepayment row; on an Investment row it is filled in from the deal&#39;s funding when the call is computed. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AllocationEventUseOfProceeds import AllocationEventUseOfProceeds

instance = AllocationEventUseOfProceeds(
    purpose="...",  # required — What the row pays for: Investment, FacilityRepayment, FacilityInterest, ManagementFee or Expenses. Available values: Investment, FacilityRepayment, FacilityInterest, ManagementFee, Expenses.
    deal_id="...",  # optional — The deal the row funds, or whose facility draw it repays. Required for an Investment row.
    amount=0.0,  # required — The part of the call the row takes, in the event currency. Greater than zero.
    facility_id="..."  # optional — The facility the row repays. Required for a FacilityRepayment row; on an Investment row it is filled in from the deal&#39;s funding when the call is computed.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

