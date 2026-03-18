# InstrumentPaymentDiaryRow

An individual row containing details of a single cashflow in the diary.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **quantity** | **float** | Optional | The quantity (amount) that will be paid. Note that this can be empty if the payment is in the future and a model is used that cannot estimate it. |
| **currency** | **str** | Optional | The payment currency of the cash flow. |
| **payment_date** | **datetime** | Optional | The date at which the given cash flow is due to be paid. |
| **pay_or_receive** | **str** | Optional | Does the cash flow belong to the Pay or Receive leg. |
| **accrual_start** | **datetime** | Optional | The date on which accruals start for this cashflow. |
| **accrual_end** | **datetime** | Optional | The date on which accruals end for this cashflow. |
| **cash_flow_type** | **str** | Optional | The type of cashflow. |
| **is_cash_flow_determined** | **bool** | Optional | Is the cashflow determined as of the effective date time. |
| **is_cash_flow_historic** | **bool** | Optional | Has the cashflow been paid, i.e. has it become a historic cashflow, as of the date and time pointed to be effectiveAt. |
| **discount_factor** | **float** | Optional | Weighting factor to discount cashflow to the present value. |
| **discounted_expected_cash_flow_amount** | **float** | Optional | The expected cashflow amount taking into account the discount factor. |
| **day_count_fraction** | **float** | Optional | The day count fraction, if appropriate. |
| **forward_rate** | **float** | Optional | Forward rate for cash flow if appropriate. (as in for a rates fixed or floating leg) |
| **reset_rate** | **float** | Optional | The value of the reset, if any. |
| **spread** | **float** | Optional | The spread that exists on the payoff. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.InstrumentPaymentDiaryRow import InstrumentPaymentDiaryRow

instance = InstrumentPaymentDiaryRow(
    quantity=0.0,  # optional — The quantity (amount) that will be paid. Note that this can be empty if the payment is in the future and a model is used that cannot estimate it.
    currency="...",  # optional — The payment currency of the cash flow.
    payment_date=datetime.now(),  # optional — The date at which the given cash flow is due to be paid.
    pay_or_receive="...",  # optional — Does the cash flow belong to the Pay or Receive leg.
    accrual_start=datetime.now(),  # optional — The date on which accruals start for this cashflow.
    accrual_end=datetime.now(),  # optional — The date on which accruals end for this cashflow.
    cash_flow_type="...",  # optional — The type of cashflow.
    is_cash_flow_determined=True,  # optional — Is the cashflow determined as of the effective date time.
    is_cash_flow_historic=True,  # optional — Has the cashflow been paid, i.e. has it become a historic cashflow, as of the date and time pointed to be effectiveAt.
    discount_factor=0.0,  # optional — Weighting factor to discount cashflow to the present value.
    discounted_expected_cash_flow_amount=0.0,  # optional — The expected cashflow amount taking into account the discount factor.
    day_count_fraction=0.0,  # optional — The day count fraction, if appropriate.
    forward_rate=0.0,  # optional — Forward rate for cash flow if appropriate. (as in for a rates fixed or floating leg)
    reset_rate=0.0,  # optional — The value of the reset, if any.
    spread=0.0  # optional — The spread that exists on the payoff.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

