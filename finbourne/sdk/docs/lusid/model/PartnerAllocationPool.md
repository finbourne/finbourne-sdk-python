# PartnerAllocationPool

One pool of an allocation run: an amount of a given character, split across the partners on a basis.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **character** | **str** | Required | The character of the pool&#39;s amount, for example Income, RealisedGain or Expense. |
| **origin_member_short_code** | **str** | Optional | For a deal-linked pool, the short code of the member fund the amount originates from. |
| **pool_amount** | **float** | Required | The amount in the pool. |
| **basis** | **str** | Required | The basis the pool was shared on. Available values: CommittedCapital, PaidInCapital, DealPaidIn. |
| **allocations** | [List[PartnerAllocation]](PartnerAllocation.md) | Required | Each partner&#39;s share of the pool. |
| **residual** | **float** | Required | The rounding residual, carried by the largest allocation. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PartnerAllocationPool import PartnerAllocationPool

instance = PartnerAllocationPool(
    character="...",  # required — The character of the pool&#39;s amount, for example Income, RealisedGain or Expense.
    origin_member_short_code="...",  # optional — For a deal-linked pool, the short code of the member fund the amount originates from.
    pool_amount=0.0,  # required — The amount in the pool.
    basis="...",  # required — The basis the pool was shared on. Available values: CommittedCapital, PaidInCapital, DealPaidIn.
    allocations=[],  # required — Each partner&#39;s share of the pool.
    residual=0.0  # required — The rounding residual, carried by the largest allocation.
)
```

- [PartnerAllocation](PartnerAllocation.md) — used in `allocations`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

