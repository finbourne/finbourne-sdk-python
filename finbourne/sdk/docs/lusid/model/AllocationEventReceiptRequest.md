# AllocationEventReceiptRequest

The request used to record cash received from an investor against a booked capital call.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **investor_record_id** | **str** | Required | The investor record the cash came from. |
| **amount** | **float** | Required | The cash the partner sent, as sent and before any bank charge: in the payment currency if one is given and otherwise in the event currency. |
| **receipt_date** | **datetime** | Required | The date the cash was received. |
| **payment_currency** | **str** | Optional | The ISO 4217 code of the currency the cash arrived in, when it differs from the event currency. |
| **payment_fx_rate** | **float** | Optional | The rate the payment was converted at, as units of event currency per unit of payment currency. Required with a payment currency. |
| **notice_fx_rate** | **float** | Optional | The rate the call was noticed at in the payment currency, in the same terms as the payment FX rate. With one, only the rate&#39;s effect on the payment is an FX difference; without one a payment converting to less than the call is simply short. Only with a payment currency. |
| **bank_charge** | **float** | Optional | Any bank charge deducted from the cash before it arrived, in the event currency. |
| **bank_charge_bearer** | **str** | Optional | Who bears the bank charge: Partner leaves it outstanding on the investor, Fund books it as a fund expense. Defaults to the map&#39;s policy. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AllocationEventReceiptRequest import AllocationEventReceiptRequest

instance = AllocationEventReceiptRequest(
    investor_record_id="...",  # required — The investor record the cash came from.
    amount=0.0,  # required — The cash the partner sent, as sent and before any bank charge: in the payment currency if one is given and otherwise in the event currency.
    receipt_date=datetime.now(),  # required — The date the cash was received.
    payment_currency="...",  # optional — The ISO 4217 code of the currency the cash arrived in, when it differs from the event currency.
    payment_fx_rate=0.0,  # optional — The rate the payment was converted at, as units of event currency per unit of payment currency. Required with a payment currency.
    notice_fx_rate=0.0,  # optional — The rate the call was noticed at in the payment currency, in the same terms as the payment FX rate. With one, only the rate&#39;s effect on the payment is an FX difference; without one a payment converting to less than the call is simply short. Only with a payment currency.
    bank_charge=0.0,  # optional — Any bank charge deducted from the cash before it arrived, in the event currency.
    bank_charge_bearer="..."  # optional — Who bears the bank charge: Partner leaves it outstanding on the investor, Fund books it as a fund expense. Defaults to the map&#39;s policy.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

