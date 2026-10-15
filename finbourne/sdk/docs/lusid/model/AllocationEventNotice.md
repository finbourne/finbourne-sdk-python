# AllocationEventNotice

A capital call or distribution notice for one partner on an allocation event: the lines allocated to the  partner, the net amount due, the partner's unfunded commitment rolled through the event, cumulative balances  for the partner and the general partner, and a DRAFT watermark while the event is not yet booked.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **fund** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **event** | [AllocationEventNoticeEvent](AllocationEventNoticeEvent.md) | Required | *No description available.* |
| **partner** | [AllocationEventNoticePartner](AllocationEventNoticePartner.md) | Required | *No description available.* |
| **currency** | **str** | Required | The currency the notice amounts are expressed in. |
| **lines** | [List[AllocationEventNoticeLine]](AllocationEventNoticeLine.md) | Required | The notice lines, one per component of the partner&#39;s allocation. |
| **net_amount_due** | **float** | Required | The net amount due, positive when the partner pays the fund and negative when the fund pays the partner. |
| **unfunded_reconciliation** | [AllocationEventNoticeUnfundedReconciliation](AllocationEventNoticeUnfundedReconciliation.md) | Required | *No description available.* |
| **cumulative** | [AllocationEventNoticeCumulative](AllocationEventNoticeCumulative.md) | Required | *No description available.* |
| **gp_column** | [AllocationEventNoticeCumulative](AllocationEventNoticeCumulative.md) | Optional | *No description available.* |
| **wire** | [AllocationEventNoticeWire](AllocationEventNoticeWire.md) | Optional | *No description available.* |
| **payment_hold** | [AllocationPaymentHold](AllocationPaymentHold.md) | Optional | *No description available.* |
| **watermark** | **str** | Optional | DRAFT until the allocation event is booked, otherwise null. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AllocationEventNotice import AllocationEventNotice

instance = AllocationEventNotice(
    fund=ResourceId(...),  # required
    event=AllocationEventNoticeEvent(...),  # required
    partner=AllocationEventNoticePartner(...),  # required
    currency="...",  # required — The currency the notice amounts are expressed in.
    lines=[],  # required — The notice lines, one per component of the partner&#39;s allocation.
    net_amount_due=0.0,  # required — The net amount due, positive when the partner pays the fund and negative when the fund pays the partner.
    unfunded_reconciliation=AllocationEventNoticeUnfundedReconciliation(...),  # required
    cumulative=AllocationEventNoticeCumulative(...),  # required
    gp_column=AllocationEventNoticeCumulative(...),  # optional
    wire=AllocationEventNoticeWire(...),  # optional
    payment_hold=AllocationPaymentHold(...),  # optional
    watermark="..."  # optional — DRAFT until the allocation event is booked, otherwise null.
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [AllocationEventNoticeEvent](AllocationEventNoticeEvent.md)
- [AllocationEventNoticePartner](AllocationEventNoticePartner.md)
- [AllocationEventNoticeLine](AllocationEventNoticeLine.md) — used in `lines`
- [AllocationEventNoticeUnfundedReconciliation](AllocationEventNoticeUnfundedReconciliation.md)
- [AllocationEventNoticeCumulative](AllocationEventNoticeCumulative.md)
- [AllocationEventNoticeCumulative](AllocationEventNoticeCumulative.md)
- [AllocationEventNoticeWire](AllocationEventNoticeWire.md)
- [AllocationPaymentHold](AllocationPaymentHold.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

