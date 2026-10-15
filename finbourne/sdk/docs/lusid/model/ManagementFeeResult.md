# ManagementFeeResult

The outcome of a management fee calculation.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **fund_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **period_start** | **datetime** | Required | The start of the fee period, exclusive. |
| **period_end** | **datetime** | Required | The end of the fee period, inclusive. |
| **basis** | **str** | Required | The capital base the fee is charged on. Available values: Auto, CommittedCapital, InvestedCapital. Auto charges on committed capital until the investment period ends and on invested capital after. |
| **lines** | [List[ManagementFeeLine]](ManagementFeeLine.md) | Required | The fee per partner. |
| **totals** | [ManagementFeeTotals](ManagementFeeTotals.md) | Required | *No description available.* |
| **booked_transaction_ids** | **List[str]** | Required | The identifiers of the transactions booked, if any. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ManagementFeeResult import ManagementFeeResult

instance = ManagementFeeResult(
    fund_id=ResourceId(...),  # required
    period_start=datetime.now(),  # required — The start of the fee period, exclusive.
    period_end=datetime.now(),  # required — The end of the fee period, inclusive.
    basis="...",  # required — The capital base the fee is charged on. Available values: Auto, CommittedCapital, InvestedCapital. Auto charges on committed capital until the investment period ends and on invested capital after.
    lines=[],  # required — The fee per partner.
    totals=ManagementFeeTotals(...),  # required
    booked_transaction_ids=  # required — The identifiers of the transactions booked, if any.
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [ManagementFeeLine](ManagementFeeLine.md) — used in `lines`
- [ManagementFeeTotals](ManagementFeeTotals.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

