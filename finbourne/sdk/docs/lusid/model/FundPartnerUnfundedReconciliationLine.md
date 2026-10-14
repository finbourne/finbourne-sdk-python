# FundPartnerUnfundedReconciliationLine

One booked allocation to the partner on the unfunded commitment statement.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **allocation_event_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **event_date** | **datetime** | Required | The event date of the allocation. |
| **event_type** | **str** | Required | The kind of allocation event: CapitalCall, Distribution, FeeExpense, ValuationMove, Equalisation, RecallExpiry, Transfer, Default or Commitment. |
| **component** | **str** | Optional | The component of the event the amount belongs to, for example Investment, MgmtFee or ROC. |
| **ilpa_transaction_type** | **str** | Required | The ILPA transaction type the line is reported under, from the map&#39;s override or the default for the event type and component. |
| **inside_fund** | **bool** | Required | Whether the flow is inside the fund&#39;s commitment. False for flows outside it, such as equalisation interest or late payment interest, which do not move unfunded. |
| **amount** | **float** | Required | The amount allocated to the partner, in the statement currency. |
| **unfunded_impact** | **float** | Required | The effect of the line on unfunded commitment: negative for a call inside the commitment or an expired recallable, positive for a recallable distribution, and the signed amount for a commitment change or transfer. Zero for a flow that does not move unfunded. |
| **recallable_until** | **datetime** | Optional | For a recallable distribution, the last date it may be recalled. Absent when there is no deadline or the line is not recallable. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FundPartnerUnfundedReconciliationLine import FundPartnerUnfundedReconciliationLine

instance = FundPartnerUnfundedReconciliationLine(
    allocation_event_id=ResourceId(...),  # required
    event_date=datetime.now(),  # required — The event date of the allocation.
    event_type="...",  # required — The kind of allocation event: CapitalCall, Distribution, FeeExpense, ValuationMove, Equalisation, RecallExpiry, Transfer, Default or Commitment.
    component="...",  # optional — The component of the event the amount belongs to, for example Investment, MgmtFee or ROC.
    ilpa_transaction_type="...",  # required — The ILPA transaction type the line is reported under, from the map&#39;s override or the default for the event type and component.
    inside_fund=True,  # required — Whether the flow is inside the fund&#39;s commitment. False for flows outside it, such as equalisation interest or late payment interest, which do not move unfunded.
    amount=0.0,  # required — The amount allocated to the partner, in the statement currency.
    unfunded_impact=0.0,  # required — The effect of the line on unfunded commitment: negative for a call inside the commitment or an expired recallable, positive for a recallable distribution, and the signed amount for a commitment change or transfer. Zero for a flow that does not move unfunded.
    recallable_until=datetime.now()  # optional — For a recallable distribution, the last date it may be recalled. Absent when there is no deadline or the line is not recallable.
)
```


## Related Models

- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

