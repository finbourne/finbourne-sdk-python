# ManagementFeeRequest

The request to calculate a period's management fee for the partners of a partnership fund.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **period_start** | **datetime** | Required | The start of the fee period, exclusive. |
| **period_end** | **datetime** | Required | The end of the fee period, inclusive. |
| **basis** | **str** | Optional | The capital base the fee is charged on. Available values: Auto, CommittedCapital, InvestedCapital. Auto charges on committed capital until the investment period ends and on invested capital after. |
| **offsets** | [List[ManagementFeeOffset]](ManagementFeeOffset.md) | Optional | Fee income received by the manager that offsets the management fee. |
| **book** | **bool** | Optional | When true, the net fee per partner is booked. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ManagementFeeRequest import ManagementFeeRequest

instance = ManagementFeeRequest(
    period_start=datetime.now(),  # required — The start of the fee period, exclusive.
    period_end=datetime.now(),  # required — The end of the fee period, inclusive.
    basis="...",  # optional — The capital base the fee is charged on. Available values: Auto, CommittedCapital, InvestedCapital. Auto charges on committed capital until the investment period ends and on invested capital after.
    offsets=[],  # optional — Fee income received by the manager that offsets the management fee.
    book=True  # optional — When true, the net fee per partner is booked.
)
```

- [ManagementFeeOffset](ManagementFeeOffset.md) — used in `offsets`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

