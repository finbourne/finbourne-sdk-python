# AllocationEventTransfer

One leg of a Transfer Allocation Event: a fraction of a capital interest line moving to another line.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **from_line_id** | **str** | Required | The identifier of the capital interest line the fraction moves from, as it appears on the register of one of the map&#39;s members. |
| **to_investor_record_id** | **str** | Required | The investor record that receives the transferred interest. |
| **to_line_id** | **str** | Required | The identifier of the capital interest line the fraction moves to. Created if it does not exist. |
| **to_portfolio_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **fraction** | **float** | Required | The fraction of the source line transferred, greater than zero and at most one. The legs out of one line together move each balance times the sum of their fractions, rounded to the currency&#39;s minor unit; each leg takes its share truncated to the minor unit and the last leg out of the line takes the remainder, so no leg takes more than its share, the legs never move more than the line holds, and fractions summing to one close the line. |
| **pnl_split** | **str** | Optional | How the profit and loss of the period containing the transfer is split: InterimClose closes the books on the transfer date; DailyProration prorates by days held. Defaults to InterimClose. Available values: InterimClose, DailyProration. |
| **consideration** | [AllocationEventTransferConsideration](AllocationEventTransferConsideration.md) | Optional | *No description available.* |
| **consent_reference** | **str** | Optional | A reference to the consent obtained for the transfer, when the fund requires one. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AllocationEventTransfer import AllocationEventTransfer

instance = AllocationEventTransfer(
    from_line_id="...",  # required — The identifier of the capital interest line the fraction moves from, as it appears on the register of one of the map&#39;s members.
    to_investor_record_id="...",  # required — The investor record that receives the transferred interest.
    to_line_id="...",  # required — The identifier of the capital interest line the fraction moves to. Created if it does not exist.
    to_portfolio_id=ResourceId(...),  # optional
    fraction=0.0,  # required — The fraction of the source line transferred, greater than zero and at most one. The legs out of one line together move each balance times the sum of their fractions, rounded to the currency&#39;s minor unit; each leg takes its share truncated to the minor unit and the last leg out of the line takes the remainder, so no leg takes more than its share, the legs never move more than the line holds, and fractions summing to one close the line.
    pnl_split="...",  # optional — How the profit and loss of the period containing the transfer is split: InterimClose closes the books on the transfer date; DailyProration prorates by days held. Defaults to InterimClose. Available values: InterimClose, DailyProration.
    consideration=AllocationEventTransferConsideration(...),  # optional
    consent_reference="..."  # optional — A reference to the consent obtained for the transfer, when the fund requires one.
)
```

- [ResourceId](ResourceId.md)
- [AllocationEventTransferConsideration](AllocationEventTransferConsideration.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

