# InstrumentCashFlow

The details for the cashflow associated with an instrument from a given portfolio.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **payment_date** | **datetime** | Required | The date at which the given cash flow is due to be paid (SettlementDate is used somewhat interchangeably with PaymentDate.) |
| **amount** | **float** | Optional | The quantity (amount) that will be paid. Note that this can be empty if the payment is in the future and a model is used that cannot estimate it. |
| **currency** | **str** | Required | The payment currency of the cash flow. |
| **source_portfolio_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **source_transaction_id** | **str** | Required | The identifier for the parent transaction on the instrument that will pay/receive this cash flow. |
| **source_instrument_scope** | **str** | Required | The unique Lusid Instrument Id (LUID) of the instrument that the holding is in. |
| **source_instrument_id** | **str** | Required | The unique Lusid Instrument Id (LUID) of the instrument that the holding is in. |
| **diagnostics** | **Dict[str, Optional[str]]** | Required | Whilst a cash flow is defined by an (amount,ccy) pair and the date it is paid on there is additional information required for diagnostics. This includes a range of information and can be empty in the case of a simple cash quantity or where further information is not available. Typical information includes items such as reset dates, RIC, accrual start/end, number of days and curve data. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.InstrumentCashFlow import InstrumentCashFlow

instance = InstrumentCashFlow(
    payment_date=datetime.now(),  # required — The date at which the given cash flow is due to be paid (SettlementDate is used somewhat interchangeably with PaymentDate.)
    amount=0.0,  # optional — The quantity (amount) that will be paid. Note that this can be empty if the payment is in the future and a model is used that cannot estimate it.
    currency="...",  # required — The payment currency of the cash flow.
    source_portfolio_id=ResourceId(...),  # required
    source_transaction_id="...",  # required — The identifier for the parent transaction on the instrument that will pay/receive this cash flow.
    source_instrument_scope="...",  # required — The unique Lusid Instrument Id (LUID) of the instrument that the holding is in.
    source_instrument_id="...",  # required — The unique Lusid Instrument Id (LUID) of the instrument that the holding is in.
    diagnostics=,  # required — Whilst a cash flow is defined by an (amount,ccy) pair and the date it is paid on there is additional information required for diagnostics. This includes a range of information and can be empty in the case of a simple cash quantity or where further information is not available. Typical information includes items such as reset dates, RIC, accrual start/end, number of days and curve data.
    links=[]  # optional
)
```

- [ResourceId](ResourceId.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

