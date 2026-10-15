# PartnerAllocationRunResult

The outcome of a partner allocation run: the pools the period's income was split into and what, if anything,  could not be attributed to a pool.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **fund_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **period_start** | **datetime** | Required | The start of the period to allocate, exclusive. |
| **period_end** | **datetime** | Required | The end of the period to allocate, inclusive. A valuation point must end on this date. |
| **nav_type_code** | **str** | Required | The NAV type to allocate under. Defaults to the fund&#39;s primary NAV type. |
| **status** | **str** | Required | The outcome of the run. Available values: Computed, Booked, DryRun. |
| **run_id** | **str** | Required | The identifier of the run, which prefixes every transaction it books. |
| **pools** | [List[PartnerAllocationPool]](PartnerAllocationPool.md) | Required | The pools of fund-level amount that were allocated. |
| **unattributed** | [List[UnattributedAmount]](UnattributedAmount.md) | Required | Fund-level amounts that no pool claimed. |
| **booked_transaction_ids** | **List[str]** | Required | The identifiers of the transactions the run booked, if any. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PartnerAllocationRunResult import PartnerAllocationRunResult

instance = PartnerAllocationRunResult(
    fund_id=ResourceId(...),  # required
    period_start=datetime.now(),  # required — The start of the period to allocate, exclusive.
    period_end=datetime.now(),  # required — The end of the period to allocate, inclusive. A valuation point must end on this date.
    nav_type_code="...",  # required — The NAV type to allocate under. Defaults to the fund&#39;s primary NAV type.
    status="...",  # required — The outcome of the run. Available values: Computed, Booked, DryRun.
    run_id="...",  # required — The identifier of the run, which prefixes every transaction it books.
    pools=[],  # required — The pools of fund-level amount that were allocated.
    unattributed=[],  # required — Fund-level amounts that no pool claimed.
    booked_transaction_ids=  # required — The identifiers of the transactions the run booked, if any.
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [PartnerAllocationPool](PartnerAllocationPool.md) — used in `pools`
- [UnattributedAmount](UnattributedAmount.md) — used in `unattributed`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

